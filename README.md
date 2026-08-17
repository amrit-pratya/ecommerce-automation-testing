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
