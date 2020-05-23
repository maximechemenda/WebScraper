# WebScraper
text

## Installation
Go to the terminal and run:
- mkdir new_folder && cd new_folder && git clone https://github.com/maximechemenda/WebScraper.git .


## Usage
1. Open the file main.py, and on line 74, give the name of the final file (the file where the data should be written)

2. In the terminal, go to the directory of the project, and run:
   - **python3 main.py**\
If you now open the final file, you should see the name of the companies, their website url and their contact.
  
3. Open the file main.py, and:
   - comment the line 53 (main.run())
   - uncomment the line 54 (main.main_loop())

4. Go to the website https://www.polemermediterranee.com/Reseau/Annuaire-des-membres and:
   - right click on the page and select "Inspect"
   - If you are not already there, navigate to the console
   
5. Go to the file namesExtractor.js and copy its content, then:
   - on the website, select one filter (make sure that there is only one filter selected, it will not work if more than 1 filter is selected)
   - as there is an infinite scroll, make sure to scroll until the bottom of the page until no more companies appear
   - right click on the console, and select "Clear console"
   - paste the copied code in the console and press enter: you should see company names appear in the console
   - right click on the console
   - click on "Save as..." and save the content of the console to the file "content_chrome.log". Make sure this file will be located in your project folder
   - to the right of the company names, there will be a sequence of characters (like VM360:4). Copy those characters, and paste them on line xxx of the main.py file (it doesn't matter if you include trailing spaces or not)
   - copy the name of the selected filter, then go to the file main.py, and on line xxx, paste it
   - go to the terminal, make sure you are in the directory of the project, and run: "python3 main.py"
   
6. Repeat the previous step as many times as there are filters, and every time, unselect the previous filter, and select a new one
   
