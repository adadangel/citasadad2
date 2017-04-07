# -*- coding: utf-8 -*-
from odoo import http

# class Citasadad(http.Controller):
#     @http.route('/citasadad/citasadad/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/citasadad/citasadad/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('citasadad.listing', {
#             'root': '/citasadad/citasadad',
#             'objects': http.request.env['citasadad.citasadad'].search([]),
#         })

#     @http.route('/citasadad/citasadad/objects/<model("citasadad.citasadad"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('citasadad.object', {
#             'object': obj
#         })