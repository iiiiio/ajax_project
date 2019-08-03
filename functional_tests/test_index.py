from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class IndexTest(FunctionalTest):
    def test_index_page_renders_properly(self):
        # John goes to index
        self.browser.get(self.live_server_url + "/joke_app/")

        # He notices the html title on top
        self.assertIn('HTML Joke of the Day', self.browser.title)

        # He also sees the joke on the page
        joke_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Where do bees go when they get married?', joke_text)

        # Then, he sees the link to fetch the answer to the joke
        answer_text = self.browser.find_element_by_tag_name('input').get_attribute("value")
        self.assertIn('Fetch Answer', answer_text)
