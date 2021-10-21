import argparse

if __name__ == "__main__":
    parser= argparse.ArgumentParser()
    parser.add_argument("--order","Order of the model",type=int,default=2)
    parser.add_argument("--source","Source text file", default="example.txt")
    #parser.add_argument("--output","Output file name",default="output.csv")
    parser.add_argument("--smoothing", "smoothing parameter", type=int,default=2) #maybe replace this with a function of alphabet size