import frappe
from frappe.utils import getdate, add_days

def daily_reminder_task_user():
    # Get today's date
    today = getdate()
    
    # Query members whose membership is expiring in the next 7 days
    expiring_members = frappe.get_all(
        'Members', 
        filters={
            'end_date': ['between', [today, add_days(today, 7)]]
        },
        fields=['name', 'email', 'end_date']
    )
    
    # Send reminders to these members (you can use frappe.sendmail or any other method)
    for member in expiring_members:
        # Example of sending an email reminder (you can customize this)
        frappe.sendmail(
            recipients=member.email,
            subject="Your Membership is Expiring Soon",
            message=f"Dear {member.name},\n\nYour membership is expiring on {member.end_date}. Please renew your membership."
        )

def daily_reminder_task_owners():
    # Get today's date
    today = getdate()
    
    # Query members whose membership is expiring in the next a day
    upcoming_renewals = frappe.get_all(
        'Members', 
        filters={
            'end_date': ['between', [today, add_days(today, 1)]]
        },
        fields=['name', 'email', 'end_date']
    )
    
    # You can send the summary to admins or a distribution list
    if upcoming_renewals:
        # Example of sending a weekly summary email
        recipients = "rohan.s@techbulls.co.in"  # Replace with actual recipients
        member_names = ", ".join([member.name for member in upcoming_renewals])
        member_details = "\n".join([f"{member.name}: {member.end_date}" for member in upcoming_renewals])

        frappe.sendmail(
            recipients=recipients,
            subject="Daily reminders for upcoming renewals.",
            message=f"The following are some of the upcoming renewals for today:\n\n{member_details}"
        )

def weekly_summary_task():
    # Query expired memberships
    expired_members = frappe.get_all(
        'Members', 
        filters={
            'membership_status': 'Expired'
        },
        fields=['name', 'email', 'end_date']
    )
    
    # You can send the summary to admins or a distribution list
    if expired_members:
        # Example of sending a weekly summary email
        recipients = "rohan.s@techbulls.co.in"  # Replace with actual recipients
        member_names = ", ".join([member.name for member in expired_members])
        member_details = "\n".join([f"{member.name}: {member.end_date}" for member in expired_members])

        frappe.sendmail(
            recipients=recipients,
            subject="Weekly Summary of Expired Memberships",
            message=f"The following memberships have expired:\n\n{member_details}"
        )


def on_membership_creation(doc, method):
        # Triggered when a new membership is created
        # frappe.msgprint(f"Membership for {doc.full_name} has been created.")

        # Example: Send a welcome email to the new member
        frappe.sendmail(
            recipients=doc.email,
            subject="Welcome to Our Membership Program!",
            message=f"Dear {doc.full_name},\n\nThank you for joining! Your membership has been successfully created."
        )

def on_membership_updates(doc, method):
        # Triggered when a new membership is created
        frappe.msgprint(f"Membership for {doc.full_name} has been updated.")

        # Example: Send a welcome email to the new member
        frappe.sendmail(
            recipients=doc.email,
            subject="Your Membership has an update!",
            message=f"Dear {doc.full_name},\n\n Your membership has been updated."
        )
