import sys

if len(sys.argv) != 3 :
    print ("Usage is 'python getdata.py [filename] [items per column]")
    sys.exit()

readFile = open(sys.argv[1], 'r')

print ("Pulling data from " + sys.argv[1] + " and saving it to outputTable.csv")

line = readFile.readline()
line.strip()

data = []

counter = 0
rows = int(sys.argv[2])
columns = 0

while line != "":
    if line[0:12] == "compute time":
        data.append(line[14:-3])
        counter += 1
        if counter % rows == 0:
            # data.append("\n")
            columns += 1

    line = readFile.readline()
    line.strip()

readFile.close()

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

