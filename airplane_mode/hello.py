import frappe
def test_logging():  
    try:  
        # Simulate an error for testing  
       a=5/2
       frappe.log(a) 
    except Exception as e:  
        # Log the error  
        frappe.log_error("An error occurred: {e}")  

    # Log an informational message  
    frappe.log("This is an info message.")  

# Call the test function to see the logs  
test_logging()