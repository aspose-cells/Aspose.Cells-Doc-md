using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Create workbook
var workbook = new Workbook();
var sheet = workbook.Worksheets[0];
var cells = sheet.Cells;

// Add sample data (Fruit/Year/Amount)
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");

cells["A2"].PutValue("Apple");
cells["B2"].PutValue("2020");
cells["C2"].PutValue("100");

cells["A3"].PutValue("Apple");
cells["B3"].PutValue("2021");
cells["C3"].PutValue("150");

cells["A4"].PutValue("Banana");
cells["B4"].PutValue("2020");
cells["C4"].PutValue("200");

cells["A5"].PutValue("Banana");
cells["B5"].PutValue("2021");
cells["C5"].PutValue("250");

// Add pivot table at E3
var pivotTables = sheet.PivotTables;
int pivotIndex = pivotTables.Add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables[pivotIndex];

// Add fields: Fruit→Row, Amount→Data, Year→Page
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// Page-field-specific operations
pivotTable.PageFields[0].CurrentPageItem = 1; // 1 = second item in sorted order (e.g. "2021")

// Refresh and calculate pivot table
pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output.xlsx");