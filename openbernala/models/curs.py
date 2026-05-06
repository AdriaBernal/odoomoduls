# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Curs(models.Model):
    _name = 'openbernala.curs'
    _description = 'Curs OpenBernalA'

    name = fields.Char(string = 'Nom', required = True)
    
    description = fields.Text(string = 'Descripció')

    nivell = fields.Selection([
        ('eso', 'ESO'),
        ('batx', 'BATX'),
        ('cfgm', 'CFGM'),
        ('cfgs', 'CFGS'),
    ], string = 'Nivell')

    num_alumnes = fields.Integer(string = 'Nombre d\'alumnes')

    total_alumnes_materies = fields.Integer(
        string = 'Total d\'alumnes (Matèries)',
        compute = '_compute_total_alumnes_materies',
        store=True
    )

    inici_curs = fields.Date(string = 'Inici del curs')

    materia_ids = fields.Many2many(
        'openbernala.materia',
        'curs_id',
        string = 'Matèries'
    )

    @api.depends('materia_ids.num_alumnes')
    def _compute_total_alumnes_materies(self):
        for record in self:
            record.total_alumnes_materies = sum(record.materia_ids.mapped('num_alumnes'))
    
    @api.constrains('name')
    def _check_name(self):
        for record in self:
            if self.search_count([('name', '=', record.name)]) > 1:
                raise ValidationError('El nom del curs ja existeix. Si us plau, tria un nom diferent.')