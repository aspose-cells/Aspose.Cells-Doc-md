import com.aspose.cells.*;

// - The pivot table and page field are constructed exactly as in
//   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit->Row,
//   Amount->Data). Below we obtain the Year PivotField from the
//   BaseFields collection and pass it to PageFields.Add - the
//   low-level alternative to AddFieldToArea. The result is
//   functionally identical to Scenario 1a.

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);

// Headers
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

// Sample data (9 rows)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);

// Add pivot table at E3 covering A1:C10
int pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = sheet.getPivotTables().get(pivotIndex);

// Fruit -> Row, Amount -> Data (Year will go to Page below)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Low-level approach: grab the existing Year PivotField from BaseFields
// and register it in the Page area via PageFields.Add(PivotField).
PivotField yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);

// Refresh so the new page field is reflected in the saved workbook
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");