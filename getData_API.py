from urllib.request import urlopen , Request
import csv
import json

def get_jsonparsed_data(my_url):


    req = Request(url=my_url, headers=headers)


    response = urlopen(req)
    data = response.read().decode("utf-8")
    return json.loads(data)

filename = "sneakerData.csv"
f = open(filename,"w+")
headers = "Brand, Colorway, Gender, Name, Title, Release Date, Retail Price, Below Retail, Shoe\n"
f.write(headers)

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                      'AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

url = ("https://stockx.com/api/browse?page=1&productCategory=sneakers")
parsed_data = get_jsonparsed_data(url)
page_data = parsed_data['Pagination']

print("Collecting Data")
for n in range(int(page_data['limit'])):
    url = ("https://stockx.com/api/browse?page="+str(n)+"&productCategory=sneakers")

    parsed_data = get_jsonparsed_data(url)

    products = parsed_data['Products']
    for p in products:
        toWrite = p['brand']+p['colorway']+p['gender']+p['name']+p['title']+p['releaseDate']+str(p['retailPrice'])+str(p['belowRetail'])+p['shoe']+"\n"
        print(toWrite)
        f.write(toWrite)
print("Data Collection Complete. See sneakerData.csv")
    #print(page_data['limit'])
