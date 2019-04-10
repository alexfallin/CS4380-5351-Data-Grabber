import sys

if len(sys.argv) != 2 :
    print ("Usage is 'python getdata.py [filename]")
    sys.exit()

readFile = open(sys.argv[1], 'r')

print ("Pulling data from " + sys.argv[1] + " and saving it to outputTable.csv")

line = readFile.readline()
line.strip()

rows = 0
thread_indicator = 0
data = []

while line != "":

    if line[:7] == "threads" and thread_indicator != -1:
        if thread_indicator == 0:
            thread_indicator = int(line[9:])
        elif thread_indicator == int(line[9:]):
            rows += 1
            thread_indicator =-1
        else:
            rows += 1
    elif line[:12] == "compute time":
        data.append(line[14:-3])

    line = readFile.readline()
    line.strip()

readFile.close()

columns = len(data) / rows

transposeData = [[0 for column in range(columns)] for row in range(rows)]
dataItem = 0
for column in range(columns):
    for row in range(rows):
        transposeData[row][column] = data[dataItem]
        dataItem += 1

writeFile = open('outputTable.csv', 'wb')

for row in range(rows):
    for column in range(columns):
        writeFile.write(str(transposeData[row][column]) + ", ")
    writeFile.write('\n')

writeFile.close()

print ("Done.")

