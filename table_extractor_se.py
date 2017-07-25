"""

table_extractor_se.py is similar to extractor.py the only change is here the TableExtractor class which
inherits the HTMLParser class is bit more complicated compared to LinkExtractor class in links_extractor.py.
This table_extractor_se.py is called only when a table from webpage needs to be scraped.

"""
from html.parser import HTMLParser
from html_page_source_se import *


# Extractor class will return a set which contains all the links required
class TableExtractor(HTMLParser):

    def __init__(self, e_tag):
        super().__init__()
        self.e_tag = e_tag
        self.table_counter = 0
        self.head_counter = 0
        self.data_counter = 0
        self.row_counter = 0
        self.table_head = []
        self.table_data = []
        self.row_data = []
        self.table = []
        self.table_list = []

# when we call HTMLParser feed() this method is called.
    def handle_starttag(self, tag, attrs):
        if tag == self.e_tag:
            self.table_counter += 1
        elif tag == 'th':
            self.head_counter += 1
        elif tag == 'td':
            self.data_counter += 1
        elif tag == 'tr':
            self.row_counter += 1

    def handle_endtag(self, tag):
        if tag == self.e_tag:
            self.table_counter -= 1
            self.table_list.append(self.table)
            self.table = []
        elif tag == 'th':
            self.head_counter -= 1
            self.row_data.append(self.table_head)
            self.table_head = []
        elif tag == 'td':
            self.data_counter -= 1
            self.row_data.append(self.table_data)
            self.table_data = []
        elif tag == 'tr':
            self.row_counter -= 1
            self.table.append(self.row_data)
            self.row_data = []

    def handle_data(self, data):
        if self.table_counter == 1:
            if self.head_counter == 1 and self.row_counter == 1:
                if data != ('\n' or '\t'):
                    self.table_head.append(data)
            else:
                if data != ('\n' or '\t'):
                    self.table_data.append(data)

    def extracted(self):
        return self.table_list

    def error(self, message):
        pass


# table_extractor function will extract the required table from website
def table_extractor(url, tag):
    response = html_page_source(url)
    e_link = TableExtractor(tag)
    print('\nGot table to extract.\n')
    e_link.feed(response)
    return e_link.extracted()
