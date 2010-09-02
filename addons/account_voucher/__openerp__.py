# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
    "name" : "Accounting Voucher Entries",
    "version" : "1.0",
    "author" : 'OpenERP SA & Axelor',
    "description": """Account Voucher module includes all the basic requirements of
    Voucher Entries for Bank, Cash, Sales, Purchase, Expanse, Contra, etc...
    * Voucher Entry
    * Voucher Receipt
    * Cheque Register
    """,
    "category" : "Generic Modules/Accounting",
    "website" : "http://tinyerp.com",
    "depends" : ["account"],
    "init_xml" : [],

    "demo_xml" : [],

    "update_xml" : [
        "security/ir.model.access.csv",
        "voucher_sequence.xml",
        "voucher_workflow.xml",
        "voucher_report.xml",
        "wizard/account_voucher_open_view.xml",
        "wizard/account_voucher_unreconcile_view.xml",
        "voucher_view.xml",
        "voucher_payment_receipt_view.xml",
        "voucher_sales_purchase_view.xml",
        "voucher_wizard.xml",
    ],
    "test" : [
#         "test/account_voucher.yml",
          "test/sales_receipt.yml",
          "test/sales_payment.yml",
    ],

    'certificate': '0037580727101',
    "active": False,
    "installable": True,
}
