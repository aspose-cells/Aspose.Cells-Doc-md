---
title: 创建图表
type: docs
weight: 20
url: /zh/net/create-charts/
---

## **Aspose.Cells - 创建图表**
可以使用Aspose.Cells向电子表格添加各种图表。Aspose.Cells提供许多灵活的图表对象。

**C#**

{{< highlight cs >}}

 // Instantiating a Workbook object

Workbook workbook = new Workbook();

// Obtaining the reference of the first worksheet

WorksheetCollection worksheets = workbook.Worksheets;

Worksheet sheet = worksheets[0];

// Adding some sample value to cells

Cells cells = sheet.Cells;

Cell cell = cells["A1"];

cell.Value = 50;

cell = cells["A2"];

cell.Value = 100;

cell = cells["A3"];

cell.Value = 150;

cell = cells["B1"];

cell.Value = 4;

cell = cells["B2"];

cell.Value = 20;

cell = cells["B3"];

cell.Value = 50;

ChartCollection charts = sheet.Charts;

// Adding a chart to the worksheet

int chartIndex = charts.Add(ChartType.Pyramid, 5, 0, 15, 5);

Chart chart = charts[chartIndex];

// Adding NSeries (chart data source) to the chart ranging from "A1" cell to "B3"

SeriesCollection serieses = chart.NSeries;

serieses.Add("A1:B3", true);

// Saving the Excel file

workbook.Save("Chart_Aspose.xls");

{{< /highlight >}}
## **下载运行代码**
从以下提到的任何社交编码网站下载**创建图表**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Create.Charts.Aspose.Cells.zip)

{{% alert color="primary" %}} 

有关更多详细信息，请访问[如何创建图表](/cells/zh/net/create-charts/)。

{{% /alert %}}
