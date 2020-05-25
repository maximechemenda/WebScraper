with open('pole_mer_data.txt', 'r+') as file:
    file_content = file.readlines()
    counter = 0

    for line in file_content:
        splitted_line = line.split('|||')
        if len(splitted_line) != 4:
            print(splitted_line)
            counter += 1
    print(counter)
