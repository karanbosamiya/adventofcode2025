with open("input_31.txt", 'r') as file:
    invalids = 0
    for line in file.readlines():
        print(line[:-1], line[-1])
        a = line[:-1]
        b = [int(i) for i in a]
        k = max(b[:-1])
        l = b.index(k)

        m = max(b[l+1:])
        sum_a = int(str(k) + str(m))
        invalids += sum_a
    print(invalids)
