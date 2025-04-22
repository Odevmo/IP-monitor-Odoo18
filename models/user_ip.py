from odoo import models, fields, api
from odoo.http import request
import requests
import json

class UserIp(models.Model):
    _name = 'user.ip'
    _description = 'Odoo User IP Address'
    _rec_name = 'ip_address'

    user_id = fields.Many2one('res.users', string='User', required=True, ondelete='cascade', index=True)
    ip_address = fields.Char(string='IP Address', required=True, index=True)
    last_seen = fields.Datetime(string='Last Seen', default=fields.Datetime.now)
    is_tor_exit = fields.Boolean(string='Tor Exit Node', readonly=True, default=False)

    _sql_constraints = [
        ('user_ip_unique', 'unique(user_id, ip_address)', 'Each user must have a unique IP address recorded.'),
    ]

    def _check_tor_exit_node(self, ip_address):
        try:
            url = f'https://check.torproject.org/api/ip/{ip_address}'
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            data = response.json()
            print("responce is: ", data )
            return data.get('IsTor', False)
        except requests.exceptions.RequestException as e:
            print(f"Error checking Tor exit node for {ip_address}: {e}")
            return False

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for record in records:
            if record.ip_address:
                is_tor = self._check_tor_exit_node(record.ip_address)
                record.is_tor_exit = is_tor
        return records

    @api.model
    def record_user_ip_manual(self, user_id, ip_address):
        existing_record = self.search([('user_id', '=', user_id), ('ip_address', '=', ip_address)], limit=1)
        if existing_record:
            existing_record.write({'last_seen': fields.Datetime.now()})
        else:
            is_tor = self._check_tor_exit_node(ip_address)
            self.create([{'user_id': user_id, 'ip_address': ip_address, 'is_tor_exit': is_tor}])