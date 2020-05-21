from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import csv

class Request(object):
    def __init__(self,url):
        self.url = url

    def get_data(self, raw_html, fileToWrite):
        #raw_html = self.simple_get(self.url)
        html = BeautifulSoup(raw_html, 'html.parser')
        
        with open(fileToWrite, mode='w') as test_file:
            test_writer = csv.writer(test_file)
            test_writer.writerow(['Company, Link, Contact'])

            for article in html.find_all('article'):
                name = article.find('h2').get_text()
                row = ''.join([name]) + ','
                for link in article.find_all('a'):
                    link = link.get_text()
                    row = ''.join(row + link) + ','
                test_writer.writerow([row])

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


    