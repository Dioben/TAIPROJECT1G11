# TAIPROJECT1
Text Analyzer + Text Generator made for a Algorithmic Information Theory project based on Finite-Context Models.

## How to run
The project was implemented in python 3.9, the python3 interpreter is necessary to run code and the matplotlib, pandas, and numpy extensions are required for plotting-related code.

The extensions can be installed as follows:
```bash
pip3 install matplotlib
pip3 install pandas
pip3 install numpy
```
Both our entropy calculator and text generator are detached from these dependencies and can be run without installing them as follows from within the */bin/* folder context.
```bash
python3 fcm.py <options>
python3 generator.py <options>
```
The options for these scripts are as follows:

### fcm.py
- --order: Sets the order of the model, the default value is **2**
- --smoothing: Sets the smoothing value, the default value is **1**
- --source: The name of the file that will be read to generate the model, the default value is **example.txt**, and is sensitive to the current folder context

### generator.py
- --order: Sets the order of the model, the default value is **2**
- --smoothing: Sets the smoothing value, the default value is **0.00001**
- --source: The name of the file that will be read to generate the model, the default value is **example.txt**, and is sensitive to the current folder context
- --output: The name of  the file that will be used to output the generated text, the default value is **output.txt**, and is sensitive to the current folder context
- --length: The length of the text to be generated, the default value is **1000**
- --start: The starting sentence so the program knows which context to use first, if no value is provided one is randomly selected from the provided text, with weights decided by how frequently a string occurs in the text

### Running with options - examples
```bash
python3 fcm.py --order 10 --smoothing 0.05 --source ../example/english.txt
python3 generator.py --order 10 --smoothing 0.05 --source ../example/english.txt --output "more_bee_movie.txt" --length 10000 --start "Ya like jazz?"
```
