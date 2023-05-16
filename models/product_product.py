# -*- coding: utf-8 -*-
from odoo import models, fields


class ProductProduct(models.Model):
    _inherit = ["product.product"]

    def create_so(self):
        """To Create sale order from a single click"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': "Create SO",
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'customer.details',
            'target': 'new',
            'context': {'default_product': self.id}
        }
