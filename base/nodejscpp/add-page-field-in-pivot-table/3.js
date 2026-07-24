var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// Add sample data (Fruit/Year/Amount)
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");

cells.get("A2").putValue("Apple");
cells.get("B2").putValue("2020");
cells.get("C2").putValue("100");

cells.get("A3").putValue("Apple");
cells.get("B3").putValue("2021");
cells.get("C3").putValue("150");

cells.get("A4").putValue("Banana");
cells.get("B4").putValue("2020");
cells.get("C4").putValue("200");

cells.get("A5").putValue("Banana");
cells.get("B5").putValue("2021");
cells.get("C5").putValue("250");

// Add pivot table at E3
var pivotTables = sheet.getPivotTables();
var pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables.get(pivotIndex);

// Add fields: Fruit→Row, Amount→Data, Year→Page
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// Page-field-specific operations
pivotTable.getPageFields().get(0).setCurrentPageItem(1); // 1 = second item in sorted order (e.g. "2021")

// Refresh and calculate pivot table
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");