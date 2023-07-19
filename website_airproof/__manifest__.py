{
    'name': 'Airproof Theme',
    'author': 'Sergey Omelianenko',
    'description': 'Quest 4 from odoo-learing projects',
    'category': 'Website/Theme',
    'version': '15.0.0',
    'depends': ['website'],
    'data': [
        # ...
    ],
    'assets': {
        'web._assets_primary_variables': [
            ('append', 'website_airproof/static/src/scss/primary_variables.scss'),
        ],
        'web._assets_frontend_helpers': [
            ('prepend', 'website_airproof/static/src/scss/bootstrap_overridden.scss'),
        ],
    },
}
