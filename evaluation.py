import pickle
import glob
import pprint

#gold_nouns = pickle.load(open('gold_nouns/a1k-fragment02.pickle', 'rb'))
#result_nouns = pickle.load(open('results_nouns/a1k-fragment02.pickle', 'rb'))

all_gold_nouns = glob.glob('gold_testnouns/*.pickle')
all_result_nouns = glob.glob('results_testnouns/*.pickle')

def view_results(gold_nouns, result_nouns):
	for gold_dict in gold_nouns:
		for result_dict in result_nouns:
			if gold_dict.keys() == result_dict.keys():
				print(gold_dict, result_dict)

#view_results(gold_nouns, result_nouns)

# Precision: All positive results / correct positive results

def all_positives(result_nouns): 

	all_positive = 0


	for result_dict in result_nouns:
		for resultid, result in result_dict.items():
			if result == 'mrw':
				all_positive += 1
		
	return all_positive


# Recall: Correct positives / gold positives

def correct_positives(result_nouns, gold_nouns): 

	correct_positives = 0

	for result_dict in result_nouns:
		for gold_dict in gold_nouns:
			for resultid, result in result_dict.items():
				for goldid, goldresult in gold_dict.items():

					if resultid == goldid:

						if (result == 'mrw') and (goldresult == 'mrw'):
							correct_positives += 1
	return correct_positives


def gold_positives(gold_nouns):

	gold_positives  = 0

	for  gold_dict in gold_nouns:

		for goldid, goldresult in gold_dict.items():

			if goldresult == 'mrw':
				gold_positives += 1
	return gold_positives


#def total_scores(all_result_nouns, all_gold_nouns)
total_all_positives = 0 # all positives returned by the system
total_correct_positives = 0 # all correctly returned positives
total_gold_positives = 0 # all positives that should have been returned

sorted_results = sorted(all_result_nouns)
sorted_gold = sorted(all_gold_nouns)

print(len(sorted_results), len(sorted_gold))


for resultfile, goldfile in zip(sorted_results, sorted_gold):
	resultname = resultfile.lstrip('result_testnouns/')
	goldname = goldfile.lstrip('gold_testnouns/')
	print(resultname, goldname)

	if resultname == goldname:
		print(resultname, goldname)

		result_list = pickle.load(open(resultfile,  'rb'))
		gold_list = pickle.load(open(goldfile,  'rb'))
		#pprint.pprint(gold_list)
		#pprint.pprint(result_list)

		#print(type(result_list), type(gold_list))

		total_all_positives += all_positives(result_list)
		total_correct_positives += correct_positives(result_list, gold_list)
		total_gold_positives += gold_positives(gold_list)



		

			
precision =   total_correct_positives / total_all_positives
recall = total_correct_positives / total_gold_positives
f1 = 2 * ((precision * recall) / (precision + recall) )


print(total_correct_positives, total_all_positives, total_gold_positives)
print('p ', precision)
print('r ', recall)
print('f1 ', f1)

#p is the number of correct positive results divided by the number of all positive results, 
#and r is the number of correct positive results divided by the number of positive results that should have been returned. 
#The F1 score can be interpreted as a weighted average of the precision and recall, where an F1 score reaches its best value at 1 and worst at 0.
		



	




