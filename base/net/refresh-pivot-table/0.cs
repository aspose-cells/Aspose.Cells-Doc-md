using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Create a new workbook
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Write header row into cells A1:C1
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
worksheet.Cells["A2"].PutValue("grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(50);

worksheet.Cells["A3"].PutValue("blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(60);

worksheet.Cells["A4"].PutValue("kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(70);

worksheet.Cells["A5"].PutValue("cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(80);

worksheet.Cells["A6"].PutValue("grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(90);

worksheet.Cells["A7"].PutValue("blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(100);

worksheet.Cells["A8"].PutValue("kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(110);

worksheet.Cells["A9"].PutValue("cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(120);

// Add a pivot table: source range "A1:C9", destination cell "E3", name "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Modify several Amount values in the source data to simulate changes
worksheet.Cells["C2"].PutValue(55);
worksheet.Cells["C5"].PutValue(85);
worksheet.Cells["C9"].PutValue(125);

// Refresh every pivot table / pivot cache in the workbook
workbook.RefreshAll();

// Save the workbook
workbook.Save("output.xlsx");