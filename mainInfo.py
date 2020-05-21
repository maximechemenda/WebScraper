from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import csv 


class DataManager(object):
    """ def __init__(self):
        pass """
    

def update_data(values, parameter):
    with open('my_test_web.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter='\n', quotechar='|')
     file_content = []
     for row in spamreader:
        line_content = row[0]
        file_content.append(line_content)
    
    result = []
    for line in file_content:
        splitted_line = line.split(',')
        name = splitted_line[0]
        for value in values:
            if name == value:
                line = line + parameter  
        result.append(line)

    delete_file_content('infooo_test.csv')

    with open('infooo_test.csv', mode='w') as test_file:
        test_writer = csv.writer(test_file)
        test_writer.writerow(['Company, Link, Contact'])
        for line in result:
            test_writer.writerow([line])
    print(result)


    
def delete_file_content(file_name):
    file = open(file_name, "r+")
    file.truncate(0)
    file.close()

#PROBABLY SHOULD GO IN A SEPARATE CLASS
def file_reader(file_name):
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




if __name__ == '__main__':
    #get_data('https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/456')
    values = file_reader("../content_chrome.log")
    update_data(values, 'Ile de France')

