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

results = {}
for listing in listings:
	match = []
	for product in products:
		score = 0
		score = score + similar(listing['manufacturer'], product['manufacturer']) * 2

		score = score + similar(listing['title'], product['manufacturer'])
		score = score + similar(listing['title'], product['product_name'].replace('_',' ')) * 2

		if 'family' in product:
			score = score + similar(listing['title'], product['family'])

		score = score + similar(listing['title'], product['model'])		

		match.append({'score':score, 'product': product})
	product_name = sorted(match, key=itemgetter('score'), reverse=True)[0]['product']['product_name']
	if product_name in results:
		results[product_name].append(listing)
	else:
		results[product_name] = [listing]

results_file = open('results.txt','w')
for product_name in results:
	results_file.write('{\"product_name\":\"%s\", \"listings\":%s}\n' % (product_name, json.dumps(results[product_name])))