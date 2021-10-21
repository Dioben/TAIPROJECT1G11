import math

def getFileFrequencies(filename,order):
    file = open(filename,"r")
    text= file.read()
    file.close()

    alphabet = set(text)
                #if (len(alphabet)**(order+1))*64>8...   #assumes int size is 64, actually grows forever -> actually just always using hash table
    current_buffer = text[:order]
    text = text[order:]
    table = {}
    appearances = {current_buffer:1}
    for character in text:
        if current_buffer not in table.keys(): #have we seen this predecessor yet?
            table[current_buffer]= {}
        if character not in table[current_buffer].keys(): #have we seen this sequence?
            table[current_buffer][character]=1
        else:
            table[current_buffer][character]+=1
        current_buffer = current_buffer [1:]+character
        if current_buffer in appearances.keys():
            appearances[current_buffer]+=1
        else:
            appearances[current_buffer]=1
    return table,appearances,alphabet

def calculateProbabilityMap(frequencies,alphabet,smoothing):
    result = {}
    smoothing_denominator = smoothing*len(alphabet)

    for sequence in frequencies.keys():
        total = sum(sequence.values())
        denominator = total+smoothing_denominator
        result[sequence] = { x: (sequence[x]+smoothing)/denominator for x in sequence.keys() }
        result[sequence]['default']=smoothing/denominator
    return result


def calculateEntropy(probabilities,appearances):
    statetotal = sum(appearances.values())
    #individual formula: − log P(e|c)
    #row formula: sum of (individual * probability)
    #overall formula: sum (rowvalue * row probability)
    rowvalues = {x: sum([-probabilities[y]*math.log2(probabilities[y]) for y in probabilities[x]]) for x in probabilities.keys()}
    return sum([rowvalues*appearances[state]/statetotal for state in appearances])