# Copyright (c) 2025, Mr Rohan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Attendance(Document):

	def validate(self):
		# To eliminate Duplicates Attendance
		members_updated = set()
		for record in self.members_attended:
			if record.members in members_updated:
				frappe.throw(f"The attendence for '{record.name1}' has already been updated for {self.date}.")
			members_updated.add(record.members)
		