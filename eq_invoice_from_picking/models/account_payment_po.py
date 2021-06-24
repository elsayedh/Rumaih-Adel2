# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class CustomAccountPaymentPo(models.Model):
    _inherit = 'account.payment'
    _description = 'account payment Custom'

    #

    choose_po = fields.Many2one(comodel_name="purchase.order", string="Choose Po", required=True,
                                domain=[('state', '=', 'purchase')])
