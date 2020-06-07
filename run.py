import sys
import argparse
import os



if __name__ == '__main__':
    if sys.version_info[0] < 3:
        print("!!!WARNING!!! RUN with PYTHON 3...")
        sys.exit(1)
    import binary_splitter, binary_merger, clean

    des = "!........................! IMAGE SPLITTER MERGER !........................!\n " \
          "\rpython main.py -s -b split size in bytes(default=100MB) binary_file\n" \
           "\rpython main.py -m  -i folder_path(splitted images) - o out_file_name\n" \
            "python main.py -clean"
    parser = argparse.ArgumentParser(description=des, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-b', metavar= 'split size in bytes(default=100MB)', default=104857600, type=int)
    parser.add_argument('-s', action="store_true", default=False, help='to split')
    parser.add_argument('-m', action="store_true", default=False, help= 'to merge')
    parser.add_argument('-i', action="store", metavar='input_path', help='folder_path(contains split images)')
    parser.add_argument('-o', action="store", metavar='merge_outfile_name', help='merge_file_name')
    parser.add_argument('-hashvalue', action="store", metavar='hash check', \
                        default=False, help='Check the genearted file\'s hash with value provided')
    parser.add_argument('-clean', action="store_true", default=False, help='clean the split and merge output folder')
    parser.add_argument('binary_file', nargs='?')
    arg = parser.parse_args()

    if arg.clean:
        clean.clean()
        sys.exit(1)
    result = [arg.s, arg.m]
    count = [0 for _ in result if _ ]
    if count.count(0) == 2:
        print("pass only one argument")
        sys.exit(1)
    if count.count(0) == 0:
        print("pass any argument")
        sys.exit(1)

    if arg.s:
        if not arg.binary_file:
            print("\nPass binary_file for splitting..")
            sys.exit(1)
        if not os.path.isfile(arg.binary_file):
            print(str(arg.binary_file) + " is not a valid file path")
            sys.exit(1)
        print("!!.........................! BINARY SPLITTER !.........................!!")
        print("\nSplittig the file " + str(arg.binary_file) + " with CHUNK SIZE " + str(arg.b))
        binary_splitter.main(arg.binary_file, arg.b)
    elif arg.m:
        print("!!.........................! BINARY MERGER !.........................!!")
        if not arg.i:
            print("\nPass the path which contains the splitted images with -i option")
            sys.exit(1)
        if not os.path.isdir(arg.i):
            print("\n" + str(arg.i) + " is not a valid folder path")
            sys.exit(1)
        if not arg.o:
            out_file_name = input("\nEnter the output file name.... ")
        else:
            out_file_name = arg.o
        print("\nMerging the files from " + str(arg.i) + " folder to " + str(out_file_name))
        if not arg.hashvalue:
            print("\nCheck sha256_sum of merged file with -hashvalue option")
        binary_merger.main(arg.i, out_file_name, arg.hashvalue)

