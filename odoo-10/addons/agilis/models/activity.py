# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Activity(models.Model):

    _name = 'agilis.activity'

    deliverable_id = fields.Many2one('agilis.deliverable',
                        string="Entregable",
                        ondelete='cascade',
                        required=True )

    name = fields.Char(string="Nombre de Actividad", 
                        required=True)

    cooperativista_id = fields.Many2one('res.users', 
                        string="Cooperativista",
                        ondelete='cascade',
                        required=True)

    journals = fields.Integer(string="N Jornadas Planificadas", 
                        required=True)

    project_id = fields.Many2one('agilis.project',
                        ondelete='cascade', 
                        string="Proyecto")
