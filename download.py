#!/usr/bin/env python3

# Candidates
# http://www.moscow_city.vybory.izbirkom.ru/region/izbirkom?action=show&root=772000001&tvd=27720001539819&vrn=27720001539308&prver=0&pronetvd=null&region=77&sub_region=0&type=427&vibid=27720001539819

# Early results

# http://www.moscow_city.vybory.izbirkom.ru/region/izbirkom?action=show&root=772000001&tvd=27720002327741&vrn=27720002327736&prver=0&pronetvd=null&region=77&sub_region=0&type=426&vibid=27720002327741
# http://www.moscow_city.vybory.izbirkom.ru/region/izbirkom?action=show&root=772000001&tvd=27720002327741&vrn=27720002327736&prver=0&pronetvd=null&region=77&sub_region=0&type=426&vibid=27720002327741

# 2014 - tvd=27720001539819

# 2019 - tvd=27720002327740

import requests
import re
import os

def download(directory, url, tp):
    r = requests.get(url)
    d = "data/%s" % directory
    if not os.path.isdir(d):
        os.makedirs(d)
    index = 1
    for u in re.findall("(?P<url>https?://[^\s\>\\\"]+)", r.text):
        if u.find('type=0') >= 0:
            u = u.replace('&amp;', '&')
            u = u.replace('type=0', tp)
            print(u)
            r2 = requests.get(u)
            with open("%s/%d.html" % (d, index), "wb") as f:
                f.write(r2.content.decode('cp1251').encode('utf8'))
            index += 1

if __name__ == "__main__":
    download('2014', 'http://www.vybory.izbirkom.ru/region/izbirkom?action=show&vrn=27720001539308&region=77&prver=0&pronetvd=null', 'type=423')
    download('2019', 'http://www.vybory.izbirkom.ru/region/izbirkom?action=show&vrn=27720002327736&region=77&prver=0&pronetvd=null', 'type=426')
