{
    'name' : 'Sales ABC Retail Custom',
    'version' : '17.0',
    'depends' : ['sale','stock','product'],
    'author' : 'PT.ABC',
    'category' : 'Reporting',
    'summary' : 'Custom module for sales in ABC retail',
    'description' : """
 Modul ini Report barang yang paling banyak terjual dan Report barang yang mendekati kadaluarsa.
 """,
    'data' : [
        'security/ir.model.access.csv',
        'views/laporan_kadaluarsa_produk_views.xml',
        'views/laporan_terjual_views.xml'
        
    ],
    'installable': True, 
    'application': False,
    'license': 'LGPL-3',
}
