import pandas as pd




def check_condition(row):
    if row[len(row) - 1] == '+':
        return row[:-1].sum()
    else:
        return row[:-1].prod()



with open("input_61.txt", "r") as file:
    ranges = []
    for line in file.readlines():
        try:
            a = [int(i) for i in line.rstrip("\n").split(" ") if i != '']
        except:
            a = [i for i in line.rstrip("\n").split(" ") if i!= '']
        ranges+= [a]
    print(ranges)
    df = pd.DataFrame(ranges)
    print(df)
    new_df = df.T
    a_df = new_df.copy()
    a_df['ans'] = new_df.apply(check_condition, axis=1)
    print("A_DF")
    print(a_df)
    print(a_df.sum())






