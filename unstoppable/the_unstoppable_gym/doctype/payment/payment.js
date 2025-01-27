// Copyright (c) 2025, Mr Rohan and contributors
// For license information, please see license.txt

frappe.ui.form.on("Payment", {
	refresh(frm) {
        // frm.set_df_property('member_id', 'reqd', 1);

        frm.set_value('date', frappe.datetime.nowdate());
        frm.add_custom_button(__('Go back to Members'), function () {
            if (frm.saved = true) {
                frm.set_df_property('member_id', 'reqd', 1);
                let account_number = frm.doc.name;
                let member_id = frm.doc.member_id;
                // Checking if a Members with the same account number exists in paymants doctype
                frappe.db.get_value('Members', { name: member_id }, 'name', function(result) {
                    if (result && result.name) {
                        // If it exists then routing to that record
                        frappe.set_route('Form', 'Members', result.name);
                    } else {
                        frappe.msgprint(__('Member ID does not exists.'));
                    }        
                });
            } else {
                frappe.msgprint(__('Please save the form before proceeding.'));        
            }
        });
	},
    pay_now: function(frm) {
        if (frm.doc.name && frm.doc.date && frm.doc.amount) {
            // Add a new row in the payment_history
            let row = frm.add_child('payment_history');
            // row.account_number = frm.doc.name;
            row.date = frm.doc.date;
            row.amount = frm.doc.amount;

            // Clear the fields after adding to payment_history
            frm.set_value('amount', '');

            // Refresh the field so that the new row is displayed
            frm.refresh_field('payment_history');
            frm.save();
        } else {
            frappe.msgprint(__('Please fill the date and amount before paying.'));
        }
    },
    // after_save(frm) {
    //     frm.set_df_property('member_id', 'reqd', 1);
    // }
});
