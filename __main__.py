# __author__ = 'ximera'

import pefile
import sys
import os
from colors import red, green


def main():

    path = sys.argv[1]
    if path == 0:
        usage(sys.argv[0])
        exit()

    files_count = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])
    sys.stdout.write("Total files in dir: %s\n" % str(files_count))
    i = 0
    for pe_file in os.listdir(path):
        if os.path.isfile(os.path.join(path, pe_file)):
            if is_pe_file(os.path.join(path, pe_file)):
                sys.stdout.write("\nFile: " + pe_file + "\n")
                print_eq_sections(os.path.join(path, pe_file), False)
                i += 1


def print_eq_sections(in_file, flag):
    sample = pefile.PE(in_file)
    for section in sample.sections:
        if section.Misc_VirtualSize == section.SizeOfRawData:
            sys.stdout.write(red("Name: %0s" % section.Name + "\tRawSize = 0x%08x" % section.SizeOfRawData))
            sys.stdout.write(red("\tVirtualSize = 0x%08x" % section.Misc_VirtualSize))
            sys.stdout.write(red("\tEntropy = %02d" % section.get_entropy() + "\n"))
        elif flag == True:
            sys.stdout.write(green("Name: %0s" % section.Name + "\tRawSize = 0x%08x" % section.SizeOfRawData))
            sys.stdout.write(green("\tVirtualSize = 0x%08x" % section.Misc_VirtualSize))
            sys.stdout.write(green("\tEntropy = %02d" % section.get_entropy() + "\n"))


def is_pe_file(in_file):
    readed_file = open(in_file, 'r')
    if readed_file.read(2) == 'MZ':
        return 1
    else:
        return 0



def print_msg(code, msg):
    if code == -1:
        print "[ERROR]\t" + msg
    else:
        print "[INFO]\t" + msg


def usage(module_name):
    print 'Usage: ' + module_name + " <folder_with_pe_files>"


if __name__ == '__main__':
    main()
