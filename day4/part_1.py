
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
        for i in range(self.dataframe.shape[0]):
            self.curr_x = i
            for j in range(self.dataframe.shape[1]):
                self.curr_y = j
                print(f"X, Y-> {(self.curr_x, self.curr_y)}")
                if self.dataframe.iloc[self.curr_x, self.curr_y] == ".":
                    continue
                if self.check_x():
                    print("ADDS X")
                    self.x_s_vals +=1
        return self.x_s_vals




with open("input41.txt", "r") as file:
    rows= []
    for line in file.readlines():
        print(line[:-1], line[-1])
        row = list(line[:-1])
        rows.append(row)
    df = pd.DataFrame(rows)

    print(df)
    a = DfChecker(df)
    a.total_x()
