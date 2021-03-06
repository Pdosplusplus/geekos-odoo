# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Disease(models.Model):

    _name = 'sigesalud.disease'

    name = fields.Char(string="Nombre de Enfermedad", 
                       required=True)

    expedient_id = fields.Many2one('sigesalud.expedient',
                         ondelete='cascade', 
                         string="Expediente")

    beneficiary_id = fields.Many2one('sigesalud.beneficiary',
                         ondelete='cascade', 
                         string="Beneficiario")

