import xml.etree.ElementTree as etree


def news_filenames(newsfilenames):
    """
    opens txt fiel with filenames
    rurns list of filename strings
    """

    with open(newsfilenames, 'r') as file:
        news_filenames = file.read()

    news_filenames_list = news_filenames.split(', ')

    clean_filenames = []

    for name in news_filenames_list:
        clean_name = name.strip()
        clean_filenames.append(clean_name)

    return clean_filenames


def extract_texts(corpus):
    """
    Input: name of a corpus file
    Output: list of individual texts (as xml elements)
    """
    tree = etree.parse(corpus)

    root = tree.getroot()

    header, text1 = root.getchildren()

    group = text1.getchildren()[0]

    texts = group.getchildren()

    return texts


def extract_news_texts(newsfilenames, corpus):
    """
    extracts news files from the corpus
    """
    news_xml = []
    filenames = news_filenames(newsfilenames)
    corpus_texts = extract_texts(corpus)

    for text in corpus_texts:
        xml_id = list(text.attrib.values())[0]
        filename = xml_id.split('-')[0]

        if filename in filenames:
            news_xml.append(text)

    return news_xml


def split_corpus(split_index):

    news_xml = extract_news_texts('news_files.txt', '2541/VUAMC.xml')

    development = news_xml[:split_index]
    test = news_xml[split_index:]

    print(len(development), len(test))

    root_development = etree.Element("Development")

    for element in development:
        root_development.append(element)

    tree_development = etree.ElementTree(root_development)
    tree_development.write("news_development.xml")

    root_test = etree.Element("Test")

    for element in test:
        root_test.append(element)
        
    tree_test = etree.ElementTree(root_test)
    tree_test.write("news_test.xml")

split_corpus(33)
