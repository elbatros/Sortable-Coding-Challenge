import json
from operator import itemgetter

def similar(a, b):
    score = 0.0
    for word in b.split():
    	if word in a:
    		score = score + 1
    score = score / len(a)
    return score


listings_file = open ('challenge_data_20110429/listings.txt')

listings = []
for line in listings_file:
	listings.append(json.loads(line))

products_file = open ('challenge_data_20110429/products.txt')

products = []
for line in products_file:
	products.append(json.loads(line))


for listing in listings[:10]:
	print listing
	match = []
	for product in products:
		score = 0
		score = score + similar(listing['manufacturer'], product['manufacturer']) * 4
		score = score + similar(listing['title'], product['manufacturer'])
		match.append({'score':score, 'product': product})
	print sorted(match, key=itemgetter('score'), reverse=True)[0]
