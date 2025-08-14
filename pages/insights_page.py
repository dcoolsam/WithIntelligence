from pages.base_page import BasePage
from playwright.sync_api import Page

class InsightsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.explore_link = page.locator('a[href*="/explore"]')
        self.search_box = page.get_by_test_id('globalSearch-input')
        self.search_results_title = page.locator('h1, h2, .search-title')
        self.search_results = page.get_by_test_id('tabsHandlers-tabPanel-insightsResults')
        self.no_results_message = page.get_by_test_id('tabsHandlers-tabPanel-insightsResults')

    def click_explore_link(self):
        """Click on Explore link in main menu"""
        self.click(self.explore_link)

    def search(self, query: str):
        """Perform search"""
        self.click(self.search_box)
        self.fill(self.search_box, query)
        self.page.keyboard.press('Space')
        self.page.keyboard.press('Enter')
        self.page.wait_for_load_state("networkidle")

    def get_search_results_title(self) -> str:
        """Get search results title"""
        return self.get_text(self.search_results_title)

    def get_no_results_message(self) -> str:
        """Get no results message"""
        return self.get_text(self.no_results_message)

    def has_search_results(self) -> bool:
        """Check if search results are displayed"""
        return self.is_visible(self.search_results)
