import aspose.cells as ac

# Create a new workbook
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# Populate Fruit/Year/Amount data
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
]

for r in range(len(data)):
    for c in range(len(data[r])):
        sheet.cells[r + 1, c].put_value(data[r][c])

# Create pivot table at E3
pivot_tables = sheet.pivot_tables
index = pivot_tables.add("=A1:C7", "E3", "PivotTable1")
pivot_table = pivot_tables[index]

# Configure pivot fields: Fruit→Row, Amount→Data, Year→Page
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.Page, "Year")

pivot_table.refresh_data()
pivot_table.calculate_data()

# Clear the page filter so every item in the page field is visible.
# 0x7FFD (decimal 32765) is the special sentinel value that means "all items" —
# equivalent to selecting "(All)" in Excel's page-field dropdown.
pivot_table.page_fields[0].current_page_item = 0x7FFD

workbook.save("output.xlsx")