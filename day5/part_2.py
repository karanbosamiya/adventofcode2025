import pandas as pd
import numpy as np


class RangeChecker():
    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.fresh_count = 0
    def check_fresh(self, fresh_nums):
        for i in fresh_nums:
            if any(np.where(((self.dataframe['start'] <=i) &(self.dataframe['end']>=i)), True, False)):
                self.fresh_count += 1
        return self.fresh_count

    def check_total_fresh_ids(self):
        range_df = self.dataframe.copy()
        
        print("SORTED_DF>>>>>>>>>>>>>>>>>>>>>>>>>>")
        range_df = range_df.sort_values(by=[ 'start', 'end']).reset_index(drop=True)
        old_df = range_df.copy()
        old_df = old_df.rename(columns={'start': 'start_org', 'end': 'end_org'})
        print(range_df.head(190))
        end_idx = 0
        for i in range_df.index:
            # if i == 83:
            #     breakpoint()
            #if range_df.iloc[i, 0] == 0:
            #    continue
            #if end_idx > range_df.iloc[i, 0]:
            #    range_df.iloc[i, 0] = end_idx
            #    if end_idx > range_df.iloc[i, 1]:
            #        range_df.iloc[i, 0] = 0
            #        range_df.iloc[i, 1] = 0
            #        continue
            if i+1< range_df.shape[0] and range_df.iloc[i, 1] == range_df.iloc[i+1, 0] and range_df.iloc[i+1, 0] == range_df.iloc[i+1, 1]:
                range_df.iloc[i+1, 0] = 0
                range_df.iloc[i+1, 1] = 0
                continue
            if i+1 < range_df.shape[0] and range_df.iloc[i, 1] == range_df.iloc[i+1, 0]:
                if range_df.iloc[i, 1] < range_df.iloc[i+1, 1]:
                    range_df.iloc[i, 1] = range_df.iloc[i+1, 1] - 2

                range_df.iloc[i+1, 0] = range_df.iloc[i, 1] + 1
                range_df.iloc[i+1, 1] = range_df.iloc[i, 1] + 2
            elif i+1 < range_df.shape[0] and range_df.iloc[i, 1] > range_df.iloc[i+1, 0]:
                range_df.iloc[i +1, 0] = range_df.iloc[i, 1]+1
                if range_df.iloc[i+1, 1] < range_df.iloc[i+1, 0]:
                    range_df.iloc[i+1, 1] = range_df.iloc[i+1, 0] - 1
            
            if i+1 < range_df.shape[0] and end_idx < range_df.iloc[i+1, 1]:
                end_idx = range_df.iloc[i+1, 1]
            
        range_df['diff'] = range_df.apply(lambda x: x['end'] - x['start'] + 1 if x['end'] - x['start']+1>0 and x['start'] !=0 else 0, axis=1)
        tot_df = old_df.join(range_df)

        print("TOT_DF>>>>>>>>>>>")
        print(tot_df.head(190))

        return range_df['diff'].sum()

pd.set_option('display.max_rows', None)

with open("input_52.txt", "r") as file:
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
    total_fresh_ids = a.check_total_fresh_ids()
    print(total_fresh_ids)
