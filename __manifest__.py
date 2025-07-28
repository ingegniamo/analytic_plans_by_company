{
    'name': "Analytic Plans by Company",
    'version': '17.0.2.0.0',
    'depends': [
        'account'
    ],
    'author': "Muhammad Wael",
    'category': 'Analytic Plan',
    'description': """
    Making company field for analytic plans to be seen by company_id only
    """,
    
    'data': [
        'security/account_security.xml',
        'views/account_analytic_plan_view.xml',
    ],
    'images': [
        'static/description/icon.png'
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}
