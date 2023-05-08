from odoo import models, fields
class planeaf_vol(models.Model):
    _name = 'planeaf.vol'
    codi = fields.Integer('Codi', required=True)
    passatgers = fields.Integer('Passatgers', required=True)
    dataSortida = fields.Date('Data de Sortida', required=True)
    dataArribada = fields.Date("Data d'arribada", required=True)