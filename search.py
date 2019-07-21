from fuzzywuzzy import fuzz

def absoluteSearch(keywordsFilePath, query):
	for x in query:
		file = open(keywordsFilePath, 'r')
		for i in file:
			counter = 0
			fileLoc = 'empty'
			allwords=i.split('\t')
			keywords = allwords[1:]
			for j in keywords:
				if (x in j):
					counter = counter + 1 
					fileLoc = allwords[0]
			if counter>0:
				print(counter, "matches in the file", fileLoc," for ", x)
		file.close()
	if fileLoc == 'empty':
		return 'none'

def fuzzySearch(keywordsFilePath, query):
	query = query.lower()
	file = open(keywordsFilePath, 'r')
	maxScore = 0
	maxWord = ''
	for i in file:
		fileLoc = 0
		allwords=i.split('\t')
		keywords = allwords[1:]
		for j in keywords:
			tempScore = fuzz.ratio(j, query)
			if maxScore<tempScore:
				maxScore=tempScore
				maxWord =j
	if(maxScore<100):
		print("Did you mean \"",maxWord,"\" instead of \"",query,"\"")
def search(keywordsFilePath, query):
	absResults = absoluteSearch(keywordsFilePath, query)
	if absResults == 'none':
		for x in query:
			fuzzySearch(keywordsFilePath, x)
query = "hassan minhaj"
query = query.split(' ')
search('keywords.txt',query)