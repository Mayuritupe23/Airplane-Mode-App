# # Copyright (c) 2024, Mayuri Tupe and contributors
# # For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document

class AirplaneTicket(Document):
    def validate(self):
        self.prevent_duplicate_addons()
        self.calculate_total_amount()
        # self.prevent_submission_if_not_boarded()
        # self.before_submit()

    def prevent_duplicate_addons(self):
        unique_addons = set()
        for addon in self.add_ons:
            if addon.item in unique_addons:
                frappe.throw(f"{addon.item} is already added.")
            unique_addons.add(addon.item)

    def calculate_total_amount(self):
        total_addon_amount = sum(item.amount for item in self.add_ons) if self.add_ons else 0
        self.total_amount = int(self.flight_price) + total_addon_amount

    def before_insert(self):
        self.assign_seat()

    def assign_seat(self):
        seat_number = random.randint(1, 100)
        seat_letter = random.choice(['A', 'B', 'C', 'D', 'E'])
        self.seat = f"{seat_number}{seat_letter}"

    # def on_submit(self):
    #     if self.status != 'Boarded':
    #         frappe.throw("Cannot submit unless status is Boarded.")

    def before_submit(self):
        print(self.status, "hello")
        if self.status != "Boarded":
            frappe.log("Current Ticket Status: {}".format(self.status))
            frappe.throw("cannot submit unless status is Boarded.")
            
