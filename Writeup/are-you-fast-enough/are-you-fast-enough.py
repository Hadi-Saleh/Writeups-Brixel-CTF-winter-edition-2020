from lxml import html
import requests
url = 'http://timesink.be/speedy/'
req = requests.get(url)
tree = html.fromstring(req.content)
pas = tree.xpath('//div[@id="rndstring"]/text()')
print(pas)
password = [str(s) for s in pas]
password = ''.join(password)
print(password)
cookies = req.cookies
data = {"inputfield":password}
req = requests.post(url=url,data=data,cookies = cookies)
print(req.content)