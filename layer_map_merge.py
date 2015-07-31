## Import necessary libraries
import os.path
import sys
import unittest
import filecmp

def check_args(file_list):
    if (len(file_list) < 2):
        print ("-ERROR- Please provide two files to merge")
        return 1
    for inputfile in file_list :
        if (not os.path.isfile(inputfile)):
               print ("-ERROR- File " + inputfile + " does not exist")
               return 1
    return 0


def layer_map_merge(file_list):
    if (check_args(file_list) != 0):
        print ("-ERROR- Insufficent args")
        return
    mapping_dict = {}
    for inputfile in file_list:
        print ("Reading input file " + inputfile)
        filehandle = open(inputfile,"r");
        for line in filehandle:
            #Ignore blank lines
            if not line.strip():
                continue
            #Ignore comments
            if line.startswith("#"):
                continue
            #Remove redundant white spaces
            line = ' '.join(line.split())
            # Define keys and values for mapping
            oa_layer_purpose = ' '.join(line.split()[:2])
            gds_num = ' '.join(line.split()[2:])
            mapping_dict[oa_layer_purpose]=gds_num
        filehandle.close()
    #Open and write to output file
    outputfile = open("output.txt","w");
    print ("Output file is " + os.getcwd() + "\output.txt");
    for key in sorted(mapping_dict.keys()):
        outputstring = str(key)+" "+str(mapping_dict[key])+"\n"
        outputfile.write(outputstring)
    outputfile.close()
    
        

#file_list = input("Enter a list of files to perform layer map merge:\n").split(" ")
#layer_map_merge(file_list)







        
               
        
