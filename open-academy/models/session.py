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
    number_of_taken_seats = fields.Integer(string='Number of taken seats', compute='_compute_taken_seats', store='True')
    percentage_of_taken_seats = fields.Float(string='Percentage of taken seats', compute='_compute_percent_of_taken_seats')

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
            lasting_days = (fields.Date.today() - records.start_date).days
            if lasting_days < 0:
                records.lasting_days = 0
            else:
                records.lasting_days = lasting_days

    @api.depends('start_date', 'duration')
    def _compute_finish_date(self):
        for records in self:
            records.finish_date = self.start_date + datetime.timedelta(days=records.duration)

    @api.depends('number_of_seats', 'attendees_ids')
    def _compute_taken_seats(self):
        for record in self:
            record.number_of_taken_seats = len(record.attendees_ids)

    @api.onchange('number_of_seats', 'attendees_ids')
    def _onchange_seats(self):
        if self.number_of_taken_seats < 0:
            return {
                'warning': {
                    'title': "Wrong value",
                    'message': "The number of seats can't be negative"
                }
            }
        elif len(self.attendees_ids) > self.number_of_seats:
            return {
                'warning': {
                    'title': "Too much attendees",
                    'message': "Attendees more than number of seats"
                }
            }

    @api.depends('number_of_taken_seats', 'number_of_seats')
    def _compute_percent_of_taken_seats(self):
        for record in self:
            record.percentage_of_taken_seats = record.number_of_taken_seats / record.number_of_seats * 100.0