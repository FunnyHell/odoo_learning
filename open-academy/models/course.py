from odoo import models, fields


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Courses of the Open Academy'

    title = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')

    session_ids = fields.One2many(comodel_name='openacademy.session', string='Session', inverse_name='course_id')
    responsible_user_id = fields.Many2one(comodel_name='res.users', string='Responsible user')

    _sql_constraints = [
        ('unique_title', 'unique(title)', 'Course title already exist'),
        ('check_difference', 'check(title != description)', 'Title and description must be different')
    ]