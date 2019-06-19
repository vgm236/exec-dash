# dashboard_generator.py

import os.path # helps to save in a different folder
import pandas as pd
import itertools
import locale # from https://stackoverflow.com/Questions/320929/currency-formatting-in-python
from os import listdir
from os.path import isfile, join

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
selected_month = input("Please input a month (Example 01 -- for January = ): ")

# FILE SELECTED

file_name = "sales-" + selected_year + selected_month + ".csv"
while not os.path.exists(file_name):
    print("---------------------------------------------------------------------")
    print("\n")
    print("The file selected do not exist. Please try again")
    print("\n")
    print("---------------------------------------------------------------------")
    exit()

# OPENING SPECIFIC FILE

find_file = os.path.join(save_path, file_name) #find the file

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

print("---------------------------------------------------------------------")

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