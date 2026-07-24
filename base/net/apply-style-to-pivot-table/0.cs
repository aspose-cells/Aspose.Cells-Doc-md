using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Scenario 1: Apply a legacy XLS preset autoformat
// API in use: PivotTable.AutoFormatType
// Target file format: .xls (legacy)
// For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET

// Create a new workbook
Workbook workbook = new Workbook();

// Get the first worksheet
Worksheet sheet = workbook.Worksheets[0];

// Populate the source data with header row (Fruit, Year, Amount)
// and 9 data rows covering grape, blueberry, kiwi, cherry across 2020 and 2021
sheet.Cells[0, 0].PutValue("Fruit");
sheet.Cells[0, 1].PutValue("Year");
sheet.Cells[0, 2].PutValue("Amount");

sheet.Cells[1, 0].PutValue("grape");
sheet.Cells[1, 1].PutValue(2020);
sheet.Cells[1, 2].PutValue(50);

sheet.Cells[2, 0].PutValue("blueberry");
sheet.Cells[2, 1].PutValue(2020);
sheet.Cells[2, 2].PutValue(30);

sheet.Cells[3, 0].PutValue("kiwi");
sheet.Cells[3, 1].PutValue(2020);
sheet.Cells[3, 2].PutValue(25);

sheet.Cells[4, 0].PutValue("cherry");
sheet.Cells[4, 1].PutValue(2020);
sheet.Cells[4, 2].PutValue(40);

sheet.Cells[5, 0].PutValue("grape");
sheet.Cells[5, 1].PutValue(2021);
sheet.Cells[5, 2].PutValue(60);

sheet.Cells[6, 0].PutValue("blueberry");
sheet.Cells[6, 1].PutValue(2021);
sheet.Cells[6, 2].PutValue(35);

sheet.Cells[7, 0].PutValue("kiwi");
sheet.Cells[7, 1].PutValue(2021);
sheet.Cells[7, 2].PutValue(28);

sheet.Cells[8, 0].PutValue("cherry");
sheet.Cells[8, 1].PutValue(2021);
sheet.Cells[8, 2].PutValue(45);

sheet.Cells[9, 0].PutValue("grape");
sheet.Cells[9, 1].PutValue(2020);
sheet.Cells[9, 2].PutValue(45);

// Add a pivot table at destination cell E3, named "Pivot1", using source range A1:C10
int pivotIndex = sheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];

// Assign fields: Fruit -> Rows, Year -> Columns, Amount -> Data
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Apply the legacy XLS preset autoformat "Report5"
// Note: This property is only meaningful when saving as .xls.
// When saved as .xlsx/.xlsm/.xlsb, Excel ignores AutoFormatType
// and uses whatever PivotTableStyleType / PivotTableStyleName specifies.
pivotTable.AutoFormatType = PivotTableAutoFormatType.Report5;

// Save the workbook in legacy .xls format
workbook.Save("output.xls");