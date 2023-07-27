{
    'name': 'Airproof Theme',
    'author': 'Sergey Omelianenko',
    'description': 'Quest 4 from odoo-learing projects',
    'category': 'Website/Theme',
    'version': '15.0.0',
    'depends': ['website'],
    'data': [
        'views/website_templates.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            ('append', 'website_airproof/static/src/scss/primary_variables.scss'),
        ],
        'web._assets_frontend_helpers': [
            ('append', 'website_airproof/static/src/scss/bootstrap_overridden.scss'),
        ],
        'web.assets_frontend': [
            'website_airproof/static/src/scss/theme.scss',
            'website_airproof/static/src/js/theme.js',
        ],
    },
}
