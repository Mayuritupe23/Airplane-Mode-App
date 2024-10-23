<p>Dear System Manager,</p>

<p>The flight <strong>{{ doc.name }}</strong> operated by <strong>{{ doc.airplane }}</strong> is scheduled to depart on <strong>{{ frappe.utils.format_date(doc.date_of_departure, "d MMMM, YYYY") }}</strong> at <strong>{{ doc.time_of_departure }}</strong>.</p>

<p>Please ensure all preparations are in place.</p>

<p>Thank you!</p>
