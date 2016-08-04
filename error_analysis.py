from find_metaphors import nouns_pickle
from extract_hypernyms_of_nouns import get_hypernyms
from nltk.corpus import wordnet as wn

with open('record_gold/gold_overviewa1k-fragment02txt') as goldfile:
	gold_list = goldfile.read().split('\n')

with open('record_results/overview_results_a1k-fragment02.txt') as resultfile:
	result_list = resultfile.read().split('\n')

wsd_output = nouns_pickle('processed_files_out/a1k-fragment02.naf')

wsd_dict = {}

for nd in wsd_output:
	wsd_dict.update(nd)

print(type(wsd_dict))

nouns = []
errorcount = 0
totalcounter = 0

for noun_line_gold in gold_list:

	noun_list_gold = noun_line_gold.split('\t')

	if len(noun_list_gold) == 3:

		gold_noun_id = noun_list_gold[0]
		gold_noun = noun_list_gold[1]
		gold_noun_label = noun_list_gold[2]

		for noun_line_result in result_list:

			noun_list_result = noun_line_result.split('\t')

			if len(noun_list_result) == 4:

				result_noun_id = noun_list_result[0]
				result_noun = noun_list_result[1]
				result_noun_label = noun_list_result[2]
				result_basic = noun_list_result[3]


				if gold_noun_id == result_noun_id:
					totalcounter += 1
					context_sense = wsd_dict[int(gold_noun_id)]

					if (gold_noun_label != result_noun_label) and (gold_noun_label == 'mrw'):
						errorcount += 1

						print(gold_noun, context_sense[0], result_basic)
						nouns.append(gold_noun)

print(errorcount, totalcounter)




#with open('error_hyponyms_nouns_None.tsv', 'w') as outfile:
 #   
#
 #   for noun  in nouns:
  #      
   #     outfile.write('\n'+noun+'\n')
    #    
     #   senses = wn.synsets(noun, 'n')
      #  
       # for sense in senses:
        #    
         #   hyp_list = []
          #  
           # 
            #hypernyms = get_hypernyms(sense)
            #
            #for hyp in hypernyms:
             #   hyp_list.append(str(hyp))
                
           # definition = sense.definition()
     
         
            
            #hypernyms_line = '\t'.join(hyp_list)
            
            #outfile.write(str(definition)+'\t'+hypernyms_line+'\n')



