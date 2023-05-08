from odoo import models, fields     
class zooaf_especie(models.Model): 
    _name = 'zooaf.especie' 
    id = fields.Integer('Id', required=True) 
    familia = fields.Char("Família", required=True)
    nomCientific = fields.Char("Nom científic", required=True)
    nomVulgar = fields.Char("Nom vulgar", required=True)
    perill = fields.Char("Perill", required=True)