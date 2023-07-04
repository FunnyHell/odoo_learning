import datetime
from odoo import models, fields, api


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
    course_id = fields.Many2one(comodel_name='openacademy.course', inverse_name='session_ids', string='Course',
                                required=True)

    instructor_id = fields.Many2one(comodel_name='res.partner', inverse_name='session_ids',
                                    string='Instructor', required=True,
                                    domain="['|',"
                                           "('instructor','=','True'),"
                                           "('category_id.name','=like','teacher /%')]")

    attendees_ids = fields.Many2many(comodel_name='res.partner', inverse_name='session_ids', relation='session_ids',
                                     string='Attendees')

    @api.depends('start_date')
    def _compute_lasting_days(self):
        for records in self:
            lasting_days = (fields.Date.today() - self.start_date).days
            if lasting_days < 0:
                records.lasting_days = 0
            else:
                records.lasting_days = lasting_days

    @api.depends('start_days', 'duration')
    def _compute_finish_date(self):
        for records in self:
            finish_days = self.start_date + datetime.timedelta(days=records.duration)

    #TODO: percentage of taken seats