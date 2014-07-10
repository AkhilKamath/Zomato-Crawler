import requests
from lxml import html

def crawl():
    links=['http://www.zomato.com/bangalore/restaurants?category=3']
    for i in range(2,10):
        a='http://www.zomato.com/bangalore/restaurants?category='+'&page='+str(i)
        links.append(a)
    getmorelinks(links)
	

def getmorelinks(li):
    links=[]
    for i in range(0,len(li)):
        age = requests.get(li[i])
        page=age.content
        c=page.count('<a  class="result-title"  href=')
        n=0
        
        while(n<c):
            index=page.find('<a  class="result-title"  href=')
            index2=page.find('"',index+33)
            link=page[index+32:index2]
            links.append(link)
            n+=1
            page=page[index2+1:]
    maincrawl(links)


def maincrawl(links):
    for i in range(0,len(links)):
        page = requests.get(links[i])
        tree = html.fromstring(page.text)

        #This will create a list of buyers:
        buyers = tree.xpath('//span[@itemprop="name"]/text()')
        #[@style="font-size: 100%"]
        #This will create a list of prices
        add1 = tree.xpath('//h4[@class="res-main-address-text left"][@itemprop="address"]/text()')
        add2=tree.xpath('//strong[@itemprop="addressLocality"]/text()')

        f=tree.xpath('//span[@class="res-info-timings"]/text()')
        number=tree.xpath('//span[@class="tel"]/text()')
        if(',' in number):
            number.remove(',')
        print 'Name: ', buyers
        print 'Address: ', add1[0].strip()+' '+add2[0]
        for j in range(0,len(f)):
            f[j]=f[j].strip()
        print 'Timings: ', f
        print 'Number: ', number
        print "\n\n"


crawl()


