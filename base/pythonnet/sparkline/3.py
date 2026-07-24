import aspose.cells as ac
import System.Drawing

# Step 1: Create a Workbook and get the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Step 2: Populate sample data in row 1 (A1:E1)
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# Step 3: Add a Line sparkline group at F1
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)
line_group = worksheet.sparkline_groups[line_idx]

# Customize the line sparkline color via CellsColor
line_color = workbook.create_cells_color()
line_color.color = System.Drawing.Color.Blue
line_group.series_color = line_color

# Step 4: Add a Column sparkline group at F2
column_area = ac.CellArea()
column_area.start_column = 5
column_area.end_column = 5
column_area.start_row = 1
column_area.end_row = 1
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)
column_group = worksheet.sparkline_groups[column_idx]

# Customize the column sparkline series color
column_color = workbook.create_cells_color()
column_color.color = System.Drawing.Color.Green
column_group.series_color = column_color

# Step 5: Add a Win/Loss (Stacked) sparkline group at F3
stacked_area = ac.CellArea()
stacked_area.start_column = 5
stacked_area.end_column = 5
stacked_area.start_row = 2
stacked_area.end_row = 2
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)
stacked_group = worksheet.sparkline_groups[stacked_idx]

# Customize the win/loss sparkline series color
stacked_color = workbook.create_cells_color()
stacked_color.color = System.Drawing.Color.DarkOrange
stacked_group.series_color = stacked_color

# Step 6: Save the workbook
workbook.save("output_all.xlsx")