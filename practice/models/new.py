from odoo import fields, api, models


class PracticeNew(models.Model):
    _name = 'practice.new'
    _rec_name = 'id'
    _description = 'Practice New'

    # logic goes here
    sawan_name = fields.Char(string="Name")
    # gender = fields.Selection([()], default='m', string="Gender")
    gender = fields.Selection(selection=[('female', 'Female'), ('male', 'Male')], default='female', string="Gender")
    dob = fields.Date(String="Date Of Birth")
    age = fields.Integer(string="Age")
    address = fields.Char(string="Address")
    mobile = fields.Integer(string="Mobile")
    pin = fields.Integer(string="Pin")
    file = fields.Binary(String="select file")
    practice_ids = fields.One2many('practice.line', 'practice_id')
    # m2o = fields.Many2one('practice.new',String="m2o")
    # m2m = fields.Many2Many('practice.new', String="m2m")


class PracticeLine(models.Model):
    _name = "practice.line"
    _description = "Practice Line"

    name = fields.Char()
    product_id = fields.Many2one('product.product')
    practice_id = fields.Many2one('practice.new')
