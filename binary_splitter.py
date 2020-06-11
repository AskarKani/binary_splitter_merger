import os
import math
import sys
from pathlib import Path
import hash_find


def gen_file_name(index, binary_file_path):
    if len(binary_file_path.split("\\")) > 1:
        file_name = str(index) + "_" + str(binary_file_path.split("\\")[-1])
    elif len(binary_file_path.split("/")) > 1:
        file_name = str(index) + "_" + str(binary_file_path.split("/")[-1])
    else:
        file_name = str(index) + "_" + str(binary_file_path)
    return file_name


def main(binary_file, split_bytes):
    binary_file_size = os.path.getsize(binary_file)
    if binary_file_size < split_bytes:
        print("\n" + str(binary_file) + " size is lesser than split_file_size : " + str(split_bytes))
        print("PASS the chunk size in bytes with -b option")
        sys.exit(1)

    # store the hash in out folder
    hash_folder_path = Path(os.getcwd()) / "hash_out"
    if not os.path.isdir(hash_folder_path):
        os.mkdir(hash_folder_path)
    hash_file_path = hash_folder_path / "sha_256.txt"
    print("\nThe sha256sum hash of  " + str(binary_file) + " stored in " + str(hash_file_path))
    with open(hash_file_path, 'w') as hash_file:
        hash_file.write("Hash value of " + str(binary_file) + " : ")
        hash_file.write(hash_find.sha256(binary_file) + "\n")

    number_of_files = math.ceil(binary_file_size / split_bytes)
    print("\nTOTAL NUMBER OF FILES : " + str(number_of_files))
    binary_file_content = open(binary_file, 'rb')
    out_folder_path = Path(os.getcwd()) / "split_out"
    if not os.path.isdir(out_folder_path):
        os.mkdir(out_folder_path)

    for file_number in range(1, number_of_files+1):
        file_name = gen_file_name(file_number, binary_file)
        gen_file = out_folder_path / file_name
        with open(gen_file, 'wb') as write_file:
            write_file.write(binary_file_content.read(split_bytes))
        with open(hash_file_path, 'a') as hash_file:
            hash_file.write("Hash value of " + str(file_name) + " : ")
            hash_file.write(hash_find.sha256(gen_file) + "\n")

        print("Generating file : " + str(file_name) + str(" and hash...."), end ='\r', flush=True)

    print("\n\nThe splitted files are stored in " + str(out_folder_path))
    print("The sha256sum hash of splitted files are stored in " + str(hash_file_path))