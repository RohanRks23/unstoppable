# Copyright (c) 2025, Mr Rohan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
from dateutil.relativedelta import relativedelta
from frappe.utils import getdate, add_days

class Members(Document):
    def before_naming(self):
        # For full name
        if self.last_name:
            self.full_name = f"{self.first_name} {self.last_name}"
        else:
            self.full_name = self.first_name
        
    def before_save(self):
        #To calculate outstanding amount
        self.payments()
        
		# For membership status
        # Convert end date to yyyy-mm-dd format
        end_date = datetime.strptime(self.end_date, "%Y-%m-%d")
        current_date = datetime.now()

        if self.account_number:
            # now compare end date and current date
            if current_date >= end_date:
                self.membership_status = 'Expired'
            else:
                self.membership_status = 'Active'
        else:
            self.membership_status = 'Pending'

    def validate(self):
        self.payments()
        
		# Calculate the difference in months between start and end dates
        start_date_obj = datetime.strptime(self.start_date, "%Y-%m-%d")
        end_date_obj = datetime.strptime(self.end_date, "%Y-%m-%d")
        difference = relativedelta(end_date_obj, start_date_obj)
        months_left = difference.years * 12 + difference.months

        # To validate the start date and end date inline with the membership plan duration
        if months_left == self.membership_duration:
            validated = True
        else:
            validated = False

        if not validated:
            frappe.throw("Start date and End dates should enline with the selected Membership plan duration.")
            
    def payments(self):
        # To calculate total fee
        self.total_fee = self.monthly_fee * self.membership_duration
        
        # The amount user have to pay till the current month.
        start_date_obj = datetime.strptime(self.start_date, "%Y-%m-%d")
        current_date_obj = datetime.now()
        difference = relativedelta(current_date_obj, start_date_obj)
        months = difference.years * 12 + difference.months
        
        self.amount_to_pay_till_date = months * self.monthly_fee

        if self.account_number:
            #write code to get the total amount paid till date by the user
            # self.amount_paid
            total_paid = frappe.db.get_value(
                doctype="Payment", 
                filters={"name": self.account_number}, 
                fieldname="total_paid"
                )
            if total_paid:
                self.amount_paid = total_paid
            else:
                self.amount_paid = 0.00
        else:
            self.amount_paid = 0.00
        #The total outstanding amount the user have to pay till date to clear his dues
        self.outstanding_amount = self.amount_to_pay_till_date - self.amount_paid

        if self.account_number:
            # Updateing payment status based on the outstanding amount
            if self.outstanding_amount:
                self.payment_status='Unpaid'
            else:
                self.payment_status='Paid'
        else:
            self.payment_status='Pending'



    
