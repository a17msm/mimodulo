# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Animal(models.Model):
    _name = 'mimodulo.animal'
    _description = 'Animal acogido'

    name = fields.Char('Nombre o identificador')
    species = fields.Char('Especie')
    age = fields.Integer('Edad')
    sex = fields.Char('Sexo')
    dateIn = fields.Date('Fecha de ingreso')
    instalacion_id = fields.Many2one('mimodulo.instalacion', string='Instalación', ondelete='restrict')
    state = fields.Selection([
        ('apto', 'Apto'),
        ('noApto', 'No apto')],
        'Liberación', default="noApto")

    @api.model
    def change_state(self, new_state):
        for animal in self:
            animal.state = new_state
    
    def apto(self):
        self.change_state('apto')

    def noApto(self):
        self.change_state('noApto')