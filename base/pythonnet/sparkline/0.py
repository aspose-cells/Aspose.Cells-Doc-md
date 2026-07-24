import aspose.cells as ac
import System.Drawing

# Step 1: Create a Workbook and get the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells

# Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells["A1"].put_value(5)
cells["B1"].put_value(-3)
cells["C1"].put_value(8)
cells["D1"].put_value(-2)
cells["E1"].put_value(6)

# Step 3: Build a CellArea pointing to destination cell F1
dest = ac.CellArea()
dest.start_column = 5   # column F (0-indexed)
dest.end_column = 5
dest.start_row = 0      # row 1 (0-indexed)
dest.end_row = 0

# Step 4: Add a Line sparkline from A1:E1 into F1
# SparklineGroups.Add returns the index of the newly added group
index = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, dest)
group = worksheet.sparkline_groups[index]

# Step 5: Create a red CellsColor and assign it to the sparkline line color
red = workbook.create_cells_color()
red.color = System.Drawing.Color.Red
group.series_color = red

# Step 6: Enable high-point and low-point markers
group.show_high_point = True
group.show_low_point = True

# Step 7: Save the workbook
workbook.save("output_line.xlsx")