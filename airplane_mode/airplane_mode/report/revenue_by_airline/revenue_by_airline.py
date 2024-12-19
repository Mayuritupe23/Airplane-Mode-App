# # Copyright (c) 2024, Mayuri Tupe and contributors
# # For license information, please see license.txt

# import frappe
# from frappe import _


# def execute(filters: dict | None = None):
# 	"""Return columns and data for the report.

# 	This is the main entry point for the report. It accepts the filters as a
# 	dictionary and should return columns and data. It is called by the framework
# 	every time the report is refreshed or a filter is updated.
# 	"""
# 	columns = get_columns()
# 	data = get_data()

# 	return columns, data


# def get_columns() -> list[dict]:
# 	"""Return columns for the report.

# 	One field definition per column, just like a DocType field definition.
# 	"""
# 	return [
# 		{
# 			"label": _("Column 1"),
# 			"fieldname": "column_1",
# 			"fieldtype": "Data",
# 		},
# 		{
# 			"label": _("Column 2"),
# 			"fieldname": "column_2",
# 			"fieldtype": "Int",
# 		},
# 	]


# def get_data() -> list[list]:
# 	"""Return data for the report.

# 	The report data is a list of rows, with each row being a list of cell values.
# 	"""
# 	return [
# 		["Row 1", 1],
# 		["Row 2", 2],
# 	]
import frappe
from frappe import _

def execute(filters=None):
    # Define the columns for the report
    columns = [
        {"fieldname": "airline", "label": _("Airline"), "fieldtype": "Link", "options": "Airline","width": 200},
        {"fieldname": "revenue", "label": _("Revenue"), "fieldtype": "Currency", "options": "currency","width": 200},
    ]

    # Initialize an empty result set
    results = []
    
    # Fetch all airlines to include even those with zero revenue
    airlines = frappe.get_all("Airline", fields=["name"])

    # Initialize a dictionary to store revenue by airline
    revenue_by_airline = {airline.name: 0 for airline in airlines}

    # Fetch the relevant tickets and their associated revenue
    tickets = frappe.db.sql("""
        SELECT a.airline AS airline, 
               SUM(t.total_amount) AS total_amount
        FROM `tabAirplane Ticket` t
        JOIN `tabAirplane Flight` f ON t.flight = f.name
        JOIN `tabAirplane` a ON f.airplane = a.name
        GROUP BY a.airline
    """, as_dict=True)

    # Total revenue
    total_revenue = 0

    # Populate the revenue by airline dictionary and calculate total revenue
    for ticket in tickets:
        revenue_by_airline[ticket.airline] += ticket.total_amount
        total_revenue += ticket.total_amount

    # Create result rows for the report
    for airline, revenue in revenue_by_airline.items():
        results.append({
            "airline": airline,
            "revenue": revenue,
        })

    # Prepare data for the Donut Chart
    chart_data = {
        "data": {
            "labels": list(revenue_by_airline.keys()),
            "datasets": [{
                "name": _("Revenue by Airline"),
                "values": list(revenue_by_airline.values()),
            }]
        },
        "type": "donut",  # Set the chart type to donut
    }

    # Add total revenue to the chart data
    chart_data["summary"] = {
        "title": _("Total Revenue"),
        "value": total_revenue,
    }

    # # Return the columns, results, and chart data
    return columns, results,None, chart_data
