import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Get the target cell C6
cell = worksheet.cells["C6"]

# Read the image file into a byte array
with open("logo.png", "rb") as f:
    imageData = f.read()

# Embed the image directly into the cell
cell.embedded_image = imageData

# Optionally adjust row height and column width so the embedded image is more visible
worksheet.cells.set_column_width(2, 30)   # Column C (index 2)
worksheet.cells.set_row_height(5, 100)     # Row 6 (index 5)

# Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", ac.SaveFormat.XLSX)