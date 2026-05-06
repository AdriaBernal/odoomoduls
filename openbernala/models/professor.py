# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Professor(models.Model):
    _name = 'openbernala.professor'
    _description = 'Professor OpenBernalA'

    name = fields.Char(string = 'Nom', required = True)
    
    description = fields.Text(string = 'Descripció')

    email = fields.Char(string = 'Correu electrònic')

    baixa = fields.Boolean(string = 'Baixa')

    materia_ids = fields.Many2many(
        'openbernala.materia',
        string='Matèries'
    )

    @api.constrains('email')
    def _check_unique_email(self):
        for record in self:
            if record.email:
                existing_professor = self.search([('email', '=', record.email), ('id', '!=', record.id)])
                if existing_professor:
                    raise ValidationError('El correu electrònic ja està en ús per un altre professor.')