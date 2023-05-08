from odoo import models, fields
class planeaf_avio(models.Model):
    _name = 'planeaf.avio'
    codi = fields.Integer('Codi', required=True)
    imatge = fields.Char('Imatge')
    marca = fields.Integer('Marca')
    model = fields.Char('Model')
    maxVel = fields.Float('Màxima velocitat')