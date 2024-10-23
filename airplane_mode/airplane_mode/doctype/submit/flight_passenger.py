# Copyright (c) 2024, Mayuri Tupe and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


	
class FlightPassenger(Document):
    def before_save(self):
        self.set_full_name()

    def set_full_name(self):
        if self.first_name and self.last_name:
            self.full_name = f"{self.first_name} {self.last_name}"
        elif self.first_name:
            self.full_name = self.first_name
        else:
            self.full_name = ""