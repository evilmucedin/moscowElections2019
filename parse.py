#!/usr/bin/env python3

import re

def detag(s):
    count = 0
    result = ""
    for ch in s:
        if ch == '<':
            count += 1
        elif ch == '>':
            count -= 1
        else:
            if count == 0:
                result += ch
    return result

def detagV(v):
    res = []
    for x in v:
        res.append(detag(x))
    return res

def dequote(s):
    if len(s) and s[0] == '\'':
        return s[1:len(s) - 1]
    else:
        return s

def dequoteV(v):
    res = []
    for x in v:
        res.append(dequote(x))
    return res

def main():
    for y in ["2014", "2019"]:
        with open("data/%s.csv" % y, "w") as fOut:
            print("Station,FullName,Count", file=fOut)
            for index in range(1, 46):
                with open("data/%s/%d.html" % (y, index)) as f:
                    cand = []
                    for line in f:
                        line = line.strip()
                        if len(re.findall("\<\/td\>", line)) != 3:
                            continue
                        if line.find('Число') >= 0:
                            continue
                        parts = dequoteV(detagV(re.split("\<\/td\>", line)))
                        print("%d,%s,%s" % (index, parts[1], parts[2]), file=fOut)
                

if __name__ == "__main__":
    main()
