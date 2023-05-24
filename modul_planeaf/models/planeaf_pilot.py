from odoo import models, fields     
class planeaf_pilot(models.Model): 
    _name = 'planeaf.pilot' 
    name = fields.Char(compute='_get_name', string='Nom i Cognoms', readonly='true', store=False)
    nom = fields.Char("Nom", required=True)
    cognoms = fields.Char("Cognoms", required=True)
    nif = fields.Char("NIF", required=True)
    telf = fields.Char("Telf")
    email = fields.Char("Email")
    vol_id = fields.One2many('planeaf.vol', 'pilot_id', string='Vol')

    def _get_name(self):
        for record in self:
            record.name = str(record.nom) + " " + str(record.cognoms)