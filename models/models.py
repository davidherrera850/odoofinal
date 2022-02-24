# -*- coding: utf-8 -*-

from odoo import models, fields, api

class odoo58(models.Model):
	_name = 'odoo58.odoo58'
	_description = 'odoo58.odoo58'

	name = fields.Char('DNI',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	pais = fields.Char(string='pais',required=True)


	torneos_ids = fields.Many2many('odoo58.torneo','jugadores_ids', string='torneos')

class torneo(models.Model):
	_name = 'odoo58.torneo'
	_description = 'odoo58.torneo'

	name = fields.Char('codtorneo',required=True)
	nombretorneo = fields.Char(string='nombretorneo',required=True)
	nparticipantes = fields.Char(string='nparticipantes',required=True)

	jugadores_ids = fields.Many2many('odoo58.odoo58', string='Numero jugadores')
	arbitros_ids = fields.Many2many('odoo58.arbitro', string='Nombre arbitro')





class arbitro(models.Model):
	_name = 'odoo58.arbitro'
	_description = 'odoo58.arbitro'

	name = fields.Char('codarbitro',required=True)
	nombrearbitro = fields.Char(string='nombrearbitro',required=True)
	origen = fields.Char(string='origen',required=True)

	torneos1_ids = fields.Many2many('odoo58.torneo','arbitros_ids', string='Nombre torneo')
	partidas_ids = fields.One2many('odoo58.partida', 'arbitro_id', string='nombre partida')


class partida(models.Model):
	_name = 'odoo58.partida'
	_description = 'odoo58.partida'

	name = fields.Char('codpartida',required=True)
	ronda = fields.Char(string='ronda',required=True)
	njugadas = fields.Char(string='njugadas',required=True)

	arbitro_id = fields.Many2one('odoo58.arbitro', string='nombre arbitro')
	movimiento_ids = fields.One2many('odoo58.movimiento', 'partida1_id', string='movimiento')
	salas_ids = fields.One2many('odoo58.sala', 'partida2_id', string='sala')


class sala(models.Model):
	_name = 'odoo58.sala'
	_description = 'odoo58.sala'

	name = fields.Char('codsala',required=True)
	nombresala = fields.Char(string='nombresala',required=True)
	mesa = fields.Char(string='mesa',required=True)

	partida2_id = fields.Many2one('odoo58.partida', string='Parti')

class movimiento(models.Model):
	_name = 'odoo58.movimiento'
	_description = 'odoo58.movimiento'

	name = fields.Char('codmovimiento',required=True)
	piezamovida = fields.Char(string='piezamovida',required=True)
	captura = fields.Char(string='captura',required=True)

	partida1_id = fields.Many2one('odoo58.partida', string='Partida')





#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
