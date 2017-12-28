import requests
from bs4 import BeautifulSoup

a = requests.get("http://www.baidu.com")
print type(a)
print a.status_code
print a.encoding
print a.cookies
