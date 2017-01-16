# -*- coding: utf-8 -*-

"""
Created on Fri Jan 13 11:11:14 2017

This is a sdf renamer, it takes a list of sdf, and then for each
sdf entry change the sdf title to contain the the name of the sdf

This is a true alpha,
it is has not undergone testing and been written the JCW as for a problem
with maestro

@author: holmes

Thing to do:
refactor code
test code


Please note: DO NOT USE, SPEAK TO AJH FIRST, use at own risk.

"""

def main(a_raw_data, a_out_file):
    """
    main running file
    @oara a_raw_data this is the raw data_location
    @return a_out_file this will return the return list
    """

    # Used for testing
    #a_raw_data = "xxx.sdf"

    def opener(a_file_name):
        """
        This function opens the file and extracts the data
        @para a_file this is the file location
        @return unprocessed_data this returns the unprocessed data as a list
        """
        file1 = open(a_file_name, 'r')

        unprocessed_data = file1.read()
        file1.close()

        return unprocessed_data

    ### access the file and extracts data
    output_file = opener(a_raw_data)
    output_file = output_file.split("$$$$")
    temp_string = output_file[0]
    temp_string = str("\n") + temp_string
    output_file[0] = temp_string
    ##

    def sdf_title_renamer(a_sdf_entry):
        """
        the open the sdf entry and then then makes a new line which is lines
        1 and 2 into one line, this then replace line 1 with the new line
        and returns the list
        @para a_sdf_entry this is sdf entry
        @return joined edited entry
        """
        a_sdf_entry = a_sdf_entry.split("\n")
        temp_entry = a_sdf_entry[2].split()
        new_entry = str(a_sdf_entry[1]) + str(" ")+ str(temp_entry[0])
        a_sdf_entry[1] = new_entry
        a_sdf_entry[-1] = "$$$$"
        joined = ''

        for element in a_sdf_entry:
            if "$$$$"  in element:
                joined = joined + str(element)
            else:
                joined = joined + str(element) + "\n"

        print (joined)
        return joined

    def out_put_list(a_output_file, a_out_put_sdf):
        """
        this returns the this take the raw_list opens it then runs
        sdf_title_rename, the adds it to a new title
        @para a_out_file this is the output_file
        @return a_out_put_sdf this is the output sdf
        """
        for element in a_output_file:
            if(len(element) < 2):
                print ("\n\n*** Caution: empty entry found, possible empty entry at the end of file ***\n\n")
            else:
                renamed = sdf_title_renamer(element)
                a_out_put_sdf.append(renamed)
            pass
        return

    ## this rames the file then removes new line
    out_put_sdf = []
    out_put_list(output_file, out_put_sdf)
    temp_string = out_put_sdf[0]
    temp_string = temp_string[1:]
    out_put_sdf[0] = temp_string
    ##

    #this is used for testing
    ##a_out_file = "xxx.sdf"

    def out_putter(a_file_name, a_data):
        """
        this opens the the output sdf then outputs this data into a file
        @para a_file_name this is the file name, location
        @return a_data this returns the data
        """
        a_file = open(a_file_name, 'w')
        a_file.writelines(a_data)
        a_file.close()

        return

    out_putter(a_out_file, out_put_sdf)

    print ("######\nScript Has Run\n#####")

    return

##########

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=str, help="input file name")
parser.add_argument("output_file", type=str, help="output file name")
args = parser.parse_args()

print (args.input_file)
print (args.output_file)

file_info = args.input_file
file_out = args.output_file

#file_info = "C4X_6003_ensemble4D_08Oct13.sdf"
#file_out = "C4X_6003_ensemble4D_08Oct13_rename.sdf"

#file_info = input ("please input file location: ")
#file_out = input("please input file out put location: ")

main(file_info, file_out)
