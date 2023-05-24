from odoo import models, fields
class zooaf_zoo(models.Model):
    _name = 'zooaf.zoo'
    name = fields.Char(compute='_get_name', string='Id', readonly='true', store=False)
    nom = fields.Char('Nom', required=True)
    grandaria = fields.Float('Grandària', required=True)
    ciutat = fields.Char('Ciutat', required=True)
    pais = fields.Char('Pais', required=True)
    animal_ids = fields.One2many('zooaf.animal','zoo_id', string='Animals')

    def _get_name(self):
        for record in self:
            record.name = str(record.nom)