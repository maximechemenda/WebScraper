with open('pole_mer_data.txt', 'r+') as file:
    file_content = file.readlines()
    counter = 0
    other_one = 0
    for line in file_content:
        splitted_line = line.split('|||')
        if len(splitted_line) == 6:
            counter += 1
            if splitted_line[4] == 'not provided':
                other_one += 1
        
    print(counter)
    print(other_one)

    

    """ for i,line in enumerate(file_content):
        splitted_line = line.split('|||')
        if len(splitted_line) < 5 and i != 0:
            print(splitted_line)
            #file_content[i] = splitted_line[0] + '|||' + splitted_line[1] + '|||' + splitted_line[2] + '|||' + 'not provided' + '|||' + splitted_line[3]
    file.seek(0)

    for line in file_content:
        file.write(line) """

          
