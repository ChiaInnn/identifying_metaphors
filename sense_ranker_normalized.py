from nltk.corpus import wordnet as wn
from collections import Counter
import pickle
from pandas import *
import pprint
from collections import defaultdict

def collect_sim(features_sim, target):
    
    sim_collected = []


    for feature in features_sim:
	    

    	feature = feature[8:].rstrip("')")

    	feature = wn.synset(feature)
    	

    	feature_list = []

    	for syn in target:
    
    			feature_list.append([syn.path_similarity(feature), syn])

    	sim_collected.append(sorted(feature_list))
        
    
    return sim_collected

def collect_hypo(features_hypo, target):
    
    hypo_collected = []

    with open('person_hyponyms.csv', 'r') as personfile:
        person = personfile.read().split('\n')

    data = pandas.read_csv('hyponyms.csv', names=features_hypo, delimiter = '\t')
                         
 
    for feature in features_hypo:
    	feature_list = []

	   

    	for syn in target:

    		syn_str = str(syn)

    		if syn_str not in data[feature].tolist():
    			feature_list.append([0, syn])

    		elif (syn_str in data[feature].tolist()) and (syn_str not in person):
    			feature_list.append([1, syn])

    	hypo_collected.append(feature_list)

    return hypo_collected

def collect_senses(target):
    
    senses_collected = []
    feature_list = []
    for n, syn in enumerate(reversed(target)):
    	feature_list.append([n, syn])

    senses_collected.append(feature_list)

    return senses_collected

def collect_depth(target):
    
    senses_collected = []
    feature_list = []
    for syn in target:
    	feature_list.append([syn.min_depth(), syn])

    senses_collected.append(feature_list)

    return senses_collected

def count_features(collected_list):
    
    rank = Counter()

    for feature in collected_list:
      
        for line in feature:


        	rank[line[1]] += line[0]

    return rank


def rank_values(counted_features):


    rank_counter = Counter()

    if list(counted_features.most_common()):

        top_tuple = list(counted_features.most_common())[0]
        top_value = top_tuple[1]
        for syn, count in counted_features.most_common():
            if top_value != 0:
                rank_counter[syn] = count / top_value
            else:
                rank_counter[syn] = 0

    return rank_counter



features_concepts = [
			"Synset('object.n.01')", 
			"Synset('artifact.n.01')",	
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



#target = wn.synsets('roller', 'n')
#print(target)


#sim_collected =  collect_sim(features_concepts, target, body = None)
#hypo_collected = collect_hypo(features_concepts, target, body = None)
#senses_collected = collect_senses(target)
#depth_collected = collect_depth(target)

#for key, value in count_features(sim_collected).most_common():
#	print(key, value)
#print('\n ---------------\n')

#for key, value in count_features(hypo_collected).most_common():
#	print(key, value)


#for key, value in count_features(depth_collected).most_common():
#	print(key, value)


#print('\n ---------------\n')

#counted_features_sim = count_features(sim_collected)
#counted_features_hypo = count_features(hypo_collected)
#counted_features_senses = count_features(senses_collected)
#counted_features_depth = count_features(depth_collected)



#for syn, rank in rank_values(counted_features_senses).most_common():
#	print(syn, rank)




