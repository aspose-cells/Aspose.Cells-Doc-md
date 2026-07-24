import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType

# Step 1: Create a Workbook and get the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Step 2: Write sample values into A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.getCells().get(0, i).putValue(values[i])

# Step 3: Build a CellArea pointing to F1 (column index 5, row index 0)
dest = CellArea()
dest.setStartColumn(5)
dest.setEndColumn(5)
dest.setStartRow(0)
dest.setEndRow(0)

# Step 4: Add a Column sparkline to the destination cell
idx = worksheet.getSparklineGroups().add(
    SparklineType.Column, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(idx)

# Step 5: Confirm the sparkline type by reading group.Type
print("Sparkline Type added: " + str(group.getType()))

# Step 6: Save the workbook
workbook.save("output_column.xlsx")

print("Workbook saved as output_column.xlsx")

jpype.shutdownJVM()