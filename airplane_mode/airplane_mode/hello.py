import frappe
def print_hello():
    
    frappe.log().info("Hello From Frappe")
    frappe.log_error("This is a test error message", "Test Error")
