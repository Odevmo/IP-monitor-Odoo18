# -*- coding: utf-8 -*-

{
    'name': 'Network IP Monitor',
    'version': '1.0',
    'summary': 'Monitors network IP addresses and their status',
    'website': 'https://github.com/Odevmo',
    'category': 'Security',
    'description': """
        This module allows you to manage and monitor network IP addresses,
        including their type, status, and description.
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/network_ip_views.xml',
    ],
    'installable': True,
    'application': True,
}