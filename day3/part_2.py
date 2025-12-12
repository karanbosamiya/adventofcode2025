with open("input_32.txt", 'r') as file:
    invalids = 0
    for line in file.readlines():
        curr_num = ""
        print(line)
        if line =="\n":
            break
        xl = 0
        for i in range(12, 0, -1):
          print("line[:-i], line[-i]", line[:-i], line[-i])
          a = line[xl:-i]
          print("A>>>", a)
          b = [int(z) for z in a]
          print("b", b)
          k = max(b)
          xl += b.index(k) + 1
          print("XL", xl)

          curr_num += str(k)
        print("CURREN_NUM", curr_num)
        invalids += int(curr_num)
    print(invalids)
