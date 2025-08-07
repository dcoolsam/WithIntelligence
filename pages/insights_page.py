from pages.base_page import BasePage

class InsightsPage(BasePage):
    # Locators
    EXPLORE_LINK = 'a[href*="/explore"]'
    SEARCH_BOX = 'input[type="search"], [data-testid="search-input"]'
    SEARCH_RESULTS_TITLE = 'h1, h2, .search-title'
    SEARCH_RESULTS = '.search-results, .results-list'
    NO_RESULTS_MESSAGE = '.no-results, .empty-state'
    
    def click_explore_link(self):
        """Click on Explore link in main menu"""
        self.click(self.EXPLORE_LINK)
    
    def search(self, query: str):
        """Perform search"""
        self.click(self.SEARCH_BOX)
        self.fill(self.SEARCH_BOX, query)
        self.page.keyboard.press('Enter')
    
    def get_search_results_title(self) -> str:
        """Get search results title"""
        return self.get_text(self.SEARCH_RESULTS_TITLE)
    
    def get_no_results_message(self) -> str:
        """Get no results message"""
        return self.get_text(self.NO_RESULTS_MESSAGE)
    
    def has_search_results(self) -> bool:
        """Check if search results are displayed"""
        return self.is_visible(self.SEARCH_RESULTS)