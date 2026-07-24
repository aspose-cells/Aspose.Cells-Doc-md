import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, SparklineType
from java.awt import Color

# Step 1: Create a Workbook and get the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()

# Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells.get("A1").putValue(5)
cells.get("B1").putValue(-3)
cells.get("C1").putValue(8)
cells.get("D1").putValue(-2)
cells.get("E1").putValue(6)

# Step 3: Build a CellArea pointing to destination cell F1
dest = CellArea()
dest.setStartColumn(5)  # column F (0-indexed)
dest.setEndColumn(5)
dest.setStartRow(0)     # row 1 (0-indexed)
dest.setEndRow(0)

# Step 4: Add a Line sparkline from A1:E1 into F1
# SparklineGroups.add returns the index of the newly added group
index = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(index)

# Step 5: Create a red CellsColor and assign it to the sparkline line color
red = workbook.createCellsColor()
red.setColor(Color.RED)
group.setSeriesColor(red)

# Step 6: Enable high-point and low-point markers
group.setShowHighPoint(True)
group.setShowLowPoint(True)

# Step 7: Save the workbook
workbook.save("output_line.xlsx")

jpype.shutdownJVM()