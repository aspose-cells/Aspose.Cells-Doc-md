import aspose.cells as ac
import os

# Define the data directory and file paths
dataDir = "data/"
sourcePath = os.path.join(dataDir, "book1.xls")
outputPath = os.path.join(dataDir, "outputrange.xls")

# Open the source Excel file
sourceWorkbook = ac.Workbook(sourcePath)

# Get the first worksheet from the source workbook
sourceWorksheet = sourceWorkbook.worksheets[0]

# Define the source cell range A1:C10 (10 rows, 3 columns starting at row 0, col 0)
sourceRange = sourceWorksheet.cells.create_range(0, 0, 10, 3)

# Create a new destination workbook
destWorkbook = ac.Workbook()

# Access the first worksheet in the destination workbook
destWorksheet = destWorkbook.worksheets[0]

# Create the destination range at A1 with the same dimensions as the source range
destRange = destWorksheet.cells.create_range(0, 0, 10, 3)

# Copy the source range to the destination range
destRange.copy(sourceRange)

# Save the destination workbook to a new .xls file
destWorkbook.save(outputPath, ac.SaveFormat.EXCEL97_TO2003)