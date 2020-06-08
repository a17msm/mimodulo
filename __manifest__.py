# -*- coding: utf-8 -*-
{
    'name': "Fauna",

    'summary': """
        Permite gestionar las intalaciones y los animales de un centro de rehabilitación de fauna salvaje""",

    'description': """
        Este módulo facilita la gestión de las instalaciones y los animales de un centro de rehabilitación de animales
    """,

    'author': "María Serafín",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/animal.xml',
        'views/instalacion.xml'
        #'views/templates.xml',
    ],

}
