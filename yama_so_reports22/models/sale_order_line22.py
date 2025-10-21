from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'


    # is_subtotal_merge = fields.Boolean(string='Subtotal Merge', default=False,
    #                              help='If checked, this line will be merged with other selected lines in the PDF report, showing a summed subtotal.')

    x_studio_related_field_1vq_1j310c68a = fields.Selection(
        string='Approval',
        selection=[('UL', 'UL'),
                   ('FM', 'FM'),
                   ('UL/FM', 'UL/FM'),
                   ],)

    x_studio_related_field_94b_1j312kksb = fields.Char(
        string=' Brand')



class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    @api.model
    def create(self, vals):
        record = super(IrAttachment, self).create(vals)
        if record.res_model == 'product.template' and record.mimetype == 'application/pdf':
            record.sudo().write({'public': True})
        return record