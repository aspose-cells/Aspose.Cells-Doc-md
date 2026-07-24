import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat

# Define the data directory and file paths
dataDir = "data/"
sourcePath = dataDir + "book1.xls"
outputPath = dataDir + "outputrange.xls"

# Open the source Excel file
sourceWorkbook = Workbook(sourcePath)

# Get the first worksheet from the source workbook
sourceWorksheet = sourceWorkbook.getWorksheets().get(0)

# Define the source cell range A1:C10 (10 rows, 3 columns starting at row 0, col 0)
sourceRange = sourceWorksheet.getCells().createRange(0, 0, 10, 3)

# Create a new destination workbook
destWorkbook = Workbook()

# Access the first worksheet in the destination workbook
destWorksheet = destWorkbook.getWorksheets().get(0)

# Create the destination range at A1 with the same dimensions as the source range
destRange = destWorksheet.getCells().createRange(0, 0, 10, 3)

# Copy the source range to the destination range
destRange.copy(sourceRange)

# Save the destination workbook to a new .xls file
destWorkbook.save(outputPath, SaveFormat.Excel97To2003)

jpype.shutdownJVM()