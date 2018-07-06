from lxml import html
import requests

url =r'https://www.nytimes.com/'

page = requests.get(url)
tree = html.fromstring(page.content)


print(page.text)
print(tree.text)
print(dir(tree))
