#TODO: CRAM OVERLAP HERE

def getFileFrequencies(filename,order):
    text = open(filename,"r").read()
    alphabet = set(text)
                #if (len(alphabet)**(order*2))*64>8...   #assumes int size is 64, actually grows forever -> actually just always using hash table
    start_text = text[:order]
    text = text[order:]
    table = {}
    for character in text:
        pass