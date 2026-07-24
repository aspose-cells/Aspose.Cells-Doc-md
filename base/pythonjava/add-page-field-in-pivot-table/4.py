import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
import os
import re

# — The pivot table and page field are constructed exactly as in
#   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit→Row,
#   Amount→Data, Year→Page via AddFieldToArea).
#   Below we apply multi-select filtering on the page field.

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Sample data: Fruit | Year | Amount
cells.get(0, 0).putValue("Fruit")
cells.get(0, 1).putValue("Year")
cells.get(0, 2).putValue("Amount")

data = [
    ["apple",  "2019", "100"],
    ["apple",  "2020", "150"],
    ["apple",  "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape",  "2019", "120"],
    ["grape",  "2020", "170"],
    ["grape",  "2021", "220"]
]

for i in range(len(data)):
    cells.get(i + 1, 0).putValue(data[i][0])
    cells.get(i + 1, 1).putValue(int(data[i][1]))
    cells.get(i + 1, 2).putValue(int(data[i][2]))

pivotSheet = workbook.getWorksheets().add("Pivot")
pivots = pivotSheet.getPivotTables()
pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1")
pivotTable = pivots.get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# — Enable multi-select on the page field
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(True)

# Part A — select ALL items (make every item visible)
pivotItems = pivotTable.getPageFields().get(0).getPivotItems()
for i in range(pivotItems.getCount()):
    pivotItems.get(i).setHidden(False)

# Part B — select only specific items by source value
for i in range(pivotItems.getCount()):
    value = pivotItems.get(i).getStringValue()
    if value == "2020" or value == "grape" or value == "blueberry":
        pivotItems.get(i).setHidden(False)
    else:
        pivotItems.get(i).setHidden(True)

pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()