from sys import argv, exit
import csv


# Check for command-line args
if len(argv) != 3:
    print("Error")
    exit(1)

# Open the csv file with the data
database = open(argv[1], "r")
if (database == None):
    exit(2)

# Open the csv file with the format
formatdata = open(argv[2], "r")
if (formatdata == None):
    exit(3)

# Answer Sheet
file = open('Income Statement Ans.csv', 'w', newline="")
if (file == None):
    exit(4)

csvReader = csv.DictReader(database)
formatReader = csv.DictReader(formatdata)
fieldnames = ['Details','1','2','3']
csvWriter = csv.DictWriter(file, fieldnames=fieldnames)

csvWriter.writeheader()

# Prompt for FC, VC and price
closedInventory = int(input("Enter closed inventory: "))


salesReturnsExists = False
for row in csvReader:

    # Store Revenue
    if row['Details'] == "Revenue":
        revenue = row['1']
    if row['Details'] == "Sales returns" or row['Details'] == "Returns inwards":
        salesReturns = row['1']
        salesReturnsExists = True


for row in formatReader:
    writeRow = True
    if row['Details'] == "Revenue":
        row['3'] = revenue
    if row['Details'] == "Less:Sales returns":
        if  salesReturnsExists == True:
            row['3'] = salesReturns
            print("yes")
        else: 
            writeRow = False

    if writeRow == True:
        csvWriter.writerow(row)


# Close files
database.close()
file.close()
