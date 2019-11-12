# JSONMerge
A Python command line application to merge JSON files with support for maximum output file size.


_Developed and tested in **Linux** environment but this should work fine for Windows and Mac environments too as the **os** module of Python takes care of **compatability**_

### Requirements
- Python3
- Python standard library
- Click package - To create robust command line application ($pip install click - to install)

### Usage
- Clone and cd into this repo

- **Help:** python src.py --help
- python src.py [OPTIONS] PATH_TO_FOLDER INPUT_BASE_FILE_NAME
	
	**Options**
	- -o (or) --output-base -> OUTPUT BASE FILE NAME
	- -m (or) --max-file-size -> MAXIMUM_OUTPUT_FILE_SIZE

By default it writes the the Output directory, but this can be changed in the function. The reason it was done this way is that the permissible inputs to the program were only the 4 listed in the first functional requirements.

## Files

- utils.py - Holds all the utility functions
- src.py - Source file that needs to be executed

## Functional Requirements Coverage

 - [x] Accept **folder path**, **input file base name**, **output file base name**, **maximum file size**

 - [x] Read all files in the folder path and process the files in increasing order of the suffix

 - [x] Output files are named using the output file base name as prefix and a counter as a suffix

 - [x] Merged files are never greater than the maximum file size

 - [x] Each output file contains a proper JSON array

 - [x] Any kind of JSON arrays can be merged

 - [x] Supports non-English characters too


## Non-functional Requirements Coverage

- [x] Algorithmic Complexity

	_**O(number of input files * log (number of input files))**_ - Mainly because of the **sorting** procedure used to handle the files in increasing order of the suffixes

- [x] The merged files are as large as possible, without exceeding the maximum file size