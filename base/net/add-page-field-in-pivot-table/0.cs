using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Create a new workbook
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

// Set up the header row
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// Populate 9 rows of sample data: Fruit, Year, Amount
object[,] data = new object[,]
{
    { "apple", 2020, 100 },
    { "banana", 2021, 200 },
    { "apple", 2021, 150 },
    { "grape", 2020, 120 },
    { "orange", 2022, 180 },
    { "banana", 2020, 90 },
    { "grape", 2021, 130 },
    { "apple", 2022, 170 },
    { "orange", 2021, 110 }
};

for (int i = 0; i < data.GetLength(0); i++)
{
    worksheet.Cells[i + 1, 0].PutValue(data[i, 0]);
    worksheet.Cells[i + 1, 1].PutValue(data[i, 1]);
    worksheet.Cells[i + 1, 2].PutValue(data[i, 2]);
}

// Add a pivot table anchored at cell E3
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Add fields to their areas: Fruit as Row, Amount as Data, Year as Page field
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// Refresh and calculate the pivot table data
pivotTable.RefreshData();
pivotTable.CalculateData();

// Save the workbook
workbook.Save("pageFieldSample.xlsx");