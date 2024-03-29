import argparse
import random
import common_modules

if __name__ == "__main__":
    parser= argparse.ArgumentParser()
    parser.add_argument("--order",help="Order of the model",type=int,default=2)
    parser.add_argument("--source",help="Source text file", default="../example/example.txt")
    parser.add_argument("--output",help="Output file name",default="output.txt")
    parser.add_argument("--smoothing", help="Smoothing parameter", type=float,default=0.00001) #maybe replace this with a function of alphabet size
    parser.add_argument("--length", help="Length of generated text", type=int, default=1000)
    parser.add_argument("--start", help="Starting text", default="")#use a random method to calculate if empty

    args = parser.parse_args()

    if args.order<1:
        raise ValueError("Order must be at least 1")
    if args.smoothing<0:
        raise ValueError("Smoothing must be non-negative")


    table,appearances,alphabet = common_modules.getFileFrequencies(args.source,args.order)
    p_map = common_modules.calculateProbabilityMap(table,alphabet,args.smoothing)
    
    if args.start =="":
        total_appearances = sum(appearances.values())
        cumulative_value = 0
        target = random.random()
        for key,value in appearances.items():
            cumulative_value+=value/total_appearances
            if cumulative_value>=target:
                args.start=key
                break

    text = args.start + common_modules.generateText(p_map,alphabet,args.length,args.start)
    output = open(args.output,"w")
    output.write(text)
    output.close()
