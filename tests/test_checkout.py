from playwright.sync_api import Page, expect

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage


def test_complete_purchase(logged_in_page):
    # Add product
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")

    # Open cart
    cart_page = CartPage(logged_in_page)
    cart_page.open()
    cart_page.click_checkout()

    # Enter customer details
    checkout_page = CheckoutPage(logged_in_page)
    checkout_page.enter_customer_details(
        "Amrit",
        "Pratya",
        "560062"
    )
    checkout_page.continue_to_overview()

    # Checkout overview
    overview_page = CheckoutOverviewPage(logged_in_page)

    expect(overview_page.product_name).to_have_text(
        "Sauce Labs Backpack"
    )

    expect(overview_page.product_price).to_have_text("$29.99")

    expect(overview_page.subtotal).to_have_text(
        "Item total: $29.99"
    )

    expect(overview_page.tax).to_be_visible()
    expect(overview_page.total).to_be_visible()

    # Finish order
    overview_page.finish_order()

    expect(overview_page.complete_header).to_have_text(
        "Thank you for your order!"
    )


def test_checkout_empty_first_name(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")

    cart_page = CartPage(logged_in_page)
    cart_page.open()
    cart_page.click_checkout()

    checkout_page = CheckoutPage(logged_in_page)
    checkout_page.enter_customer_details(
        "",
        "Pratya",
        "560062"
    )
    checkout_page.continue_to_overview()

    error_message = logged_in_page.locator("[data-test='error']")

    expect(error_message).to_have_text(
        "Error: First Name is required"
    )


def test_checkout_empty_last_name(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")

    cart_page = CartPage(logged_in_page)
    cart_page.open()
    cart_page.click_checkout()

    checkout_page = CheckoutPage(logged_in_page)
    checkout_page.enter_customer_details(
        "Amrit",
        "",
        "560062"
    )
    checkout_page.continue_to_overview()

    error_message = logged_in_page.locator("[data-test='error']")

    expect(error_message).to_have_text(
        "Error: Last Name is required"
    )


def test_checkout_empty_postal_code(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")

    cart_page = CartPage(logged_in_page)
    cart_page.open()
    cart_page.click_checkout()

    checkout_page = CheckoutPage(logged_in_page)
    checkout_page.enter_customer_details(
        "Amrit",
        "Pratya",
        ""
    )
    checkout_page.continue_to_overview()

    error_message = logged_in_page.locator("[data-test='error']")

    expect(error_message).to_have_text(
        "Error: Postal Code is required"
    )