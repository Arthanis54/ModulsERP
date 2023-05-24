from odoo import models, fields
class planeaf_avio(models.Model):
    _name = 'planeaf.avio'
    name = fields.Char(compute='_get_name', string='Id', readonly='true', store=False)
    imatge = fields.Char('Imatge')
    marca = fields.Integer('Marca')
    model = fields.Char('Model')
    maxVel = fields.Float('Màxima velocitat')
    vol_id = fields.One2many('planeaf.vol', 'avio_id', string='Vol')

    def _get_name(self):
        for record in self:
            record.name = str(record.id)