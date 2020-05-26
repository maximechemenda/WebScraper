with open('pole_mer_data.txt', 'r+') as file:
    file_content = file.readlines()
    for line in file_content:
        if not line.endswith('|||\n'):
            print(line)
        


    

    """ for i,line in enumerate(file_content):
        splitted_line = line.split('|||')
        if len(splitted_line) < 5 and i != 0:
            print(splitted_line)
            #file_content[i] = splitted_line[0] + '|||' + splitted_line[1] + '|||' + splitted_line[2] + '|||' + 'not provided' + '|||' + splitted_line[3]
    file.seek(0)

    for line in file_content:
        file.write(line) """

          
