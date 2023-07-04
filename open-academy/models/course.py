from odoo import models, fields


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Courses of the Open Academy'

    title = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')

    session_ids = fields.One2many(comodel_name='openacademy.session', string='Session', inverse_name='course_id')
    responsible_user_id = fields.Many2one(comodel_name='res.users', string='Responsible user')
