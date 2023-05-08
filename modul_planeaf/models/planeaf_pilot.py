from odoo import models, fields     
class planeaf_pilot(models.Model): 
    _name = 'planeaf.pilot' 
    codi = fields.Integer('Codi', required=True) 
    nom = fields.Char("Nom", required=True)
    cognoms = fields.Char("Cognoms", required=True)
    nif = fields.Char("NIF", required=True)
    telf = fields.Char("Telf")
    email = fields.Char("Email")