# Copyright (c) 2024, vintrosys and contributors
# For license information, please see license.txt


import frappe
from frappe.website.website_generator import WebsiteGenerator
from textblob import TextBlob

class TFTestimonial(WebsiteGenerator):
    def before_save(self):
        self.update_rating_based_on_feedback()

    def on_submit(self):
        self.update_member_profile_rating()
    
    def update_rating_based_on_feedback(self):
        if self.testimonial_type == "Quick Words":
            if not self.feedback:
                frappe.throw("Feedback is required when 'Quick Words' is selected.")
            else:
                try:
                    print(f"Feedback for sentiment analysis: {self.feedback}")
                    blob = TextBlob(self.feedback)
                    sentiment = blob.sentiment.polarity
                    
                    # Adjusting the sentiment polarity to rating conversion
                    if -1 <= sentiment < -0.5:
                        self.rating = 0.1              # For sentiment between -1 and -0.5
                    elif -0.5 <= sentiment <= 0:
                        self.rating = 0.2              # For sentiment between -0.5 and 0
                    elif 0 < sentiment <= 0.25:
                        self.rating = 0.6              # For sentiment between 0 and 0.25
                    elif 0.25 < sentiment <= 0.5:
                        self.rating = 0.8              # For sentiment between 0.25 and 0.5
                    elif 0.5 < sentiment <= 1:
                        self.rating = 1                # For sentiment between 0.5 and 1
                    else:
                        self.rating = 0.4              # Default rating if sentiment does not match any range

                except Exception as e:
                    print(f"Error in sentiment analysis: {e}")
                    frappe.log_error(f"Error in sentiment analysis: {e}", "TFTestimonial")
                    self.rating = 0.1  # Default rating in case of error
        else:
            self.rating = None

    def update_member_profile_rating(self):
        if self.rating and self.member_id:
            try:
                get_member = frappe.get_doc("TF Member Profile", self.member_id)
                
                if self.industry:
                    set = 0
                    for i in get_member.industry:
                        if i.industry == self.industry:
                            rating = self.rating if i.rating == 0 else (i.rating + self.rating) / 2
                            i.set("rating", rating)
                            set = 1
                    if set == 0:
                        get_member.append("industry", dict(
                            industry=self.industry,
                            rating=self.rating
                        ))
                
                if self.frappe_app:
                    set = 0
                    for i in get_member.frappe_apps:
                        if i.frappe_app == self.frappe_app:
                            rating = self.rating if i.rating == 0 else (i.rating + self.rating) / 2
                            i.set("rating", rating)
                            set = 1
                    if set == 0:
                        get_member.append("frappe_apps", dict(
                            frappe_app=self.frappe_app,
                            rating=self.rating
                        ))
                
                if self.erp_module:
                    set = 0
                    for i in get_member.erp_module:
                        if i.erp_module == self.erp_module:
                            rating = self.rating if i.rating == 0 else (i.rating + self.rating) / 2
                            i.set("rating", rating)
                            set = 1
                    if set == 0:
                        get_member.append("erp_module", dict(
                            erp_module=self.erp_module,
                            rating=self.rating
                        ))
                
                if self.skill:
                    set = 0
                    for i in get_member.pcm_skills:
                        if i.skill == self.skill:
                            rating = self.rating if i.rating == 0 else (i.rating + self.rating) / 2
                            i.set("rating", rating)
                            set = 1
                    if set == 0:
                        get_member.append("pcm_skills", dict(
                            skill=self.skill,
                            rating=self.rating
                        ))
                
                get_member.save(ignore_permissions=True)
            except Exception as e:
                print(f"Error updating member profile: {e}")
                frappe.log_error(f"Error updating member profile: {e}", "TFTestimonial")
