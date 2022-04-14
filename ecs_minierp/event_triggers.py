from __future__ import unicode_literals
import frappe
from frappe import auth
import datetime
import json, ast


################ Quotation
@frappe.whitelist()
def quot_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def quot_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def quot_onload(doc, method=None):
    pass
@frappe.whitelist()
def quot_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def quot_validate(doc, method=None):
    pass
@frappe.whitelist()
def quot_on_submit(doc, method=None):
    pass
@frappe.whitelist()
def quot_on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def quot_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def quot_before_save(doc, method=None):
    pass
@frappe.whitelist()
def quot_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def quot_on_update(doc, method=None):
    pass


################ Sales Order
@frappe.whitelist()
def so_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def so_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def so_onload(doc, method=None):
    pass
@frappe.whitelist()
def so_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def so_validate(doc, method=None):
    pass
@frappe.whitelist()
def so_on_submit(doc, method=None):
    pass
@frappe.whitelist()
def so_on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def so_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def so_before_save(doc, method=None):
    pass
@frappe.whitelist()
def so_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def so_on_update(doc, method=None):
    pass


################ Delivery Note
@frappe.whitelist()
def dn_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def dn_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def dn_onload(doc, method=None):
    pass
@frappe.whitelist()
def dn_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def dn_validate(doc, method=None):
    pass
@frappe.whitelist()
def dn_on_submit(doc, method=None):
    pass
@frappe.whitelist()
def dn_on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def dn_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def dn_before_save(doc, method=None):
    pass
@frappe.whitelist()
def dn_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def dn_on_update(doc, method=None):
    pass

################ Sales Invoice
@frappe.whitelist()
def siv_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def siv_after_insert(doc, method=None):
    pass
def siv_onload(doc, method=None):
    pass
@frappe.whitelist()
def siv_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def siv_validate(doc, method=None):
    pass
@frappe.whitelist()
def siv_on_submit(doc, method=None):
    pass
@frappe.whitelist()
def siv_on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def siv_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def siv_before_save(doc, method=None):
    pass
@frappe.whitelist()
def siv_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def siv_on_update(doc, method=None):
    pass


################ Payment Entry
@frappe.whitelist()
def pe_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def pe_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def pe_onload(doc, method=None):
    pass
@frappe.whitelist()
def pe_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def pe_validate(doc, method=None):
    pass
@frappe.whitelist()
def pe_on_submit(doc, method=None):
    pass
@frappe.whitelist()
def pe_on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def pe_on_update_after_submit(doc, method=None):

################################################ Start Of CHEQUES code #################################################
    default_payback_cheque_wallet_account = frappe.db.get_value("Company", doc.company,
                                                                "default_payback_cheque_wallet_account")
    default_rejected_cheque_account = frappe.db.get_value("Company", doc.company, "default_rejected_cheque_account")
    default_cash_account = frappe.db.get_value("Company", doc.company, "default_cash_account")
    default_bank_commissions_account = frappe.db.get_value("Company", doc.company, "default_bank_commissions_account")

    if not doc.cheque_bank and doc.cheque_action == "إيداع شيك تحت التحصيل":
        frappe.throw(_(" برجاء تحديد البنك والحساب البنكي "))

    if not doc.bank_acc and doc.cheque_action == "إيداع شيك تحت التحصيل":
        frappe.throw(_("برجاء تحديد الحساب البنكي"))

    if not doc.account and doc.cheque_action == "إيداع شيك تحت التحصيل" and doc.with_bank_commission:
        frappe.throw(_(" برجاء تحديد الحساب الجاري داخل الحساب البنكي وإعادة إختيار الحساب البنكي مرة أخرى "))

    if not doc.account and doc.cheque_action == "صرف شيك تحت التحصيل":
        frappe.throw(_(" برجاء تحديد الحساب الجاري داخل الحساب البنكي وإعادة إختيار الحساب البنكي مرة أخرى "))

    if not doc.account and doc.cheque_action == "رفض شيك تحت التحصيل" and doc.with_bank_commission:
        frappe.throw(_(" برجاء تحديد الحساب الجاري داخل الحساب البنكي وإعادة إختيار الحساب البنكي مرة أخرى "))

    if not doc.account and doc.cheque_action == "صرف الشيك":
        frappe.throw(_(" برجاء تحديد الحساب الجاري داخل الحساب البنكي وإعادة إختيار الحساب البنكي مرة أخرى "))

    if not doc.collection_fee_account and doc.cheque_action == "إيداع شيك تحت التحصيل":
        frappe.throw(_(" برجاء تحديد حساب برسم التحصيل داخل الحساب البنكي وإعادة إختيار الحساب البنكي مرة أخرى "))

    if not doc.collection_fee_account and doc.cheque_action == "صرف شيك تحت التحصيل":
        frappe.throw(_(" برجاء تحديد حساب برسم التحصيل داخل الحساب البنكي وإعادة إختيار الحساب البنكي مرة أخرى "))

    if not doc.collection_fee_account and doc.cheque_action == "رفض شيك تحت التحصيل":
        frappe.throw(_(" برجاء تحديد حساب برسم التحصيل داخل الحساب البنكي وإعادة إختيار الحساب البنكي مرة أخرى "))

    if not doc.payable_account and doc.cheque_action == "صرف الشيك":
        frappe.throw(_(" برجاء تحديد حساب برسم الدفع داخل الحساب البنكي وإعادة إختيار الحساب البنكي مرة أخرى "))

    if doc.cheque_action == "تحويل إلى حافظة شيكات أخرى":
        new_mode_of_payment_account = frappe.db.get_value('Mode of Payment Account',
                                                          {'parent': doc.new_mode_of_payment}, 'default_account')
        old_mode_of_payment_account = frappe.db.get_value("Mode of Payment Account", {'parent': doc.mode_of_payment},
                                                          'default_account')
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action = "" where name = %s""", doc.name)
        if not new_mode_of_payment_account == old_mode_of_payment_account:
            accounts = [
                {
                    "doctype": "Journal Entry Account",
                    "account": new_mode_of_payment_account,
                    "credit": 0,
                    "debit": doc.paid_amount,
                    "debit_in_account_currency": doc.paid_amount,
                    "user_remark": doc.name
                },
                {
                    "doctype": "Journal Entry Account",
                    "account": old_mode_of_payment_account,
                    "credit": doc.paid_amount,
                    "debit": 0,
                    "credit_in_account_currency": doc.paid_amount,
                    "user_remark": doc.name
                }
            ]
            new_doc = frappe.get_doc({
                "doctype": "Journal Entry",
                "voucher_type": "Bank Entry",
                "reference_doctype": "Payment Entry",
                "reference_link": doc.name,
                "cheque_no": doc.reference_no,
                "cheque_date": doc.reference_date,
                "pe_status": "حافظة شيكات واردة",
                "posting_date": doc.cheque_action_date,
                "accounts": accounts,
                "payment_type": doc.payment_type,
                "user_remark": doc.party_name

            })
            new_doc.insert()
            new_doc.submit()
        # frappe.db.sql(""" update `tabPayment Entry` set cheque_action_date = NULL where name = %s""", doc.name)
        # doc.reload()

        x = str(doc.logs) + "\n" + str(doc.new_mode_of_payment) + " " + str(doc.cheque_action_date)
        frappe.db.set_value('Payment Entry', doc.name, 'logs', x)
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action = "" where name = %s""", doc.name)
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action_date = NULL where name = %s""", doc.name)
        doc.reload()

    if doc.cheque_action == "تحصيل فوري للشيك":
        frappe.db.sql("""update `tabPayment Entry` set clearance_date = %s where name=%s """,
                      (doc.cheque_action_date, doc.name))
        frappe.db.sql(""" update `tabPayment Entry` set cheque_status = "محصل فوري" where name = %s""", doc.name)
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action = "" where name = %s""", doc.name)
        accounts = [
            {
                "doctype": "Journal Entry Account",
                "account": default_cash_account,
                "credit": 0,
                "debit": doc.paid_amount,
                "debit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            },
            {
                "doctype": "Journal Entry Account",
                "account": doc.paid_to,
                "credit": doc.paid_amount,
                "debit": 0,
                "credit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            }
        ]
        new_doc = frappe.get_doc({
            "doctype": "Journal Entry",
            "voucher_type": "Bank Entry",
            "reference_doctype": "Payment Entry",
            "reference_link": doc.name,
            "cheque_no": doc.reference_no,
            "cheque_date": doc.reference_date,
            "pe_status": "محصل فوري",
            "posting_date": doc.cheque_action_date,
            "accounts": accounts,
            "payment_type": doc.payment_type,
            "user_remark": doc.party_name

        })
        new_doc.insert()
        new_doc.submit()
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action_date = NULL where name = %s""", doc.name)
        doc.reload()

    if doc.cheque_action == "إيداع شيك تحت التحصيل" and doc.with_bank_commission and not doc.cheque_status == "مرفوض بالبنك":
        frappe.db.sql(""" update `tabPayment Entry` set cheque_status = "تحت التحصيل" where name = %s""", doc.name)
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action = "" where name = %s""", doc.name)
        accounts = [
            {
                "doctype": "Journal Entry Account",
                "account": doc.collection_fee_account,
                "credit": 0,
                "debit": doc.paid_amount,
                "debit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            },
            {
                "doctype": "Journal Entry Account",
                "account": default_bank_commissions_account,
                "credit": 0,
                "debit": doc.co3_,
                "debit_in_account_currency": doc.co3_,
                "user_remark": doc.name
            },
            {
                "doctype": "Journal Entry Account",
                "account": doc.paid_to,
                "debit": 0,
                "credit": doc.paid_amount,
                "credit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            },
            {
                "doctype": "Journal Entry Account",
                "account": doc.account,
                "debit": 0,
                "credit": doc.co3_,
                "credit_in_account_currency": doc.co3_,
                "user_remark": doc.name
            }
        ]
        new_doc = frappe.get_doc({
            "doctype": "Journal Entry",
            "voucher_type": "Bank Entry",
            "reference_doctype": "Payment Entry",
            "reference_link": doc.name,
            "cheque_no": doc.reference_no,
            "cheque_date": doc.reference_date,
            "pe_status": "تحت التحصيل",
            "posting_date": doc.cheque_action_date,
            "accounts": accounts,
            "payment_type": doc.payment_type,
            "user_remark": doc.party_name
        })
        new_doc.insert()
        new_doc.submit()
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action_date = NULL where name = %s""", doc.name)
        doc.reload()

    if doc.cheque_action == "إيداع شيك تحت التحصيل" and not doc.with_bank_commission and not doc.cheque_status == "مرفوض بالبنك":
        frappe.db.sql(""" update `tabPayment Entry` set cheque_status = "تحت التحصيل" where name = %s""", doc.name)
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action = "" where name = %s""", doc.name)
        accounts = [
            {
                "doctype": "Journal Entry Account",
                "account": doc.collection_fee_account,
                "credit": 0,
                "debit": doc.paid_amount,
                "debit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            },
            {
                "doctype": "Journal Entry Account",
                "account": doc.paid_to,
                "debit": 0,
                "credit": doc.paid_amount,
                "credit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            }
        ]
        new_doc = frappe.get_doc({
            "doctype": "Journal Entry",
            "voucher_type": "Bank Entry",
            "reference_doctype": "Payment Entry",
            "reference_link": doc.name,
            "cheque_no": doc.reference_no,
            "cheque_date": doc.reference_date,
            "pe_status": "تحت التحصيل",
            "posting_date": doc.cheque_action_date,
            "accounts": accounts,
            "payment_type": doc.payment_type,
            "user_remark": doc.party_name
        })
        new_doc.insert()
        new_doc.submit()
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action_date = NULL where name = %s""", doc.name)
        doc.reload()

    if doc.cheque_action == "إيداع شيك تحت التحصيل" and not doc.with_bank_commission and doc.cheque_status == "مرفوض بالبنك":
        frappe.db.sql(""" update `tabPayment Entry` set cheque_status = "تحت التحصيل" where name = %s""", doc.name)
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action = "" where name = %s""", doc.name)
        accounts = [
            {
                "doctype": "Journal Entry Account",
                "account": doc.collection_fee_account,
                "credit": 0,
                "debit": doc.paid_amount,
                "debit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            },
            {
                "doctype": "Journal Entry Account",
                "account": default_payback_cheque_wallet_account,
                "debit": 0,
                "credit": doc.paid_amount,
                "credit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            }
        ]
        new_doc = frappe.get_doc({
            "doctype": "Journal Entry",
            "voucher_type": "Bank Entry",
            "reference_doctype": "Payment Entry",
            "reference_link": doc.name,
            "cheque_no": doc.reference_no,
            "cheque_date": doc.reference_date,
            "pe_status": "تحت التحصيل 2",
            "posting_date": doc.cheque_action_date,
            "accounts": accounts,
            "payment_type": doc.payment_type,
            "user_remark": doc.party_name
        })
        new_doc.insert()
        new_doc.submit()
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action_date = NULL where name = %s""", doc.name)
        doc.reload()

    if doc.cheque_action == "إرجاع لحافظة شيكات واردة" and not doc.with_bank_commission and doc.cheque_status == "مرفوض بالبنك":
        frappe.db.sql(""" update `tabPayment Entry` set cheque_status = "حافظة شيكات واردة" where name = %s""",
                      doc.name)
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action = "" where name = %s""", doc.name)
        accounts = [
            {
                "doctype": "Journal Entry Account",
                "account": doc.paid_to,
                "credit": 0,
                "debit": doc.paid_amount,
                "debit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            },
            {
                "doctype": "Journal Entry Account",
                "account": default_rejected_cheque_account,
                "debit": 0,
                "credit": doc.paid_amount,
                "credit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            }
        ]
        new_doc = frappe.get_doc({
            "doctype": "Journal Entry",
            "voucher_type": "Bank Entry",
            "reference_doctype": "Payment Entry",
            "reference_link": doc.name,
            "cheque_no": doc.reference_no,
            "cheque_date": doc.reference_date,
            "pe_status": "حافظة شيكات واردة",
            "posting_date": doc.cheque_action_date,
            "accounts": accounts,
            "payment_type": doc.payment_type,
            "user_remark": doc.party_name
        })
        new_doc.insert()
        new_doc.submit()
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action_date = NULL where name = %s""", doc.name)
        doc.reload()

    if doc.cheque_action == "رد شيك" and not doc.with_bank_commission and doc.cheque_status == "مرفوض بالبنك":
        frappe.db.sql(""" update `tabPayment Entry` set cheque_status = "مردود" where name = %s""", doc.name)
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action = "" where name = %s""", doc.name)
        accounts = [
            {
                "doctype": "Journal Entry Account",
                "account": doc.paid_from,
                "party_type": "Customer",
                "party": doc.party,
                "credit": 0,
                "debit": doc.paid_amount,
                "debit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            },
            {
                "doctype": "Journal Entry Account",
                "account": doc.paid_to,
                "debit": 0,
                "credit": doc.paid_amount,
                "credit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            }
        ]
        new_doc = frappe.get_doc({
            "doctype": "Journal Entry",
            "voucher_type": "Bank Entry",
            "reference_doctype": "Payment Entry",
            "reference_link": doc.name,
            "cheque_no": doc.reference_no,
            "cheque_date": doc.reference_date,
            "pe_status": "مردود 2",
            "posting_date": doc.cheque_action_date,
            "accounts": accounts,
            "payment_type": doc.payment_type,
            "user_remark": doc.party_name
        })
        new_doc.insert()
        new_doc.submit()
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action_date = NULL where name = %s""", doc.name)
        doc.reload()

    if doc.cheque_action == "إيداع شيك تحت التحصيل" and doc.with_bank_commission and doc.cheque_status == "مرفوض بالبنك":
        frappe.db.sql(""" update `tabPayment Entry` set cheque_status = "تحت التحصيل" where name = %s""", doc.name)
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action = "" where name = %s""", doc.name)
        accounts = [
            {
                "doctype": "Journal Entry Account",
                "account": doc.collection_fee_account,
                "credit": 0,
                "debit": doc.paid_amount,
                "debit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            },
            {
                "doctype": "Journal Entry Account",
                "account": default_bank_commissions_account,
                "credit": 0,
                "debit": doc.co3_,
                "debit_in_account_currency": doc.co3_,
                "user_remark": doc.name
            },
            {
                "doctype": "Journal Entry Account",
                "account": default_payback_cheque_wallet_account,
                "debit": 0,
                "credit": doc.paid_amount,
                "credit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            },
            {
                "doctype": "Journal Entry Account",
                "account": doc.account,
                "debit": 0,
                "credit": doc.co3_,
                "credit_in_account_currency": doc.co3_,
                "user_remark": doc.name
            }
        ]
        new_doc = frappe.get_doc({
            "doctype": "Journal Entry",
            "voucher_type": "Bank Entry",
            "reference_doctype": "Payment Entry",
            "reference_link": doc.name,
            "cheque_no": doc.reference_no,
            "cheque_date": doc.reference_date,
            "pe_status": "تحت التحصيل 2",
            "posting_date": doc.cheque_action_date,
            "accounts": accounts,
            "payment_type": doc.payment_type,
            "user_remark": doc.party_name
        })
        new_doc.insert()
        new_doc.submit()
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action_date = NULL where name = %s""", doc.name)
        doc.reload()

    if doc.cheque_action == "صرف شيك تحت التحصيل":
        frappe.db.sql("""update `tabPayment Entry` set clearance_date = %s where name=%s """,
                      (doc.cheque_action_date, doc.name))
        frappe.db.sql(""" update `tabPayment Entry` set cheque_status = "محصل" where name = %s""", doc.name)
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action = "" where name = %s""", doc.name)
        accounts = [
            {
                "doctype": "Journal Entry Account",
                "account": doc.account,
                "credit": 0,
                "debit": doc.paid_amount,
                "debit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            },
            {
                "doctype": "Journal Entry Account",
                "account": doc.collection_fee_account,
                "debit": 0,
                "credit": doc.paid_amount,
                "credit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            }
        ]
        new_doc = frappe.get_doc({
            "doctype": "Journal Entry",
            "voucher_type": "Bank Entry",
            "reference_doctype": "Payment Entry",
            "reference_link": doc.name,
            "cheque_no": doc.reference_no,
            "cheque_date": doc.reference_date,
            "pe_status": "محصل",
            "posting_date": doc.cheque_action_date,
            "accounts": accounts,
            "payment_type": doc.payment_type,
            "user_remark": doc.party_name
        })
        new_doc.insert()
        new_doc.submit()
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action_date = NULL where name = %s""", doc.name)
        doc.reload()

    if doc.cheque_action == "رفض شيك تحت التحصيل" and doc.with_bank_commission:
        frappe.db.sql(""" update `tabPayment Entry` set cheque_status = "مرفوض بالبنك" where name = %s""",
                      doc.name)
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action = "" where name = %s""", doc.name)
        accounts = [
            {
                "doctype": "Journal Entry Account",
                "account": default_payback_cheque_wallet_account,
                "credit": 0,
                "debit": doc.paid_amount,
                "debit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            },
            {
                "doctype": "Journal Entry Account",
                "account": default_bank_commissions_account,
                "credit": 0,
                "debit": doc.co5_,
                "debit_in_account_currency": doc.co5_,
                "user_remark": doc.name
            },
            {
                "doctype": "Journal Entry Account",
                "account": doc.collection_fee_account,
                "debit": 0,
                "credit": doc.paid_amount,
                "credit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            },
            {
                "doctype": "Journal Entry Account",
                "account": doc.account,
                "debit": 0,
                "credit": doc.co5_,
                "credit_in_account_currency": doc.co5_,
                "user_remark": doc.name
            }
        ]
        new_doc = frappe.get_doc({
            "doctype": "Journal Entry",
            "voucher_type": "Bank Entry",
            "reference_doctype": "Payment Entry",
            "reference_link": doc.name,
            "cheque_no": doc.reference_no,
            "cheque_date": doc.reference_date,
            "pe_status": "مرفوض بالبنك",
            "posting_date": doc.cheque_action_date,
            "accounts": accounts,
            "payment_type": doc.payment_type,
            "user_remark": doc.party_name
        })
        new_doc.insert()
        new_doc.submit()
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action_date = NULL where name = %s""", doc.name)
        doc.reload()

    if doc.cheque_action == "رفض شيك تحت التحصيل" and not doc.with_bank_commission:
        frappe.db.sql(""" update `tabPayment Entry` set cheque_status = "مرفوض بالبنك" where name = %s""",
                      doc.name)
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action = "" where name = %s""", doc.name)
        accounts = [
            {
                "doctype": "Journal Entry Account",
                "account": default_payback_cheque_wallet_account,
                "credit": 0,
                "debit": doc.paid_amount,
                "debit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            },
            {
                "doctype": "Journal Entry Account",
                "account": doc.collection_fee_account,
                "debit": 0,
                "credit": doc.paid_amount,
                "credit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            }
        ]
        new_doc = frappe.get_doc({
            "doctype": "Journal Entry",
            "voucher_type": "Bank Entry",
            "reference_doctype": "Payment Entry",
            "reference_link": doc.name,
            "cheque_no": doc.reference_no,
            "cheque_date": doc.reference_date,
            "pe_status": "مرفوض بالبنك",
            "posting_date": doc.cheque_action_date,
            "accounts": accounts,
            "payment_type": doc.payment_type,
            "user_remark": doc.party_name
        })
        new_doc.insert()
        new_doc.submit()
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action_date = NULL where name = %s""", doc.name)
        doc.reload()

    if doc.cheque_action == "تظهير شيك":
        frappe.db.sql(""" update `tabPayment Entry` set cheque_status = "مظهر" where name = %s""", doc.name)
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action = "" where name = %s""", doc.name)
        accounts = [
            {
                "doctype": "Journal Entry Account",
                "account": doc.account_1,
                "party_type": doc.party_type_,
                "party": doc.party_,
                "credit": 0,
                "debit": doc.paid_amount,
                "debit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            },
            {
                "doctype": "Journal Entry Account",
                "account": doc.paid_to,
                "debit": 0,
                "credit": doc.paid_amount,
                "credit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            }
        ]
        new_doc = frappe.get_doc({
            "doctype": "Journal Entry",
            "voucher_type": "Bank Entry",
            "reference_doctype": "Payment Entry",
            "reference_link": doc.name,
            "cheque_no": doc.reference_no,
            "cheque_date": doc.reference_date,
            "pe_status": "مظهر",
            "posting_date": doc.cheque_action_date,
            "accounts": accounts,
            "payment_type": doc.payment_type,
            "user_remark": doc.party_name
        })
        new_doc.insert()
        new_doc.submit()
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action_date = NULL where name = %s""", doc.name)
        doc.reload()

    if not doc.encashment_amount and doc.cheque_action == "تسييل الشيك":
        frappe.throw(_("برجاء إدخال مبلغ التسييل"))

    if doc.encashment_amount > doc.paid_amount and doc.cheque_action == "تسييل الشيك":
        frappe.throw(_("مبلغ التسييل لا يمكن أن يكون أكبر من مبلغ الشيك"))
        doc.reload()

    if doc.encashed_amount > doc.paid_amount and doc.cheque_action == "تسييل الشيك":
        frappe.throw(_("مبلغ التسييل لا يمكن أن يكون أكبر من المبلغ الغير مسيل"))
        doc.reload()

    if doc.cheque_action == "تسييل الشيك":
        frappe.db.sql(""" update `tabPayment Entry` set cheque_status = "حافظة شيكات مرجعة" where name = %s""",
                      doc.name)
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action = "" where name = %s""", doc.name)
        accounts = [
            {
                "doctype": "Journal Entry Account",
                "account": default_cash_account,
                "credit": 0,
                "debit": doc.encashment_amount,
                "debit_in_account_currency": doc.encashment_amount,
                "user_remark": doc.name
            },
            {
                "doctype": "Journal Entry Account",
                "account": default_payback_cheque_wallet_account,
                "debit": 0,
                "credit": doc.encashment_amount,
                "credit_in_account_currency": doc.encashment_amount,
                "user_remark": doc.name
            }
        ]
        new_doc = frappe.get_doc({
            "doctype": "Journal Entry",
            "voucher_type": "Bank Entry",
            "reference_doctype": "Payment Entry",
            "reference_link": doc.name,
            "cheque_no": doc.reference_no,
            "cheque_date": doc.reference_date,
            "pe_status": "حافظة شيكات مرجعة",
            "posting_date": doc.cheque_action_date,
            "accounts": accounts,
            "payment_type": doc.payment_type,
            "user_remark": doc.party_name
        })
        new_doc.insert()
        new_doc.submit()
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action_date = NULL where name = %s""", doc.name)
        frappe.db.sql(""" update `tabPayment Entry` set encashment_amount = 0 where name = %s""", doc.name)
        doc.reload()

    if doc.cheque_action == "رد شيك" and doc.cheque_status == "حافظة شيكات واردة":
        frappe.db.sql(""" update `tabPayment Entry` set cheque_status = "مردود" where name = %s""", doc.name)
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action = "" where name = %s""", doc.name)
        doc.reload()

        accounts = [
            {
                "doctype": "Journal Entry Account",
                "account": doc.paid_from,
                "party": doc.party,
                "party_type": doc.party_type,
                "credit": 0,
                "debit": doc.paid_amount,
                "debit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            },
            {
                "doctype": "Journal Entry Account",
                "account": doc.paid_to,
                "debit": 0,
                "credit": doc.paid_amount,
                "credit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            }
        ]
        new_doc = frappe.get_doc({
            "doctype": "Journal Entry",
            "voucher_type": "Bank Entry",
            "reference_doctype": "Payment Entry",
            "reference_link": doc.name,
            "cheque_no": doc.reference_no,
            "cheque_date": doc.reference_date,
            "pe_status": "مردود 1",
            "posting_date": doc.cheque_action_date,
            "accounts": accounts,
            "payment_type": doc.payment_type,
            "user_remark": doc.party_name
        })
        new_doc.insert()
        new_doc.submit()
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action_date = NULL where name = %s""", doc.name)
        doc.reload()

    if not doc.bank_acc and doc.cheque_action in ("سحب الشيك", "صرف الشيك"):
        frappe.throw(_("برجاء تحديد الحساب البنكي"))

    if doc.cheque_action == "صرف الشيك" and doc.payment_type == "Pay":
        frappe.db.sql("""update `tabPayment Entry` set clearance_date = %s where name=%s """,
                      (doc.cheque_action_date, doc.name))
        frappe.db.sql(""" update `tabPayment Entry` set cheque_status_pay = "مدفوع" where name = %s""", doc.name)
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action = "" where name = %s""", doc.name)
        accounts = [
            {
                "doctype": "Journal Entry Account",
                "account": doc.payable_account,
                "credit": 0,
                "debit": doc.paid_amount,
                "debit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            },
            {
                "doctype": "Journal Entry Account",
                "account": doc.account,
                "debit": 0,
                "credit": doc.paid_amount,
                "credit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            }
        ]
        new_doc = frappe.get_doc({
            "doctype": "Journal Entry",
            "voucher_type": "Bank Entry",
            "reference_doctype": "Payment Entry",
            "reference_link": doc.name,
            "cheque_no": doc.reference_no,
            "cheque_date": doc.reference_date,
            "pe_status": "مدفوع",
            "posting_date": doc.cheque_action_date,
            "accounts": accounts,
            "payment_type": doc.payment_type,
            "user_remark": doc.party_name
        })
        new_doc.insert()
        new_doc.submit()
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action_date = NULL where name = %s""", doc.name)
        doc.reload()

    if doc.cheque_action == "سحب الشيك":
        frappe.db.sql(""" update `tabPayment Entry` set cheque_status_pay = "مسحوب" where name = %s""", doc.name)
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action = "" where name = %s""", doc.name)
        accounts = [
            {
                "doctype": "Journal Entry Account",
                "account": doc.payable_account,
                "credit": 0,
                "debit": doc.paid_amount,
                "debit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            },
            {
                "doctype": "Journal Entry Account",
                "account": doc.paid_to,
                "party": doc.party,
                "party_type": doc.party_type,
                "debit": 0,
                "credit": doc.paid_amount,
                "credit_in_account_currency": doc.paid_amount,
                "user_remark": doc.name
            }
        ]
        new_doc = frappe.get_doc({
            "doctype": "Journal Entry",
            "voucher_type": "Bank Entry",
            "reference_doctype": "Payment Entry",
            "reference_link": doc.name,
            "cheque_no": doc.reference_no,
            "cheque_date": doc.reference_date,
            "pe_status": "مسحوب",
            "posting_date": doc.cheque_action_date,
            "accounts": accounts,
            "payment_type": doc.payment_type,
            "user_remark": doc.party_name
        })
        new_doc.insert()
        new_doc.submit()
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action_date = NULL where name = %s""", doc.name)
        doc.reload()

################################################## End Of CHEQUES code #################################################

@frappe.whitelist()
def pe_before_save(doc, method=None):
    pass
@frappe.whitelist()
def pe_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def pe_on_update(doc, method=None):
    pass

################ Journal Entry
@frappe.whitelist()
def je_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def je_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def je_onload(doc, method=None):
    pass
@frappe.whitelist()
def je_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def je_validate(doc, method=None):
    pass
@frappe.whitelist()
def je_on_submit(doc, method=None):
    pass
@frappe.whitelist()
def je_on_cancel(doc, method=None):
################################################## Start Of CHEQUES code ###############################################
    if doc.reference_doctype == "Payment Entry" and doc.reference_link and (
            doc.pe_status == "محصل فوري" or doc.pe_status == "مظهر" or doc.pe_status == "تحت التحصيل"):
        frappe.db.sql(""" update `tabPayment Entry` set cheque_status = "حافظة شيكات واردة" where name = %s""",
                      doc.reference_link)
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action = "" where name = %s""", doc.reference_link)
        frappe.db.sql(""" update `tabPayment Entry` set clearance_date = NULL where name = %s""", doc.reference_link)

    if doc.reference_doctype == "Payment Entry" and doc.pe_status == "تحت التحصيل 2":
        frappe.db.sql(""" update `tabPayment Entry` set cheque_status = "مرفوض بالبنك" where name = %s""",
                      doc.reference_link)
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action = "" where name = %s""", doc.reference_link)

    if doc.reference_doctype == "Payment Entry" and doc.pe_status == "مردود 1":
        frappe.db.sql(""" update `tabPayment Entry` set cheque_status = "حافظة شيكات واردة" where name = %s""",
                      doc.reference_link)
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action = "" where name = %s""", doc.reference_link)

    if doc.reference_doctype == "Payment Entry" and doc.pe_status == "مردود 2":
        frappe.db.sql(""" update `tabPayment Entry` set cheque_status = "مرفوض بالبنك" where name = %s""",
                      doc.reference_link)
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action = "" where name = %s""", doc.reference_link)

    if doc.reference_doctype == "Payment Entry" and doc.reference_link and (
            doc.pe_status == "محصل" or doc.pe_status == "مرفوض بالبنك"):
        frappe.db.sql(""" update `tabPayment Entry` set cheque_status = "تحت التحصيل" where name = %s""",
                      doc.reference_link)
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action = "" where name = %s""", doc.reference_link)
        frappe.db.sql(""" update `tabPayment Entry` set clearance_date = NULL where name = %s""", doc.reference_link)

    if doc.reference_doctype == "Payment Entry" and doc.reference_link and doc.pe_status == "حافظة شيكات مرجعة":
        frappe.db.sql(""" update `tabPayment Entry` set cheque_status = "مرفوض بالبنك" where name = %s""",
                      doc.reference_link)
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action = "" where name = %s""", doc.reference_link)

    if doc.reference_doctype == "Payment Entry" and doc.reference_link and (
            doc.pe_status == "مدفوع" or doc.pe_status == "مسحوب"):
        frappe.db.sql(""" update `tabPayment Entry` set cheque_status_pay = "حافظة شيكات برسم الدفع" where name = %s""",
                      doc.reference_link)
        frappe.db.sql(""" update `tabPayment Entry` set cheque_action = "" where name = %s""", doc.reference_link)
        frappe.db.sql(""" update `tabPayment Entry` set clearance_date = NULL where name = %s""", doc.reference_link)
################################################## End Of CHEQUES code #################################################

@frappe.whitelist()
def je_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def je_before_save(doc, method=None):
    pass
@frappe.whitelist()
def je_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def je_on_update(doc, method=None):
    pass

################ Material Request
@frappe.whitelist()
def mr_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def mr_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def mr_onload(doc, method=None):
    pass
@frappe.whitelist()
def mr_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def mr_validate(doc, method=None):
    pass
@frappe.whitelist()
def mr_on_submit(doc, method=None):
    pass
@frappe.whitelist()
def mr_on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def mr_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def mr_before_save(doc, method=None):
    pass
@frappe.whitelist()
def mr_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def mr_on_update(doc, method=None):
    pass

################ Purchase Order
@frappe.whitelist()
def po_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def po_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def po_onload(doc, method=None):
    pass
@frappe.whitelist()
def po_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def po_validate(doc, method=None):
    pass
@frappe.whitelist()
def po_on_submit(doc, method=None):
    pass
@frappe.whitelist()
def po_on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def po_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def po_before_save(doc, method=None):
    pass
@frappe.whitelist()
def po_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def po_on_update(doc, method=None):
    pass

################ Purchase Receipt
@frappe.whitelist()
def pr_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def pr_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def pr_onload(doc, method=None):
    pass
@frappe.whitelist()
def pr_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def pr_validate(doc, method=None):
    pass
@frappe.whitelist()
def pr_on_submit(doc, method=None):
    pass
@frappe.whitelist()
def pr_on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def pr_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def pr_before_save(doc, method=None):
    pass
@frappe.whitelist()
def pr_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def pr_on_update(doc, method=None):
    pass


################ Purchase Invoice
@frappe.whitelist()
def piv_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def piv_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def piv_onload(doc, method=None):
    pass
@frappe.whitelist()
def piv_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def piv_validate(doc, method=None):
    pass
@frappe.whitelist()
def piv_on_submit(doc, method=None):
    pass
@frappe.whitelist()
def piv_on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def piv_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def piv_before_save(doc, method=None):
    pass
@frappe.whitelist()
def piv_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def piv_on_update(doc, method=None):
    pass

################ Employee Advance
@frappe.whitelist()
def emad_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def emad_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def emad_onload(doc, method=None):
    pass
@frappe.whitelist()
def emad_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def emad_validate(doc, method=None):
    pass
@frappe.whitelist()
def emad_on_submit(doc, method=None):
    pass
@frappe.whitelist()
def emad_on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def emad_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def emad_before_save(doc, method=None):
    pass
@frappe.whitelist()
def emad_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def emad_on_update(doc, method=None):
    pass

################ Expense Claim
@frappe.whitelist()
def excl_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def excl_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def excl_onload(doc, method=None):
    pass
@frappe.whitelist()
def excl_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def excl_validate(doc, method=None):
    pass
@frappe.whitelist()
def excl_on_submit(doc, method=None):
    pass
@frappe.whitelist()
def excl_on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def excl_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def excl_before_save(doc, method=None):
    pass
@frappe.whitelist()
def excl_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def excl_on_update(doc, method=None):
    pass

################ Stock Entry
@frappe.whitelist()
def ste_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def ste_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def ste_onload(doc, method=None):
    pass
@frappe.whitelist()
def ste_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def ste_validate(doc, method=None):
    pass
@frappe.whitelist()
def ste_on_submit(doc, method=None):
    pass
@frappe.whitelist()
def ste_on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def ste_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def ste_before_save(doc, method=None):
    pass
@frappe.whitelist()
def ste_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def ste_on_update(doc, method=None):
    pass

################ Blanket Order
@frappe.whitelist()
def blank_before_insert(doc, method=None):
    pass
@frappe.whitelist()
def blank_after_insert(doc, method=None):
    pass
@frappe.whitelist()
def blank_onload(doc, method=None):
    pass
@frappe.whitelist()
def blank_before_validate(doc, method=None):
    pass
@frappe.whitelist()
def blank_validate(doc, method=None):
    pass
@frappe.whitelist()
def blank_on_submit(doc, method=None):
    pass
@frappe.whitelist()
def blank_on_cancel(doc, method=None):
    pass
@frappe.whitelist()
def blank_on_update_after_submit(doc, method=None):
    pass
@frappe.whitelist()
def blank_before_save(doc, method=None):
    pass
@frappe.whitelist()
def blank_before_cancel(doc, method=None):
    pass
@frappe.whitelist()
def blank_on_update(doc, method=None):
    pass
