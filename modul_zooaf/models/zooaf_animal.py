from odoo import models, fields     
class zooaf_animal(models.Model): 
    _name = 'zooaf.animal' 
    id = fields.Integer('Id', required=True)
    continentOrigen = fields.Char("Continent d'origen", required=True)
    dataNaix = fields.Date("Data de naixement", required=True)
    paisOrigen = fields.Char("Pais d'origen", required=True)
    sexe = fields.Char("Sexe", required=True)    