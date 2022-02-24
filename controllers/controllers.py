# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo58(http.Controller):
#     @http.route('/odoo58/odoo58/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo58/odoo58/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo58.listing', {
#             'root': '/odoo58/odoo58',
#             'objects': http.request.env['odoo58.odoo58'].search([]),
#         })

#     @http.route('/odoo58/odoo58/objects/<model("odoo58.odoo58"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo58.object', {
#             'object': obj
#         })
