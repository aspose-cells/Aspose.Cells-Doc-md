import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType

# Create a new workbook
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")

# Set up the header row
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Populate 9 rows of sample data: Fruit, Year, Amount
data = [
    ["apple", 2020, 100],
    ["banana", 2021, 200],
    ["apple", 2021, 150],
    ["grape", 2020, 120],
    ["orange", 2022, 180],
    ["banana", 2020, 90],
    ["grape", 2021, 130],
    ["apple", 2022, 170],
    ["orange", 2021, 110]
]

for i in range(len(data)):
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0])
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1])
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2])

# Add a pivot table anchored at cell E3
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Add fields to their areas: Fruit as Row, Amount as Data, Year as Page field
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# Refresh and calculate the pivot table data
pivotTable.refreshData()
pivotTable.calculateData()

# Save the workbook
workbook.save("pageFieldSample.xlsx")

jpype.shutdownJVM()