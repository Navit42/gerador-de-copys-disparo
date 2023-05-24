import os
import datetime
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')


with open("./entrada/lista_cidades.txt", "r", encoding='utf-8') as f:
    info = f.readlines()

city = []
place = []
address = []
landmark = []
date = []

for line in info:
    if line.strip() == "&":
        continue
    city_val, place_val, address_val, landmark_val, date_val = line.strip().split(';')
    city.append(city_val)
    place.append(place_val)
    address.append(address_val)
    landmark.append(landmark_val)
    date.append(date_val)

count = len(city)

for j in range(count):
    copy_number = 0

    with open("./copys/primeira_copy.txt", "r", encoding='utf-8') as f:
        data = f.readlines()

    copy_1 = []
    copy_2 = []
    copy_3 = []

    for line in data:
        if copy_number == 0:
            if "+-+" in line:
                copy_number += 1
            copy_1.append(line)
        elif copy_number == 1:
            if "+-+" in line:
                copy_number += 1
            copy_2.append(line)
        else:
            copy_3.append(line)

#copy 1

    day, month = date[j].split('/')
    day = int(day)
    month=int(month)
    current_year = datetime.datetime.now().year
    date_week_day  = datetime.datetime(current_year, month, day)

    # Obter o dia da semana correspondente
    week_day = date_week_day.strftime("%A")
    week_day = week_day.encode('latin-1').decode('utf-8')

    print(city[j])
    print(count)
    print(j)    
    for i in range(len(copy_1)):
        if "{city}" in copy_1[i]:
            copy_1[i] = copy_1[i].replace("{city}", city[j])
            


    for i in range(len(copy_1)):
        if "{city_split.upper()}" in copy_1[i]:
            copy_1[i] = copy_1[i].replace("{city_split.upper()}", city[j].upper())
            print(copy_1[i])

    for i in range(len(copy_1)):
        if "{place}" in copy_1[i]:
            copy_1[i] = copy_1[i].replace("{place}", place[j])


    for i in range(len(copy_1)):
        if "{address}" in copy_1[i]:
            copy_1[i] = copy_1[i].replace("{address}", address[j])

    for i in range(len(copy_1)):
        if "{landmark}" in copy_1[i]:
            copy_1[i] = copy_1[i].replace("{landmark}", landmark[j])
            
    for i in range(len(copy_1)):
        if "{day_month}" in copy_1[i]:
            copy_1[i] = copy_1[i].replace("{day_month}", date[j])
            
    for i in range(len(copy_1)):
        if "{week_day}" in copy_1[i]:
            copy_1[i] = copy_1[i].replace("{week_day}", week_day)


#copy 2

    for i in range(len(copy_2)):
        if "{city}" in copy_2[i]:
            copy_2[i] = copy_2[i].replace("{city}", city[j])

    for i in range(len(copy_2)):
        if "{city_split.upper()}" in copy_2[i]:
            copy_2[i] = copy_2[i].replace("{city_split.upper()}", city[j].upper())


    for i in range(len(copy_2)):
        if "{place}" in copy_2[i]:
            copy_2[i] = copy_2[i].replace("{place}", place[j])


    for i in range(len(copy_2)):
        if "{address}" in copy_2[i]:
            copy_2[i] = copy_2[i].replace("{address}", address[j])


    for i in range(len(copy_2)):
        if "{landmark}" in copy_2[i]:
            copy_2[i] = copy_2[i].replace("{landmark}", landmark[j])

    for i in range(len(copy_2)):
        if "{day_month}" in copy_2[i]:
            copy_2[i] = copy_2[i].replace("{day_month}", date[j])      

    for i in range(len(copy_2)):
        if "{week_day}" in copy_2[i]:
            copy_2[i] = copy_2[i].replace("{week_day}", week_day)              

#copy 3


    for i in range(len(copy_3)):
        if "{city}" in copy_3[i]:
            copy_3[i] = copy_3[i].replace("{city}", city[j])

    for i in range(len(copy_3)):
        if "{city_split.upper()}" in copy_3[i]:
            copy_3[i] = copy_3[i].replace("{city_split.upper()}", city[j].upper())


    for i in range(len(copy_3)):
        if "{place}" in copy_3[i]:
            copy_3[i] = copy_3[i].replace("{place}",place[j])


    for i in range(len(copy_3)):
        if "{address}" in copy_3[i]:
            copy_3[i] = copy_3[i].replace("{address}", address[j])


    for i in range(len(copy_3)):
        if "{landmark}" in copy_3[i]:
            copy_3[i] = copy_3[i].replace("{landmark}", landmark[j])

    for i in range(len(copy_3)):
        if "{day_month}" in copy_3[i]:
            copy_3[i] = copy_3[i].replace("{day_month}", date[j])   

    for i in range(len(copy_3)):
        if "{week_day}" in copy_3[i]:
            copy_3[i] = copy_3[i].replace("{week_day}", week_day)                
            
    directory = city[j].split('/')
    path = f"./saida/{directory[0]}"

    try:
        os.makedirs(path)  # Create the directory and any missing parent directories
    except FileExistsError:
        pass  # Directory already exists, no need to create it again

    # Write to the files inside the created directory
    with open(os.path.join(path, "primeira_copy1.txt"), "w", encoding='utf-8') as f:
        for line in copy_1:
            f.write(line)

    with open(os.path.join(path, "primeira_copy2.txt"), "w", encoding='utf-8') as f:
        for line in copy_2:
            f.write(line)

    with open(os.path.join(path, "primeira_copy3.txt"), "w", encoding='utf-8') as f:
        for line in copy_3:
            f.write(line)
