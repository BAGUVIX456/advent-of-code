# Advent Of Code 2021 - Day 1 , Puzzle 1

path = "--<insert complete file location>--"     #specifies path of input file
input_file = open(path, 'r')      #opens the input file

count = 0
numi=0
numf = input_file.readline()            #to read line

while(numf != ""):
    numf = int(numf)

    if numi == 0:
        print(numf, " - no previous value")
    else:
        if numi > numf:
            print(numf," - decreases")
        else:
            print(numf, " - increases")
            count += 1
    
    numi = numf
    numf = input_file.readline()

print()
print("The required count is: ", count)



