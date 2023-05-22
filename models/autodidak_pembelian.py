from odoo import models, fields, api, _
from datetime import date, datetime

class autodidak_pembelian(models.Model):
    _name = 'autodidak.pembelian'

    name = fields.Char(string='Name')
    tanggal = fields.Date(string="Tanggal")
    status = fields.Selection([('draft','Draft'),('to_approve','To Approve'),('approved','Approved'),('done','Done')])
    autodidak_pembelian_ids = fields.One2many('autodidak.pembelian.line',  'autodidak_pembelian_id', string="Autodidak Pembelian Ids")
    brand_ids = fields.Many2many('autodidak.brand', 'autodidak_pembelian_brand_rel', 'autodidak_pembelian_id', 'brand_id', string="Brand Ids")

class autodidak_pembelian_line(models.Model):
    _name = 'autodidak.pembelian.line'

    name = fields.Char(string='Name')
    autodidak_pembelian_id = fields.Many2one('autodidak.pembelian', string="Autodidak Pembelian Id")
    product_id = fields.Many2one('product.product', string="Product Id")
    quantity = fields.Float(string='Quantity', default=0.0)
    uom_id = fields.Many2one('uom.uom', string="Uom Id")

class autodidak_brand(models.Model):
    _name = 'autodidak.brand'

    name = fields.Char(string='Name')