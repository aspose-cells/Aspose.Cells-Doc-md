using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Scenario 2: Apply a modern Excel 2007+ named preset style using PivotTableStyleType.
// Target file format: .xlsx. The PivotTableStyleType enum lives in the Aspose.Cells namespace
// (not in Aspose.Cells.Pivot) — that is why we do not need any extra using for it.
// GitHub reference: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Header row: Fruit / Year / Amount
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// 9 data rows of Fruit / Year / Amount
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(150);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(200);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(180);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(120);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(170);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(210);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(190);

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(130);

// Add a pivot table at E3 named "Pivot1", sourced from A1:C10
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Apply a modern Excel 2007+ named preset pivot style.
// PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
// is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
// family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
// newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleDark1;

// Save as modern .xlsx — this is the format for which PivotTableStyleType is meaningful.
workbook.Save("output.xlsx");