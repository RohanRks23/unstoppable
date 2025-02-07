# The Unstoppable Gym 💪

**Find your better self, challenge yourself, become Unstoppable!**

This Frappe application empowers gym owners to manage their business efficiently, helping them focus on what matters most: motivating their members to achieve their fitness goals.

## Key Features

* **Flexible Membership Plan Management:** Create and customize membership plans to cater to diverse needs and preferences.
* **Seamless Member Management:** Effortlessly manage member enrollments, memberships, and contact information.
* **Attendance Tracking:** Track member attendance with ease, gaining valuable insights into gym usage patterns.
* **Simplified Dashboards:** Intuitive and easy-to-use dashboards that provide a clear, real-time overview of key business metrics, enabling quick decision-making and performance tracking.
* **Streamlined Operations:** Automate workflows to save time and reduce administrative overhead.

## Installation and setup

**1. Set up your Frappe Bench:**
If you prefer to test the application by setting up a local frappe bench environment (Follow the link provided below).

   - Follow the official Frappe Framework Installation guide: https://docs.frappe.io/framework/user/en/installation
   - Create a site in the frappe bench enviornment using the `bench` command:
   ```
   bench new-site <site-name>
   ```

**Testing the Application:**

If you prefer to test the application without setting up a local environment, you can use a codespace repository (Follow the link provided below).

   **[Codespace Repository](https://github.com/ankush/frappe_codespace.git)**
   - This will open your bench environment in VSCode (Browser) where you can follow the below process.
   
   - Create a site in the frappe bench enviornment using the `bench` command:
      ```
      bench new-site <site-name>
      ```

**2. Install the App:**

   - Clone this repository: 
   - Using git command: `git clone <URL_OF_THIS_REPO>`
                        OR
   - Navigate to your Frappe bench directory.
   - Install the app using the `bench` command:
     ```bash
     bench get-app unstoppable
     ```

**3. Install the app in your site:**

   - Create a new Frappe site (if you havent already). Skip if you already have a site in your bench environment.
```
bench new-site <site-name>
```
   - Install the app on your site:
```
bench --site <site-name> install-app unstoppable
```

**4. Start your Frappe bench:**

   - Start the Frappe bench: `bench start`
   - Access your application: http://localhost:8000


## Getting Started: A Beginner’s Guide to Membership Plans

### For Gym Officials

[Managing Membership Plans](https://github.com/user-attachments/assets/5808d38d-f676-413d-89e6-4335a91edbc2)

Gym officials can easily access the **Membership Plan list** by clicking on **Membership Plans** shotcut in **Gym Dashboard Workspace** or by searching for it in the **Awesome Bar**. This will redirect them to the **Membership Plan Doctype List View**, where they can create multiple membership plans by defining their names, amenities, and pricing structures.

Additionally, they have the option to control the visibility of these plans—either making them publicly available or restricting them to an exclusive inner circle.

**Note:** A new user can only access publicly available plans. Once they become a member, they gain access to exclusive inner-circle plans.

### For Members

**Accessing Membership Plans**

Users can visit the publicly accessible membership page via:
 - http://Domain/unstoppable or http://localhost:8000/unstoppable.

Video 2: Membership Registration Process

A dedicated webpage has been created where users can explore available membership plans. Clicking the “**Register Now**” button redirects them to a web view of the **Membership Plans Doctype List View**.

**Users can:**

 - View plan details by clicking “**View Plan.**”

 - Explore plan features through the detailed form view.

 - Book a membership by clicking the “**Book Plan**” button.

Upon selecting a plan, the system will autofill the details. The user can then enter personal information, choose a preferred start and end date, and confirm the booking.

Once confirmed, a new record is created in the **Members Doctype**, storing the user’s details in the database. The user is then redirected to the **Members Doctype List View**.

### Membership Payment Process

Video 3: Payment Setup and Status Updates

Upon accessing their new membership record, users can review their provided details. Initially, the membership and payment status remain **“Pending”** until payment details are provided.

**To proceed with payment:**

The user clicks on the account number to create a new payment record.

A dialog box appears where they can enter their account number and save the details.

This generates a new payment record in the **Payment Doctype**, tracking all transactions.

The system automatically updates payment and membership statuses and calculates payment history details.

Video 4: Clearing Outstanding Dues

**To settle outstanding amounts:**

Users can click the **“Pay Now”** button, which redirects them to their **Payment Information** page.

The system autofills the outstanding amount along with the current date.

Clicking **“Pay Now”** confirms the payment, updating the payment history with the date and amount.

A comprehensive payment history is available in the **Payment Doctype**, listing all previous transactions.

Users can navigate back to the **Members Doctype** via the **“Back to Members”** button, where the **Payments and Validity** section updates accordingly.

### Membership Renewal

Video 5: Renewing Membership Plans

If a user’s membership is nearing expiration or they wish to renew, they can do so by clicking the **“Renew”** button. This action:

Transfers current membership details to the **Membership Renewals** section.

Clears previous plan details, allowing selection of a new plan.

**Note:** Once a user becomes a member, they gain access to both public and inner-circle membership plans. During renewal, users must manually select a new plan, specify start and end dates, and provide an account number for tracking transactions before saving the form.

### Attendance Management

Video 6: Tracking Member Attendance

Gym coaches can efficiently track attendance by clicking on **Gym Attendance** shotcut in **Gym Dashboard Workspace** or by searching for the **Attendance List** in the **Awesome Bar**. They can create new attendance records by:

Selecting a specific date.

Adding attending members to the **Members Attended Child Table**.

All supporting dashboards update automatically with new attendance data.

### Dashboard & Analytics

Video 7: Simplified Dashboards for Gym Officials

Gym officials can monitor membership, payment, and attendance details using a streamlined **Dashboard Charts** available within **"The Unstoppable Gym" Workspace**. This ensures efficient tracking and management of all relevant data in a user-friendly interface.



### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/unstoppable
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade
### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

mit
