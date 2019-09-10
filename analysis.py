#!/usr/bin/env python3

import pandas
import numpy
import math

def main():
    stats = []
    for y in ["2014", "2019"]:
        print(y)
        df = pandas.read_csv('data/%s.csv' % y)
        rems = []
        s = 0
        for dfStation in df.sort_values(['Count'], ascending=False).groupby('Station'):
            count0 = 0
            count1 = 0
            countSum = 0
            index = 0
            for _, row in dfStation[1].iterrows():
                c = float(row['Count'])
                if index == 0:
                    count0 = c
                elif index == 1:
                    count1 = c
                countSum += c
                index += 1
                s += c
            # print(countSum, count0, count1)
            rem = float(countSum - count0 - count1) / countSum / (index - 2)
            print(rem)
            rems.append(rem)
        st = (y, numpy.mean(rems), numpy.std(rems), s)
        print(st)
        stats.append(st)
    print('T=%f' % ((stats[0][1] - stats[1][1])/math.sqrt(stats[0][2] + stats[1][2])))

if __name__ == "__main__":
    main()
