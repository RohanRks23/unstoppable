// Copyright (c) 2025, Mr Rohan and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Attendance", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("Attendance", {
    refresh: function (frm) {

        check_for_duplicates(frm);

        // Add button to recalculate durations if needed
        frm.add_custom_button("Recalculate Durations", function () {
            frm.doc.members_attended.forEach(row => {
                if (row.from_time && row.to_time) {
                    // Convert time strings to Date objects
                    let from_time = moment(row.from_time, "HH:mm");
                    let to_time = moment(row.to_time, "HH:mm");

                    // Calculate the duration in seconds
                    let duration = to_time.diff(from_time, "seconds");
                    if (duration < 0) {
                        frappe.msgprint(__("To Time cannot be earlier than From Time."));
                        return;
                    }

                    // Update the duration in the child table
                    row.duration = duration;

                }
            });
            frm.refresh_field("members_attended");
        });

    },
    before_save: function (frm) {
        frm.doc.members_attended.forEach(row => {
            if (row.from_time && row.to_time) {
                // Convert time strings to Date objects
                let from_time = moment(row.from_time, "HH:mm");
                let to_time = moment(row.to_time, "HH:mm");

                // Calculate the duration in seconds
                let duration = to_time.diff(from_time, "seconds");
                if (duration < 0) {
                    frappe.msgprint(__("To Time cannot be earlier than From Time."));
                    return;
                }

                // Update the duration in the child table
                row.duration = duration;

            }
        });
    }
});


// Trigger for the child table
frappe.ui.form.on("Attendance Table", {
    members_attended_add: function (frm, cdt, cdn) {
        check_for_duplicates(frm);
    },
    members: function (frm, cdt, cdn) {
        check_for_duplicates(frm);
    }
});

// Function to check for duplicates in the child table
function check_for_duplicates(frm) {
    let membersUpdated = new Set();
    let duplicatesFound = false;

    frm.doc.members_attended.forEach(record => {
        if (membersUpdated.has(record.members)) {
            duplicatesFound = true;
            frappe.msgprint(__(`The attendance for '${record.members}' has already been added for ${frm.doc.date}.`));
        }
        membersUpdated.add(record.members);
    });

    if (duplicatesFound) {
        frappe.throw(__('Please remove duplicate entries from the members attended.'));
    }
}
