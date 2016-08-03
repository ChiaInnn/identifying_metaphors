from __future__ import print_function
from KafNafParserPy import *
import sys
import glob


def create_naf_from_txt(infile):
    '''
    Creates naffile together with header (fileDesc based on file name) and raw text based on flat text in raw
    '''
    
    mynaf = KafNafParser(type='NAF')
    
    #adding public_id and file name
    fileDesc = CfileDesc()
    fileDesc.set_filename(infile)
    pubId = Cpublic()
    pubId.set_publicid(infile)
    header = CHeader()
    header.set_fileDesc(fileDesc)
    header.set_publicId(pubId)
    mynaf.set_header(header)
    mynaf.set_language('en')
    mynaf.set_version('v3')
    
    #create rawtext
    with open(infile, 'r') as myfile:
        raw=myfile.read().replace('\n', '')
        raw=raw.encode('utf8')
        
    mynaf.set_raw(raw)

    infile = infile.strip('test_txt/')
    print(infile)
    mynaf.dump('raw_naf_test/'+infile+'naf')



infiles = glob.glob('test_txt/*.txt')
print(infiles, len(infiles))


for infile in infiles:

	create_naf_from_txt(infile)


def main(argv=None):
    if argv==None:
        argv=sys.argv
    
    if len(argv) > 1:
        create_naf_from_txt(argv[1])
    else:
        print >> sys.stderr, 'Usage: python create_naf_from_raw.py inputfile'





if __name__ == '__main__':
    main()
