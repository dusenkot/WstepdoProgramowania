def znaki(napis):
    dict_1={}
    for i in napis:
        dict_1[i]=dict_1.get(i,0) + 1
       # if i in dict_1:
       #     dict_1[i] += 1
        #
       # else:
       #     dict_1[i] = 1

    return dict_1

dict_2=(znaki("samochódao"))

for i in sorted(dict_2.keys()):
    print(i,dict_2[i])