from playwright.sync_api import expect

from pages.inventory_page import InventoryPage


def test_add_product_to_cart(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)

    inventory_page.add_product_to_cart("Sauce Labs Backpack")

    expect(inventory_page.cart_badge).to_have_text("1")