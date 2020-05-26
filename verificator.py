with open('pole_mer_data.txt', 'r+') as file:
    file_content = file.readlines()

    for i,line in enumerate(file_content):
        splitted_line = line.split('|||')
        if len(splitted_line) != 7 and i != 0:
            print(splitted_line)
            file_content[i] = splitted_line[0] + '|||' + splitted_line[1] + '|||' + splitted_line[2] + '|||' + splitted_line[3] + '|||' + splitted_line[4] + '|||' + 'not provided' + '|||' + splitted_line[5]
    file.seek(0)

    #for line in file_content:
    #    file.write(line)




    """ counter = 0
    for line in file_content:
        splitted_line = line.split('|||')
        if len(splitted_line) != 7:
            print(line)
            counter += 1
    print(counter) """
        


    

    

          
