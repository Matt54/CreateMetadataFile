'''
    File name: CreateMetadataFile.py
    Author: Matt Pfeiffer
    Date created: 1/27/2020
    Python Version: 3.8
'''

import os
import csv

#dataDirectory is your top-level directory name for the data files
#change this according to your folder name/path
dataDirectory = 'CategorizedData'

#Creates Metadata.cvs file in same directory as .py file
with open('Metadata.csv','w',newline='\n') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    #Creates Column Titles
    filewriter.writerow(['filename', 'class_type'])

    #Loops through the data directory
    for subdir, dirs, files in os.walk(dataDirectory):

        numFiles = 0

        #filter out any files not stored in a classes sub-directory
        if subdir != dataDirectory:

            #Loops through each file
            for file in files:
                
                numFiles += 1
                
                #column 1 - populated with the file name
                #column 2 - populated with the sub-directory name (named after the class_type)
                filewriter.writerow([file, os.path.basename(subdir)])
                
            print('files found in ' + os.path.basename(subdir) + ': ' + str(numFiles))

            
            
        
