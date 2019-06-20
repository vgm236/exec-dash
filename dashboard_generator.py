# dashboard_generator.py

import os.path # helps to save in a different folder
import pandas as pd
import itertools
import locale # from https://stackoverflow.com/Questions/320929/currency-formatting-in-python
from os import listdir
from os.path import isfile, join

#for chart generation
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# FILES PATH

save_path = 'C:/Users/Owner/Desktop/NYU-MBA/Programming/Files/monthly-sales/data'

# INTRODUCTION

print("Select one month to report")
print("---------------------------------------------------------------------")

# LISTING FILES (sorted and in a proper list)

onlyfiles = [f for f in listdir(save_path) if isfile(join(save_path, f))] #https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
onlyfiles.sort()
print(*onlyfiles, sep = "\n") #https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/

print("---------------------------------------------------------------------")

# REPORT SELECTION

selected_year = input("Please input a year (Example 2018 -- for Year): ")
selected_month = input("Please input a month (Example 01 -- for January): ")

# FILE SELECTED

file_name = "sales-" + selected_year + selected_month + ".csv"

# OPENING SPECIFIC FILE

find_file = os.path.join(save_path, file_name) #find the file
while not os.path.exists(find_file): #correct if does not exist
    print("---------------------------------------------------------------------")
    print("\n")
    print("The file selected do not exist. Please try again")
    print("\n")
    print("---------------------------------------------------------------------")
    exit()


stats = pd.read_csv(find_file)

# PERFORMING THE SUM

total_sales =  stats["sales price"].sum()

# FORMATTING TOTAL SALES

locale.setlocale( locale.LC_ALL, '' )
total_sales_format = locale.currency(total_sales, grouping= True)

print("---------------------------------------------------------------------")


# SALES REPORT DATE
if selected_month == "01":
    month_name = "JANUARY"
if selected_month == "02":
    month_name = "FEBRUARY"
if selected_month == "03":
    month_name = "MARCH"
if selected_month == "04":
    month_name = "APRIL"
if selected_month == "05":
    month_name = "MAY"
if selected_month == "06":
    month_name = "JUNE"
if selected_month == "07":
    month_name = "JULY"
if selected_month == "08":
    month_name = "AUGUST"
if selected_month == "09":
    month_name = "SEPTEMBER"
if selected_month == "10":
    month_name = "OCTOBER"
if selected_month == "11":
    month_name = "NOVEMBER"
if selected_month == "12":
    month_name = "DECEMBER"

print("SALES REPORT " + "(" + month_name + " " + selected_year + ")")

# PRINTING TOTAL SALES

print("TOTAL SALES: " + (total_sales_format))

print("\n")

# TOP SELLING PRODUCTS

product_totals = stats.groupby(["product"]).sum()
product_totals = product_totals.sort_values("sales price", ascending=False)

top_sellers = []
rank = 1
for i, row in product_totals.iterrows():
    d = {"rank": rank, "name": row.name, "monthly_sales": row["sales price"]}
    top_sellers.append(d)
    rank = rank + 1

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

print("TOP SELLING PRODUCTS:")
for d in top_sellers:
    locale.setlocale( locale.LC_ALL, '' )
    print("  " + str(d["rank"]) + ") " + d["name"] +
          ": " + to_usd(d["monthly_sales"]))

print("\n")

print("---------------------------------------------------------------------")

print("\n")

print("GENERATING BAR CHART...")

print("\n")

print("---------------------------------------------------------------------")

### PRINT BAR CHART 

# first two lines are the list comprehensions to make a list of dictionaries into a list)

x = [p["name"] for p in top_sellers] ## VERY IMPORTANT


y = [p["monthly_sales"] for p in top_sellers] ## VERY IMPORTANT

#sorting in the correct order

x.reverse()
y.reverse()

# break charts into two

fig, ax = plt.subplots() # enables us to further customize the figure and/or the axes

#formatting chart

usd_formatter = ticker.FormatStrFormatter('$%1.0f')
ax.xaxis.set_major_formatter(usd_formatter)

# CHART GENERATION

plt.barh(x, y) 

plt.title("TOP-SELLING PRODUCTS " + "(" + month_name + " " + selected_year + ")") # AXIS TITLES
plt.ylabel('Sales (USD)') # AXIS TITLES     
plt.ylabel("Product") # AXIS TITLES

# formatting numbers

for i, v in enumerate(y):
    ax.text(v, i, usd_formatter(v), color='black', fontweight='bold')  
    
    #https://matplotlib.org/users/colors.html
    #https://matplotlib.org/3.1.0/gallery/pyplots/text_commands.html#sphx-glr-gallery-pyplots-text-commands-py

plt.tight_layout() # ensures all areas of the chart are visible by default (fixes labels getting cut off)
plt.show()

exit()

## FULL SOLUTION PROVIDED BY THE PROFESSOR

#  # this section needs to come before the chart construction

#  fig, ax = plt.subplots() # enables us to further customize the figure and/or the axes
#  usd_formatter = ticker.FormatStrFormatter('$%1.0f')
#  ax.xaxis.set_major_formatter(usd_formatter)
#  
#  # chart construction
#  plt.barh(sorted_products, sorted_sales)
#  plt.title(chart_title)
#  plt.ylabel("Product")
#  plt.xlabel("Monthly Sales (USD)")
#  
#  plt.tight_layout() # ensures all areas of the chart are visible by default (fixes labels getting cut off)
#  plt.show()