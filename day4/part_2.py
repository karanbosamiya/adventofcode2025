
class DfChecker():
    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.curr_x, self.curr_y = 0, 0

    def check_left(self):
        if self.curr_x -1 < 0:
            return False
        if self.dataframe.iloc[self.curr_x -1, self.curr_y] == '@':
            return True
        return False
    def check_right(self):
        if self.curr_x + 1>= self.dataframe.shape[0]:
            return False
        if self.dataframe.iloc[self.curr_x+1, self.curr_y] == '@':
            return True
        return False
    def check_up(self):
        if self.curr_y - 1 < 0:
            return False
        if self.dataframe.iloc[self.curr_x, self.curr_y -1] == '@':
            return True
        return False
    def check_down(self):
        if self.curr_y + 1>= self.dataframe.shape[1]:
            return False
        if self.dataframe.iloc[self.curr_x, self.curr_y +1] == '@':
            return True
        return False
    def check_left_up(self):
        if self.curr_x - 1 < 0 or self.curr_y - 1 < 0:
            return False
        if self.dataframe.iloc[self.curr_x-1, self.curr_y-1] == '@':
            return True
        return False
    def check_right_up(self):
        if self.curr_x + 1>= self.dataframe.shape[0] or self.curr_y -1 < 0:
            return False
        if self.dataframe.iloc[self.curr_x +1, self.curr_y-1] == '@':
            return True
        return False
    def check_left_down(self):
        if self.curr_x - 1< 0 or self.curr_y+1 >= self.dataframe.shape[1]:
            return False
        if self.dataframe.iloc[self.curr_x-1, self.curr_y+1] == '@':
            return True
        return False
    def check_right_down(self):
        if self.curr_x + 1>= self.dataframe.shape[0] or self.curr_y + 1 >= self.dataframe.shape[1]:
            return False
        if self.dataframe.iloc[self.curr_x+1, self.curr_y +1] == '@':
            return True
        return False
    def check_x(self):
        sum_at = sum([
        self.check_left(),
        self.check_right(),
        self.check_up(),
        self.check_down(),
        self.check_left_up(),
        self.check_right_up(),
        self.check_left_down(),
        self.check_right_down(),
        ])
        if sum_at < 4:
            return True
        return False
    def total_x(self):
        self.x_s_vals = 0
        self.note_endpoints = []
        for i in range(self.dataframe.shape[0]):
            self.curr_x = i
            for j in range(self.dataframe.shape[1]):
                self.curr_y = j
                print(f"X, Y-> {(self.curr_x, self.curr_y)}")
                if self.dataframe.iloc[self.curr_x, self.curr_y] == ".":
                    continue
                if self.check_x():
                    self.note_endpoints += [(self.curr_x, self.curr_y)]

                    print("ADDS X")
                    self.x_s_vals +=1
        if self.note_endpoints:
            for i, j in self.note_endpoints:
                self.dataframe.iloc[i, j] = "."
        return self.x_s_vals

    def total_x_recursive(self):
        self.x_init = 0
        self.total_fin_x = 0
        self.x_new = self.total_x()
        count = 0
        print("COUNT>>>>>>>>>>>>>>>>>", count)
        print(self.dataframe)
        print("SELF.X_NEW>>>>>>", self.x_new)
        print("SELF.TOTAL_FIN_X", self.total_fin_x)
        print("self.x_new != self.total_fin_x and count < 9", self.x_new != self.total_fin_x and count < 9)
        while self.x_new !=0:
            count+= 1
            print("self.df", self.dataframe)
            self.total_fin_x += self.x_new
            self.x_new = self.total_x()
            print("SELF.X_NEW>>>>>>", self.x_new)
            print("SELF.TOTAL_FIN_X", self.total_fin_x)
            print("COUNT", count)
            print("self.x_new != self.total_fin_x and count < 9", self.x_new != self.total_fin_x and count < 9)
        return self.total_fin_x




with open("input_42.txt", "r") as file:
    rows= []
    for line in file.readlines():
        print(line[:-1], line[-1])
        row = list(line[:-1])
        rows.append(row)
    df = pd.DataFrame(rows)

    print(df)
    a = DfChecker(df)
    print(a.total_x_recursive())