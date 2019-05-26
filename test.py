import requests
from bs4 import BeautifulSoup

page = requests.get("https://nerdstore.com.br/categoria/especiais/game-of-thrones/")

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())


a = soup.find_all(class_="woocommerce-loop-product__title")
b = soup.find_all(class_="attachment-woocommerce_thumbnail size-woocommerce_thumbnail")
c = soup.find_all(class_="price")

# --------------------------------------------------------------------------------------
for link in b:
    print(link.get('src'))
# get img links

# --------------------------------------------------------------------------------------


d = c[0].find_all('span')
print('C[0] len: ' + str(len(c[0])))
for i in range(len(d)):
    print('d[{}]'.format(i) + str(d[i].get_text()))
# get prices specific position
for i in range(len(c)):
    print(c[i].get_text())
# get all prices


# --------------------------------------------------------------------------------------
for i in a:
    print(i.get_text())

# get all names