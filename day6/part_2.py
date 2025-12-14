import pandas as pd
import numpy as np




def check_condition(row):
    if row[len(row) - 1] == '+':
        return row[:-1].sum()
    else:
        return row[:-1].prod()

def new_condition(row):
    # print("----------------")
    # print(row[len(row)-4])
    print(row.iloc[-1])
    if row[len(row)-4] == '+':
        return np.sum(row.iloc[-1])
    else:
        return np.prod(row.iloc[-1])

def check_length(row):
    return max([len(i) for i in row])


def apply_new_nums(row):

    # if row.iloc[-2] == "*":
    #     row = [k[::-1] for k in row[:-2]] + row[-2:]

    row_nums = []
    # print("ROW.iloc[-3]")
    # print(row.iloc[-3])
    if row.iloc[-3] == "+":
        for i in range(0, row.iloc[-1]):
            new_num = ""
            for j in row[:-3]:
                new_num += j[i:i+1]
            row_nums += [int(new_num)]
    else:
        for i in range(1, row.iloc[-1]+1):
            print("I>>>>", i)
            new_num = ""
            for j in row[:-3]:
                new_num += j[-i:-i-1:-1]
                print("j>>>>", j)
                print("j[-i:-i-1:-1]", j[-i:-i-1:-1])
            row_nums += [int(new_num)]
    return row_nums


pd.set_option('display.max_rows', None)


with open("input_61.txt", "r") as file:
    ranges = []
    for line in file.readlines():
        try:
            a = [i for i in line.rstrip("\n").split(" ") if i != '']
        except:
            a = [i for i in line.rstrip("\n").split(" ") if i!= '']
        ranges+= [a]
    print(ranges)
    df = pd.DataFrame(ranges)
    print(df)
    new_df = df.T
    a_df = new_df.copy()
    a_df['new'] = np.array([] for i in range(0, a_df.shape[0]))
    a_df['leng'] = new_df.apply(check_length, axis=1)
    print("NEW_A_DF")
    print(a_df)
    a_df['new_2'] = a_df.apply(apply_new_nums, axis=1)
    # a_df['ans'] = new_df.apply(check_condition, axis=1)
    a_df['comp'] = a_df.apply(new_condition, axis=1)
    # print("A_DF")
    print(a_df)
    print(a_df['comp'].sum())
    # print(a_df.sum())






