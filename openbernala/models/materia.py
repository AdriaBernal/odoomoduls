# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.exceptions import ValidationError


class Materia(models.Model):
    _name = 'openbernala.materia'
    _description = 'Matària OpenBernalA'

    name = fields.Char(string = 'Matèria', required = True)
    
    description = fields.Text(string = 'Descripció')

    num_alumnes = fields.Integer(string = 'Número d\'alumnes')

    curs_ids = fields.Many2one(
        'openbernala.curs',
        string = 'Curs',
        ondelete = 'cascade'
    )

    professor_ids = fields.Many2many(
        'openbernala.professor',
        string='Professors'
    )

    @api.constrains('num_alumnes')
    def _check_num_alumnes(self):
        for record in self:
            if record.num_alumnes < 0:
                raise ValidationError('El número d\'alumnes no pot ser negatiu.')
