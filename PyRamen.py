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
    quantity = int(i[3])
    sales_item = i[4]
    if sales_item not in report.keys():
        report[sales_item] = nested_dic

    for x in menu:

        item = x[0]
        price = float(x[3])
        cost = float(x[4])

        profit = price - cost

        if sales_item == item:
            x
            report[sales_item]["01-count"] += quantity
            report[sales_item]["02-revenue"] += price * quantity
            report[sales_item]["03-cogs"] += cost * quantity
            report[sales_item]["04-profit"] += profit * quantity
        else:
            pass
            # print(f"{sales_item} does not equal {item}! NO MATCH!")
print(report)

with open("report.txt", "w") as txt_file:
    for key, value in report.items():

        line = f"{key} {value}\n"
        txt_file.write(line)

