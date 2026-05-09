# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Professor(models.Model):
    _name = 'openbernala.professor'
    _description = 'Professor OpenBernalA'

    name = fields.Char(string = 'Nom', required = True)

    cognoms = fields.Char(string = 'Cognoms', required = True)

    email = fields.Char(string = 'Correu electrònic')

    telefon = fields.Char(string = 'Telèfon')

    baixa = fields.Boolean(string = 'Baixa')

    materia_ids = fields.Many2many(
        'openbernala.materia',
        string='Matèries'
    )

    display_name = fields.Char(
        string='Nom complet',
        compute='_get_display_name'
    )

    def _get_display_name(self):
        for record in self:
            record.display_name = (record.name or '') + " " + (record.cognoms or '')

    @api.constrains('email')
    def _check_unique_email(self):
        for record in self:
            if record.email:
                existing_professor = self.search([('email', '=', record.email), ('id', '!=', record.id)])
                if existing_professor:
                    raise ValidationError('El correu electrònic ja està en ús per un altre professor.')

    def action_baixa(self):
        for record in self:
            record.baixa = True

    def action_alta(self):
        for record in self:
            record.baixa = False