import json
from operator import itemgetter
from pprint import pprint

def similar(a, b):
    score = 0.0
    for word in b.split():
    	if word in a:
    		score = score + 1
    if a:
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


for listing in listings[:5]:
	print listing['title'], listing['manufacturer']
	match = []
	for product in products:
		score = 0
		score = score + similar(listing['manufacturer'], product['manufacturer']) * 2

		score = score + similar(listing['title'], product['manufacturer'])
		score = score + similar(listing['title'], product['product_name'].replace('_',' '))

		if 'family' in product:
			score = score + similar(listing['title'], product['family'])

		score = score + similar(listing['title'], product['model'])		

		match.append({'score':score, 'product': product})
	pprint(sorted(match, key=itemgetter('score'), reverse=True)[0]['product'])
	print "\n\n\n"