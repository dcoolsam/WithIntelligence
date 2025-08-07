from pages.base_page import BasePage

class ExplorePage(BasePage):
    # Locators
    PAGE_TITLE = 'h1, .page-title'
    
    def get_page_title(self) -> str:
        """Get page title"""
        return self.get_text(self.PAGE_TITLE)
    
    def is_loaded(self) -> bool:
        """Check if explore page is loaded"""
        return "/explore" in self.page.url