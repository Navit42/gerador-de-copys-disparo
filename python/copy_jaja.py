import os


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

    with open("./copys/jaja.txt", "r", encoding='utf-8') as f:
        data = f.readlines()

    copy_number = 0
    copy_1 = []
    copy_2 = []
    copy_3 = []

    print(city[j])
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

    for i in range(len(copy_1)):
        if "{city}" in copy_1[i]:
            copy_1[i] = copy_1[i].replace("{city}", city[j])


    for i in range(len(copy_1)):
        if "{place}" in copy_1[i]:
            copy_1[i] = copy_1[i].replace("{place}", place[j])


    for i in range(len(copy_1)):
        if "{address}" in copy_1[i]:
            copy_1[i] = copy_1[i].replace("{address}", address[j])

    for i in range(len(copy_1)):
        if "{landmark}" in copy_1[i]:
            copy_1[i] = copy_1[i].replace("{landmark}", landmark[j])
    
    for i in range(len(copy_2)):
        if "{city}" in copy_2[i]:
            copy_2[i] = copy_2[i].replace("{city}", city[j])


    for i in range(len(copy_2)):
        if "{place}" in copy_2[i]:
            copy_2[i] = copy_2[i].replace("{place}", place[j])


    for i in range(len(copy_2)):
        if "{address}" in copy_2[i]:
            copy_2[i] = copy_2[i].replace("{address}", address[j])


    for i in range(len(copy_2)):
        if "{landmark}" in copy_2[i]:
            copy_2[i] = copy_2[i].replace("{landmark}", landmark[j])


    for i in range(len(copy_3)):
        if "{city}" in copy_3[i]:
            copy_3[i] = copy_3[i].replace("{city}", city[j])


    for i in range(len(copy_3)):
        if "{place}" in copy_3[i]:
            copy_3[i] = copy_3[i].replace("{place}",place[j])


    for i in range(len(copy_3)):
        if "{address}" in copy_3[i]:
            copy_3[i] = copy_3[i].replace("{address}", address[j])


    for i in range(len(copy_3)):
        if "{landmark}" in copy_3[i]:
            copy_3[i] = copy_3[i].replace("{landmark}", landmark[j])                
            
    directory = city[j].split('/')
    path = f"./saida/{directory[0]}"
    
    try:
        os.makedirs(path)  # Create the directory and any missing parent directories
    except FileExistsError:
        pass  # Directory already exists, no need to create it again
    
    # Write to the files inside the created directory
    with open(os.path.join(path, "copy_jaja1.txt"), "w", encoding='utf-8') as f:
        for line in copy_1:
            f.write(line)
    
    with open(os.path.join(path, "copy_jaja2.txt"), "w", encoding='utf-8') as f:
        for line in copy_2:
            f.write(line)
    
    with open(os.path.join(path, "copy_jaja3.txt"), "w", encoding='utf-8') as f:
        for line in copy_3:
            f.write(line)
    