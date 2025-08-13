from pages.base_page import BasePage

class ExplorePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Locators
        self.page_title = page.locator('h1, .page-title')

    def get_page_title(self) -> str:
        """Get page title"""
        return self.page_title.text_content()

    def is_loaded(self) -> bool:
        """Check if explore page is loaded"""
        return "/explore" in self.page.url
