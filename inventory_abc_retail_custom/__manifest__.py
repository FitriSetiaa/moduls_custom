{
 'name' : 'Inventory ABC Retail Custom',
 'version' : '17.0',
 'depends': ['base','product'],
 'author': 'PT. ABC',
 'category' : 'Inventory',
 'summary': 'Custom fields for Inventory module',
 'description' : """
 Modul ini menambahkan custom field pada modul Inventory untuk PT. A B C.
 """,
 'data': [
        'views/product_template_views.xml',
        'security/ir.model.access.csv'

    ],
    'installable': True,
    'license': 'LGPL-3',
}