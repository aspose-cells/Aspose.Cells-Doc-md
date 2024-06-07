---
title: 在xlsx4j中创建数据透视图
type: docs
weight: 30
url: /zh/java/create-pivot-charts-in-xlsx4j/
---

## **Aspose.Cells - 创建数据透视图**
数据透视表是记录的交互式摘要。例如，您可能在工作表的列表中有数百个发票条目。数据透视表可以按客户、产品或日期对发票进行汇总。使用 Microsoft Excel，可以通过将按钮拖动到新位置来快速重新排列数据透视表中的信息。
数据透视图是数据透视表中数据的交互式图形表示。数据透视图是在 Excel 2000 中引入的。使用数据透视图可以更容易地理解数据，因为数据透视表会自动创建小计和合计。

Aspose.Cells支持数据透视表和数据透视图

**Java**

{{< highlight java >}}

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


{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/charts/createpivotcharts/AsposePivotChart.java)

{{% alert color="primary" %}} 

有关更多详细信息，请访问[创建数据透视表和数据透视图] (/cells/zh/java/create-pivot-tables-and-pivot-charts)

{{% /alert %}}
