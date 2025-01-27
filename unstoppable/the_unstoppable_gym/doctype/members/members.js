// Copyright (c) 2025, Mr Rohan and contributors
// For license information, please see license.txt

frappe.ui.form.on("Members", {
    refresh(frm){
        calculate_payments(frm);
    },
    membership_plan: function(frm){
        calculate_payments(frm);
    },
    end_date: function(frm){
        membership_status(frm)
    },
    pay_now: function(frm) {
        if (frm.saved = true) {
            let account_number = frm.doc.account_number;
            let amount = frm.doc.outstanding_amount;
            // Checking if a payment with the same account number exists in paymants doctype
            frappe.db.get_value('Payment', { name: account_number }, 'name', function(result) {
                if (result && result.name) {
                    // If it exists then routing to that record
                    // frappe.set_route('Form', 'Payment', result.name);

                    frappe.db.set_value('Payment', result.name, 'amount', amount)
                        .then(() => {
                            frappe.db.set_value('Payment', result.name, 'member_id', frm.doc.name)
                            frappe.set_route('Form', 'Payment', result.name);
                            frappe.ui.form.refresh(doc);
                            frm.refresh_field('member_id');
                            
                        });

                } else {
                    frappe.msgprint(__('Please have a valid account number.'));
                }        
            });
        } else {
            frappe.msgprint(__('Please save the form before proceeding.'));        
        }
    },
    renew_plan: function(frm) {
        if (frm.doc.outstanding_amount <= 0){
            if (frm.doc.start_date && frm.doc.end_date && frm.doc.account_number) {
                // Add a new row in the previous plans
                let row = frm.add_child('previous_plans');
                row.plan = frm.doc.membership_plan;
                row.start_date = frm.doc.start_date;
                row.end_date = frm.doc.end_date;
                row.account_no = frm.doc.account_number;

                // Clear the fields after adding to payment_history
                frm.set_value('membership_plan', '');
                frm.set_value('start_date', '');
                frm.set_value('end_date', '');
                frm.set_value('membership_duration', '');
                frm.set_value('membership_status', 'Pending');

                frm.set_value('payment_status', 'Pending');
                frm.set_value('amount_to_pay_till_date', '0');
                frm.set_value('monthly_fee', '0');
                frm.set_value('total_fee', '0');
                frm.set_value('account_number', '');
                frm.set_value('amount_paid', '0');
                
                // Refresh the field so that the new row is displayed
                frm.refresh_field('previous_plans');
                // frm.save();
            } else {
                frappe.msgprint(__('Please verify the start date, end date and account number'))
            }
        }
        else {
            frappe.msgprint(__('Please clear the outstanding amount on your previous membership plan.'))
        }
    }
});

// Function to calculate payments
function calculate_payments(frm) {
    // Calculate total fee
    let total_fee = frm.doc.monthly_fee * frm.doc.membership_duration;
    frm.set_value('total_fee', total_fee);

    // Calculate amount to pay till the current month
    let current_date = frappe.datetime.now_date();
    let start_date = frm.doc.start_date;

    if (start_date) {
        let current_date_obj = new Date(current_date);
        let start_date_obj = new Date(start_date);

        let yearDifference = current_date_obj.getFullYear() - start_date_obj.getFullYear();
        let monthDifference = current_date_obj.getMonth() - start_date_obj.getMonth();
        let totalMonths = yearDifference * 12 + monthDifference;

        let amount_till_date = totalMonths * frm.doc.monthly_fee;
        frm.set_value('amount_to_pay_till_date', amount_till_date);

        // Fetch the total amount paid till date by the user
        frappe.call({
            method: "frappe.client.get_value",
            args: {
                doctype: "Payment",
                filters: { name: frm.doc.account_number },
                fieldname: "total_paid"
            },
            callback: function (response) {
                if (response && response.message) {
                    frm.set_value("amount_paid", response.message.total_paid);
                } else {
                    frm.set_value("amount_paid", 0.00);
                }

                // Calculate outstanding amount
                let outstanding_amount = amount_till_date - frm.doc.amount_paid;
                frm.set_value("outstanding_amount", outstanding_amount);

                // Update payment status
                if (outstanding_amount > 0){
                    frm.set_value("payment_status", 'Unpaid');
                }
                else{
                    frm.set_value("payment_status", 'Paid');
                }
            }
        });
    }
}

function membership_status(frm) {
    //  For membership status
    if (frm.doc.end_date){
        let current_date = frappe.datetime.now_date();
        // frappe.msgprint(current_date);
        let end_date = frm.doc.end_date;

        // converting to date object to compare them
        let current_date_obj = new Date(current_date);
        let end_date_obj = new Date(end_date);

        if (current_date_obj >= end_date_obj) {
            frm.set_value('membership_status', 'Expired');
            // frappe.msgprint('Expired');
        }
        else{
            frm.set_value('membership_status', 'Active');
            // frappe.msgprint('Active');
        }
    }
}