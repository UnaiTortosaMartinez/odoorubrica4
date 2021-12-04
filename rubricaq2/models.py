# -*- coding: utf-8 -*-
import random
from odoo import models, fields, api


class Persona(models.Model):
    _name ="persona"
    nombre = fields.Char(string='nombre')
    direccion = fields.Char(string='direccion')
    telefono = fields.Char(string='telefono')

class Estudiante(models.Model):
    _inherit = 'persona'
    _name = "estudiante"
    portatiles  = fields.One2many('portatil',
                                'estudiante_id',
                                string="Portatiles asociados")
    ofertas = fields.Boolean()

class Portatil(models.Model):
    _name = "portatil"
    modelo = fields.Char(string='modelo');
    marca = fields.Char(string='marca')
    cpu = fields.Char(string='cpu')
    fechaAdquisicion = fields.Date(string='fechaAdquisición')
    tiempousoestimado = fields.Float(string='tiempousoestimado')
    vendido = fields.Boolean(string='vendido')
    comprador = fields.Char(string='comprador')
    precioventa = fields.Float(string='')
    campoobservaciones = fields.Text(string='campoobservaciones')
    estudiante_id = fields.Many2one("estudiante", "Estudiante asociados")

