---
title: 使用Aspose.Cells创建数据透视表图表
type: docs
weight: 40
url: /zh/java/create-pivot-charts-using-aspose-cells/
---

## **Aspose.Cells - 创建数据透视图图表**
数据透视表是记录的互动摘要。例如，您可能有数百个工作表中列表中的发票条目。数据透视表可以按客户、产品或日期总计发票。使用Microsoft Excel，可以通过将按钮拖到新位置，快速重新排列数据透视表中的信息。
数据透视图图表是数据透视表中数据的交互式图形表示。数据透视图图表在Excel 2000中引入。使用数据透视图图表使数据更容易理解，因为数据透视表会自动创建小计和总计。

Aspose.Cells支持数据透视表和数据透视图图表。

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

{{< /highlight >}}
## **下载运行代码**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposePivotChart.java)

{{% alert color="primary" %}} 

要了解更多详情，请访问[创建数据透视表和数据透视图图表](/cells/zh/java/create-pivot-tables-and-pivot-charts/)。

{{% /alert %}}
