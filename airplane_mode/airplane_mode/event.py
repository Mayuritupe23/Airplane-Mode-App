import frappe

def send_rent_reminder_email():
    # Fetch the settings from the Airport Shop Settings single DocType
    settings = frappe.get_single("Airport Shop Settings")

    # Check if the enable_rent_reminder field is enabled
    if not settings.enable_rent_reminder:
        frappe.log("Please enable 'Rent Reminder' in Airport Shop Settings to send reminders.")
        return

    # Fetch rent payment records with linked tenant details
    rent_payments = frappe.get_all(
        "Rent Payment",
        fields=["tenant", "amount_paid"],  # Fetch tenant and amount paid fields
        filters={"docstatus": 0}  # Add other filters as required
    )

    if not rent_payments:
        frappe.msgprint("No rent payment records found.")
        return

    emails_sent = 0

    for rent_payment in rent_payments:
        # Fetch the Tenant Information record using the linked tenant field
        tenant_doc = frappe.get_doc("Tenant Information", rent_payment.tenant)
        tenant_name = tenant_doc.tenant_name  # Tenant name from Tenant Information
        tenant_email = tenant_doc.email  # Email field in Tenant Information

        if not tenant_email:
            continue

        # If amount_paid is already set by default, use that value
        amount_paid = rent_payment.amount_paid if rent_payment.amount_paid else settings.default_rent_amount

        # Prepare email subject and simple HTML message
        subject = "Rent Payment Reminder"
        message = f"""
        <html>
        <body>
            <p>Dear {tenant_name},</p>
            <p>Greetings from Airport Shop Management Team!</p>
            <p>We hope this email finds you well. This is a gentle reminder that your rent payment is due. Kindly make the payment at your earliest convenience to avoid any inconvenience.</p>
            <p>If you have already made the payment, please ignore this reminder.</p>
            <p><strong>Rent Amount:</strong> {amount_paid}</p>
            <p>For any questions or assistance, feel free to contact our support team.</p>
            <p>Best regards,<br>Airport Shop Management Team</p>
        </body>
        </html>
        """

        # Send the email
        frappe.sendmail(
            recipients=[tenant_email],
            subject=subject,
            message=message,
            delayed=False,  # Sends the email immediately
        )
        emails_sent += 1

    # Show a message with the count of emails sent
    frappe.msgprint(f"Rent reminder emails sent to {emails_sent} tenants.")
