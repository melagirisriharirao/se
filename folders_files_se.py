"""

folders-files-se.py creates the necessary folders and files required for se.

"""

import os
import csv


# separate folder for each and every website
def create_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        print("\n'{}' folder created.\n".format(folder))
    else:
        print("\n'{}' folder already exists.\n".format(folder))


# to create a new file
def create_new_file(path, data):
    with open(path, 'w') as file:
        file.write(data)


# to append data to an existing file
def append_data_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data)


# to save links to a file
def links_to_file(path, data):
    with open(path, 'w') as file:
        for link in sorted(data):
            file.write(link + '\n')


# to save text data to a file
def text_to_file(path, data):
    with open(path, 'w') as file:
        file.write(data)


# to save table data to csv file
def table_to_csv(path, data):
    print('\nsaving data to csv file.\n')
    with open(path, 'w') as f:
        writer = csv.writer(f)
        for eachTable in data:
            for eachRow in eachTable:
                writer.writerow(eachRow)
