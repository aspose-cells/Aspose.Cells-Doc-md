using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Create a new workbook and access the first worksheet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Write header row: Fruit / Year / Amount
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// Write approximately 9 data rows (grape / blueberry / kiwi / cherry across 2020-2021)
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(500);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(600);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(700);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(800);

// Add the first pivot table "Pivot1" anchored at cell E3, source range A1:C9
int pivotIndex1 = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.PivotTables[pivotIndex1];

// Assign fields for Pivot1
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

// Add a SECOND pivot table "Pivot2" anchored at E15 using the SAME source range A1:C9
// Both Pivot1 and Pivot2 share a single PivotCache because the source range is identical.
int pivotIndex2 = worksheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.PivotTables[pivotIndex2];

// Assign the same fields for Pivot2
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

// Modify several Amount cell values in the source data to simulate a data change
worksheet.Cells["C2"].PutValue(150);
worksheet.Cells["C4"].PutValue(350);
worksheet.Cells["C7"].PutValue(650);

// Refresh the shared PivotCache.
// Because Pivot1 and Pivot2 share the same PivotCache, this single call
// refreshes BOTH pivot tables (data + style) from the updated source.
pivotTable1.PivotCache.Refresh();

// Save the workbook
workbook.Save("output.xlsx");