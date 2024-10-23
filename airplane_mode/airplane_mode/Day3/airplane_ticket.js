// Copyright (c) 2024, Mayuri Tupe and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Ticket", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {
        // Add a custom button for seat assignment
        frm.add_custom_button(__('Assign Seat'), function() {
            // Create a dialog to input the seat number
            let d = new frappe.ui.Dialog({
                title: 'Assign Seat',
                fields: [
                    {
                        label: 'Seat Number',
                        fieldname: 'seat_number',
                        fieldtype: 'Data',
                        reqd: 1, // Make it a required field
                        placeholder: 'e.g. 12A'
                    }
                ],
                primary_action_label: 'Assign',
                primary_action(values) {
                    // Set the seat number in the form
                    frm.set_value('seat', values.seat_number);
                    d.hide(); // Close the dialog after assignment
                }
            });
            d.show(); // Show the dialog
        });
    }
});
