# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010 Eric CAUDAL.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################


{
    'name': 'Account Analytic Default',
    'version': '1.0',
    'category': 'Generic Modules/Accounting',
    'description': """
Allows to automatically select analytic accounts based on criterions:
* Category
* Product
* Partner
* User
* Company
* Date
    """,
    'author': 'Eric CAUDAL',
    'website': '',
    'depends': ['account', 'sale'],
    'init_xml': [],
    'update_xml': ['account_analytic_default_category_view.xml'],
    'demo_xml': [],
    'installable': True,
    'active': False,
    'certificate': '',
}