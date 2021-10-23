import argparse
import common_modules

if __name__ == "__main__":
    parser= argparse.ArgumentParser()
    parser.add_argument("--order",help="Order of the model",type=int,default=2)
    parser.add_argument("--source",help="Source text file", default="example.txt")
    parser.add_argument("--smoothing", help="Smoothing parameter", type=float,default=1) #maybe replace this default with a function of alphabet size

    args = parser.parse_args()

    table,appearances,alphabet = common_modules.getFileFrequencies(args.source,args.order)

    p_map = common_modules.calculateProbabilityMap(table,alphabet,args.smoothing)

    entropy = common_modules.calculateEntropy(p_map,appearances,len(alphabet))
    print(entropy)