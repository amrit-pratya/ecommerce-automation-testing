# E-Commerce Automation Testing Framework

A scalable end-to-end UI automation testing framework built with **Python, Playwright, and PyTest**.

The framework automates critical e-commerce workflows including authentication, product selection, cart validation, checkout, form validation, and order completion.

---

## 🚀 Key Features

- ✅ Page Object Model (POM)
- ✅ Playwright browser automation
- ✅ PyTest test framework
- ✅ Positive testing
- ✅ Negative testing
- ✅ Data-driven testing with PyTest parameterization
- ✅ Reusable PyTest fixtures
- ✅ End-to-end workflow testing
- ✅ Checkout form validation
- ✅ Cross-browser testing
- ✅ HTML test reporting
- ✅ Automatic screenshots on test failure
- ✅ Chromium, Firefox, and WebKit support
- ✅ Git version control
- ✅ GitHub repository

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Playwright | Browser automation |
| PyTest | Test framework |
| pytest-playwright | Playwright integration with PyTest |
| pytest-html | HTML test reporting |
| Git | Version control |
| GitHub | Source code hosting |

---

## 🏗️ Framework Architecture

The framework follows the **Page Object Model (POM)** design pattern to separate test logic from page-specific locators and actions.

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
          +-----------------+------------------+
          |                 |                  |
      LoginPage        InventoryPage        CartPage
                                                 |
                                          CheckoutPage
                                                 |
                                      CheckoutOverviewPage
                            |
                        Playwright
                            |
                +-----------+-----------+
                |           |           |
            Chromium     Firefox      WebKit
```

---

## 📁 Project Structure

```text
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
+-- reports/                    # Local generated HTML reports
+-- screenshots/                # Local failure screenshots
|
+-- conftest.py
+-- pytest.ini
+-- requirements.txt
+-- .gitignore
+-- README.md
```

---

## 🧪 Test Coverage

| Module | Test Scenarios |
|---|---|
| Login | Valid and invalid authentication |
| Inventory | Product selection and add-to-cart |
| Cart | Product and quantity validation |
| Checkout | Customer information and checkout workflow |
| Checkout Validation | Empty first name, last name, and postal code |
| Order Completion | Product, price, subtotal, tax, total, and confirmation |
| Cross-Browser | Chromium, Firefox, and WebKit |

### Current Test Execution

**9 test scenarios × 3 browsers = 27 test executions**

- 🟢 Chromium: 9/9 passed
- 🟢 Firefox: 9/9 passed
- 🟢 WebKit: 9/9 passed
- 🟢 Total: **27/27 passed**

---

## 🔐 Authentication Testing

The login module includes both positive and negative scenarios.

### Positive Test

- Valid username
- Valid password
- Successful login
- Inventory page verification

### Negative Tests

- Invalid username + invalid password
- Valid username + invalid password
- Invalid username + valid password

---

## 🛒 Inventory & Cart Testing

The framework validates core shopping functionality.

### Inventory

- Product selection
- Add product to cart
- Cart badge validation

### Cart

- Verify product name
- Verify product quantity
- Verify cart contents

---

## 💳 Checkout Testing

The framework automates the complete checkout workflow:

```text
Login
  ↓
Product Selection
  ↓
Add Product to Cart
  ↓
Open Cart
  ↓
Checkout
  ↓
Enter Customer Details
  ↓
Checkout Overview
  ↓
Validate Product and Price
  ↓
Validate Subtotal, Tax and Total
  ↓
Finish Order
  ↓
Verify Order Confirmation
```

---

## ❌ Checkout Validation Testing

Negative testing is implemented for mandatory checkout fields.

### Tested Validation Scenarios

- Empty First Name
- Empty Last Name
- Empty Postal Code

Example workflow:

```text
Enter Invalid / Missing Data
          ↓
Click Continue
          ↓
Application Validation
          ↓
Error Message
          ↓
PyTest Assertion
```

---

## 🌐 Cross-Browser Testing

The framework supports three Playwright browser engines:

- Chromium
- Firefox
- WebKit

### Run Chromium

```powershell
pytest --browser chromium
```

### Run Firefox

```powershell
pytest --browser firefox
```

### Run WebKit

```powershell
pytest --browser webkit
```

### Run All Browsers

```powershell
pytest --browser chromium --browser firefox --browser webkit
```

This executes:

```text
9 test scenarios × 3 browsers = 27 test executions
```

Latest verified result:

```text
27 passed
```

---

## 📊 HTML Test Reporting

The framework uses **pytest-html** to generate HTML test reports.

### Create Reports Directory

```powershell
mkdir reports
```

### Generate HTML Report

```powershell
pytest --html=reports/test_report.html --self-contained-html
```

The report provides information about:

- Test results
- Passed tests
- Failed tests
- Test duration
- Environment information
- Test metadata

The generated report is stored locally at:

```text
reports/test_report.html
```

---

## 📸 Automatic Failure Screenshots

The framework automatically captures a **full-page screenshot whenever a UI test fails**.

Screenshots are stored locally in:

```text
screenshots/
```

### Failure Handling Flow

```text
Test Execution
      |
      ↓
Test Fails
      |
      ↓
PyTest Detects Failure
      |
      ↓
Playwright Captures Screenshot
      |
      ↓
Screenshot Saved
      |
      ↓
Developer Investigates Failure
```

This makes debugging UI automation failures significantly easier.

---

## 🧩 Page Object Model

The project uses the **Page Object Model** to separate test logic from page-specific implementation.

### Page Objects

```text
LoginPage
    ↓
InventoryPage
    ↓
CartPage
    ↓
CheckoutPage
    ↓
CheckoutOverviewPage
```

Each Page Object contains:

- Page locators
- Page actions
- Reusable methods

This approach improves:

- Maintainability
- Reusability
- Readability
- Scalability
- Test isolation

---

## 🔧 PyTest Fixtures

Reusable PyTest fixtures are implemented through `conftest.py`.

The framework includes fixtures for:

- Base URL configuration
- Logged-in browser state
- Failure screenshot handling

Example concept:

```text
Test
  ↓
logged_in_page fixture
  ↓
Automatic Login
  ↓
Test Execution
```

This prevents repeated setup code across multiple test cases.

---

## 📈 Data-Driven Testing

The framework supports PyTest parameterization for executing the same test logic with multiple input combinations.

Example:

```python
@pytest.mark.parametrize(
    "username,password",
    [
        ("wrong_user", "wrong_password"),
        ("standard_user", "wrong_password"),
        ("wrong_user", "secret_sauce"),
    ]
)
```

This approach improves test coverage while reducing code duplication.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ecommerce-automation-testing.git
cd ecommerce-automation-testing
```

> Replace `YOUR_USERNAME` with your actual GitHub username.

### 2. Create a Virtual Environment

Windows PowerShell:

```powershell
python -m venv venv
```

### 3. Activate the Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 5. Install Playwright Browsers

```powershell
playwright install
```

---

## ▶️ Running Tests

### Run All Tests

```powershell
pytest
```

### Run Login Tests

```powershell
pytest tests/test_login.py
```

### Run Inventory Tests

```powershell
pytest tests/test_inventory.py
```

### Run Checkout Tests

```powershell
pytest tests/test_checkout.py
```

### Run All Tests on Chromium

```powershell
pytest --browser chromium
```

### Run All Tests on Firefox

```powershell
pytest --browser firefox
```

### Run All Tests on WebKit

```powershell
pytest --browser webkit
```

### Run Across All Supported Browsers

```powershell
pytest --browser chromium --browser firefox --browser webkit
```

---

## 📝 Test Execution Results

### Latest Verified Execution

```text
Platform: Windows 11
Python: 3.14
PyTest: 9.1.1
Playwright: 1.62.0

Test Scenarios: 9
Browsers: 3
Total Executions: 27

Chromium: 9/9 PASSED
Firefox: 9/9 PASSED
WebKit: 9/9 PASSED

TOTAL: 27/27 PASSED
```

---

## 🔄 Continuous Integration

CI/CD integration using **GitHub Actions** is planned as the next enhancement.

The intended pipeline will automatically:

```text
Git Push
   ↓
GitHub Actions
   ↓
Setup Python
   ↓
Install Dependencies
   ↓
Install Playwright
   ↓
Run Automated Tests
   ↓
Generate Test Results
   ↓
Pass / Fail
```

---

## 🚀 Future Improvements

Planned improvements include:

- [ ] API testing and API automation
- [ ] Database validation
- [ ] Advanced test data management
- [ ] Environment-specific configuration
- [ ] Parallel test execution
- [ ] GitHub Actions CI/CD
- [ ] Automated CI test reports
- [ ] Advanced logging
- [ ] PyTest markers for test categorization
- [ ] Additional e-commerce scenarios
- [ ] API + UI integration testing
- [ ] Test execution dashboard

---

## 🎯 Skills Demonstrated

This project demonstrates practical experience with:

### Testing

- Functional Testing
- Regression Testing
- UI Testing
- Integration-style workflow testing
- Negative Testing
- Test Case Design
- Test Execution
- Bug/Failure Analysis

### Automation

- Playwright
- PyTest
- Page Object Model
- PyTest Fixtures
- Parameterization
- Cross-Browser Testing
- Automated Reporting
- Failure Screenshots

### Software Engineering

- Python
- Object-Oriented Programming
- Modular Architecture
- Git
- GitHub
- Virtual Environments
- Test Framework Design

---

## 💼 SDET Relevance

This project was designed to demonstrate practical **Software Development Engineer in Test (SDET)** skills rather than isolated automation scripts.

The framework focuses on:

```text
Reusable Automation
        +
Maintainable Architecture
        +
Functional Testing
        +
Negative Testing
        +
Cross-Browser Testing
        +
Automated Reporting
        +
Failure Debugging
        =
SDET Automation Framework
```

---

## 👨‍💻 Author

**Amrit Pratya**

B.Tech | AI & Robotics | Software Testing & Automation

---

## ⚠️ Disclaimer

This project is created for **educational, portfolio, and SDET automation testing practice** using the SauceDemo application.

The project is not affiliated with or endorsed by Sauce Labs.

---
