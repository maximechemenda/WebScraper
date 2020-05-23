from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import csv 

class DataManager(object):
    def __init__(self, fileToWrite, filter, ignoring_characters_length):
        self.fileToWrite = fileToWrite
        self.filter = filter
        self.ignoring_characters_length = ignoring_characters_length


    def main(self):
        values = self.file_reader('./content_chrome.log')
        self.update_data(values)


    def update_data(self, values):
        with open(self.fileToWrite, 'r+') as file:
            file_content = file.readlines()
            for i,line in enumerate(file_content):
                for value in values:
                    if line.startswith(value):
                        print('writing to file')
                        file_content[i] = (file_content[i])[:-1].strip() + self.filter + ',\n'
            file.seek(0)   

            for line in file_content:
                file.write(line)

        print(len(values))


    def delete_file_content(self, file_name):
        file = open(file_name, "r+")
        file.truncate(0)
        file.close()


    def file_reader(self, file_name):
        with open(file_name) as file:
            file_content = file.readlines()

            temp_content = []
            for i in range(len(file_content)):
                if i > 4 and i != len(file_content) - 1: 
                    line = file_content[i]
                    temp_name = line[self.ignoring_characters_length:] #######THIS VALUE CAN CHANGE BECAUSE SOMETIMES IN THE LOG FILE THE NUMBER OF CHARACTERS TO IGNORE CAN BE DIFFERENT
                    temp_content.append(temp_name)
            
            final_content = []
            for i in range(len(temp_content)):
                name = temp_content[i][:-1]
                final_content.append(name)

            return final_content

