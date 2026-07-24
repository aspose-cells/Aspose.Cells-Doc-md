import aspose.cells as ac

# Create workbook
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# Add sample data (Fruit/Year/Amount)
cells["A1"].put_value("Fruit")
cells["B1"].put_value("Year")
cells["C1"].put_value("Amount")

cells["A2"].put_value("Apple")
cells["B2"].put_value("2020")
cells["C2"].put_value("100")

cells["A3"].put_value("Apple")
cells["B3"].put_value("2021")
cells["C3"].put_value("150")

cells["A4"].put_value("Banana")
cells["B4"].put_value("2020")
cells["C4"].put_value("200")

cells["A5"].put_value("Banana")
cells["B5"].put_value("2021")
cells["C5"].put_value("250")

# Add pivot table at E3
pivot_tables = sheet.pivot_tables
pivot_index = pivot_tables.add("A1:C5", "E3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

# Add fields: Fruit→Row, Amount→Data, Year→Page
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, "Year")

# Page-field-specific operations
pivot_table.page_fields[0].current_page_item = 1  # 1 = second item in sorted order (e.g. "2021")

# Refresh and calculate pivot table
pivot_table.refresh_data()
pivot_table.calculate_data()

workbook.save("output.xlsx")