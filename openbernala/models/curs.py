# -*- coding: utf-8 -*-

from odoo import models, fields


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

    inici_curs = fields.Date(string = 'Inici del curs')

    materia_ids = fields.One2many(
        'openbernala.materia',
        'curs_id',
        string = 'Matèries'
    )
