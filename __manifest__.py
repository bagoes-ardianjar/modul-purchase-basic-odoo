{
    'name': 'Module Custom',
    'version': '13.0.1.0.0',
    'category': 'purchase',
    'summary': 'Module Custom',
    'description': """ Ini adalah Module Custom Autodidak """,
    'website': '',
    'author': 'AutoDidak',
    'depends': ['web','base','product'],
    'data': [
        'security/ir.model.access.csv',
        'views/autodidak_pembelian_view.xml',
        'views/autodidak_pembelian_action.xml',
        'views/autodidak_pembelian_menuitem.xml',
        'reports/autodidak_pembelian_qweb.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'OEEL-1',
}