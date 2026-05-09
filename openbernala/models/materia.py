# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Materia(models.Model):
    _name = 'openbernala.materia'
    _description = 'Matària OpenBernalA'

    name = fields.Char(string = 'Matèria', required = True)
    
    description = fields.Text(string = 'Descripció')

    num_alumnes = fields.Integer(string = 'Número d\'alumnes')

    curs_id = fields.Many2many(
        'openbernala.curs',
        string = 'Curs',
        ondelete = 'cascade'
    )

    professor_ids = fields.Many2many(
        'openbernala.professor',
        string='Professors'
    )

    total_alumnes = fields.Integer(
        string='Total d\'alumnes',
        compute='_compute_total_alumnes',
    )

    @api.constrains('num_alumnes')
    def _check_num_alumnes(self):
        for record in self:
            if record.num_alumnes < 0:
                raise ValidationError('El número d\'alumnes no pot ser negatiu.')
            
    @api.depends('num_alumnes')
    def _compute_total_alumnes(self):
        for record in self:
            record.total_alumnes = record.num_alumnes
