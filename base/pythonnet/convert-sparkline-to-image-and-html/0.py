import aspose.cells as ac

# Create a new workbook and access the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Populate sample data in cells A1:E1
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# Add a Line sparkline group anchored at F1 (column 5, row 0)
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)

# Add a Column sparkline group anchored at G1 (column 6, row 0)
column_area = ac.CellArea()
column_area.start_column = 6
column_area.end_column = 6
column_area.start_row = 0
column_area.end_row = 0
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)

# Add a Win/Loss (Stacked) sparkline group anchored at H1 (column 7, row 0)
stacked_area = ac.CellArea()
stacked_area.start_column = 7
stacked_area.end_column = 7
stacked_area.start_row = 0
stacked_area.end_row = 0
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)

# Configure image options for PNG output
image_options = ac.ImageOrPrintOptions()
image_options.image_type = ac.ImageType.PNG

# Convert the Line sparkline to image and embed it in cell F2
line_sp = worksheet.sparkline_groups[line_idx].sparklines[0]
ms = ac.MemoryStream()
line_sp.to_image(ms, image_options)
worksheet.cells["F2"].embedded_image = ms.to_array()

# Convert the Column sparkline to image and embed it in cell G2
column_sp = worksheet.sparkline_groups[column_idx].sparklines[0]
ms = ac.MemoryStream()
column_sp.to_image(ms, image_options)
worksheet.cells["G2"].embedded_image = ms.to_array()

# Convert the Win/Loss sparkline to image and embed it in cell H2
stacked_sp = worksheet.sparkline_groups[stacked_idx].sparklines[0]
ms = ac.MemoryStream()
stacked_sp.to_image(ms, image_options)
worksheet.cells["H2"].embedded_image = ms.to_array()

# Save the workbook to disk
workbook.save("output_with_sparklines.xlsx")