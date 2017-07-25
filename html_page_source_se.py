"""

It uses selenium to parse javascript based websites too. HTML source of website
is also stored in a text file as source.txt.

"""

from folders_files_se import *
from selenium import webdriver


# html_page_source method is used to extract html_source of website using selenium
def html_page_source(url):
    html_source = ''
    working_dir = os.getcwd()
    try:
        browser = webdriver.PhantomJS()
        browser.get(url)
        html_source = browser.page_source
        print('\nGot HTML source of requested page.\n')
        create_new_file(os.path.join(working_dir, 'source.txt'), html_source)
        browser.close()
    except Exception as e:
        print(e)
    return html_source
