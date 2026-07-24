import aspose.cells as ac

# Step 1: Create a Workbook and get the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Step 2: Write sample values into A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.cells[0, i].put_value(values[i])

# Step 3: Build a CellArea pointing to F1 (column index 5, row index 0)
dest = ac.CellArea()
dest.start_column = 5
dest.end_column = 5
dest.start_row = 0
dest.end_row = 0

# Step 4: Add a Column sparkline to the destination cell
idx = worksheet.sparkline_groups.add(
    ac.SparklineType.COLUMN, "A1:E1", False, dest)
group = worksheet.sparkline_groups[idx]

# Step 5: Confirm the sparkline type by reading group.Type
print("Sparkline Type added: " + str(group.type))

# Step 6: Save the workbook
workbook.save("output_column.xlsx")

print("Workbook saved as output_column.xlsx")