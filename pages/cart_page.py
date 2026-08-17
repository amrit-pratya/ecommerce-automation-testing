from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page):
        self.page = page

        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator("#checkout")

    def open(self):
        self.page.goto("https://www.saucedemo.com/cart.html")

    def get_product_name(self):
        return self.cart_items.locator(".inventory_item_name").inner_text()

    def get_quantity(self):
        return self.cart_items.locator(".cart_quantity").inner_text()

    def click_checkout(self):
        self.checkout_button.click()