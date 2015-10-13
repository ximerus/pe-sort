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


def cmp_vsize_rsize(full_path_to_pe):
    result  = 0
    if full_path_to_pe == 0:
        print_msg(-1, "Specified file in't exist!")
    pe_file = pefile.PE(full_path_to_pe)
    if pe_file.is_exe() or pe_file.is_dll() or pe_file.is_driver():
        for section in pe_file.sections:
            if (section.Misc_VirtualSize == section.SizeOfRawData) and (".rsrc" in section.Name):
                result = 1
    return result


def print_msg(code, msg):
    if code == -1:
        print "[ERROR]\t"+msg
    else:
        print "[INFO]\t"+msg


def usage(module_name):
    print 'Usage: '+module_name+" <folder_with_pe_files>"

if __name__ == '__main__':
    main()