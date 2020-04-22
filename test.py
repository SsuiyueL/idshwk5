list2=[]
with open("test.txt") as f1:
    for line in f1:
        if line=="":
            continue
        strs=line[:-1]
        if len(strs)<=29:
            strs=strs+",notdga\n"
        else:
            strs = strs + ",dga\n"
        list2.append(strs)

print(list2)
with open("result.txt",'w+') as f:
    f.writelines(list2)