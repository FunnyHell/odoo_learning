from odoo import models, fields


class Seller(models.Model):
    _name = 'market.seller'
    _description = 'Seller of products'

    name = fields.Char(string='Name', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], default='male', required=True)
    products_ids = fields.One2many(comodel_name='market.product', inverse_name='seller_id', string='Product')
