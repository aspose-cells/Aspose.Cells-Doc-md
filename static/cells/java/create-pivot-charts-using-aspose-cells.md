##Create Pivot Charts using Aspose.Cells
## **Aspose.Cells - Create Pivot Charts**
A pivot table is an interactive summary of records. For example, you may have hundreds of invoice entries in a list in a worksheet. A pivot table can total the invoices by customer, product or date. With Microsoft Excel it is possible to quickly re-arrange the information in the pivot table by dragging buttons to a new position.
A pivot chart is an interactive graphical representation of the data in a pivot table. Pivot charts were introduced in Excel 2000. Using a pivot chart makes it even easier to understand the data since the pivot table creates subtotals and totals automatically.
Aspose.Cells supports pivot tables and pivot charts.
**Java**
// Instantiating an Workbook object
Workbook workbook = new Workbook(dataDir + "AsposePivotTable.xls");
// Adding a new sheet
int sheetIndex = workbook.getWorksheets().add(SheetType.CHART);
Worksheet sheet3 = workbook.getWorksheets().get(sheetIndex);
// Naming the sheet
sheet3.setName("PivotChart");
// Adding a column chart
int chartIndex = sheet3.getCharts().add(ChartType.COLUMN, 0, 5, 28, 16);
Chart chart = sheet3.getCharts().get(chartIndex);
// Setting the pivot chart data source
chart.setPivotSource("PivotTable!PivotTable1");
chart.setHidePivotFieldButtons(false);
## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposePivotChart.java)
For more details, visit [Create Pivot Tables and Pivot Charts](https://docs.aspose.com/cells/java/create-pivot-tables-and-pivot-charts/).
