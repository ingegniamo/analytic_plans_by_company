{
    'name': "Analytic Plans by Company",
    'version': '1.0',
    'depends': ['account'],
    'author': "Muhammad Wael",
    'category': 'Analytic Plan',
    'description': """
    Making company field for analytic plans to be seen by company_id only
    """,
    
    'data': [
        'views/inherit_account_analytic_plan.xml',
    ],
    'images': [
        'static/description/icon.png'
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}
