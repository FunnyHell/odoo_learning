{
    'name': 'Open Academy',
    'author': 'Sergey Omelianenko',
    'summary': 'Odoo 15 learning module based on official documentation',

    'depends': ['board'],

    'data': [
        'security/openacademy_groups.xml',
        'security/openacademy_course_rules.xml',
        'security/ir.model.access.csv',
        'views/openacademy_course_view.xml',
        'views/openacademy_session_view.xml',
        'views/menus.xml',
        'wizard/session_fill_view.xml',
        'report/openacademy_session_report.xml',
        'report/openacademy_session_templates.xml',
        'views/dashboard.xml',
    ]
}
