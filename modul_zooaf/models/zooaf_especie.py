from odoo import models, fields     
class zooaf_especie(models.Model): 
    _name = 'zooaf.especie'
    name = fields.Char(compute='_get_name', string='Id', readonly='true', store=False)
    familia = fields.Char("Família", required=True)
    nomCientific = fields.Char("Nom científic", required=True)
    nomVulgar = fields.Char("Nom vulgar", required=True)
    perill = fields.Char("Perill", required=True)
    especie_ids = fields.One2many('zooaf.animal','especie_id', string='Animals')

    def _get_name(self):
        for record in self:
            record.name = str(record.nomCientific)