from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError
from dateutil.relativedelta import relativedelta
from datetime import date


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _rec_name = "pno"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "hospital Patient"

    pno = fields.Char(string='Order Reference', required=True, readonly=True, default=lambda self: _('New'))
    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),
    ], required=True)
    note = fields.Text(string='Description', tracking=True)
    dob = fields.Date(String='Date of Birth in')

    is_adult = fields.Boolean('Is Adult', compute='_compute_age')

    state = fields.Selection(
        [('draft', 'Draft'), ('confirm', 'Confirmed'), ('done', 'Done'), ('cancel', 'Cancelled')], default="draft",
        string="Status", tracking=True)

    state_id = fields.Many2one("res.country.state", string='State', help='Enter State', ondelete='restrict')
    country_id = fields.Many2one('res.country', string='Country', help='Select Country', ondelete='restrict')
    hide = fields.Boolean(string='Hide', compute="_compute_hide")

    # this is one2many of PatientDetailsLine for HospitalPatient
    # doctor_ids = fields.One2many('sale.order.line', 'parent_id', string='Doctor Line')
    doctor_ids = fields.One2many('patient.detail.line', 'parent_id', string='Doctor Line')

    patient_parent_id = fields.Many2one('patient.detail.line', 'Patient Parent id')

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

    # responsible_id = fields.one2many('res.partner', String='responsible')
    def action_confirm(self):
        self.state = 'confirm'
        # print("Clicked on Button")

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def button_cancel(self):
        self.state = 'cancel'

    @api.onchange('name')
    def compute_desc(self):
        for rec in self:
            rec.note = rec.name

    @api.depends('age')
    def _compute_age(self):
        for rec in self:
            if rec.age >= 18:
                rec.is_adult = True
            else:
                rec.is_adult = False

    @api.depends('dob')
    def _age_calculate(self):
        for i in self:
            if i.dob:
                today = date.today()
                i.age = relativedelta(today, i.dob).years

    # @api.model
    # def create(self, vals):
    #     if not vals.get('pno') or vals['pno'] == _('New'):
    #         vals['pno'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
    #     res = super(HospitalPatient, self).create(vals)
    #     return res

    # if not vals.get['note']:
    #     vals['name'] = 'New Patient'
    # print("successfully override create method")
    # vals['age'] = 18
    # res = super(HospitalPatient, self).create(vals)
    # print("res -----", res)
    # print("vals -----", vals)
    # return res

    # @api.constrains('age')
    # def _check_date_end(self):
    #     for rec in self:
    #         if rec.age >= 80:
    #             raise ValidationError("You are Too old..")


class PatientDetailsLine(models.Model):
    _name = 'patient.detail.line'
    # _inherit = 'sale.order.line'
    _rec_name = 'doctor_name'

    doctor_name = fields.Char('Doctor Name')
    doct_age = fields.Integer('Doctor Age')
    ward_no = fields.Integer('Ward No')
    sale_order_id = fields.Many2one('sale.order', 'Sale Order Id')

    # this field is for the relation between PatientDetailsLine and HospitalPatient
    patient_ids = fields.One2many('hospital.patient', 'patient_parent_id', String="Patient Line")

    parent_id = fields.Many2one('hospital.patient')
