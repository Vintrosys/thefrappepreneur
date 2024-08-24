import frappe

def after_install():
    create_membertype()

def create_membertype():
    member_type = ["Client", "Providers", "Professional", "Student", "Freelancer"]
    for type in member_type:
        if frappe.db.exists("Member Type", type):
            return

        frappe.get_doc(
            {
                "doctype": "Member Type",
                "member_type": type,
            }
        ).insert(ignore_permissions=True)