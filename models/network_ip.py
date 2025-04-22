from odoo import _, models, fields

class NetworkIP(models.Model):
    _name = 'network.ip'
    _description = 'Network IP Address'
    _order = 'ip_address'

    ip_address = fields.Char(string='IP Address', required=True, index=True)
    ip_type = fields.Selection([
        ('ipv4', 'IPv4'),
        ('ipv6', 'IPv6')
    ], string='Type', required=True)
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('blacklisted', 'Blacklisted'),
    ], string='Status', default='active')
    description = fields.Text(string='Description')