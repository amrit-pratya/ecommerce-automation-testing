from playwright.sync_api import Page


class CheckoutOverviewPage:

    def __init__(self, page: Page):
        self.page = page

        self.product_name = page.locator(".inventory_item_name")
        self.product_price = page.locator(".inventory_item_price")
        self.subtotal = page.locator(".summary_subtotal_label")
        self.tax = page.locator(".summary_tax_label")
        self.total = page.locator(".summary_total_label")
        self.finish_button = page.locator("#finish")
        self.complete_header = page.locator(".complete-header")

    def get_product_name(self):
        return self.product_name.inner_text()

    def get_product_price(self):
        return self.product_price.inner_text()

    def get_subtotal(self):
        return self.subtotal.inner_text()

    def get_tax(self):
        return self.tax.inner_text()

    def get_total(self):
        return self.total.inner_text()

    def finish_order(self):
        self.finish_button.click()

    def get_confirmation_message(self):
        return self.complete_header.inner_text()