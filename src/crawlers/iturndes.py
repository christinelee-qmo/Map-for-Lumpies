import requests
import csv
from bs4 import BeautifulSoup

# links = ["https://itunes.apple.com/us/app/id475905823","https://itunes.apple.com/us/app/id475905822"]
# for link in links:
#     response = requests.get(link)
#     soup = BeautifulSoup(response.text, "html.parser")
#     print(soup.get_text())



url = requests.get("https://www.top500.org/list/2018/06")
soup = BeautifulSoup(url.content, 'html.parser')

filename = "computerRank10.csv"
csv_writer = csv.writer(open(filename, 'w'))

csv_writer.writerow("sasd")

for tr in soup.find_all("tr"):
    data = []
    # for headers ( entered only once - the first time - )
    for th in tr.find_all("th"):
        data.append(th.text)
    if data:
        print("Inserting headers : {}".format(','.join(data)))
        csv_writer.writerow(data)
        continue

    for td in tr.find_all("td"):
        if td.a:
            data.append(td.a.text.strip())
        else:
            data.append(td.text.strip())
    if data:
        print("Inserting data: {}".format(','.join(data)))
        csv_writer.writerow(data)