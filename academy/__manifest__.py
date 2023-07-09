{
    'name': 'Academy',
    'author': 'Sergey Omelianenko',
    'summary': 'Odoo 15 learning module based on official documentation, Quest num 3',
    'depends': [
        'website',
        'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/teachers_views.xml',
        'views/courses_views.xml',
        'views/menus.xml'
    ],
    'demo': [
        'demo/demo.xml'
    ],
}
