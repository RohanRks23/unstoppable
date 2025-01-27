# Copyright (c) 2025, Mr Rohan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Payment(Document):	
	
	def before_save(self):
		self.total_paid = 0

		if self.payment_history:
			total_paid = 0
			for value in self.payment_history:
				total_paid += value.amount
			self.total_paid = total_paid
