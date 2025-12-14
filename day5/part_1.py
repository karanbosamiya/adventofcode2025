class RangeChecker():
    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.fresh_count = 0
    def check_fresh(self, fresh_nums):
        for i in fresh_nums:
            if any(np.where(((self.dataframe['start'] <=i) &(self.dataframe['end']>=i)), True, False)):
                self.fresh_count += 1
        return self.fresh_count


with open("input_51.txt", "r") as file:
    ranges = []
    nums = []
    switch_0 = True
    for line in file.readlines():
        if line =="\n":
            switch_0 = False
            continue
        if switch_0:
          start_range, end_range = line[:-1].split("-")
          print(start_range, end_range)
          ranges += [(int(start_range), int(end_range))]
          continue
        nums.append(int(line[:-1]))
    range_df = pd.DataFrame(data=ranges, columns=['start', 'end'])
    print(ranges)
    print(nums)
    print(range_df)
    a = RangeChecker(range_df)
    tot_nums = a.check_fresh(nums)
    print(tot_nums)