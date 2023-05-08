from odoo import models, fields     
class planeaf_aeroport(models.Model): 
    _name = 'planeaf.aeroport' 
    codi = fields.Integer('Codi', required=True)
    nom = fields.Char("Nom", required=True)
    imatge = fields.Char("Imatge")
    ciutat = fields.Char("Ciutat")
    pais = fields.Char("Pais")
    latitud = fields.Float("Latitud")
    longitud = fields.Float("Longitud")  