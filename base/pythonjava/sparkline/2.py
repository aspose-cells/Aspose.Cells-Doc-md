import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, CellsColor, Color

# Step 1: Create a Workbook and get the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("WinLoss")

# Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# Step 3: Build a CellArea pointing to F1 (column 5, row 0)
dest = CellArea()
dest.setStartColumn(5)   # F
dest.setEndColumn(5)
dest.setStartRow(0)      # row 1
dest.setEndRow(0)

# Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
groupIndex = worksheet.getSparklineGroups().add(
    SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.getSparklineGroups().get(groupIndex)

# Step 5: Customize the sparkline group
# Enable high-point and low-point markers
group.setShowHighPoint(True)
group.setShowLowPoint(True)
group.setShowNegativePoints(True)

# Set the high-point color to green
highColor = workbook.createCellsColor()
highColor.setColor(Color.GREEN)
group.setHighPointColor(highColor)

# Set the low-point color to red
lowColor = workbook.createCellsColor()
lowColor.setColor(Color.RED)
group.setLowPointColor(lowColor)

# Set the negative-point color to orange
negColor = workbook.createCellsColor()
negColor.setColor(Color.ORANGE)
group.setNegativePointsColor(negColor)

# Set the default series color (used for positive bars)
seriesColor = workbook.createCellsColor()
seriesColor.setColor(Color.STEELBLUE)
group.setSeriesColor(seriesColor)

# Step 6: Save the workbook
workbook.save("output_winloss.xlsx")

print("Workbook saved successfully: output_winloss.xlsx")

jpype.shutdownJVM()