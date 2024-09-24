import frappe

def set_doc_permisssion(doc, user):
    
    user_email = frappe.db.get_value("User", user, "email")
    return doc.email_id == user_email