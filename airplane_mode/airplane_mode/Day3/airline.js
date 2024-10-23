// Copyright (c) 2024, Mayuri Tupe and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airline", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Airline', {
    refresh: function(frm) {
        // Check if the website field has a value
        if (frm.doc.website) {
            // Ensure the URL starts with http:// or https://
            let website_url = frm.doc.website;
            if (!website_url.startsWith('http://') && !website_url.startsWith('https://')) {
                website_url = 'https://' + website_url;  // Default to https
            }

            // Add a web link directly on the form
            frm.add_web_link(website_url, "Visite Website");
        }
    }
});



