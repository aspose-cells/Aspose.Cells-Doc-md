using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// — The pivot table and page field are constructed exactly as in
//   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit→Row,
//   Amount→Data). Below we obtain the Year PivotField from the
//   BaseFields collection and pass it to PageFields.Add — the
//   low-level alternative to AddFieldToArea. The result is
//   functionally identical to Scenario 1a.

Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// Headers
sheet.Cells["A1"].PutValue("Fruit");
sheet.Cells["B1"].PutValue("Year");
sheet.Cells["C1"].PutValue("Amount");

// Sample data (9 rows)
sheet.Cells["A2"].PutValue("apple");    sheet.Cells["B2"].PutValue("2020"); sheet.Cells["C2"].PutValue(100);
sheet.Cells["A3"].PutValue("apple");    sheet.Cells["B3"].PutValue("2021"); sheet.Cells["C3"].PutValue(150);
sheet.Cells["A4"].PutValue("apple");    sheet.Cells["B4"].PutValue("2022"); sheet.Cells["C4"].PutValue(200);
sheet.Cells["A5"].PutValue("grape");    sheet.Cells["B5"].PutValue("2020"); sheet.Cells["C5"].PutValue(300);
sheet.Cells["A6"].PutValue("grape");    sheet.Cells["B6"].PutValue("2021"); sheet.Cells["C6"].PutValue(400);
sheet.Cells["A7"].PutValue("grape");    sheet.Cells["B7"].PutValue("2022"); sheet.Cells["C7"].PutValue(500);
sheet.Cells["A8"].PutValue("blueberry"); sheet.Cells["B8"].PutValue("2020"); sheet.Cells["C8"].PutValue(250);
sheet.Cells["A9"].PutValue("blueberry"); sheet.Cells["B9"].PutValue("2021"); sheet.Cells["C9"].PutValue(350);
sheet.Cells["A10"].PutValue("blueberry");sheet.Cells["B10"].PutValue("2022"); sheet.Cells["C10"].PutValue(450);

// Add pivot table at E3 covering A1:C10
int pivotIndex = sheet.PivotTables.Add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];

// Fruit -> Row, Amount -> Data (Year will go to Page below)
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Low-level approach: grab the existing Year PivotField from BaseFields
// and register it in the Page area via PageFields.Add(PivotField).
PivotField yearField = pivotTable.BaseFields["Year"];
pivotTable.PageFields.Add(yearField);

// Refresh so the new page field is reflected in the saved workbook
pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output.xlsx");