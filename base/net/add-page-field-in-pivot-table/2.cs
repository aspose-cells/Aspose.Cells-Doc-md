using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

class Program
{
    static void Main()
    {
        // Create a new workbook
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];

        // Populate Fruit/Year/Amount data
        sheet.Cells["A1"].PutValue("Fruit");
        sheet.Cells["B1"].PutValue("Year");
        sheet.Cells["C1"].PutValue("Amount");

        object[,] data = new object[,]
        {
            {"Apple", 2022, 100},
            {"Apple", 2023, 150},
            {"Banana", 2022, 80},
            {"Banana", 2023, 120},
            {"Cherry", 2022, 200},
            {"Cherry", 2023, 250}
        };

        for (int r = 0; r < data.GetLength(0); r++)
        {
            for (int c = 0; c < data.GetLength(1); c++)
            {
                sheet.Cells[r + 1, c].PutValue(data[r, c]);
            }
        }

        // Create pivot table at E3
        var pivotTables = sheet.PivotTables;
        int index = pivotTables.Add("=A1:C7", "E3", "PivotTable1");
        PivotTable pivotTable = pivotTables[index];

        // Configure pivot fields: Fruit→Row, Amount→Data, Year→Page
        pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
        pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
        pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

        pivotTable.RefreshData();
        pivotTable.CalculateData();

        // Clear the page filter so every item in the page field is visible.
        // 0x7FFD (decimal 32765) is the special sentinel value that means "all items" —
        // equivalent to selecting "(All)" in Excel's page-field dropdown.
        pivotTable.PageFields[0].CurrentPageItem = 0x7FFD;

        workbook.Save("output.xlsx");
    }
}