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

        for i in range(len(file_content)):
            if file_content[i].find('\n') != -1:
                file_content[i] = (file_content[i])[:-2]

        is_empty_file = len(file_content) == 0

        html = BeautifulSoup(raw_html, 'html.parser')

        if is_empty_file:
            file_object.write('Entreprise|||Lien|||Contact|||Localisation|||Collège|||Activité' + '\n')

        for article in html.find_all('article'):
            name = article.find('h2').get_text().strip()
            row = (''.join([name]) + '|||').strip()

            if len(article.find_all('a')) == 0:
                row = (''.join(row + 'not provided' + '|||' + 'not provided' + '|||')).strip()
            elif len(article.find_all('a')) == 1:
                link = article.find_all('a')[0].get_text().strip()
                if link.startswith('http'):
                    row = (''.join(row + link + '|||' + 'not provided' + '|||'))
                else:
                    row = (''.join(row + 'not provided' + '|||' + link + '|||'))
            else:
                for link in article.find_all('a'):
                    link = link.get_text().strip()
                    row = (''.join(row + link) + '|||').strip()
                    
            file_object.write(row + '\n')
        
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


    