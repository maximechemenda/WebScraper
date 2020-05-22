from Request import Request
from DataManager import DataManager

class Main(object):
    def __init__(self, site_url, fileToWrite, parameter):
        self.site_url = site_url
        self.fileToWrite = fileToWrite
        self.parameter = parameter

    
    def run(self):
        request = Request(self.site_url)

        raw_html = request.simple_get()
        request.get_data(raw_html, self.fileToWrite)

   
    def main_loop(self):
        data_manager = DataManager(self.fileToWrite, self.parameter)
        data_manager.main()


    def restart(self):
        request = Request(self.site_url)

        request.delete_file_content(self.fileToWrite)



if __name__ == "__main__":
    site_url = 'https://www.polemermediterranee.com/Reseau/Annuaire-des-membres'
    fileToWrite = 'my_second_test_web.csv'
    parameter = 'Nice'

    main = Main(site_url, fileToWrite, parameter)

    #main.restart()
    main.run()
    #main.main_loop()