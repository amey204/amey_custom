from odoo import models, fields, api


class WizardsBasic(models.TransientModel):
    _name = 'wizards.basic'
    _rec_nam = 'patient_name'
    _description = 'Wizards basic'

    state_id = fields.Many2one("res.country.state", string='State', help='Enter State', ondelete='restrict')
    country_id = fields.Many2one('res.country', string='Country', help='Select Country', ondelete='restrict')
    hide = fields.Boolean(string='Hide', compute="_compute_hide")
    patient_name = fields.Char('Patient Name')
    gender = fields.Selection([
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),
    ], required=True)

    age = fields.Integer(string='Age')


    # to get data from patient to wizard
    @api.model
    def default_get(self, fields):
        res = super(WizardsBasic, self).default_get(fields)
        active_model = self.env.context.get('active_id')
        patient_id = self.env['hospital.patient'].search([('id', '=', active_model)])
        res.update({
            'patient_name': patient_id.name,
            'age': patient_id.age,
            'country_id': patient_id.country_id.id,
            'state_id': patient_id.state_id.id
        })
        return res

    # to get data from wizard to patient
    def change_profile(self):
        active_model = self.env.context.get('active_id')
        patient_id = self.env['hospital.patient'].search([('id', '=', active_model)])
        patient_id.update({
            'name': self.patient_name,
            'age': self.age,
            'country_id': self.country_id.id,
            'state_id': self.state_id.id

        })

    # Dependent picklist code to show State based on selected Country E.g India -> Gujarat, Maharastra, Rajasthan, etc..
    @api.onchange('country_id')
    def _onchange_country_id(self):
        if self.country_id:
            return {'domain': {'state_id': [('country_id', '=', self.country_id.id)]}}
        else:
            return {'domain': {'state_id': []}}

    # Show Hide State selection based on Country
    @api.depends('country_id')
    def _compute_hide(self):
        if self.country_id:
            self.hide = False
        else:
            self.hide = True
