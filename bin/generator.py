import argparse

if __name__ == "__main__":
    parser= argparse.ArgumentParser()
    parser.add_argument("--order","Order of the model",type=int,default=2)
    parser.add_argument("--source","Source text file", default="example.txt")
    parser.add_argument("--output","Output file name",default="output.txt")
    parser.add_argument("--smoothing", "smoothing parameter", type=int,default=2) #maybe replace this with a function of alphabet size
    parser.add_argument("--length", "length of generated text", type=int, default=1000)
    parser.add_argument("--start", "Starting text", default="")#use a random method to calculate if empty