# This is a module that Python has to work with CSVs. Have this at the beginning of the script, even if you need CSV functionality at the end. 
import csv

# This code opens the CSV file all_methods which is downloaded from the Android package opened using ClassyShark. 
SDKfile = open('all_methods.csv', 'r')

# Lines is a variable that is pulling in every line of the CSV file. This part is actually reading our CSV file. 
lines = SDKfile.readlines()

# countLines isn't necessary for looping through our CSV file. It just considers what line we are on in the file. This is likely irrelevant for the purpose of this script, but I've included it in case it's useful. 
countLines = 0

# add is setting up our search. 'add' is initializes the script. This is not actually doing anything yet (just set-up). 
add=False

# Set up the list. 
mylist = []
totalC=0
row=""
 
# Check for every line that has the term 'sdk' and pull it out. 
for line in lines: 
    if 'sdk' in line:
        #print(line)
        mylist.append([line])
        totalC+=1
    else: 
        add = False

# Print the list (i.e., list of lines with 'sdk' in them)
print (mylist)

# Print the total number of lines with 'sdk' in them 
print (totalC)

# Create and export the list of SDKs into a new file 
fileCSV = open('SDK_list.csv', 'w+', newline ='')
 
with fileCSV:   
   write = csv.writer(fileCSV, delimiter = ',')
   write.writerows(mylist)


