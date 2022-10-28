import numpy as np
import csv

# min = np.array([[888, 1948, 12700], [892, 1942, 12750], [899, 1933, 12800], [902, 1945, 12800]])
min = np.array([[899, 1933, 12800], [902, 1945, 12800], [871, 1914, 13100]])
# min = np.array([[1307.36, 3291.47, 19999.54], [1290.44, 3259.17, 19999.54], [1298.13, 3214.57, 19999.54]])
num = '345'
print(min)

min_inv = np.linalg.inv(min)

ipf = open(f'data{num}nodup.csv', 'r')
opf = open(f'final{num}comp.csv', 'w', newline='')

csv_reader = csv.reader(ipf)
csv_writer = csv.writer(opf)

for i in csv_reader:
    inp = [float(x) for x in i[2:]]
    prod = np.array(inp)
    ans = np.matmul(min_inv, prod)
    csv_writer.writerow(i[:2] + list(ans))

ipf.close()
opf.close()

# i = [97.461, 96.922, 96.2752]
