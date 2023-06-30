from odoo import models, fields


class Subject(models.Model):
    _name = "subject.subname"
    _description = "Subjects info"

    name = fields.Char(string='Name', required=True)
    value = fields.Integer(string='Some value')
    is_done = fields.Boolean(string='Is done?')