frappe.listview_settings["TF Member Profile"] = {
    add_fields: ["member_name", "member_type", "profile_stage", "profile_status", "regional_area", "profile_image"],
    
    get_indicator: function (doc) {
        var indicator = [__(doc.profile_status), frappe.utils.guess_colour(doc.profile_status), "profile_status,=," + doc.profile_status];
        indicator[1] = { Open: "orange", Active: "green", Idle: "red"}[doc.profile_status];
        return indicator;
    },

    onload: function (listview) {
        // Get the current user's email
        const user_email = frappe.session.user;

        // Fetch the member_type based on the user's email
        frappe.db.get_value('TF Member Profile', { 'email_id': user_email }, 'member_type')
            .then(r => {
                if (r.message && r.message.member_type === 'student') {
                    // Filter the list view to show only profiles with member_type 'Student'
                    listview.set_filter('member_type', '=', 'student');
                } else {
                    // If not a Student, clear the filters or set to a condition that shows no records
                    listview.set_filter('member_type', '=', ''); // Adjust as needed
                }
            })
            .catch(error => {
                console.error("Error fetching member_type:", error);
            });
    }
};
