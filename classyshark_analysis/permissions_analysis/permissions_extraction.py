# -*- coding: utf-8 -*-
"""xml_parsing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10sJN_RG6i--6rTMwWtD8vLonHqDD5PGQ
"""

# This is a module that Python has to work with CSVs. Have this at the beginning of the script, even if you need CSV functionality at the end. 
import csv

# This code opens the xml file which has been renamed from AndroidManifest.xml_dumpto AndroidManifest.xml. For this to work, both the XML file and this script need to be in the same folder. Otherwise, you'll need to include the approprate path in the brackets. Because this is Google Collab, you should be able to drop your XML file (AndroidManifest.xml) into the "sample data" folder. Just drag or hover and click the option to upload.
# The 'r' in the code below stands for read only, meaning that you cannot write in this XML file. You're just bringing the file in, i.e., loading it. The 'r' is more of an instruction. It's not acting yet in the way it is in the next line. 
androidmanifestfile = open('AndroidManifest.xml', 'r')

# Lines is a variable that is pulling in every line of the XML file. This part is actually reading our AndroidManifest.xml file. 
Lines = androidmanifestfile.readlines()

# add is setting up our search. 'add' initializes the script. This is not actually doing anything yet. 
countLines = 0
add=False

# We are setting up a list for the permissions we extract. 
mylist = []
totalC=0

# We are setting up a list for the permissions we extract. 
mylist = []

# We are starting at 0 for our lines (initializing to 0). 
totalC=0

# We are going through our XML file line by line. We have scrapped the hierarchy and are just searching for <uses-permission, i.e., the tag in the XMl file that we're interested in. This is not capturing the other permissions tag. Modify code to include other permissions tag, if desired.
for line in Lines:
    countLines += 1
    line2=("{}".format(line.strip()))
# We tell our script the format for what it will parse out. 
    if add == True:
        print("Line{}: {}".format(countLines, line.strip()))
        mylist.append("{}".format(line.strip()))
# We tell our script that we're specifically looking for the line after the <uses-permission tag. 
    if line2 == "<uses-permission":
        add = True
        totalC+=1
# Otherwise, we ignore the line and move on. 
    else:
        add = False

# This prints the total number of permissions identified and extracted. 
print (totalC)

# This is a check that notes that you're printing the list of permissions. 
print ("This is my list:")

# This code prints the list of permissions extracted from the XML file. 
print (mylist)

# This line creates a CSV file called 'permissions.'
fileCSV = open('permissions.csv', 'w+', newline ='')

# This code writes the data into the CSV file. 
with fileCSV:   
    write = csv.writer(fileCSV, delimiter = ',')
    write.writerows(mylist)

# The output automatically adds commas between each character. This code removes commas. 
with open("permissions.csv") as infile, open("permissionsfirstversion.csv", "w") as outfile:
    for line in infile:
        outfile.write(line.replace(",", ""))

# This code removes the 'name =' part of the permission line so that we're just left with the permission. 
with open("permissionsfirstversion.csv") as infile, open("permissionssecondversion.csv", "w") as outfile:
    for line in infile:
        outfile.write(line.replace("name=", ""))