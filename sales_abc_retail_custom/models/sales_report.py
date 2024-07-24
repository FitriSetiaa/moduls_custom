from odoo import models, fields, api, tools
from datetime import datetime, timedelta

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    expiring_7_days = fields.Boolean(compute='_compute_expiry', store=True, string='Expiring in 7 Days')
    expiring_1_month = fields.Boolean(compute='_compute_expiry', store=True, string='Expiring in 1 Month')

    @api.model
    def get_product_expiry_data(self):
        products = self.search([])
        report_data = []
        for product in products:
            report_data.append({
                'name': product.name,
                'tanggal_kadaluarsa': product.tanggal_kadaluarsa,
            })
        return report_data 
    
    @api.depends('tanggal_kadaluarsa')
    def _compute_expiry(self):
        today = fields.Date.today()
        for product in self:
            if product.tanggal_kadaluarsa:
                product.expiring_7_days = today <= product.tanggal_kadaluarsa <= today + timedelta(days=7)
                product.expiring_1_month = today <= product.tanggal_kadaluarsa <= today + timedelta(days=30)
            else:
                product.expiring_7_days = False
                product.expiring_1_month = False

class LaporanBarangTerlaris(models.Model):
    _name = 'laporan.barang.terlaris'
    _description = 'Laporan Barang Terlaris'
    _auto = False

    produk_id = fields.Many2one('product.product', string='Produk')
    jumlah_terjual = fields.Float(string='Jumlah Terjual')
    kategori_produk = fields.Many2one('product.category', string='Kategori')
    tanggal_penjualan = fields.Date(string='Tanggal Penjualan')

    def _select(self):
        return """
            SELECT
                MIN(l.id) as id,
                l.product_id as produk_id,
                SUM(l.product_uom_qty) as jumlah_terjual,
                pt.categ_id as kategori_produk,
                s.date_order::date as tanggal_penjualan
            """

    def _from(self):
        return """
            FROM sale_order_line l
            JOIN sale_order s ON l.order_id = s.id
            JOIN product_product p ON l.product_id = p.id
            JOIN product_template pt ON p.product_tmpl_id = pt.id
            """

    def _group_by(self):
        return """
            GROUP BY
                l.product_id,
                pt.categ_id,
                s.date_order::date
            """

    @api.model
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute(f"""
            CREATE or REPLACE VIEW {self._table} as (
                {self._select()}
                {self._from()}
                {self._group_by()}
            )
        """)