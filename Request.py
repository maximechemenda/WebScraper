from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import csv

class Request(object):
    def __init__(self,url):
        self.url = url


    def delete_file_content(self, file_name):
        file = open(file_name, "r+")
        file.truncate(0)
        file.close()


    def get_data(self, raw_html, fileToWrite):
        file_object = open(fileToWrite,"r+")

        file_content = file_object.readlines()
        print(file_content)

        for i in range(len(file_content)):
            if file_content[i].find('\n') != -1:
                print('you found me')
                file_content[i] = (file_content[i])[:-2]

        is_empty_file = len(file_content) == 0
            
        self.delete_file_content(fileToWrite)

        html = BeautifulSoup(raw_html, 'html.parser')

        if is_empty_file:
            print('trueeeeee')
            file_object.write('Company,Link,Contact,Localisation' + '\n')

        for article in html.find_all('article'):
            name = article.find('h2').get_text()
            row = ''.join([name]) + ','
            for link in article.find_all('a'):
                link = link.get_text()
                row = ''.join(row + link) + ','
            file_content.append(row)
            #test_writer.writerow([row])
    
        """ for line in file_content:
            #test_writer.writerow([line])
            file_object.write(line + '\n') """


        for i in range(len(file_content)):
            file_content[i] = file_content[i] + '\n'
        
        file_object.writelines(file_content)
        
        file_object.close()


    def simple_get(self):
        """
        Attempts to get the content at `url` by making an HTTP GET request.
        If the content-type of response is some kind of HTML/XML, return the
        text content, otherwise return None.
        """
        try:
            with closing(get(self.url, stream=True)) as resp:
                if self.is_good_response(resp):
                    return resp.content
                else:
                    return None

        except RequestException as e:
            self.log_error('Error during requests to {0} : {1}'.format(self.url, str(e)))
            return None


    def is_good_response(self, resp):
        """
        Returns True if the response seems to be HTML, False otherwise.
        """
        content_type = resp.headers['Content-Type'].lower()
        return (resp.status_code == 200 
                and content_type is not None 
                and content_type.find('html') > -1)


    def log_error(self, e):
        """
        It is always a good idea to log errors. 
        This function just prints them, but you can
        make it do anything.
        """
        print(e)


    