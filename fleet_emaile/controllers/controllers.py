# -*- coding: utf-8 -*-
# from odoo import http


# class FleetEmaile(http.Controller):
#     @http.route('/fleet_emaile/fleet_emaile', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fleet_emaile/fleet_emaile/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fleet_emaile.listing', {
#             'root': '/fleet_emaile/fleet_emaile',
#             'objects': http.request.env['fleet_emaile.fleet_emaile'].search([]),
#         })

#     @http.route('/fleet_emaile/fleet_emaile/objects/<model("fleet_emaile.fleet_emaile"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fleet_emaile.object', {
#             'object': obj
#         })

