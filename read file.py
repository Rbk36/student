with open('c:/Users/hp/logger.txt', 'r',encoding='utf-8') as file:
    lines=file.readlines()
    file.close()
    for line in lines:
     if "reciept" in line:
            print(line)