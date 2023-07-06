from odoo import models, fields, api

class SessionFill(models.Model):
    _name = 'openacademy.session.fill'
    _description = 'Session fill wizard'

    session_ids = fields.Many2many(comodel_name='openacademy.session', string='Session')
    attendees_ids = fields.Many2many(comodel_name='res.partner', string='Attendees')

    @api.model
    def default_get(self, fields_list):
        result = super(SessionFill, self).default_get(fields_list)
        result['session_ids'] = self.env['openacademy.session'].browse(self._context.get('active_id'))
        return result

    def action_fill_attendees(self):
        return self.session_ids.action_fill_attendees(attendees_ids=self.attendees_ids)
