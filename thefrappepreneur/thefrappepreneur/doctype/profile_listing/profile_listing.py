# Copyright (c) 2024, vintrosys and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ProfileListing(Document):
	def validate(self):
		self.create_user()

	def create_user(self):
		if self.profile_stage != "Approved" and self.user_id:
			return
		
		if frappe.db.exists("User", self.email_id):
			self.user_id = frappe.db.exists("User", self.email_id)
			return

		pcm = self.member_name.split(" ")
		middle_name = last_name = ""

		if len(pcm) >= 3:
			last_name = " ".join(pcm[2:])
			middle_name = pcm[1]
		elif len(pcm) == 2:
			last_name = pcm[1]

		first_name = pcm[0]

		user = frappe.new_doc("User")
		user.update(
			{
				"name": self.member_name,
				"email": self.email_id,
				"enabled": 1,
				"first_name": first_name,
				"middle_name": middle_name,
				"last_name": last_name,
				"phone": self.mobile_number,
				"bio": self.bio,
			}
		)
		user.insert()
		self.user_id = user.name
