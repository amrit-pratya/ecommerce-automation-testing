# E-Commerce Automation Testing Framework

A scalable end-to-end UI automation testing framework built with **Python, Playwright, and PyTest**.

The framework automates critical e-commerce workflows including authentication, product selection, cart validation, checkout, form validation, and order completion.

## Key Features

- Page Object Model (POM)
- Playwright browser automation
- PyTest test framework
- Positive and negative testing
- Data-driven testing with PyTest parameterization
- Reusable PyTest fixtures
- End-to-end workflow testing
- Checkout form validation
- Cross-browser testing
- HTML test reporting
- Automatic screenshots on test failure
- Chromium, Firefox, and WebKit support

## Test Coverage

| Module | Test Scenarios |
|---|---|
| Login | Valid and invalid authentication |
| Inventory | Product selection and add-to-cart |
| Cart | Product and quantity validation |
| Checkout | Customer information and workflow |
| Checkout Validation | Empty first name, last name, and postal code |
| Order Completion | Product, price, subtotal, tax, total, and confirmation |
| Cross-Browser | Chromium, Firefox, WebKit |

### Current Test Execution

**9 test scenarios × 3 browsers = 27 test executions**

- Chromium: 9/9 passed
- Firefox: 9/9 passed
- WebKit: 9/9 passed
- Total: **27/27 passed**

## Framework Architecture

The framework follows the Page Object Model (POM) design pattern to separate test logic from page-specific locators and actions.

```text
                    PyTest
                       |
        +--------------+--------------+
        |              |              |
   test_login    test_inventory   test_checkout
        |              |              |
        +--------------+--------------+
                       |
                 Page Objects
                       |
       +---------------+----------------+
       |               |                |
   LoginPage      InventoryPage      CartPage
                                       |
                                       |
                                CheckoutPage
                                       |
                                CheckoutOverviewPage
                       |
                   Playwright
                       |
               Chromium / Firefox / WebKit

## Project Structure

ecommerce-automation-testing/
|
+-- pages/
|   +-- login_page.py
|   +-- inventory_page.py
|   +-- cart_page.py
|   +-- checkout_page.py
|   +-- checkout_overview_page.py
|
+-- tests/
|   +-- test_login.py
|   +-- test_inventory.py
|   +-- test_checkout.py
|
+-- reports/
+-- screenshots/
+-- conftest.py
+-- pytest.ini
+-- requirements.txt
+-- .gitignore
+-- README.md

git clone https://github.com/YOUR_USERNAME/ecommerce-automation-testing.git
cd ecommerce-automation-testing

## Installation
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/ecommerce-automation-testing.git
cd ecommerce-automation-testing
2. Create a virtual environment

Windows PowerShell:

python -m venv venv
3. Activate the virtual environment
.\venv\Scripts\Activate.ps1
4. Install dependencies
pip install -r requirements.txt
5. Install Playwright browsers
playwright install
Running Tests
Run all tests
pytest
Run on Chromium
pytest --browser chromium
Run on Firefox
pytest --browser firefox
Run on WebKit
pytest --browser webkit
Run across all supported browsers
pytest --browser chromium --browser firefox --browser webkit
Generate HTML Report
mkdir reports
pytest --html=reports/test_report.html --self-contained-html

The generated report provides an overview of passed and failed test cases.

Failure Screenshots

The framework automatically captures a full-page screenshot when a UI test fails.

Screenshots are stored locally in:

screenshots/

This helps with debugging failures by preserving the browser state at the time of failure.

Test Design

The framework uses:

Page Object Model for maintainability
PyTest fixtures for reusable setup
Parameterization for data-driven testing
Assertions for functional validation
Cross-browser execution for compatibility testing
HTML reports for test result analysis
Failure screenshots for debugging
Test Execution Results

The current automation suite contains:

9 test scenarios

Executed across:

3 browser engines

Total:

27 test executions

Latest verified result:

27 passed

Browsers:

Chromium — 9/9 passed
Firefox — 9/9 passed
WebKit — 9/9 passed


### Important README correction


Because `reports/` and `screenshots/` are in your `.gitignore`, they won't actually be present in the GitHub repository. That's intentional.


The README is documenting the **local runtime structure**, not claiming those generated artifacts are committed.


### Step 16.5 — Commit the updated README


Run:


```powershell
git add README.md

Then:

git commit -m "Expand framework documentation"

Then:

git push

