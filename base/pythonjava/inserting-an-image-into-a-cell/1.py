import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat

# ported code here
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Get the target cell C6
cell = worksheet.getCells().get("C6")

# Read the image file into a byte array
imageData = open("logo.png", "rb").read()

# Embed the image directly into the cell
cell.setEmbeddedImage(imageData)

# Optionally adjust row height and column width so the embedded image is more visible
worksheet.getCells().setColumnWidth(2, 30)   # Column C (index 2)
worksheet.getCells().setRowHeight(5, 100)    # Row 6 (index 5)

# Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", SaveFormat.Xlsx)

jpype.shutdownJVM()