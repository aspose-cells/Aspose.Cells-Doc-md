import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import PivotFieldType, TableStyleElementType, BorderType, CellBorderType
from java.awt import Color

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Populate source data: header row + 9 data rows (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(500)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(900)

# Add pivot table sourced from A1:C10, anchored at E3, named "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

# Step 1: register a new custom pivot table style and capture its index
styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle")
tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex)

# Step 2: add a WholeTable element and apply thin black borders on all four sides
wholeTableElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE)
wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex)
wholeTableStyle = workbook.createStyle()
wholeTableStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.TOP_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.BOTTOM_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.LEFT_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.RIGHT_BORDER).setColor(Color.BLACK)
wholeTableElement.setElementStyle(wholeTableStyle)

# Step 3: add a GrandTotalRow element and apply bold red font
grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW)
grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex)
grandTotalStyle = workbook.createStyle()
grandTotalStyle.getFont().setBold(True)
grandTotalStyle.getFont().setColor(Color.RED)
grandTotalElement.setElementStyle(grandTotalStyle)

# Step 4: apply the custom style by name (NOT by PivotTableStyleType, which is for built-in presets)
pivotTable.setPivotTableStyleName("CustomPivotStyle")

workbook.save("output.xlsx")

jpype.shutdownJVM()