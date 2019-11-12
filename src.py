import click
import os
import re
import json
from utils import *

@click.command()
@click.argument('path-to-folder', type = click.Path())
@click.argument('input-base')
@click.option('--output-base', '-o', help = "Output base name", default = "Output")
@click.option('--max-file-size', '-m', help = "Maximum output file size in Bytes", type = int, default = 500000)
def exec(path_to_folder, input_base, output_base, max_file_size):

	if not(is_a_directory(path_to_folder)):
		print("--------------------------------Not a directory---------------------------------")
	else:
		sorted_file_list = get_matching_files(path_to_folder, input_base)
		print(sorted_file_list)
		if not sorted_file_list:
			print("No matching files found. Make sure you check your inputs.")
		else:
			json_files = load_json(path_to_folder, sorted_file_list)

			root_key = get_root_key(json_files[0])

			merge_json(root_key, json_files, output_base, max_file_size)

	
if __name__ == '__main__':
	exec()