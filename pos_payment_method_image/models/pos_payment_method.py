# Copyright (C) 2019 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class PosPaymentMethod(models.Model):
    _inherit = "pos.payment.method"

    pos_image = fields.Image("PoS Image", attachment=True)
    
    receivable_account_id = fields.Many2one('account.account',
                                            string='Intermediary Account',
                                            required=True,
                                            # domain=[('reconcile', '=', True), ('user_type_id.type', '=', 'receivable')],
                                            default=lambda
                                                self: self.env.company.account_default_pos_receivable_account_id,
                                            ondelete='restrict',
                                            help='Account used as counterpart of the income account in the accounting entry representing the pos sales.')


