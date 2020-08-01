import csv

# Build an empty list to hold menu items
menu = []

# Open and read through each line of csv, appending row to menu list
with open ("Resources/menu_data.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader)
    for i in reader:
        menu.append(i)

# Build an empty list to contain sales, appending row to sales list
sales = []

# Open and read through each line of csv
with open ("Resources/sales_data.csv") as csv_sales_file:
    reader2 = csv.reader(csv_sales_file, delimiter = ',')
    header2 = next(reader2)
    for i in reader2:
        sales.append(i)

# Initialize a report dictionary
report = {}
nested_dic = {
"01-count": 0,
"02-revenue": 0,
"03-cogs": 0,
"04-profit": 0,
}
for i in sales:
    quantity = i[3]
    sales_item = i[4]
    if sales_item not in report:
        report[sales_item] = nested_dic
    else:
        for i in menu:
            item = i[0]
            Price = i[3]
            Cost = i[4]
            if sales_item == item:
                report[sales_item]["01-count"] += quantity
                report[sales_item]["02-revenue"] += price * quantity
                report[sales_item]["03-cogs"] += cost * quantity
                report[sales_item]["04-profit"] += profit * quantity
print(report)


