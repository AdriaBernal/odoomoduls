# -*- coding: utf-8 -*-
# from odoo import http


# class Openbernala(http.Controller):
#     @http.route('/openbernala/openbernala', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openbernala/openbernala/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('openbernala.listing', {
#             'root': '/openbernala/openbernala',
#             'objects': http.request.env['openbernala.openbernala'].search([]),
#         })

#     @http.route('/openbernala/openbernala/objects/<model("openbernala.openbernala"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openbernala.object', {
#             'object': obj
#         })

