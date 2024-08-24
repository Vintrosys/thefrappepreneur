import frappe

def after_install():
    create_membertype()
    create_role()

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
