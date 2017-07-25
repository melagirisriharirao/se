"""

links_extractor_se.py takes in base_url, e_tag and e_attribute and returns the required links by parsing
the html of a website.

base_url : the website url (example: https://www.example.com/)
e_tag : the html tag (example: 'a')
e_attribute: the attribute inside html tag (example: 'href')

"""
from html.parser import HTMLParser
from urllib import parse
from html_page_source_se import *


# Extractor class will return a set which contains all the links required
class LinkExtractor(HTMLParser):

    def __init__(self, base_url, e_tag, e_attr):
        super().__init__()
        self.base_url = base_url
        self.e_tag = e_tag
        self.e_attr = e_attr
        self.links = set()

# when we call HTMLParser feed() this method is called and collects all the links in a set
    def handle_starttag(self, tag, attrs):
        if tag == self.e_tag:
            for (attribute, value) in attrs:
                if attribute == self.e_attr:
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def extracted(self):
        return self.links

    def error(self, message):
        pass


# links_extractor function will extract the required links from website
def links_extractor(url, tag, attribute):
    response = html_page_source(url)
    e_link = LinkExtractor(url, tag, attribute)
    print('\nGot links to extract.\n')
    e_link.feed(response)
    return e_link.extracted()



