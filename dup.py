import csv

mp = {}

fname = 'data5'
ipf = open(f'{fname}.csv', 'r')
opf = open(f'{fname}nodup.csv', 'w', newline='')

csv_reader = csv.reader(ipf)
csv_writer = csv.writer(opf)

for i in csv_reader:
    if(i[1] not in mp):
        x = ''.join(c for c in i[2] if c in '.0123456789')
        if x == '':
            x = 0
        mp[i[1]] = 1
        i[-1] = str(float(x) * 0.979)
        if(float(x) != 0.0):
            csv_writer.writerow(i)

ipf.close()
opf.close()
