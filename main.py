"""

Scrape-Everything(SE) is the project that is created to scrape everthing from a webpage.
This is used to scrape links, images, tables and text data from a html page.
Scrape-Everything(SE) is created by

                                    SRIHARI RAO M

"""
from links_extractor_se import *
from table_extractor_se import *
from text_extractor_se import *
from muti_threading_se import *


class ScrapeEverything:

    def __init__(self, url):
        self.domain_name = url
        self.final_links = set()
        self.table = []
        self.text_data = ''
        self.links_folder = ''
        self.images_folder = ''
        self.table_folder = ''
        self.text_folder = ''
        self.boot()

    # creates necessary folders required
    def boot(self):
        working_dir = os.getcwd()

        self.links_folder = os.path.join(working_dir, 'Links')
        self.images_folder = os.path.join(working_dir, 'Images')
        self.table_folder = os.path.join(working_dir, 'Tables')
        self.text_folder = os.path.join(working_dir, 'Text')

        create_folder(self.links_folder)
        create_folder(self.images_folder)
        create_folder(self.table_folder)
        create_folder(self.text_folder)

    # extract links
    def extract_links(self):
        self.final_links = links_extractor(self.domain_name, 'a', 'href')
        links_to_file(os.path.join(self.links_folder, 'links.txt'), self.final_links)
        print('\nLinks saved :)\n')

    # extract images
    def extract_images(self):
        self.final_links = links_extractor(self.domain_name, 'img', 'src')
        links_to_file(os.path.join(self.images_folder, 'image_links.txt'), self.final_links)
        multi_threading_se(self.final_links)
        print('\nImages saved :)\n')

    # extract tables
    def extract_tables(self):
        self.table = table_extractor(self.domain_name, 'table')
        table_to_csv(os.path.join(self.table_folder, 'table.csv'), self.table)
        print('\nTable saved :)\n')

    # extract text
    def extract_text(self):
        self.text_data = text_extractor(self.domain_name)
        text_to_file(os.path.join(self.text_folder, 'text.txt'), self.text_data)
        print('\nText saved :)\n')


def se():
    url = input('\nenter the full url that you need to scrape\nexample: https://www.example.com/\n\n')
    print("\n{} is now being scraped.\n".format(url))
    print('\nwhat do you want to extract from the webpage?\n')

    i = input('\n1.Links\n2.Images\n3.Tables\n4.Text\n\n')

    # seo is scrape everything object :P
    seo = ScrapeEverything(url)

    if i == '1':
        print('okay, extracting links\n')
        seo.extract_links()
    elif i == '2':
        print('okay, extracting images\n')
        seo.extract_images()
    elif i == '3':
        print('okay, extracting tables\n')
        seo.extract_tables()
    elif i == '4':
        print('okay, extracting text\n')
        seo.extract_text()
    else:
        print('Invalid option. Please choose 1 or 2 or 3 or 4.')


if __name__ == "__main__":
    se()
