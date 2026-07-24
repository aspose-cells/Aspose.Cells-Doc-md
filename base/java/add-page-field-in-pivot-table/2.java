import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);

// Populate Fruit/Year/Amount data
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

Object[][] data = new Object[][]
{
    {"Apple", 2022, 100},
    {"Apple", 2023, 150},
    {"Banana", 2022, 80},
    {"Banana", 2023, 120},
    {"Cherry", 2022, 200},
    {"Cherry", 2023, 250}
};

for (int r = 0; r < data.length; r++)
{
    for (int c = 0; c < data[r].length; c++)
    {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

// Create pivot table at E3
PivotTableCollection pivotTables = sheet.getPivotTables();
int index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
PivotTable pivot = pivotTables.get(index);

// Configure pivot fields: Fruit to Row, Amount to Data, Year to Page
pivot.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivot.addFieldToArea(PivotFieldType.DATA, "Amount");
pivot.addFieldToArea(PivotFieldType.PAGE, "Year");

pivot.refreshData();
pivot.calculateData();

// Clear the page filter so every item in the page field is visible.
// 0x7FFD (decimal 32765) is the special sentinel value that means "all items",
// equivalent to selecting "(All)" in Excel's page-field dropdown.
pivot.getPageFields().get(0).setCurrentPageItem((short)0x7FFD);

workbook.save("output.xlsx");