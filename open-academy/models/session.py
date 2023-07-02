import datetime
from odoo import models, fields

class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'Sessions of the course'

    name = fields.Char(string='Name', required=True)

    start_date = fields.Date(string='Start', required=True, default=fields.Date.today())
    duration = fields.Integer(string='Duration')
    lasting_date = fields.Date(compute='_compute_lasting_days')
    is_active = fields.Boolean(string='Active', default=True)
    finish_date = fields.Date(string='Finish', compute='_compute_finish_date', store='True')

    number_of_seats = fields.Integer(string='Number of seats')
    course_id = fields.Many2one(comodel_name='openacademy.course', inverse_name='session_ids', string='Course', required=True)
