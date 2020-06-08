# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Instalacion(models.Model):
    _name = 'mimodulo.instalacion'

    name = fields.Char('Instalación')
    capacity = fields.Integer('Capacidad')
    size = fields.Integer('Tamaño (m2)')
    animal_id = fields.One2many('mimodulo.animal', 'instalacion_id', string='Animales en esta instalación')
    count = fields.Integer(compute='count_animal', string='Animales en esta instalación')
    room = fields.Integer(compute='capacidad_restante', string='Capacidad restante')


    def count_animal(self):
        for animal in self:
            for animal in self:
                animal.count = self.env['mimodulo.animal'].search_count([('instalacion_id', '=', self.id)])

    def capacidad_restante(self):
        self.room = self.capacity - self.count