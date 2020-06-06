import os, natsort, sys
from pathlib import Path


def main(input_path, out_file_name):
    input_file_path = Path(os.getcwd()) / input_path
    files = os.listdir(input_file_path)
    if not len(files):
        print("The " + str(input_path) + " folder path is empty")
        sys.exit(1)
    files_sorted = natsort.natsorted(files)
    total_files = len(files_sorted)
    print("TOTAL FILES : " + str(total_files))

    out_folder_path = Path(os.getcwd()) / "merge_out"
    if not os.path.isdir(out_folder_path):
        os.mkdir(out_folder_path)
    merge_out_file = open(out_folder_path / out_file_name, 'wb')
    count = 1
    for file in files_sorted:
        with open(input_file_path / file ,'rb') as input_file:
            merge_out_file.write(input_file.read())
        print("Merging files - " + str(count) + " out of " + str(total_files) + " finished " , end='\r', flush=True)
        count += 1
    merge_out_file.close()
    print("The merged file " + str(out_file_name) + " is stored in " + str(out_folder_path))