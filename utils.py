import os
import re
import json

def is_a_directory(path):
	""" 
    Wrapper function that checks the validity of given path to the directory

    Parameters: 
        path (str): Path to the directory that contains input JSON files
      
    Returns: 
        Boolean: True if it is a valid directory, false otherwise
    """

	return os.path.isdir(path)

def get_matching_files(path_to_folder, input_base):
	""" 
    Returns a list of JSON files in the given path that matches with the given input base name and returns the files in sorted order according to suffixes.

    Parameters: 
        path_to_folder (str): Path to the directory that contains input JSON files
        input_base (str): Base name for all input files
      
    Returns: 
        list: Sorted(according to suffixes) JSON files that match with the given input base file name in the given directory
    """

	files = os.listdir(path_to_folder) #returns unsorted list of files in the directory

	l = []
	for file in files:
		filename = os.fsdecode(file)

		if(filename.startswith(input_base) and filename.endswith('.json')):
			match = re.search(input_base + r"(\d+)", filename) # CASE SENSITIVE MATCHING
			if(match):
				l.append(int(match.group(1))) # only the suffixes are added to the list as integers

	l = sorted(l) # sorting the integer suffixes

	sorted_file_list = []
	for i in range(len(l)): # looping over the sorted suffixes
		sorted_file_list.append(input_base + str(l[i]) + ".json") # Adding files to the list sorted according to suffixes

	return sorted_file_list


def load_json(path_to_folder, file_list):
	""" 
    Opens all the matched JSON files in UTF-8 encoding and returns all the JSON files

    Parameters: 
        path_to_folder (str): Path to the directory that contains input JSON files
        file_list (list): List of JSON files
      
    Returns: 
        list: All JSON files encoded in UTF-8 format
    """

	json_files = []
	for file in file_list:
		try:
			with open(path_to_folder + "/" + file, 'r', encoding = 'utf-8') as f: # Opening the file in UTF-8 encoding to support non-English characters
				json_file = json.loads(f.read())
			json_files.append(json_file)
		except:
			print("Error in opening files")
	return json_files

def get_root_key(json_file):
	""" 
    Finds and returns the root key in the JSON files

    Parameters: 
        json_file (File): JSON file that was matched in previous steps
      
    Returns: 
        str: The root key of the JSON files
    """

	root_key = list(json_file.keys())[0] # root key is the first key in the first level of the JSON file
	return root_key

def merge_json(root_key, json_files, output_base, max_file_size, output_path = "./Output/"):
	""" 
    Function to merge JSON files while adhering the the maximum output file size limits

    Parameters: 
        root_key (str): The root key of the input JSON files
        json_files (list): All JSON files encoded in UTF-8 format
        output_base (str): Base output file name after which the output files are named
        max_file_size (int): Maximum number of Bytes that an output file can hold
        output_path (path/str): Directory to write output JSON files to
    """

	new_json = {root_key: []}

	curr_len = len(root_key.encode('utf-8')) + 6 # len(root_key) + 6 to support ': {[]}' - len of which is 6
	# print(len(root_key))
	iter = 1
	tot = len(json_files)
	completed = 0
	last_write = 0

	for i in json_files:
		if(len(str(i[root_key]).encode('utf-8')) + curr_len <= max_file_size): #len(UTF-8 encoded string) gives the bytes that a string will occupy
			# print(len(str(i[root_key])))
			new_json[root_key].extend(i[root_key])
			curr_len += len(str(i[root_key]).encode('utf-8'))
			completed += 1 
			# print(completed, "  ", len(str(i[root_key]).encode('utf-8')))
		else:
			if(len(str(i[root_key]).encode('utf-8')) > max_file_size): # If the input file is greater than maximum file size
				continue
			curr_len = len(root_key.encode('utf-8')) + 6
			with open(output_path + output_base + str(iter) + '.json', 'w', encoding='utf-8') as f:
				f.write(str(new_json))
			last_write = completed
			new_json = {root_key: []}
			new_json[root_key].extend(i[root_key])
			curr_len += len(str(i[root_key]).encode('utf-8'))
			completed += 1
			iter += 1
			# print(completed, "  ", len(str(i[root_key]).encode('utf-8')))

	if(completed == 0): # When the maximum file size if too small
		print("Maximum file size is too short to hold any values")
		return

	if(last_write < completed):
		with open(output_path + output_base + str(iter) + '.json', 'w', encoding='utf-8') as f:
			f.write(str(new_json))

	print("Write successful!")