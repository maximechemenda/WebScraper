# WebScraper
text

## Installation
Go to the terminal and copy those commands:
1. mkdir new_folder
2. cd new_folder
3. git clone https://github.com/maximechemenda/WebScraper.git .

## Usage
1. Open the file main.py, and on line 74, give the name of the final file (the file where the data should be written)

2. In the terminal, go to the directory of the project, and run:
   - **python3 main.py**\
If you now open the final file, you should see the name of the companies, their website url and their contact.
  
3. Open the file main.py, and:
   - comment the line 53 (main.run())
   - uncomment the line 54 (main.main_loop())

4. Go to the website https://www.polemermediterranee.com/Reseau/Annuaire-des-membres and:
   - right click on the page
   - click "Inspect"
   - If you are not already there, navigate to the console
   
*For this step, you need to ensure that the console is empty. If it isn't, right click in the console, and click on "Hide messages from ...". *\
5. Go to the file namesExtractor.js and copy its content, then:
   - on the website, select one filter (make sure that there is only one filter selected, it will not work if more than 1 filter are selected)
   - as there is an infinite scroll, make sure to scroll until the bottom of the page until no more companies appear
   - paste the copied code in the console
   - right click on the console
   - click on "Save as..." and save the content of the console to the file "content_chrome.log". Make sure this file will be located in the directory of the project
   
