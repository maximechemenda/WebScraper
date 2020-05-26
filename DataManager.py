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
        temp = []
        for value in values:
            temp.append(value)

        counter = 0
        with open(self.fileToWrite, 'r+') as file:
            file_content = file.readlines()
            for i,line in enumerate(file_content):
                for value in values:
                    splitted_line = line.split('|||')
                    first_element = splitted_line[0]
                    if first_element.strip() == value.strip():
                        temp.remove(value)
                        counter = counter + 1
                        file_content[i] = (file_content[i])[:-1].strip() + self.filter + '|||\n'
            file.seek(0)   

            for line in file_content:
                file.write(line)

        print(temp)
        print(len(values))
        print(counter)
        print(len(values) == counter)


    def delete_file_content(self, file_name):
        file = open(file_name, "r+")
        file.truncate(0)
        file.close()


    def file_reader(self, file_name):
        with open(file_name) as file:
            file_content = file.readlines()

            temp_content = []
            for i in range(len(file_content)):
                if i > 3 and i != len(file_content) - 1: 
                    line = file_content[i]
                    if len(line.strip()) != 0:
                        temp_name = line[self.ignoring_characters_length:]
                        temp_content.append(temp_name)
            
            final_content = []
            for i in range(len(temp_content)):
                name = temp_content[i][:-1]
                final_content.append(name)

            return final_content

