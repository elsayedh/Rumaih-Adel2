# Copyright (C) 2019 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class PosPaymentMethod(models.Model):
    _inherit = "pos.payment.method"

    pos_image = fields.Image("PoS Image", attachment=True)
    
    receivable_account_id = fields.Many2one('account.account',
                                            string='Intermediary Account',
                                            required=True,ondelete='restrict',
                                            help='Account used as counterpart of the income account in the accounting entry representing the pos sales.')
    
    name = fields.Char(string="Payment Method1", required=True)

    
class PosConfig(models.Model):
    _inherit = 'pos.config'   

    
@api.model
    def assign_payment_journals(self, companies=False):
        self = self.sudo()
        if not companies:
            companies = self.env['res.company'].search([])
         
        
