from lxml import html
import requests
counter =1;
list = []
url = 'http://timesink.be/quizbot/'
req = requests.get(url)
pass = "WrongAnswer"
cookies = req.cookies
data = {"insert_answer":pass}
while counter <=1000:
    req = requests.post(url=url,data=data,cookies = cookies)
    tree = html.fromstring(req.content)
    pas = tree.xpath('//div[@id="answer"]/text()')
    ans = [str(s) for s in pas]
    ans = ''.join(ans)
    list = list + [ans]
    counter+=1;

url = 'http://timesink.be/quizbot/'
req = requests.get(url)
cookies = req.cookies
counter = 1
while counter <=1000:
    pass = list[counter-1]
    data = {"insert_answer": pass}
    req = requests.post(url=url,data=data,cookies = cookies)
    if counter==1000:
        print(req.content)
    counter+=1;
