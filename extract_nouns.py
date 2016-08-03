import glob
import json
import pprint
#import combined_sense_ranker
import pickle

dev_files = glob.glob('test/*.json')


def gold_nouns(json_file):


	test_json = json_file


	with open(test_json) as infile:
		test_text = json.load(infile)

	nouns_dict_list = []

	filename = json_file.lstrip('test/').rstrip('.json')



	with open('record_gold/gold_overview'+filename+'txt', 'w') as outfile:


		word_count = 0
		stuff_count = 0
		for sentence in test_text:
			for word in sentence:
				word_count += 1
				
				if word['pos'].startswith('N'):
					noun_dict = dict()
					noun_dict[word_count] = word['function']
					nouns_dict_list.append(noun_dict)
					outfile.write(str(word_count)+'\t'+word['token']+'\t'+str(word['function'])+'\n')

	
	pickle.dump(nouns_dict_list, open('gold_testnouns/'+filename+'.pickle', 'wb'))

	for nounsdict in nouns_dict_list:
		print(nounsdict)

for file in dev_files:

	gold_nouns(file)

#gold_nouns('development/a1k-fragment02.json')