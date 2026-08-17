from playwright.sync_api import Page


class InventoryPage:

    def __init__(self, page: Page):
        self.page = page

        self.inventory_container = page.locator(".inventory_list")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def is_inventory_page_visible(self):
        return self.inventory_container.is_visible()

    def add_product_to_cart(self, product_name: str):
        product = self.page.locator(
            ".inventory_item",
            has_text=product_name
        )

        product.locator("button").click()

    def get_cart_count(self):
        return self.cart_badge.inner_text()