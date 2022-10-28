import requests
from bs4 import BeautifulSoup
import time
import csv

pgdict = {'https://www.ecotradegroup.com/en/carbrand/acura': 1, 'https://www.ecotradegroup.com/en/carbrand/alfa-romeo': 53, 'https://www.ecotradegroup.com/en/carbrand/227-aston-martin': 1, 'https://www.ecotradegroup.com/en/carbrand/audi': 111, 'https://www.ecotradegroup.com/en/carbrand/219-benelli': 1, 'https://www.ecotradegroup.com/en/carbrand/bentley': 2, 'https://www.ecotradegroup.com/en/carbrand/bmw': 49, 'https://www.ecotradegroup.com/en/carbrand/buick': 2, 'https://www.ecotradegroup.com/en/carbrand/cadillac': 4, 'https://www.ecotradegroup.com/en/carbrand/chery': 3, 'https://www.ecotradegroup.com/en/carbrand/chevrolet': 18, 'https://www.ecotradegroup.com/en/carbrand/chrysler': 57, 'https://www.ecotradegroup.com/en/carbrand/citroen': 46, 'https://www.ecotradegroup.com/en/carbrand/dacia': 3, 'https://www.ecotradegroup.com/en/carbrand/daewoo': 7, 'https://www.ecotradegroup.com/en/carbrand/daf-trucks': 1, 'https://www.ecotradegroup.com/en/carbrand/daihatsu': 8, 'https://www.ecotradegroup.com/en/carbrand/dodge': 9, 'https://www.ecotradegroup.com/en/carbrand/224-faw': 1, 'https://www.ecotradegroup.com/en/carbrand/ferrari': 3, 'https://www.ecotradegroup.com/en/carbrand/fiat': 55, 'https://www.ecotradegroup.com/en/carbrand/ford': 206, 'https://www.ecotradegroup.com/en/carbrand/freightliner-trucks': 2, 'https://www.ecotradegroup.com/en/carbrand/fuso': 4, 'https://www.ecotradegroup.com/en/carbrand/271-gac-motor': 1, 'https://www.ecotradegroup.com/en/carbrand/218-geely': 2, 'https://www.ecotradegroup.com/en/carbrand/gm': 92, 'https://www.ecotradegroup.com/en/carbrand/genesis': 1, 'https://www.ecotradegroup.com/en/carbrand/geo': 1, 'https://www.ecotradegroup.com/en/carbrand/gmc': 3, 'https://www.ecotradegroup.com/en/carbrand/great-wall-motors': 3, 'https://www.ecotradegroup.com/en/carbrand/223-harley-davidson': 2, 'https://www.ecotradegroup.com/en/carbrand/hino': 6, 'https://www.ecotradegroup.com/en/carbrand/holden': 4, 'https://www.ecotradegroup.com/en/carbrand/honda': 35, 'https://www.ecotradegroup.com/en/carbrand/hummer': 1, 'https://www.ecotradegroup.com/en/carbrand/hyundai': 79, 'https://www.ecotradegroup.com/en/carbrand/infiniti': 2, 'https://www.ecotradegroup.com/en/carbrand/international-trucks': 12, 'https://www.ecotradegroup.com/en/carbrand/isuzu': 10, 'https://www.ecotradegroup.com/en/carbrand/iveco': 5, 'https://www.ecotradegroup.com/en/carbrand/jaguar': 17, 'https://www.ecotradegroup.com/en/carbrand/jeep': 7, 'https://www.ecotradegroup.com/en/carbrand/228-john-deere': 4, 'https://www.ecotradegroup.com/en/carbrand/217-kawasaki': 2, 'https://www.ecotradegroup.com/en/carbrand/kenworth': 2, 'https://www.ecotradegroup.com/en/carbrand/kia': 80, 'https://www.ecotradegroup.com/en/carbrand/221-ktm': 1, 'https://www.ecotradegroup.com/en/carbrand/270-kubota': 1, 'https://www.ecotradegroup.com/en/carbrand/lada': 1, 'https://www.ecotradegroup.com/en/carbrand/lamborghini': 2, 'https://www.ecotradegroup.com/en/carbrand/lancia': 52, 'https://www.ecotradegroup.com/en/carbrand/land-rover': 16, 'https://www.ecotradegroup.com/en/carbrand/226-ldv-group': 1, 'https://www.ecotradegroup.com/en/carbrand/lexus': 6, 'https://www.ecotradegroup.com/en/carbrand/269-lifan-motors': 1, 'https://www.ecotradegroup.com/en/carbrand/lincoln': 2, 'https://www.ecotradegroup.com/en/carbrand/mack-trucks': 1, 'https://www.ecotradegroup.com/en/carbrand/222-man': 1, 'https://www.ecotradegroup.com/en/carbrand/maserati': 2, 'https://www.ecotradegroup.com/en/carbrand/mazda': 47, 'https://www.ecotradegroup.com/en/carbrand/mercedes': 46, 'https://www.ecotradegroup.com/en/carbrand/mercury': 2, 'https://www.ecotradegroup.com/en/carbrand/mg-motor': 2, 'https://www.ecotradegroup.com/en/carbrand/mini-cooper': 4, 'https://www.ecotradegroup.com/en/carbrand/mitsubishi': 44, 'https://www.ecotradegroup.com/en/carbrand/naza': 1, 'https://www.ecotradegroup.com/en/carbrand/nissan': 59, 'https://www.ecotradegroup.com/en/carbrand/oldsmobile': 1, 'https://www.ecotradegroup.com/en/carbrand/opel': 32, 'https://www.ecotradegroup.com/en/carbrand/paccar': 4, 'https://www.ecotradegroup.com/en/carbrand/perodua': 4, 'https://www.ecotradegroup.com/en/carbrand/peterbilt': 6, 'https://www.ecotradegroup.com/en/carbrand/peugeot': 46, 'https://www.ecotradegroup.com/en/carbrand/plymouth': 1, 'https://www.ecotradegroup.com/en/carbrand/pontiac': 2, 'https://www.ecotradegroup.com/en/carbrand/porsche': 14, 'https://www.ecotradegroup.com/en/carbrand/proton': 2, 'https://www.ecotradegroup.com/en/carbrand/renault': 50, 'https://www.ecotradegroup.com/en/carbrand/rolls-royce': 1, 'https://www.ecotradegroup.com/en/carbrand/rover': 4, 'https://www.ecotradegroup.com/en/carbrand/saab': 6, 'https://www.ecotradegroup.com/en/carbrand/saturn': 3, 'https://www.ecotradegroup.com/en/carbrand/scion': 1, 'https://www.ecotradegroup.com/en/carbrand/seat': 8, 'https://www.ecotradegroup.com/en/carbrand/225-sg-automotive': 1, 'https://www.ecotradegroup.com/en/carbrand/skoda': 8, 'https://www.ecotradegroup.com/en/carbrand/smart': 2, 'https://www.ecotradegroup.com/en/carbrand/ssangyong': 4, 'https://www.ecotradegroup.com/en/carbrand/266-sterling': 1, 'https://www.ecotradegroup.com/en/carbrand/subaru': 32, 'https://www.ecotradegroup.com/en/carbrand/suzuki': 17, 'https://www.ecotradegroup.com/en/carbrand/tata': 4, 'https://www.ecotradegroup.com/en/carbrand/toyota': 99, 'https://www.ecotradegroup.com/en/carbrand/220-truimph': 4, 'https://www.ecotradegroup.com/en/carbrand/unidentified': 58, 'https://www.ecotradegroup.com/en/carbrand/vauxhall': 25, 'https://www.ecotradegroup.com/en/carbrand/volkswagen': 111, 'https://www.ecotradegroup.com/en/carbrand/volvo': 35, 'https://www.ecotradegroup.com/en/carbrand/walker': 12, 'https://www.ecotradegroup.com/en/carbrand/215-yamaha': 2}

f = open('data5.csv', 'w', newline='')

csv_writer = csv.writer(f)

# pgdict = {'https://www.ecotradegroup.com/en/carbrand/acura': 1, 'https://www.ecotradegroup.com/en/carbrand/alfa-romeo': 53}

cookies = {
    '_gcl_au': '1.1.1061500278.1664283074',
    'intercom-id-bzhqa9fh': 'c3892499-396f-42d6-a86f-faade9292d54',
    '__stripe_mid': 'a6d02328-1284-4595-8657-5d52fd953594aeff64',
    '__atuvc': '35%7C39%2C26%7C40',
    '_gid': 'GA1.2.2099065362.1665975439',
    '__cf_bm': 'ZaWRE0llhTaH1IW7hz2RofecFXWOzGz5AwrwWddo04I-1665975439-0-AfDKpaDgB0Unz0+6/7M7QrTeMAr0vIwCM+1lO6YXRsolTlVlPf8DILlpCE0r5z8n1Uc5GR0Ta+nkoGunbsFcrUdkskyjNjwnFMA2wgJhS6Elj9OlO3qL84CtQtvaJJ/LSg==',
    'PHPSESSID': 'j3r4ui6uv675e7dvdp5s7oa2u8',
    '_ga_NNRZNJQQSY': 'GS1.1.1665975438.39.1.1665975496.2.0.0',
    '_ga': 'GA1.1.71512931.1664283074',
    'intercom-session-bzhqa9fh': 'N0cwcGhYRWRaa1BndldDWVpLallhSTh1bEdwcCtzRnpOLzVsS0tzdFBPWTV3WkVXa3oyZ2REbnRnSE12ZXJWbi0tUzg4c1M0dTkxVk84bU9WU3lSVXo5Zz09--4a792408b3fbeaf55c70d7447a9cb8ec1f7df390',
}

headers = {
    'authority': 'www.ecotradegroup.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_gcl_au=1.1.1061500278.1664283074; intercom-id-bzhqa9fh=c3892499-396f-42d6-a86f-faade9292d54; __stripe_mid=a6d02328-1284-4595-8657-5d52fd953594aeff64; __atuvc=35%7C39%2C26%7C40; _gid=GA1.2.2099065362.1665975439; __cf_bm=ZaWRE0llhTaH1IW7hz2RofecFXWOzGz5AwrwWddo04I-1665975439-0-AfDKpaDgB0Unz0+6/7M7QrTeMAr0vIwCM+1lO6YXRsolTlVlPf8DILlpCE0r5z8n1Uc5GR0Ta+nkoGunbsFcrUdkskyjNjwnFMA2wgJhS6Elj9OlO3qL84CtQtvaJJ/LSg==; PHPSESSID=j3r4ui6uv675e7dvdp5s7oa2u8; _ga_NNRZNJQQSY=GS1.1.1665975438.39.1.1665975496.2.0.0; _ga=GA1.1.71512931.1664283074; intercom-session-bzhqa9fh=N0cwcGhYRWRaa1BndldDWVpLallhSTh1bEdwcCtzRnpOLzVsS0tzdFBPWTV3WkVXa3oyZ2REbnRnSE12ZXJWbi0tUzg4c1M0dTkxVk84bU9WU3lSVXo5Zz09--4a792408b3fbeaf55c70d7447a9cb8ec1f7df390',
    'referer': 'https://www.ecotradegroup.com/en/profile',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Opera GX";v="91", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.72',
}

for key, value in pgdict.items():
    try:
        print(key + 'Pg Num: 1')
        url = key
        r = requests.get(url, cookies=cookies, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        small = soup.find_all('small', class_='d-block fw-600 text-truncate')
        lnk = soup.find_all('a', class_='position-relative d-block overflow-hidden text-reset')
        prices = soup.find_all('span', class_='fs-4')
        for i in range(len(small)):
            name = small[i].text
            link = "https://www.ecotradegroup.com" + lnk[i]['href']
            try:
                cost = prices[i].text.strip('\n')[:-2]
            except Exception as e:
                cost = 0
            print(cost)
            csv_writer.writerow([name, link, cost])
    except:
        print(f'{key} not added Pg1')
    for i in range(2, value+1):
        time.sleep(3)
        try:
            print(key + 'Pg Num: ' + str(i))
            url = key+ '/' + str(i)
            r = requests.get(url, cookies=cookies, headers=headers)
            soup = BeautifulSoup(r.text, 'lxml')
            small = soup.find_all('small', class_='d-block fw-600 text-truncate')
            lnk = soup.find_all('a', class_='position-relative d-block overflow-hidden text-reset')
            prices = soup.find_all('span', class_='fs-4')
            for i in range(len(small)):
                name = small[i].text
                link = "https://www.ecotradegroup.com" + lnk[i]['href']
                try:
                    cost = prices[i].text.strip('\n')[:-2]
                except Exception as e:
                    cost = 0
                print(cost)
                csv_writer.writerow([name, link, cost])
        except:
            print(f'{key} not added Pg{i}')

f.close()
