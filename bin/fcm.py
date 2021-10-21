import argparse
import common_modules

if __name__ == "__main__":
    parser= argparse.ArgumentParser()
    parser.add_argument("--order",help="Order of the model",type=int,default=2)
    parser.add_argument("--source",help="Source text file", default="example.txt")
    #parser.add_argument("--output",help="Output file name",default="output.csv")
    parser.add_argument("--smoothing", help="Smoothing parameter", type=int,default=2) #maybe replace this with a function of alphabet size

    args = parser.parse_args()

    table,appearances,alphabet = common_modules.getFileFrequencies(args.source,args.order)