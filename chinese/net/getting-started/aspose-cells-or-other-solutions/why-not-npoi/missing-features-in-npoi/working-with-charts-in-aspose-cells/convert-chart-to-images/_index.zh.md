---
title: 将图表转换为图像
type: docs
weight: 10
url: /zh/net/convert-chart-to-images/
---
## **Aspose.Cells - 将图表转换为图像**
图表在视觉上很吸引人，使用户可以轻松查看数据中的比较、模式和趋势。
Chart 类的 toImage 方法将图表转换为图像文件，可以将其保存到磁盘或流中。

**C#**

{{< highlight "cs" >}}

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

//Save the chart image file.

chart.ToImage("AsposeChartImage.png", ImageFormat.Png);

{{< /highlight >}}
## **下载运行代码**
下载**将图表转换为图像**形成以下任何一个社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Convert.Chart.To.Images.Aspose.Cells.zip)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[将图表转换为图像](/cells/zh/net/converting-chart-to-image-in-svg-format/).

{{% /alert %}}
