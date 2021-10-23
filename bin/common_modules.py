import math
import random

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

    for sequence,appearances in frequencies.items():
        total = sum(appearances.values())
        denominator = total+smoothing_denominator
        result[sequence] = { x: (y+smoothing)/denominator for x,y in appearances.items() }
        result[sequence]['default']=smoothing/denominator
    return result


def calculateEntropy(probabilities,appearances):
    statetotal = sum(appearances.values())
    #individual formula: − log P(e|c)
    #row formula: sum of (individual * probability)
    #overall formula: sum (rowvalue * row probability)
    rowvalues = {x: sum([-y[z]*math.log2(y[z]) for z in y.keys() if z!="default"]) for x,y in probabilities.items() }
    return sum([rowvalues[state]*appearances[state]/statetotal for state in appearances])


def generateText(probabilities,alphabet,length,start):
    #return length*chars 
    order = len(probabilities.keys()[0])
    if len(start)<order:
        raise ValueError("Given start is too small to work with")
    
    alphabet_indexable = list(alphabet) #allow consistent ordering for use in unseen sequences
    alphabet_size = len(alphabet)
    current_buffer = start[-order:]
    generated_string = ""
    for x in range(length):
        if current_buffer not in probabilities.keys():#if we haven't observed this any character is equally likely as a follow-up
            char = alphabet_indexable[math.floor(random.random()*alphabet_size)]
        else:
            seen = probabilities[current_buffer].keys()
            value = random.random()
            cumulative_chance = 0

            for key in seen: #first try with probabilities we already know
                if key!="default":
                    cumulative_chance+=probabilities[current_buffer][key]
                    if cumulative_chance>=value:
                        char = key
                        break
            if cumulative_chance<value: #try to get an unseen letter here
                unseen = alphabet.difference(seen)
                default_add = probabilities[current_buffer]['default']
                for char in unseen:
                    cumulative_chance+=default_add
                    if cumulative_chance>=value:
                        char = key
                        break
            if cumulative_chance>1:
                raise ValueError("oh god why is cumulative probability larger than 1?")
        generated_string+=char
        current_buffer= current_buffer[1:]+char
    return generated_string

