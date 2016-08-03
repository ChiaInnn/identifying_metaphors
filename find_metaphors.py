
from nltk.corpus import wordnet as wn
from lxml import etree
from KafNafParserPy import *
import glob
import pprint
from collections import defaultdict
import pickle


def nouns_pickle(naf_file):

	test_naf = KafNafParser(naf_file)

	test_terms = list(test_naf.get_terms())


	test_nouns_dict_list = []

	nouns_wsd_list = []

	term_counter = 0

	for  n, term in enumerate(test_terms):
		termid = term.get_id()
		tokenid = termid.replace('t', 'w')

		

		#if term.get_lemma().endswith("'"):
		#	print(term.get_lemma(), n)
		#	continue

		#if term.get_lemma() == 'course' and test_terms[n-1].get_lemma() == 'of':
		#	continue

		#else:
		term_counter += 1

		if term.get_pos() == 'N':
		

			wsd_dict = dict()

			confidence_list = []

			refs = term.get_external_references()



			for ref in refs:
				if ref.get_confidence() != None:
					confidence_list.append((float(ref.get_confidence()), ref.get_reference()))

			if confidence_list:

				highest_confidence_tuple = max(confidence_list)
				#print(highest_confidence_tuple)
				highest_confidence = highest_confidence_tuple[1]
				#print(highest_confidence)

			

				if highest_confidence[-1] == 'n':


					reference = highest_confidence[7:-2]


					wsd_dict[term_counter] = [wn._synset_from_pos_and_offset('n', int(reference))]
					wsd_dict[term_counter].append(term.get_lemma())


					nouns_wsd_list.append(wsd_dict)


	return nouns_wsd_list

###########################################
## Version of the sense ranker: 

from combined_sense_ranker_normalized import *

###########################################


def analyze_nouns(naf_file):


	test_nouns = nouns_pickle(naf_file)
	

	results_dict_list = []

	filename = naf_file.lstrip('processed_testfiles_out/').rstrip('.naf')

	with open('record_results/overview_results_'+filename+'.txt', 'w') as outfile:

		for noun in test_nouns:
			for nounid, noun_list in noun.items():

				noun_dict = dict()

				noun_token = noun_list[1]
				context_syn = noun_list[0]

				basic_syns = top_noun(noun_token)
				#print(basic_syns)

				if context_syn and basic_syns:

					if context_syn in basic_syns:
						met_value = None
					else:
						met_value = 'mrw'

					noun_dict[nounid] = met_value

					results_dict_list.append(noun_dict)

					outfile.write(str(nounid)+'\t'+noun_token+'\t'+str(met_value)+'\n')
					#print(context_syn, basic_syn, noun_dict)
	


	

	pickle.dump(results_dict_list, open('results_testnouns/'+filename+'.pickle', 'wb'))

#print(wn.synsets('roller', 'n'))
processed_naf = glob.glob('processed_testfiles_out/*.naf')
#print(processed_naf[0])


for naf in processed_naf:
	print(naf)
	analyze_nouns(naf)

