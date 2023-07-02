from odoo import models, fields

class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Courses of the Open Academy'

    title = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
