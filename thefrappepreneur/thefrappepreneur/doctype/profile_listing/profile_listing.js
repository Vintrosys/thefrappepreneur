// Copyright (c) 2024, vintrosys and contributors
// For license information, please see license.txt

frappe.ui.form.on("Profile Listing", {
    refresh(frm) {
        frm.add_custom_button(__("Referral Link"), function () {
            let site_url = window.location.origin;
            let referral_link = `${site_url}/registration/new?parent_profile_listing=${frm.doc.name}`;

            function copyToClipboard(text) {
                if (navigator.clipboard && typeof navigator.clipboard.writeText === 'function') {
                    navigator.clipboard.writeText(text).then(() => {
                        frappe.msgprint(__("Referral link has been copied to your clipboard : <a href='{0}'>{0}</a>", [text]));
                    }).catch(err => {
                        console.error('Failed to copy using Clipboard API: ', err);
                    });
                } else {
                    let tempInput = document.createElement("input");
                    tempInput.value = text;
                    document.body.appendChild(tempInput);
                    tempInput.select();
                    tempInput.setSelectionRange(0, 99999);
                    document.execCommand("copy");
                    document.body.removeChild(tempInput);
                    frappe.msgprint(__("Referral link has been copied to your clipboard : <a href='{0}'>{0}</a>", [text]));
                }
            }

            copyToClipboard(referral_link);
        });
    },
});

