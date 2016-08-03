import xml.etree.ElementTree as etree
import json


def load_file(xmlfile):

    tree = etree.parse(xmlfile)
    root = tree.getroot()

    xml_list = root.getchildren()

    return xml_list


def text_to_json(text_xml):
    """Stores information of one news file in from xml file to json format"""
    text_list = []

    bodies = text_xml.getchildren()

    for body in bodies:

        divs = body.getchildren()

        for div in divs:

            sections = div.getchildren()

            for section in sections:

                sentences = section.getchildren()

                for sentence in sentences:

                    sentence_list = []

                    words = sentence.getchildren()

                    for word in words:

                        word_dict = dict()

                        mets = word.getchildren()

                        if mets:
                            word_dict['pos'] = word.get('type')
                            word_dict['lemma'] = word.get('lemma')

                            for met in mets:
                             
                     
                                mytoken = str(met.text.strip().encode('ascii', 'ignore'))[2:].rstrip("'")

                                if mytoken != '':

                                    print(mytoken)

                                    word_dict['token'] = mytoken
                      
                              
                                    word_dict['met_type'] = met.get('type')
                                    word_dict['function'] = met.get('function')
                                    word_dict['morph'] = met.get(
                                        '{http://www.tei-c.org/ns/VICI}morph')
                                    if met.get('subtype'):
                                        word_dict['subtype'] = met.get('subtype')
                                    else:
                                        word_dict['subtype'] = None

                        else:
                            
                           

                            if type(word.text) == str:


                                mytoken = str(word.text.strip().encode('ascii', 'ignore'))[2:].rstrip("'")

                                if mytoken != '':
                               
                                    print(mytoken)
                  
                                    word_dict['token'] = mytoken
                                    word_dict['pos'] = word.get('type')
                                    word_dict['lemma'] = word.get('lemma')
                                    word_dict['met_type'] = None
                                    word_dict['subtype'] = None
                                    word_dict['function'] = None
                                    word_dict['morph'] = None


                        if 'token' in word_dict.keys():
                         
                     

                            sentence_list.append(word_dict)

                    text_list.append(sentence_list)
    return text_list


def json_to_dir(xmlfile, dirname):

    text_list = load_file(xmlfile)

    print(type(text_list), len(text_list))

    for text in text_list:

        xml_id = list(text.attrib.values())[0]
        print(xml_id)
        json_text = text_to_json(text)

        with open(dirname + '/' + xml_id + '.json', 'w') as outfile:
            json.dump(json_text, outfile)




json_to_dir('news_test.xml', 'test' )