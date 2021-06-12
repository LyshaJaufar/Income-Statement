from sys import argv, exit
import re, csv

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
closingInventory = int(input("Enter closed inventory: "))
additionalIncomes= False
additionalExpenses = False
askAdditionalIncomes = input("Do you wish to add anything extra to your incomes? ")
askAdditionalTradeExpenses = input("Do you wish to deduct anything extra to your incomes? ")
if re.search("y(es)?", askAdditionalIncomes, re.IGNORECASE):
    addAdditionalIncomes = True
if re.search("y(es)?", askAdditionalTradeExpenses, re.IGNORECASE):
    additionalExpenses = True

salesReturnsExists = False
carriageInwardsExists = False
airFreightChargesExists = False
customsDutyExists = False
repackagingWagesExists = False
purchaseReturnsExists = False
goodsDrawingsExists = False
discountReceivedExists = False
interestReceivedExists = False
rentReceievedExists = False
financeIncomeExists = False
commissionReceivedExists = False

salariesAndWagesExists = False
carriageOutwardsExists = False
insuranceExists = False
interestExists = False
rentAndRatesExists = False
discountAllowedExists = False
motorExpensesExists = False
rentExists = False
badDebtExists = False
generalExpensesExists = False
postageExists = False
depreciationExists = False
otherOperatingExpensesExists = False
telephoneExists = False
heatingAndLightingExists = False

expenses = 0
income = 0
for row in csvReader:
    # Store values
    if re.search("revenue", row['Details'], re.IGNORECASE):
        revenue = int(row['1'])
        netRevenue = revenue

    if re.search("return(s)? inwards", row['Details'], re.IGNORECASE):
        salesReturns = row['1']
        netRevenue = revenue - int(row['1'])
        salesReturnsExists = True
    
    if re.search("sales returns", row['Details'], re.IGNORECASE):
        salesReturns = row['1']
        netRevenue = revenue - int(row['1'])
        salesReturnsExists = True

    if re.search("inventory", row['Details'], re.IGNORECASE):
        openingInventory = int(row['1'])

    if re.search("purchases", row['Details'], re.IGNORECASE):
        purchases = int(row['1'])
        netPurchases = purchases
        finalNetPurchases = netPurchases

    if re.search("carriage inwards", row['Details'], re.IGNORECASE):
        carriageInwards = int(row['1'])
        carriageInwardsExists = True
        netPurchases += carriageInwards
        finalNetPurchases = netPurchases

    if re.search("air frieght charges", row['Details'], re.IGNORECASE):
        airFreightCharges = int(row['1'])
        airFrieghtChargesExists = True
        netPurchases += airFreightCharges
        finalNetPurchases = netPurchases

    if re.search("customs duty", row['Details'], re.IGNORECASE):
        customsDuty = int(row['1'])
        customsDutyExists = True
        netPurchases += customsDuty
        finalNetPurchases = netPurchases

    if re.search("repackaging wages", row['Details'], re.IGNORECASE):
        repackagingWages = int(row['1'])
        repackagingWagesExists = True
        netPurchases += repackagingWages
        finalNetPurchases = netPurchases

    if re.search("purchase returns", row['Details'], re.IGNORECASE):
        purchaseReturns = int(row['1'])
        purchaseReturnsExists = True
        finalNetPurchases -= purchaseReturns

    if re.search("return(s)? outwards", row['Details'], re.IGNORECASE):
        purchaseReturns = int(row['1'])
        purchaseReturnsExists = True
        finalNetPurchases -= purchaseReturns

    if re.search("goods drawings", row['Details'], re.IGNORECASE):
        goodsDrawings = int(row['1'])
        goodsDrawingsExists = True
        finalNetPurchases -= goodsDrawings

    # Incomes           
    if re.search("discount received", row['Details'], re.IGNORECASE):
        discountReceived = int(row['2'])
        discountReceivedExists = True
        income += discountReceived

    if re.search("Interest received", row['Details'], re.IGNORECASE):
        interestReceived = int(row['2'])
        interestReceivedExists = True
        income += interestReceived

    if re.search("rent received", row['Details'], re.IGNORECASE):
        rentReceived = int(row['2'])
        renttReceivedExists = True
        income += rentReceived

    if re.search("finance income", row['Details'], re.IGNORECASE):
        financeIncome = int(row['2'])
        financeIncomeExists = True
        income += financeIncome

    if re.search("commission received", row['Details'], re.IGNORECASE):
        commissionReceived = int(row['2'])
        commissionReceivedExists = True
        income += commissionReceived

    # Expenses
    if re.search("carriage outwards", row['Details'], re.IGNORECASE):
        carriageOutwards = int(row['2'])
        carriageOutwardsExists = True
        expenses += carriageOutwards

    if re.search("rent and rates", row['Details'], re.IGNORECASE):
        rentAndRates = int(row['2'])
        rentAndRatesExists = True
        expenses += rentAndRates

    if re.search("discount allowed", row['Details'], re.IGNORECASE):
        discountAllowed = int(row['2'])
        discountAllowedExists = True
        expenses += discountAllowed

    if ("insurance", row['Details'], re.IGNORECASE):
        insurance = int(row['2'])
        insuranceExists = True
        expenses += insurance

    if ("rent", row['Details'], re.IGNORECASE):
        rent = int(row['2'])
        rentExists = True
        expenses += rent

    if ("interest", row['Details'], re.IGNORECASE):
        interest = int(row['2'])
        interestExists = True
        expenses += interest

    if re.search("other operating expenses", row['Details'], re.IGNORECASE):
        otherOperatingExpenses = int(row['2'])
        otherOperatingExpensesExists = True
        expenses += otherOperatingExpenses

    if re.search("heating and lighting", row['Details'], re.IGNORECASE):
        heatingAndLighting = int(row['2'])
        heatingAndLightingExists = True
        expenses += heatingAndLighting

    if re.search("bad debts", row['Details'], re.IGNORECASE):
        badDebts = int(row['2'])
        badDebtsExists = True
        expenses += badDebts

    if re.search("postage", row['Details'], re.IGNORECASE):
        postage = int(row['2'])
        postageExists = True
        expenses += postage

    if re.search("general expenses", row['Details'], re.IGNORECASE):
        generalExpenses = int(row['2'])
        generalExpensesExists = True
        expenses += generalExpenses

    if re.search("telephone expenses", row['Details'], re.IGNORECASE):
        telephoneExpenses = int(row['2'])
        telephoneExpensesExists = True
        expenses += telephoneExpenses

    if re.search("motor expenses", row['Details'], re.IGNORECASE):
        motorExpenses = int(row['2'])
        motorExpensesExists = True
        expenses += motorExpenses

    if re.search("salaries and wages", row['Details'], re.IGNORECASE):
        salariesAndWages = int(row['2'])
        salariesAndWagesExists = True
        expenses += salariesAndWages

    if re.search("depreciation", row['Details'], re.IGNORECASE):
        depreciation = int(row['2'])
        depreciationExists = True
        expenses += depreciation


print("Income: ", income)
print("Expenses: ", expenses)

for row in formatReader:
    writeRow = True
    
    # Trading Section
    if row['Details'] == "Revenue":
        row['3'] = revenue

    if row['Details'] == "Less:Sales returns":
        if  salesReturnsExists == True:
            row['3'] = salesReturns
        else: 
            writeRow = False

    if row['Details'] == "Net Revenue":
        row['3'] = netRevenue
    
    if row['Details'] == "Opening inventory":
        row['2'] = openingInventory

    if row['Details'] == 'Add: Purchases':
        row['1'] = purchases

    if row['Details'] == 'Add: Carriage inwards':
        if carriageInwardsExists == True:
            row['1'] = carriageInwards
        else:
            writeRow = False

    if row['Details'] == "Add: Air freight charges":
        if  airFreightChargesExists == True:
            row['1'] = airFreightCharges
        else: 
            writeRow = False

    if row['Details'] == "Add: Customs Duty":
        if  customsDutyExists == True:
            row['1'] = customsDuty
        else: 
            writeRow = False

    if row['Details'] == "Net purchases":
        row['1'] = netPurchases

    if row['Details'] == "Less: Purchase returns":
        if  purchaseReturnsExists == True:
            row['1'] = purchaseReturns
        else: 
            writeRow = False

    if row['Details'] == "Less: Goods drawings":
        if  goodsDrawingsExists == True:
            row['1'] = goodsDrawings
        else: 
            writeRow = False

    if purchaseReturns == True:
        if goodsDrawingsExists == False:
            if row['Details'] == "Less: Purchase returns":
                row['2'] = finalNetPurchases     

    if purchaseReturns == False:
        if goodsDrawingsExists == True:
            if row['Details'] == "Less: Goods drawings":
                row['2'] = finalNetPurchases
        if goodsDrawingsExists == False:
            if row['Details'] == "Net purchases":
                row['2'] = finalNetPurchases        

    if goodsDrawingsExists == True:
        if purchaseReturnsExists == True: 
            if row['Details'] == "Less: Goods drawings":
                row['2'] = finalNetPurchases
        if purchaseReturnsExists == False: 
            if row['Details'] == "Less: Goods drawings":
                row['2'] = finalNetPurchases

    if goodsDrawingsExists == False:
        if purchaseReturnsExists == True: 
            if row['Details'] == "Less: Purchase returns":
                row['2'] = finalNetPurchases

    if row['Details'] == "Cost of sales":
        costOfSales = int(finalNetPurchases) + int(openingInventory)
        row['2'] = costOfSales

    if row['Details'] == "Less: Closing inventory":
        row['2'] = closingInventory
        salesCostMinusCI = costOfSales - closingInventory
        row['3'] = salesCostMinusCI

    if row['Details'] == "Gross Profit":
        grossProfit = int(netRevenue) - int(salesCostMinusCI)
        row['3'] = grossProfit

    # Incomes
    if row['Details'] == "Discount received":
        if discountReceivedExists == True:
            row['2'] = discountReceived 
        else:
            writeRow = False
    
    if row['Details'] == "Interest received":
        if interestReceivedExists == True:
            row['2'] = interestReceived 
        else:
            writeRow = False
        
    if row['Details'] == "Rent received":
        if rentReceievedExists == True:
            row['2'] = rentReceived 
        else:
            writeRow = False

    if row['Details'] == "Finance income":
        if financeIncomeExists == True:
            row['2'] = financeIncome 
        else:
            writeRow = False

    if row['Details'] == "Commission received":
        if commissionReceivedExists == True:
            row['2'] = commissionReceived 
        else:
            writeRow = False

    if row['Details'] == "IncomeAndGP":
        row['3'] = income + grossProfit

    if writeRow == True:
        csvWriter.writerow(row)


# Close files
database.close()
file.close()
