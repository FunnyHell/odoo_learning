from odoo import models, fields


class Product(models.Model):
    _name = "market.product"
    _description = "product information"

    name = fields.Char(string='Name', required=True)
    cost = fields.Integer(string='Cost')
    on_sale = fields.Boolean(string='On sale?')
    note = fields.Text(string='Description')
    seller = fields.Many2one('market.seller', string='Seller')