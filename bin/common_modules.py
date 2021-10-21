#TODO: CRAM OVERLAP HERE

def getFileFrequencies(filename,order):
    text = open(filename,"r").read()
    alphabet = set(text)
                #if (len(alphabet)**(order*2))*64>8...   #assumes int size is 64, actually grows forever -> actually just always using hash table
    current_buffer = text[:order]
    text = text[order:]
    table = {}

    for character in text:
        if current_buffer not in table.keys(): #have we seen this predecessor yet?
            table[current_buffer]= {}
        if character not in table[current_buffer].keys(): #have we seen this sequence?
            table[current_buffer][character]=1
        else:
            table[current_buffer][character]+=1
        current_buffer = current_buffer [1:]+character
    
    return table,alphabet