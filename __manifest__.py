{
    'name': "Automated Sale Order",
    'version': '16.0.1.0.0',
    'depends': ['sale', 'base'],
    'author': "Cybrosys",
    'category': 'Sales/Auto Sale order',
    'summary': 'Automated sale order',
    'description': """
    Creating button in  product form
    """,
    'auto_install':False,
    'installable':True,
    'application':False,
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'wizard/customer_details_wizard_view.xml',
    ],
    'license': 'LGPL-3',
}
