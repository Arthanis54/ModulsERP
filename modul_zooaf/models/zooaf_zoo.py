from odoo import models, fields
class zooaf_zoo(models.Model):
    _name = 'zooaf.zoo'
    id = fields.Integer('Id', required=True)
    nom = fields.Char('Nom', required=True)
    grandaria = fields.Float('Grandària', required=True)
    ciutat = fields.Char('Ciutat', required=True)
    pais = fields.Char('Pais', required=True)