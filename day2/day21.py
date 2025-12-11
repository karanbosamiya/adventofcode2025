with open("input_211.txt", 'r') as file:
    invalids = 0
    for line in file.readlines():
        a = line.split(",")
        for i in a:
            b = i.split("-")
            k, l = b[0], b[1]
            print(len(b))
            print(k, l)
            for i in range(int(k), int(l)+ 1):
                print("i>>>>>>>>>>", i)
                c = len(str(i))
                print("str(i)[:c//2]", str(i)[:c//2])
                print("str(i)[c//2:]", str(i)[c//2:])
                if str(i)[:c//2] == str(i)[c//2:]:
                    print("-------==========Its invalid----------------------------")
                    invalids += i
