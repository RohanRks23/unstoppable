import frappe
from frappe.utils import getdate, add_days

def on_membership_creation(doc, method):
        # Triggered when a new membership is created
        # frappe.msgprint(f"Membership for {doc.full_name} has been created.")
        frappe.sendmail(
            recipients=doc.email,
            subject="Welcome to Our Membership Program!",
            message=f"""
            <p>Dear {doc.full_name},</p>
            <p>Thank you for joining!</p> 
            <p>Your membership has been successfully created.</p>
            """
        )

def on_membership_updates(doc, method):
        # Triggered when a new membership is created
        # frappe.msgprint(f"Membership for {doc.full_name} has been updated.")
        frappe.sendmail(
            recipients=doc.email,
            subject="Your Membership has an update!",
            message=f"""
            <p>Dear {doc.full_name},</p> 
            <p>Your membership has been updated.</p>
            """
        )

def daily_reminder_task_user():

    today = getdate()
    # get data of the members whose membership is expiring in the next 7 days
    expiring_members = frappe.get_all(
        'Members', 
        filters={
            'end_date': ['between', [today, add_days(today, 7)]]
        },
        fields=['name', 'email', 'end_date']
    )
    
    for member in expiring_members:
        frappe.sendmail(
            recipients=member.email,
            subject="Your Membership is Expiring Soon",
            message=f"""
            <p>Dear {member.name},</p>
            <p>Your membership is expiring on {member.end_date}.</p> 
            <p>Please renew your membership.</p>
            """
        )

def weekly_summary_task():
    expired_members = frappe.get_all(
        'Members', 
        filters={
            'membership_status': 'Expired'
        },
        fields=['name', 'full_name', 'email', 'end_date']
    )
    
    if expired_members:
        recipients = "rohan.s@techbulls.co.in"

        # Generate HTML table rows dynamically
        # Join and seperate the data based on the rows and cells of each record using .join as string
        table_rows = "".join([
            f"<tr><td>{member.name}</td><td>{member.full_name}</td><td>{member.email}</td><td>{member.end_date}</td></tr>"
            # loop the above process for each member in expired_members to insert in new table row.
            for member in expired_members
        ])

        message = f"""
        <p>Dear User,</p>
        <p>The following memberships have expired:</p>
        <table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse; width: 100%;">
            <thead>
                <tr>
                    <th style="background-color: #f2f2f2;">Member ID</th>
                    <th style="background-color: #f2f2f2;">Member Name</th>
                    <th style="background-color: #f2f2f2;">Email</th>
                    <th style="background-color: #f2f2f2;">End Date</th>
                    
                </tr>
            </thead>
            <tbody>
                {table_rows}
            </tbody>
        </table>
        <p>Best regards,<br>The Unstoppable Gym</p>
        """

        frappe.sendmail(
            recipients=recipients,
            subject="Weekly Summary of Expired Memberships",
            message=message
        )
        
        frappe.msgprint("Weekly Summary of Expired Memberships has been sent.")

def daily_reminder_task_owners():
    # Get today's date
    today = getdate()
    
    # Query to get members whose membership is expiring Tomorrow
    upcoming_renewals = frappe.get_all(
        'Members', 
        filters={
            'end_date': ['between', [today, add_days(today, 1)]]
        },
        fields=['name', 'full_name', 'email', 'end_date']
    )
    
    # Send the summary to admins or a distribution list
    if upcoming_renewals:
        recipients = "rohan.s@techbulls.co.in"

        # Generate HTML table rows dynamically
        # Join and seperate the data based on the rows and cells of each record using .join as string
        table_rows = "".join([
            f"<tr><td>{member.name}</td><td>{member.full_name}</td><td>{member.email}</td><td>{member.end_date}</td></tr>"
            # loop the above process
            for member in upcoming_renewals
        ])
        
        message = f"""
        <p>Dear User,</p>
        <p>The following memberships are expiring within the next day:</p>
        <table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse; width: 100%;">
            <thead>
                <tr>
                    <th style="background-color: #f2f2f2;">Member ID</th>
                    <th style="background-color: #f2f2f2;">Full Name</th>
                    <th style="background-color: #f2f2f2;">Email</th>
                    <th style="background-color: #f2f2f2;">End Date</th>
                </tr>
            </thead>
            <tbody>
                {table_rows}
            </tbody>
        </table>
        <p>Best regards,<br>The Unstoppable Gym</p>
        """

        frappe.sendmail(
            recipients=recipients,
            subject="Daily Reminders for Upcoming Renewals",
            message=message
        )

