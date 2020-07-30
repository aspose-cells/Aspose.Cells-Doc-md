---
title : "Create Pivot Charts in xlsx4j" 
description : "" 
weight : 20679 
toc : false
type: docs
url: /java/plugins/xlsx4j/missingfeaturesinapscls/charts/create+pivot+charts+in+xlsx4j/
---

# Aspose.Cells for Java : Create Pivot Charts in xlsx4j


## Aspose.Cells - Create Pivot Charts

A pivot table is an interactive summary of records. For example, you may have hundreds of invoice entries in a list in a worksheet. A pivot table can total the invoices by customer, product or date. With Microsoft Excel it is possible to quickly re-arrange the information in the pivot table by dragging buttons to a new position.  
A pivot chart is an interactive graphical representation of the data in a pivot table. Pivot charts were introduced in Excel 2000. Using a pivot chart makes it even easier to understand the data since the pivot table creates subtotals and totals automatically.

Aspose.Cells supports pivot tables and pivot charts.

**Java**

{{< code lang="java" >}}
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

// Saving the Excel file
workbook.save(dataDir + "Aspose_PivotChart_Out.xls");

{{< /code >}}

## Download Running Code

*   [CodePlex](http://asposecellsjavaxlsx4j.codeplex.com/releases/view/618923)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaxlsx4j.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/asposefeatures/charts/createpivotcharts/AsposePivotChart.java)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose.Cells-for-Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/charts/createpivotcharts/AsposePivotChart.java)

For more details, visit [Create Pivot Tables and Pivot Charts](http://www.aspose.com/docs/display/cellsjava/Create+Pivot+Tables+and+Pivot+Charts).

