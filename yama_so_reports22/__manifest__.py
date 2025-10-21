# -*- coding: utf-8 -*-
{
    'name': "Sale Order Reports Enhancement22",

    'summary': "Sale Merge Lines in Report and some of  Reports Enhancement",

    'description':
        """
        Sale Merge Lines in Report and some of  Reports Enhancement    
        """,
    'author': "Eng/Muhammad Ramah && Eng/Muhammad El-Nayed",
    "license": "AGPL-3",
    'category': 'Sales',
    'version': '17.0',
    'depends': ['base', 'sale','custom_sales_report'],

    'data': [
        'views/sale_order_view22.xml',
        'views/merge_price_template22.xml',
    ],
    'installable': True,
    'application': False,
}
