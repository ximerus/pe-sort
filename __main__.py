# __author__ = 'ximera'

import pefile
import sys
import os
from colors import red, green, yellow, blue, magenta, cyan
import time


def main():

    path = sys.argv[1]
    if path == 0:
        usage(sys.argv[0])
        exit()

    files_count = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])
    sys.stdout.write("Total files in dir: %s\n" % str(files_count))
    for pe_file in os.listdir(path):
        if os.path.isfile(os.path.join(path, pe_file)):
            sys.stdout.write(cyan(("\nFile: " + pe_file + "\n")))
            if is_pe_file(os.path.join(path, pe_file)):
                print_eq_sections(os.path.join(path, pe_file), True, ".rsrc")
            else:
                print_msg(1, "File is not valid PE")
                time.sleep(2)



def print_eq_sections(in_file, flag=True, section_name=""):
    if not in_file:
        print_msg(-1, "File is't exist")
        return

    sample = pefile.PE(in_file)
    for section in sample.sections:
        if (section.Misc_VirtualSize == section.SizeOfRawData) and (section_name in section.Name):
            sys.stdout.write(magenta("Name: %0s" % section.Name + "\tRawSize = 0x%08x" % section.SizeOfRawData))
            sys.stdout.write(magenta("\tVirtualSize = 0x%08x" % section.Misc_VirtualSize))
            sys.stdout.write(magenta("\tEntropy = %02d" % section.get_entropy() + "\n"))
        elif flag == False:
            print_msg(1, "No sections with equal RSize and VSize")
        elif flag == True:
            sys.stdout.write(blue("Name: %0s" % section.Name + "\tRawSize = 0x%08x" % section.SizeOfRawData))
            sys.stdout.write(blue("\tVirtualSize = 0x%08x" % section.Misc_VirtualSize))
            sys.stdout.write(blue("\tEntropy = %02d" % section.get_entropy() + "\n"))



def is_pe_file(in_file):
    readed_file = open(in_file, 'r')
    if readed_file.read(2) == 'MZ':
        return 1
    else:
        return 0



def print_msg(code, msg):
    if code == -1:
        print red("[ERROR]\t" + msg)
    elif code == 1:
        print yellow("[WARNING]\t"+msg)
    else:
        print green("[INFO]\t" + msg)


def usage(module_name):
    print 'Usage: ' + module_name + " <folder_with_pe_files>"


if __name__ == '__main__':
    main()
