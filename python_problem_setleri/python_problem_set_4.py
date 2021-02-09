num_list = input("Sayıları aralarına virgül koyarak yazınız.").split(",")
newn_list = [int(i) for i in num_list]
newn_list.sort(reverse=True)
newn_list = [i for i in newn_list if i % 2 == 1]
print(newn_list[0])