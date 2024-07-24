from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    bahan = fields.Char(string='Bahan')
    warna = fields.Char(string='Warna')
    ukuran = fields.Char(string='Ukuran')
    tanggal_kadaluarsa = fields.Date(string='Tanggal Kadaluarsa')
    instruksi_perawatan = fields.Text(string='Instruksi Perawatan')
    status_ketersediaan = fields.Selection([
    ('available', 'Tersedia'),
    ('out_of_stock', 'Tidak Tersedia')
    ], string='Status Ketersediaan')
    lokasi_penyimpanan = fields.Char(string='Lokasi Penyimpanan')
    kondisi_produk = fields.Selection([
        ('new', 'Baru'),
        ('used', 'Bekas'),
        ('refurbished', 'Rekondisi')
    ], string='Kondisi Produk')
    merk = fields.Char(string='Merk')
    deskripsi_produk = fields.Text(string='Deskripsi Produk')
