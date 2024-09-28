
// Copyright (c) 2024, vintrosys and contributors
// For license information, please see license.txt
// frappe.ui.form.on('TF Frappe Provider Detail', {
//     frappe_provider: function(frm, cdt, cdn) {
//         let row = locals[cdt][cdn];
        
//         if (row.frappe_provider) {
//             frappe.call({
//                 method: 'frappe.client.get_value',
//                 args: {
//                     doctype: 'TF Frappe Provider',  // Assuming you're fetching from 'Item' doctype
//                     filters: { 'name': row.frappe_provider },
//                     fieldname: ['provider_name']  // The title to fetch
//                 },
//                 callback: function(r) {
//                     if (r.message) {
//                         // Instead of setting a field, you can update the row display or add a tooltip
//                         const provider_name = r.message.provider_name;
//                         // Dynamically update the label of the field
//                         frm.fields_dict["items"].grid.get_field("frappe_provider").set_label("Item ID ( " + provider_name + " )");

//                         // Optionally, you could display the `provider_name` as a tooltip or custom UI element
//                         $(frm.fields_dict['items'].grid.grid_rows_by_docname[cdn].row).find('[data-fieldname="frappe_provider"]').attr("title", provider_name);
//                     } else {
//                         frappe.msgprint(__('Item not found'));
//                     }
//                 }
//             });
//         }
//     }
// });


// frappe.ui.form.on("TF Member Profile", {
//     refresh(frm) {
// 			frm.fields_dict['pcm_frappe_provider'].grid.get_field('frappe_provider').grid.on('change', function(frm, cdt, cdn) {
// 				var row = locals[cdt][cdn];
// 				// Perform some action when 'rate' field changes
// 				frappe.msgprint(`Rate updated to: ${row.rate}`);
// 			});
// 		}
// 	})