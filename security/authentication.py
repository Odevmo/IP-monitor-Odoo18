from odoo import models, api, http
from odoo.http import request

class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def _check_credentials(self, login, password):  # Renamed method
        res = super()._check_credentials(login, password)
        if res and self.env.user:
            if request and request.httprequest:
                ip_address = request.httprequest.remote_addr
                self.env['user.ip'].sudo().record_user_ip_manual(self.env.user.id, ip_address)
        return res