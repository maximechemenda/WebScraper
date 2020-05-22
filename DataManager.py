from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import csv 


class DataManager(object):
    def __init__(self, fileToWrite, parameter):
        self.fileToWrite = fileToWrite
        self.parameter = parameter

    def main(self):
        values = self.file_reader('../content_chrome.log')
        self.update_data(values)

    def update_data(self, values):
        with open(self.fileToWrite) as file:
            file_content = file.readlines()

        """ with open(self.fileToWrite, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter='\n', quotechar='|')
            file_content = []
            for row in spamreader:
                line_content = row[0]
                file_content.append(line_content)
            print(file_content) """
        
        result = []
        for line in file_content:
            new_line = line[1:-2] #TODO: NOT SURE IF I HAVE TO KEEP THIS!!!!
            splitted_line = new_line.split(',')  
            print(line)
            print(new_line)
            print('bbb')

            name = splitted_line[0]
            for value in values:
                if name == value:
                    new_line = new_line + self.parameter
            result.append(new_line)
            #print(result)


        self.delete_file_content(self.fileToWrite)

        with open(self.fileToWrite, mode='w') as test_file:
            test_writer = csv.writer(test_file)
            for line in result:
                test_writer.writerow([line])
        print(result == file_content)


        
    def delete_file_content(self, file_name):
        file = open(file_name, "r+")
        file.truncate(0)
        file.close()

    #PROBABLY SHOULD GO IN A SEPARATE CLASS
    def file_reader(self, file_name):
        with open(file_name) as file:
            file_content = file.readlines()

            temp_content = []
            for i in range(len(file_content)):
                if i > 4 and i != len(file_content) - 1: 
                    line = file_content[i]
                    temp_name = line[7:]
                    temp_content.append(temp_name)
            
            final_content = []
            for i in range(len(temp_content)):
                name = temp_content[i][:-1]
                final_content.append(name)

            return final_content




#if __name__ == '__main__':
    #get_data('https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/456')
    #values = file_reader("../content_chrome.log")
    #update_data(values, 'Ile de France')
    

