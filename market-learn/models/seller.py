from odoo import models, fields

class Seller(models.Model):
    _name = 'market.seller'
    _description = 'Seller of products'

    name = fields.String(string='Name', required=True)
    gender = fields.Selection([
        'male', 'Male',
        'female', 'Female'
    ], default='male')