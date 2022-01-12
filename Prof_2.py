import re
from pprint import pprint
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

res_list = []
for i in contacts_list:
    res = (i[0] + ' ' + i[1] + ' ' + i[2]).strip().split()  # можно сделать через регулярные выражения
    if len(res) == 3:
        pass
    if len(res) == 2:
        res.append('')
    pattern = r"(\+?\d\s?\(?(\d{3})\)?\s?-?(\d{3})\-?(\d{2})\-?(\d{2})(,?\s?\(?(\w+.)\s?(\d{4})\)?)?)"
    subst = r"+7(\2)\3-\4-\5 \7\8"
    i[5] = re.sub(pattern, subst, i[5])
    for f in range(3, 7):
        res.append(i[f])
    res_list.append(res)
pprint(res_list)

c_list = []
cc_list = []
for id, k in enumerate(res_list):
    if k[0] not in c_list and k[1] not in c_list:
        c_list.append(k[0])
        cc_list.append(k)
        # print(c_list)
        # pprint(cc_list)
    else:
        for id_s, s in enumerate(c_list):
            if s == k[0]:
                for id_m, m in enumerate(cc_list):
                    if id_m == id_s:
                        for id_j, j in enumerate(m):
                            if j == '':
                                m[id_j] = k[id_j]
                            else:
                                pass
pprint(cc_list)

with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(cc_list)
