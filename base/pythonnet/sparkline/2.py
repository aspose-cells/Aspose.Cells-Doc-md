import aspose.cells as ac
import System.Drawing

# Step 1: Create a Workbook and get the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "WinLoss"

# Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# Step 3: Build a CellArea pointing to F1 (column 5, row 0)
dest = ac.CellArea()
dest.start_column = 5   # F
dest.end_column = 5
dest.start_row = 0      # row 1
dest.end_row = 0

# Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
group_index = worksheet.sparkline_groups.add(
    ac.SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.sparkline_groups[group_index]

# Step 5: Customize the sparkline group
# Enable high-point and low-point markers
group.show_high_point = True
group.show_low_point = True
group.show_negative_points = True

# Set the high-point color to green
high_color = workbook.create_cells_color()
high_color.color = System.Drawing.Color.Green
group.high_point_color = high_color

# Set the low-point color to red
low_color = workbook.create_cells_color()
low_color.color = System.Drawing.Color.Red
group.low_point_color = low_color

# Set the negative-point color to orange
neg_color = workbook.create_cells_color()
neg_color.color = System.Drawing.Color.Orange
group.negative_points_color = neg_color

# Set the default series color (used for positive bars)
series_color = workbook.create_cells_color()
series_color.color = System.Drawing.Color.SteelBlue
group.series_color = series_color

# Step 6: Save the workbook
workbook.save("output_winloss.xlsx")

print("Workbook saved successfully: output_winloss.xlsx")