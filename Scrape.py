from urllib.parse import quote
import requests
from bs4 import BeautifulSoup


URL = 'https://www.wordreference.com/enfr/'

word = input("Word?")

req = URL + quote(word)
print(req)
resp = requests.get(req)
soup = BeautifulSoup(resp.content, features='lxml')
content = soup.find("table", {'class': 'WRD'})
content = str(content).replace('vtr', 'vtr ').replace('vi', 'vi ').replace('npl', 'npl ')
content = content.replace('nf', 'nf ')


print(content)
dict = {'html': str(content)}
print(dict)
