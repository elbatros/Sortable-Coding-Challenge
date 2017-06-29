import json
from itertools import ifilter
from difflib import SequenceMatcher
from operator import itemgetter

def similar(a, b):
    # return SequenceMatcher(None, a, b).ratio()
    score = 0.0
    for word in b.split():
    	if word in a:
    		score = score + 1
    score = score / len(a)
    # print score
    return score


listings_file = open ('challenge_data_20110429/listings.txt')

listings = []
for line in listings_file:
	listings.append(json.loads(line))
	# print line
# print(listings[0]['manufacturer'])

products_file = open ('challenge_data_20110429/products.txt')

products = []
for line in products_file:
	products.append(json.loads(line))
	# print line
# print(products[0]['manufacturer'])


for listing in listings[:10]:
	# iterator = ifilter(lambda x: x['manufacturer'] is listing["manufacturer"], products)
	print listing
	match = []
	for product in products:
		# print product['manufacturer']
		score = 0
		score = score + similar(listing['manufacturer'], product['manufacturer']) * 4
		# print score
		score = score + similar(listing['title'], product['manufacturer'])
		# print score
		# 	print product
		# break
		# print match
		match.append({'score':score, 'product': product})
	print sorted(match, key=itemgetter('score'), reverse=True)[0]
	# break
