from odoo import models, fields     
class planeaf_aeroport(models.Model): 
    _name = 'planeaf.aeroport'
    name = fields.Char(compute='_get_name', string='Nom', readonly='true', store=False)
    nom = fields.Char("Nom", required=True)
    imatge = fields.Char("Imatge")
    ciutat = fields.Char("Ciutat")
    pais = fields.Char("Pais")
    latitud = fields.Float("Latitud")
    longitud = fields.Float("Longitud")
    volOrigen_id = fields.One2many('planeaf.vol', 'aeroportOrigen_id', string='Origen')
    volDesti_id = fields.One2many('planeaf.vol', 'aeroportDesti_id', string='Desti')

    def _get_name(self):
        for record in self:
            record.name = str(record.nom)