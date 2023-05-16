# -*- coding: utf-8 -*-
from odoo import models, fields
from odoo import Command


class CustomerDetails(models.TransientModel):
    """model for wizard"""
    _name = 'customer.details'

    partner_id = fields.Many2one('res.partner', string="Customer", required=True)
    quantity = fields.Float("Qty", default=1)
    product_id = fields.Many2one('product.template')
    product_variant_id = fields.Many2one(related='product_id.product_variant_id')
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id')
    price = fields.Float("Price", related='product_id.list_price')

    def create_so(self):
        """create sale order"""
        order_line = {
            'product_id': self.product_variant_id.id,
            'product_template_id': self.product_variant_id.id,
            'product_uom_qty': self.quantity,
            'name': self.product_variant_id.name,
            'price_unit': self.price,
            'product_uom': self.product_variant_id.uom_id.id,
        }
        sale_order_item = {'order_line': [Command.create(order_line),]}
        records = self.env['sale.order'].sudo().search(
            [('partner_id', '=', self.partner_id.id), ('state', '=', 'draft')])
        if records:
            for rec in records:
                rec.write(sale_order_item)
                rec.action_confirm()
                self.env['sale.order.line'].write({'display_type': 'line_note', })
                return {
                    'view_mode': 'form',
                    'type': 'ir.actions.act_window',
                    'res_model': 'sale.order',
                    'res_id': rec.id,
                    'context': self.env.context,
                }
        else:
            for record in self:
                order_item = {'partner_id': record.partner_id.id,
                              'state': 'sale',
                              'order_line': [Command.create(order_line), ]}
                order = self.env['sale.order'].create(order_item)
                order.action_confirm()
                return {
                    'view_mode': 'form',
                    'type': 'ir.actions.act_window',
                    'res_model': 'sale.order',
                    'res_id': order.id,
                    'context': self.env.context,
                }

