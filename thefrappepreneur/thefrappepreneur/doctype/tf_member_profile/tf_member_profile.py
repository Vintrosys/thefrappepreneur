# Copyright (c) 2024, vintrosys and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class TFMemberProfile(Document):
	def after_save(self):
		pass
		# # Get the base site URL
		# site_url = frappe.utils.get_url()

		# # Generate the referral link for the current document
		# referral_link = f"{site_url}/registration/new?parent_profile_listing={self.name}"

		# # Generate the testimonial link for the current document
		# testimonial_link = f"{site_url}/app/tf-testimonial?member_id={self.name}"

		# # Update both fields in the current document
		# self.qr_code = referral_link
		# self.testimonial_qr_code = testimonial_link

		# # Save the document with updated fields
		# self.save()

		# # Optionally, you can add a message or log for confirmation
		# frappe.msgprint(__('Both QR codes updated successfully.'))

	def validate(self):
		self.update_rating()
		self.create_user()

	def update_rating(self):
		self.skill_rating = self.cal_avg_rating("pcm_skills")
		self.contribution_rating = self.cal_avg_rating("pcm_contribution")
		self.industry_rating = self.cal_avg_rating("industry")
		self.erp_module_rating = self.cal_avg_rating("erp_module")
		self.frappe_apps_rating = self.cal_avg_rating("frappe_apps")
		self.profile_rating = (self.skill_rating + self.contribution_rating + self.industry_rating + self.erp_module_rating + self.frappe_apps_rating)/5
	def cal_avg_rating(self, table):
		r = 0
		if self.get(table):
			for rating in self.get(table):
				if rating.rating:
					r += rating.rating
			return (r/len(self.get(table)))
		return 0



	def create_user(self):
		if self.profile_stage != "Approved" or self.user_id:
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
				"bio": self.description,
				"role_profile_name": "Community Member"
			}
		)
		user.insert()
		self.user_id = user.name

		user_perm = frappe.new_doc("User Permission")
		user_perm.update(
			{
				"user": user.name,
				"allow": "TF Member Profile",
				"for_value": self.name
			}
		)
		user_perm.insert()

@frappe.whitelist()
def get_testimonials():
	if frappe.has_permission("TF Testimonial", "read"):
		tft_data = frappe.get_all(
			"TF Testimonial",
			fields=[
				"name",
				"feedback",
				"video"
			],
			filters={
				"docstatus": 1
			},
			order_by="creation",
		)

		# for row in tft_data:
		# 	row.video = f"""
		# 			<a class="ellipsis">{row.name}</a>
		# 		"""

		# 	row.operation_link = f"""
		# 			<a class="ellipsis" data-doctype="Operation" data-name="{row.operation}" href="/app/operation/{row.operation}" title="" data-original-title="{row.operation}">{row.operation}</a>
		# 		"""

		return tft_data

