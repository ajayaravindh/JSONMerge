import click
import os
import re
import json
from utils import is_a_directory, get_matching_files, load_json, get_root_key, merge_json

@click.command()
@click.argument('path-to-folder', type = click.Path()) # Mandatory argument - Path to the directory that holds the input JSON files
@click.argument('input-base') # Mandatory argument - Base input file name which will be taken for merging
@click.option('--output-base', '-o', help = "Output base name", default = "output") # Optional argument - Base output file name after which the output files are named - Default value: 'output'
@click.option('--max-file-size', '-m', help = "Maximum output file size in Bytes", type = int, default = 1000000) # Optional argument - Maximum output file size in Bytes - Defalut value: 1MB
def exec(path_to_folder, input_base, output_base, max_file_size):
	""" 
    Main function that calls the utility functions to accomplish the task of merging JSON files with maximum file size in mind

    Parameters: 
        path_to_folder (str): Path to the directory that contains input JSON files
        input_base (str): Base input file name which will be taken for merging
        output_base (str): Base output file name after which the output files are named
        max_file_size (int): Maximum number of Bytes that an output file can hold
    """

	if not(is_a_directory(path_to_folder)):
		print("--------------------------------Not a directory---------------------------------")
	else:
		sorted_file_list = get_matching_files(path_to_folder, input_base)

		if not sorted_file_list: # When there are no matching files
			print("No matching files found. Make sure you check your inputs.")
		else:
			json_files = load_json(path_to_folder, sorted_file_list)

			root_key = get_root_key(json_files[0])

			merge_json(root_key, json_files, output_base, max_file_size)

	
if __name__ == '__main__':
	exec()