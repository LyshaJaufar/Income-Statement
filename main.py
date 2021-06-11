from sys import argv, exit
import csv


# Check for command-line args
if len(argv) != 2:
    print("Error")
    exit(1)

# Open the csv file
database = open(argv[1], "r")
if (database == None):
    exit(2)


# Answer Sheet
file = open('Income Statement Ans.csv', 'w', newline="")
if (file == None):
    exit(3)

csvReader = csv.DictReader(database)
fieldnames = ['Details','1','2','3']
csvWriter = csv.DictWriter(file, fieldnames=fieldnames)

csvWriter.writeheader()

# Prompt for FC, VC and price
closedInventory = int(input("Enter closed inventory: "))


for row in csvReader:
    # Variables for each 
    row['details'].lower == "Revenue"
    # Calculate fixed cost
    if row['1'].lower() == "":
        if row['details'].lower == "Revenue":
            revenue = 90
        print("yes")
        row['1'] = 3

    csvWriter.writerow(row)


# Close files
database.close()
file.close()
