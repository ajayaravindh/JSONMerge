import os
import re
import json

def is_a_directory(path):
	return os.path.isdir(path)

def get_matching_files(path_to_folder, input_base):
	files = os.listdir(path_to_folder)

	l = []
	for file in files:
		filename = os.fsdecode(file)

		if(filename.startswith(input_base) and filename.endswith('.json')):
			match = re.search(input_base + r"(\d+)", filename)
			if(match):
				l.append(int(match.group(1)))

	l = sorted(l)

	sorted_file_list = []
	for i in range(len(l)):
		sorted_file_list.append(input_base + str(l[i]) + ".json")

	return sorted_file_list


def load_json(path_to_folder, file_list):
	json_files = []
	for file in file_list:

		with open(path_to_folder + "/" + file, 'r', encoding = 'utf-8') as f: # check for empty files
			json_file = json.loads(f.read())
		json_files.append(json_file)
	return json_files

def get_root_key(json_file):
	root_key = list(json_file.keys())[0]
	return root_key

def merge_json(root_key, json_files, output_base, max_file_size, output_path = "./Output/"):
	new_json = {root_key: []}

	curr_len = len(root_key.encode('utf-8')) + 6
	# print(len(root_key))
	iter = 1
	tot = len(json_files)
	completed = 0
	last_write = 0

	for i in json_files:
		if(len(str(i[root_key]).encode('utf-8')) + curr_len <= max_file_size):
			# print(len(str(i[root_key])))
			new_json[root_key].extend(i[root_key])
			curr_len += len(str(i[root_key]).encode('utf-8'))
			completed += 1 
			# print(completed, "  ", len(str(i[root_key]).encode('utf-8')))
		else:
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

	if(last_write < completed):
		with open(output_path + output_base + str(iter) + '.json', 'w', encoding='utf-8') as f:
			f.write(str(new_json))