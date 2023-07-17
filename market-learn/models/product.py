from odoo import models, fields


class Product(models.Model):
    _name = "market.product"
    _description = "product information"

    name = fields.Char(string='Name', required=True)
    cost = fields.Integer(string='Cost')
    on_sale = fields.Boolean(string='On sale?')
    note = fields.Text(string='Description')
    seller_id = fields.Many2one(comodel_name='market.seller', inverse_name='product_ids', string='Seller')