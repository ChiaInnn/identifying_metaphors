from sense_ranker_normalized import *
from nltk.corpus import wordnet as wn
from collections import Counter
import pickle
from pandas import *
import pprint
from collections import defaultdict



def rank_senses(target, features, rank1 = 'hypo', rank2 = 'sim', rank3 = None, rank4 = None):
    
    
    rankings = [rank1, rank2, rank3, rank4]
   

    # Different ranking mechanisms for different groups

    results = []

    if 'hypo' in rankings:
    
        hypo_collected = collect_hypo(features, target)
        counted_features_hypo = count_features(hypo_collected)
        ranked_hypo = rank_values(counted_features_hypo)
        results.append(ranked_hypo)
        

    if 'sim' in rankings:

        sim_collected = collect_sim(features, target)
        counted_features_sim = count_features(sim_collected)
        ranked_sim = rank_values(counted_features_sim)
        results.append(ranked_sim)
        
        
    if 'senses' in rankings:

    	senses_collected = collect_senses(target)
    	counted_features_senses = count_features(senses_collected)
    	ranked_senses = rank_values(counted_features_senses)
    	results.append(ranked_senses)
       

    
    if 'depth' in rankings:

    	depth_collected = collect_depth(target)
    	counted_features_depth = count_features(depth_collected)
    	ranked_depth = rank_values(counted_features_depth)
    	results.append(ranked_depth)
            
    return results

def ranking(combined_count, nrange):

	syns = []
	syns_score = defaultdict(list)

	for syn, score in combined_count.most_common():

		if score != 0:
	
			syns_score[score].append(syn)

		else:

			break
	

	if syns_score:

		syns_score_sorted_list = sorted(list(syns_score.items()), reverse = True)

		

		for score_syn_list_tuple in syns_score_sorted_list:
			score = score_syn_list_tuple[0]
			syn_list = score_syn_list_tuple[1]
			syns_sorted = sorted(syn_list)
			for syn in syns_sorted:
				syns.append(syn)
				

	return syns[:nrange]


def alternative_ranking(combined_count, nrange):

	score_dict = defaultdict(list)
	
	for syn, score in combined_count.most_common():

		score_dict[score].append(syn)


	syns = []

	for score, syn_list in sorted(list(score_dict.items()), reverse = True)[:nrange]:
		if score != 0:

			for syn in syn_list:
				syns.append(syn)


	return syns



def top_noun(noun):

	features_concepts = [
				"Synset('object.n.01')", 
				"Synset('artifact.n.01')",	
				"Synset('act.n.02')",
				"Synset('organism.n.01')", 
				"Synset('location.n.01')", 
				"Synset('organic_process.n.01')", 
				"Synset('natural_process.n.01')",
				"Synset('movement.n.03')",
				"Synset('physical_property.n.01')",	
				"Synset('bodily_process.n.01')",
				"Synset('body_part.n.01')",	
				"Synset('human_body.n.01')",
				"Synset('bodily_property.n.01')",
				"Synset('body.n.01')"
				]


	target = wn.synsets(noun, 'n')

	results = rank_senses(target, features_concepts, rank1 = 'hypo', rank2 = None, rank3 = None, rank4 = None)

	nrange = 1


	combined_count = results[0] #+ results[1]  + results[2]  + results[3]

	syns = alternative_ranking(combined_count, nrange)

	return syns


	





	

