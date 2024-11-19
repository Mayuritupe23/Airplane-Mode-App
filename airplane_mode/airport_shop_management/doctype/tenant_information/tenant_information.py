# Copyright (c) 2024, Mayuri Tupe and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class TenantInformation(Document):


	def send_monthly_rent_reminders():
		# Fetch tenants whose rent is due (replace with correct filter if needed)
		tenants = frappe.get_all("Tenant Information", filters={"rent_due": True}, fields=["name", "email", "tenant_name"])
		
		for tenant in tenants:
			if tenant.email:
				subject = "Monthly Rent Payment Reminder"
				message = f"""
					Dear {tenant.tenant_name},

					This is a reminder to pay your rent for this month. Please make sure to complete the payment to avoid any late fees.

					Regards,
					Airport Management
				"""
				
				# Send the email
				frappe.sendmail(
					recipients=[tenant.email],
					subject=subject,
					message=message
				)
