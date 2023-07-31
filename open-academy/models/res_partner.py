from odoo import models, fields

class Partner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(string='Instructor', default=False)
    session_ids = fields.Many2many(comodel_name='openacademy.session', relation='attendees_ids')
    category_id = fields.Many2one(comodel_name='res.partner.category', string='Category')
