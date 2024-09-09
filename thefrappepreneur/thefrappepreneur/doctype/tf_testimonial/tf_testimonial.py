# Copyright (c) 2024, vintrosys and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
# import textblob
# from textblob import TextBlob

# text = doc.feedback
# blob = TextBlob(text)
# blob.sentiment.polarity

# -1 to 1


class TFTestimonial(WebsiteGenerator):
	def on_submit(self):
		self.update_member_profile_rating()
	
	def update_member_profile_rating(self):
		if self.rating:
			get_member = frappe.get_doc("TF Member Profile", self.member_id)
			if self.industry:
				set = 0
				for i in get_member.industry:
					if i.industry == self.industry:
						rating = self.rating if i.rating == 0 else (i.rating + self.rating)/2
						i.set("rating", rating)
						set = 1
				if set == 0:
					get_member.append("industry",dict(
						industry = self.industry,
						rating = self.rating
					))
			if self.frappe_app:
				set = 0
				for i in get_member.frappe_apps:
					if i.frappe_app == self.frappe_app:
						rating = self.rating if i.rating == 0 else (i.rating + self.rating)/2
						i.set("rating", rating)
						set = 1
				if set == 0:
					get_member.append("frappe_apps",dict(
						frappe_app = self.frappe_app,
						rating = self.rating
					))
			if self.erp_module:
				set = 0
				for i in get_member.erp_module:
					if i.erp_module == self.erp_module:
						rating = self.rating if i.rating == 0 else (i.rating + self.rating)/2
						i.set("rating", rating)
						set = 1
				if set == 0:
					get_member.append("erp_module",dict(
						erp_module = self.erp_module,
						rating = self.rating
					))
			if self.skill:
				set = 0
				for i in get_member.pcm_skills:
					if i.skill == self.skill:
						rating = self.rating if i.rating == 0 else (i.rating + self.rating)/2
						i.set("rating", rating)
						set = 1
				if set == 0:
					get_member.append("pcm_skills",dict(
						skill = self.skill,
						rating = self.rating
					))
			get_member.save(ignore_permissions=True)
