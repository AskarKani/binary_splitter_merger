import os
import math
import sys
from pathlib import Path


def main(binary_file, split_bytes):
    binary_file_size = os.path.getsize(binary_file)
    if binary_file_size < split_bytes:
        print(str(binary_file) + " size is lesser than split_file_size : " + str(split_bytes))
        sys.exit(1)
    number_of_files = math.ceil(binary_file_size / split_bytes)
    print("TOTAL NUMBER OF FILES : " + str(number_of_files))
    binary_file_content = open(binary_file, 'rb')
    out_folder_path = Path(os.getcwd()) / "split_out"
    if not os.path.isdir(out_folder_path):
        os.mkdir(out_folder_path)

    for file_number in range(1, number_of_files+1):
        gen_file_name = str(file_number) + "_" + str(binary_file)
        gen_file = out_folder_path / gen_file_name
        with open(gen_file, 'wb') as write_file:
            write_file.write(binary_file_content.read(split_bytes))
        print("Generating file : " + str(gen_file_name) + str(" ...."), end ='\r', flush=True)
    print("The splitted files are stored in " + str(out_folder_path))