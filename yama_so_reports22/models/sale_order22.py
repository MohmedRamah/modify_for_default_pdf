from odoo import fields,models,api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    select_all = fields.Boolean(string="Select all")
    warranty = fields.Char(string="Warranty")
    drop_down = fields.Integer(string="Down Payment")
    a100_drp_down = fields.Integer(compute="calculate_drop_down")

    def calculate_drop_down(self):
        self.a100_drp_down= 100 - self.drop_down

    @api.onchange('select_all')
    def onchange_select_all(self):
        for order in self:
                for line in order.order_line:
                    line.is_subtotal_merge = order.select_all


