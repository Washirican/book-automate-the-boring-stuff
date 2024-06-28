# !/usr/bin/env python3
import openpyxl

wb = openpyxl.load_workbook('automate_online-materials\\produceSales.xlsx')
sheet = wb.active

n = 7 # Insert row before this row
m = 2 # Insert m-rows

for i in range(1, m + 1):
    sheet.insert_rows(n)

wb.save('automate_online-materials\\my_produceSales_row_inserter.xlsx')