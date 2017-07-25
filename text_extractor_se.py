"""

text_extractor_se.py returns the required text by parsing the html of a website.

"""

from html_page_source_se import *
from html.parser import HTMLParser


# TextExtractor will extract all the text from a webpage
class TextExtractor(HTMLParser):

    def __init__(self):
        super().__init__()
        self.txt_data = ''

# when we call HTMLParser feed() this method is called
    def handle_data(self, data):
        self.txt_data = self.txt_data + data

    def extracted(self):
        return self.txt_data

    def error(self, message):
        pass


# text_extractor function will extract the required text from website
def text_extractor(url):
    response = html_page_source(url)
    e_link = TextExtractor()
    print('\nGot text to extract.\n')
    e_link.feed(response)
    return e_link.extracted()

