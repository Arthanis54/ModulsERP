from odoo import models, fields
class planeaf_vol(models.Model):
    _name = 'planeaf.vol'
    name = fields.Char(compute='_get_name', string='Id', readonly='true', store=False)
    passatgers = fields.Integer('Passatgers', required=True)
    dataSortida = fields.Date('Data de Sortida', required=True)
    dataArribada = fields.Date("Data d'arribada", required=True)
    avio_id = fields.Many2one('planeaf.avio', string='Avió')
    aeroportOrigen_id = fields.Many2one('planeaf.aeroport', string='Aeroport Origen')
    aeroportDesti_id = fields.Many2one('planeaf.aeroport', string='Aeroport Desti')
    pilot_id = fields.Many2one('planeaf.pilot', string='Pilot')

    def _get_name(self):
        for record in self:
            record.name = str(record.id)