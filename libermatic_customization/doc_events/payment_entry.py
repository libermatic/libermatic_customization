# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe

from sms_extras.api.sms import get_sms_text, request_sms


def on_submit(doc, method):
    template = frappe.db.get_value(
        'Libermatic Settings', None, 'invoice_paid_sms',
    )
    if not template or _template_is_disabled(template):
        return
    for ref in doc.references:
        if ref.reference_doctype == 'Sales Invoice':
            si = frappe.get_doc('Sales Invoice', ref.reference_name)
            if not si.contact_mobile or si.status != 'Paid':
                continue
            try:
                content = get_sms_text(template, si)
                subject = 'SMS: {} to {}'.format(
                    template, si.contact_display or '☺'
                )
                if content:
                    request_sms(
                        si.contact_mobile,
                        content,
                        communication={
                            'subject': subject,
                            'reference_doctype': 'Sales Invoice',
                            'reference_name': ref.reference_name,
                        }
                    )
            except TypeError:
                frappe.log_error(frappe.get_traceback())


def _template_is_disabled(template):
    return frappe.db.get_value('SMS Template', template, 'disabled')
