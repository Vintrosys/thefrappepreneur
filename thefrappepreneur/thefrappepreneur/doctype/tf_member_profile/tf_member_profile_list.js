frappe.listview_settings["TF Member Profile"] = {
	add_fields: ["member_name", "member_type", "profile_stage", "profile_status", "regional_area", "profile_image"],
	get_indicator: function (doc) {
		var indicator = [__(doc.profile_status), frappe.utils.guess_colour(doc.profile_status), "profile_status,=," + doc.profile_status];
		indicator[1] = { Open: "orange", Active: "green", Idle: "red"}[doc.profile_status];
		return indicator;
	},
};
