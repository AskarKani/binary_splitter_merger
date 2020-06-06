import os, natsort, sys
from pathlib import Path


def main(input_path, out_file_name):
    input_file_path = Path(os.getcwd()) / input_path
    files = os.listdir(input_file_path)
    if not len(files):
        print("The " + str(input_path) + " folder path is empty")
        sys.exit(1)
    files_sorted = natsort.natsorted(files)

    out_folder_path = Path(os.getcwd()) / "merge_out"
    if not os.path.isdir(out_folder_path):
        os.mkdir(out_folder_path)
    merge_out_file = open(out_folder_path / out_file_name, 'wb')
    for file in files_sorted:
        with open(input_file_path / file ,'rb') as input_file:
            merge_out_file.write(input_file.read())
    merge_out_file.close()