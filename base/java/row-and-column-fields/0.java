import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);

worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);

worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);

worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);

worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);

worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);

worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);

worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);

int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

PivotField categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true);

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_automatic.xlsx");