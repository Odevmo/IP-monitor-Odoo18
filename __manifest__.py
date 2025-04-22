# -*- coding: utf-8 -*-
{
    'name': 'Network IP Monitor',
    'version': '1.0',
    'summary': 'Monitors network IP addresses and their status',
    'description': """
        This module allows you to capture, manage and monitor users IP addresses,
        including their type, status, and description.
    """,
    'website': 'https://github.com/Odevmo',
    'license': 'LGPL-3',
    'category': 'Security',
    'depends': ['base', 'web', 'auth_signup'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/user_ip_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'installable': True,
    'python': [
        'security/authentication.py',
    ],
}