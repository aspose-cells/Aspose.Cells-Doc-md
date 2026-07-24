import aspose.cells as ac

# Scenario 2: Apply a modern Excel 2007+ named preset style using PivotTableStyleType.
# Target file format: .xlsx. The PivotTableStyleType enum lives in the Aspose.Cells namespace
# (not in Aspose.Cells.Pivot) — that is why we do not need any extra using for it.
# GitHub reference: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Header row: Fruit / Year / Amount
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# 9 data rows of Fruit / Year / Amount
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(150)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(200)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(180)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(120)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(170)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(210)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(190)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(130)

# Add a pivot table at E3 named "Pivot1", sourced from A1:C10
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Column, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")

# Apply a modern Excel 2007+ named preset pivot style.
# PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
# is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
# family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
# newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivot_table.pivot_table_style_type = ac.PivotTableStyleType.PivotTableStyleDark1

# Save as modern .xlsx — this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx")