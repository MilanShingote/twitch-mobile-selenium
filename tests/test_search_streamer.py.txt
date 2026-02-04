import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage


@pytest.mark.smoke
def test_search_and_open_streamer(driver):
    home = HomePage(driver)
    search_results = SearchResultsPage(driver)

    # Step 1: Go to Twitch
    home.open()
    home.handle_popup()

    # Step 2: Click search icon
    home.tap_search()

    # Step 3: Input StarCraft II
    search_results.search_for("StarCraft II")

    # Step 4: Scroll down twice
    search_results.scroll_down_times(2)

    # Step 5: Select one streamer
    search_results.select_first_streamer()

    # Validation: video page loaded
    assert "twitch.tv" in driver.current_url
