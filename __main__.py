# __author__ = 'ximera'

import pefile
import sys
import time
import os


def main():
    files_eq = 0
    files_neq = 0
    total_files = 0
    path = sys.argv[1]
    if path == 0:
        usage(sys.argv[0])
        exit()
    files_count = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])
    sys.stdout.write("Total files in dir: "+str(files_count))
    i = 0
    percent = 0
    for pe_file in os.listdir(path):
        if os.path.isfile(os.path.join(path, pe_file)):
            if i == (files_count / 100):
                i = 0
                percent += 1
                time.sleep(1)
                sys.stdout.write("\r%d%%" % percent)
                sys.stdout.flush()
            i += 1


def print_msg(code, msg):
    if code == -1:
        print "[ERROR]\t"+msg
    else:
        print "[INFO]\t"+msg


def usage(module_name):
    print 'Usage: '+module_name+" <folder_with_pe_files>"

if __name__ == '__main__':
    main()