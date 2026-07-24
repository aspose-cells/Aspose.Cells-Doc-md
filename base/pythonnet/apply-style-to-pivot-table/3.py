from System.Drawing import Color
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells import BackgroundType, CellBorderType, BorderType

# Scenario 4: Apply a single Style to every pivot table cell using FormatAll
# API in use: PivotTable.FormatAll(Style)
# Target format: .xlsx
# GitHub reference: see Aspose.Cells-for-.NET repository — pivot table styling examples

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Populate source data: header row (row 1) + 9 data rows (rows 2-10)
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(5000)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(3000)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(4000)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(2000)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(6000)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(3500)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(4500)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(2500)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(5500)

# Add pivot table: source range A1:C10, destination cell E3, name "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

# Build a Style that will be forced onto every cell of the pivot table
style = workbook.create_style()
style.foreground_color = Color.Yellow
style.pattern = BackgroundType.SOLID
style.font.is_bold = True
style.font.color = Color.DarkBlue
style.borders[BorderType.TOP_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.TOP_BORDER].color = Color.Black
style.borders[BorderType.BOTTOM_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.BOTTOM_BORDER].color = Color.Black
style.borders[BorderType.LEFT_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.LEFT_BORDER].color = Color.Black
style.borders[BorderType.RIGHT_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.RIGHT_BORDER].color = Color.Black

# Apply FormatAll: forces this single style onto every cell of the pivot table,
# overriding any PivotTableStyleType / PivotTableStyleName previously set
pivot_table.format_all(style)

# Save the workbook in the modern .xlsx format
workbook.save("output.xlsx")