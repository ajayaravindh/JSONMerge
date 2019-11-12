# JSONMerge
A Python Command line application to merge JSON files with support for maximum output file size.


_Developed and tested in **Linux** environment but this should work fine for Windows and Mac environments too as the **os** module of Python takes care of **compatability**_

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