from odoo import models, fields     
class zooaf_animal(models.Model): 
    _name = 'zooaf.animal' 
    name = fields.Char(compute='_get_name', string='Identificador', readonly='true', store=False)
    continentOrigen = fields.Char("Continent d'origen", required=True)
    dataNaix = fields.Date("Data de naixement", required=True)
    paisOrigen = fields.Char("Pais d'origen", required=True)
    sexe = fields.Char("Sexe", required=True)
    zoo_id = fields.Many2one('zooaf.zoo', string='Zoo')
    especie_id = fields.Many2one('zooaf.especie', string='Espècie')

    def _get_name(self):
        for record in self:
            record.name = str(record.id)