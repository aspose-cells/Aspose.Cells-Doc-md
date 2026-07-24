import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.cells[0, j].put_value(headers[j])

data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020, 80],
    ["Fruit",     "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45],
]

for i in range(len(data)):
    for j in range(len(data[i])):
        worksheet.cells[i + 1, j].put_value(data[i][j])

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

category_field = pivot_table.row_fields[0]
for st in [ac.PivotFieldSubtotalType.SUM, ac.PivotFieldSubtotalType.COUNT, ac.PivotFieldSubtotalType.AVERAGE, ac.PivotFieldSubtotalType.MAX, ac.PivotFieldSubtotalType.MIN, ac.PivotFieldSubtotalType.PRODUCT]:
    category_field.set_subtotals(st, True)
pivot_table.refresh_data()
pivot_table.calculate_data()

workbook.save("output_none.xlsx")