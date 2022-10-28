import csv

mp = {}

oldnum = '345'
newnum = '2'

oldf = open(f'data{oldnum}nodup.csv', 'r')
newf = open(f'data{newnum}nodup.csv', 'r')
opf = open(f'data{oldnum + newnum}nodup.csv', 'w', newline='')

old_reader = csv.reader(oldf)
new_reader = csv.reader(newf)
csv_writer = csv.writer(opf)

for i in old_reader:
    if(i[1] not in mp):
        mp[i[1]] = i[2:]

for i in new_reader:
    if(i[1] in mp):
        i = i[:2] + mp[i[1]] + i[2:]
        csv_writer.writerow(i)

oldf.close()
newf.close()
opf.close()
