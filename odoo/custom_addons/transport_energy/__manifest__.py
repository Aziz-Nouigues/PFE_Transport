{
    'name': 'Transport - Gestion Énergie',
    'author': 'Aziz Nouigues',
    'category': 'Transport',
    'version': '17.0.0.1.0',
    'depends': [
        'base',
        'fleet',
        'stock',
        'mail',
        'hr',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/energy_type_views.xml',
        'views/fuel_station_views.xml',
        'views/vehicle_extension_views.xml',
    ],
    'installable': True,
    'application': True,
}