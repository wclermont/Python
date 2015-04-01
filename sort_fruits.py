# Coder: Woody Clermont
# CS1101 file read and write

infile = open("unsorted_fruits.txt", "r") # read the unsorted fruits file
alines = infile.readlines() # read the contents of the file into a list called alines
blines = [] # declare blines as a list
infile.close() # close the unsorted fruits file
for i in range(len(alines)): # use a for loop to cycle through the elements of alines
    temp = alines[i].strip() # strip each element of the '\n' character
    if temp != '':
        blines.append(temp) # only add a new element to the blines list if there isn't a blank
print ('Reading unsorted_fruits.txt... your original unsorted list contains', blines, '\n')
clines = sorted(blines, key=str.lower) # create a new list clines which contains the sorted fruit list
outfile=open("sorted_fruits.txt","w") # open up a sorted fruits file to write to
for i in range(len(clines)): # use a for loop to cycle through the elements of clines
    temp = clines[i] + '\n' # add the '\n' character back to the end of each fruit
    outfile.write(temp) # write each line into the sorted fruits file one by one
outfile.close() # close the sorted fruits file
print ('Writing sorted_fruits.txt... your new sorted list contains', clines)

