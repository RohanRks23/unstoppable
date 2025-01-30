# The Unstoppable Gym 💪

**Find your better self, challenge yourself, become Unstoppable!**

This Frappe application empowers gym owners to manage their business efficiently, helping them focus on what matters most: motivating their members to achieve their fitness goals.

## Key Features

* **Seamless Member Management:** Effortlessly manage member enrollments, memberships, and contact information.
* **Flexible Membership Plans:** Create and customize membership plans to cater to diverse needs and preferences.
* **Attendance Tracking:** Track member attendance with ease, gaining valuable insights into gym usage patterns.
* **Streamlined Operations:** Automate workflows to save time and reduce administrative overhead.
* **[Optional Feature]** Add any additional features your app offers.

## Installation and setup

**1. Set up your Frappe Bench:**
If you prefer to test the application without setting up a local frappe bench environment (Follow the link provided below).

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

   - Create a new Frappe site: `bench new-site <site-name>`
   - Install the app on your site: `bench --site <site-name> install-app unstoppable`

**4. Start your Frappe bench:**

   - Start the Frappe bench: `bench start`
   - Access your application: http://localhost:8000


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
