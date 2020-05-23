from Request import Request
from DataManager import DataManager
import csv


class Main(object):
    def __init__(self, fileToWrite, filter, url_list, ignoring_characters_length):
        self.url_list = url_list
        self.fileToWrite = fileToWrite
        self.filter = filter
        self.ignoring_characters_length = ignoring_characters_length

    
    def run(self):
        for url in self.url_list:
            request = Request(url)

            raw_html = request.simple_get()
            request.get_data(raw_html, self.fileToWrite)
   
    def main_loop(self):
        data_manager = DataManager(self.fileToWrite, self.filter, self.ignoring_characters_length)
        data_manager.main()


    def restart(self):
        request = Request('https://www.polemermediterranee.com/Reseau/Annuaire-des-membres')
        request.delete_file_content(self.fileToWrite)



if __name__ == "__main__":
    url_list = [
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/12",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/24",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/36",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/48",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/60",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/72",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/84",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/96",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/108",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/120",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/132",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/144",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/156",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/168",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/180",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/192",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/204",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/216",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/228",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/240",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/252",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/264",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/276",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/288",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/30O",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/312",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/324",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/336",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/348",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/360",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/372",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/384",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/396",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/408",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/420",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/432",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/444",
        "https://www.polemermediterranee.com/Reseau/Annuaire-des-membres/(offset)/456"
        ]


    fileToWrite = 'data.txt'
    console_characters = 'VM360:4'
    filter = 'Ports, logistique et transports maritimes'
    
    ignoring_characters_length = len(console_characters.strip()) + 1 

    main = Main(fileToWrite, filter, url_list, ignoring_characters_length)

    #main.restart()
    main.run()
    #main.main_loop()

   