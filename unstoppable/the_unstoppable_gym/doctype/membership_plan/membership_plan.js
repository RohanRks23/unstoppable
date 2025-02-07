// Copyright (c) 2025, Mr Rohan and contributors
// For license information, please see license.txt

frappe.ui.form.on("Membership Plan", {
	plan_price:function(frm) {
        if (frm.doc.plan_price){
            total = frm.doc.plan_price * frm.doc.plan_duration
            frm.set_value('total_price', total);
        }

	},
    refresh(frm) {
        if (!frm.doc.total_price){
            total = frm.doc.plan_price * frm.doc.plan_duration
            frm.set_value('total_price', total);
        }

	},
});
