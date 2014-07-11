#name, timings, address, map co ordinates and phone number 
from lxml import html
import requests
page = requests.get('http://www.zomato.com/bangalore/high-ultra-lounge-malleshwaram')
tree = html.fromstring(page.text)


buyers = tree.xpath('//span[@itemprop="name"][@style="font-size: 100%"]/text()')
#This will create a list of prices
add1 = tree.xpath('//h4[@class="res-main-address-text left"][@itemprop="address"]/text()')
add2=tree.xpath('//strong[@itemprop="addressLocality"]/text()')

f=tree.xpath('//span[@class="res-info-timings"]/text()')
number=tree.xpath('//span[@class="tel"]/text()')
if(',' in number):
    number.remove(',')
print 'Name: ', buyers[0].strip()

print 'Address: ', add1[0].strip()+' '+add2[0]

print 'Timings: ', f[0].strip()
print 'Number: ', number



