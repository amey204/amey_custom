from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "hospital Patient"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),
    ], required=True, default='m')
    note = fields.Text(string='Description')
