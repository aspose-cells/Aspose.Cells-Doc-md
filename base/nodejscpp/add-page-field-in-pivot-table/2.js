let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Populate Fruit/Year/Amount data
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

let data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
];

for (let r = 0; r < data.length; r++) {
    for (let c = 0; c < data[r].length; c++) {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

// Create pivot table at E3
let pivotTables = sheet.getPivotTables();
let index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
let pivotTable = pivotTables.get(index);

// Configure pivot fields: Fruit→Row, Amount→Data, Year→Page
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

pivotTable.refreshData();
pivotTable.calculateData();

// Clear the page filter so every item in the page field is visible.
// 0x7FFD (decimal 32765) is the special sentinel value that means "all items" —
// equivalent to selecting "(All)" in Excel's page-field dropdown.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD);

workbook.save("output.xlsx");