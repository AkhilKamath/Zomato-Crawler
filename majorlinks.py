def crawl():
    links=['http://www.zomato.com/bangalore/restaurants?category=3']
    for i in range(2,10):
	    a='http://www.zomato.com/bangalore/restaurants?category='+'&page='+str(i)
	    links.append(a)

    
    
