import aspose.cells as ac

# Create a new workbook
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

# Set up the header row
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Populate 9 rows of sample data: Fruit, Year, Amount
data = [
    ["apple", 2020, 100],
    ["banana", 2021, 200],
    ["apple", 2021, 150],
    ["grape", 2020, 120],
    ["orange", 2022, 180],
    ["banana", 2020, 90],
    ["grape", 2021, 130],
    ["apple", 2022, 170],
    ["orange", 2021, 110]
]

for i in range(len(data)):
    worksheet.cells[i + 1, 0].put_value(data[i][0])
    worksheet.cells[i + 1, 1].put_value(data[i][1])
    worksheet.cells[i + 1, 2].put_value(data[i][2])

# Add a pivot table anchored at cell E3
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Add fields to their areas: Fruit as Row, Amount as Data, Year as Page field
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.Page, "Year")

# Refresh and calculate the pivot table data
pivot_table.refresh_data()
pivot_table.calculate_data()

# Save the workbook
workbook.save("pageFieldSample.xlsx")