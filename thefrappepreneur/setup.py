import frappe

def after_install():
    create_role()

def create_role():
    role = ["Super Admin", "Community Member"]
    for r in role:
        if frappe.db.exists("Role", r):
            return

        frappe.get_doc(
			{
                "doctype": "Role", 
                "role_name": r, 
                "desk_access": 1
            }
		).insert(ignore_permissions=True)
