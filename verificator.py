with open('pole_mer_data.txt', 'r+') as file:
    file_content = file.readlines()
    counter = 0
    
    for i,line in enumerate(file_content):
        if i != len(file_content) - 1:
            file_content[i] = file_content[i][:-4] + '\n'
        else:
            file_content[i] = file_content[i][:-3]
            counter += 1
        print(file_content[i])
    file.seek(0)

    for line in file_content:
        file.write(line)
    
    print(counter)






    
    counter = 0
    for line in file_content:
        splitted_line = line.split('|||')
        if len(splitted_line) != 7:
            print(line)
            counter += 1
    print(counter)

   






     
        


    

    

          
