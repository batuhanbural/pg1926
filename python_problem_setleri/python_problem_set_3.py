num_list = input("Sayıları aralarına virgül koyarak yazınız.").split(",")
newn_list = [int(i) for i in num_list]

empty_list = []
for i in newn_list:
    if i == 0:
        empty_list.insert(0, i)
    else:
        empty_list.append(i)
print(empty_list)