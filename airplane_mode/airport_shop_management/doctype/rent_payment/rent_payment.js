// Copyright (c) 2024, Mayuri Tupe and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Rent Payment", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Rent Payment', {
    onload: function(frm) {
        // Fetch the default rent amount from Airport Shop Settings
        frappe.call({
            method: "frappe.client.get",
            args: {
                doctype: "Airport Shop Settings",
                name: "Default Settings"  // Only one record, assuming it's named 'Default Settings'
            },
            callback: function(data) {
                if (data.message) {
                    let default_rent_amount = data.message.default_rent_amount;
                    // If Amount Paid is not set, set the default rent amount
                    if (!frm.doc.amount_paid) {
                        frm.set_value('amount_paid', default_rent_amount);
                    }
                }
            }
        });
    }
});




