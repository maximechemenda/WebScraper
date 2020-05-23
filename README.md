# WebScraper
This code allows someone to extract data from the website https://www.polemermediterranee.com/Reseau/Annuaire-des-membres. More precisely, it gets the name of all the companies in it, along with their website, contact, location, college and activity, and writes this information to a file.

## Installation
Go to the terminal and run:
- mkdir new_folder && cd new_folder && git clone https://github.com/maximechemenda/WebScraper.git .

## Usage
1. Open the file main.py, and on line 76, give the name of the final file (the file where the data should be written)

2. In the terminal, go to the directory of the project, and run:
   - touch final_file_name.txt
   - python3 main.py\
If you now open the final file, you should see the name of the companies, their website url and their contact.
  
3. Open the file main.py, and:
   - comment the line 85 (main.run())
   - uncomment the line 86 (main.main_loop())

4. Go to the website https://www.polemermediterranee.com/Reseau/Annuaire-des-membres and:
   - right click on the page and select "Inspect"
   - If you are not already there, navigate to the console
   
5. Go on the previous website, then:
   - select one filter (make sure that there is only one filter selected, it will not work if more than 1 filter is selected)
   - as there is an infinite scroll, make sure to scroll until the bottom of the page until no more companies appear
   - right click on the console, and select "Clear console"
   - copy the code within the file namesExtractor.js
   - paste the copied code in the console and press enter: you should see company names appear in the console
   - right click on the console
   - click on "Save as..." and save the content of the console to the file "content_chrome.log". Make sure you save the file in your project folder. If you are asked if you want to replace the old file, press yes.
   - to the right of the company names, there will be a sequence of characters (like VM360:4). Copy those characters, and paste them on line 77 of the main.py file (it doesn't matter if you include trailing spaces or not)
   - copy the name of the selected filter, then go to the file main.py, and on line 78, paste it
   - go to the terminal, make sure you are in the directory of the project, and run: "python3 main.py"
   
6. Repeat the previous step as many times as there are filters, and every time, unselect the previous filter, and select a new one
   
