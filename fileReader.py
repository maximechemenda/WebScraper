import numpy as np

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


def delete_file_content(file_name):
    file = open(file_name, "r+")
    file.truncate(0)
    file.close()


if __name__ == '__main__':
    file_reader("../content_chrome.log")
    #delete_file_content("./infoo_test.csv")