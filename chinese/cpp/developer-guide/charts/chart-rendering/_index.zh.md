---
title: 图表渲染
type: docs
weight: 30
url: /zh/cpp/chart-rendering/
---
##  **创建图表**

Aspose.Cells API 支持创建大量 Excel 图表，如主题下详述[创建和自定义 Excel 图表](/cells/zh/cpp/creating-and-customizing-charts/)。为了演示如何使用 Aspose.Cells API 以图像和 PDF 格式呈现图表，我们将按照以下代码片段创建一个 Column 类型的图表。

{{< highlight "cpp" >}}

Aspose::Cells::Startup();

// Output directory path
U16String outDir(u"..\\Data\\02_OutputDirectory\\");

// Create a new workbook
Workbook workbook;

// Get first worksheet which is created by default
Worksheet worksheet = workbook.GetWorksheets().Get(0);

// Adding sample values to cells
worksheet.GetCells().Get(u"A1").PutValue(50);
worksheet.GetCells().Get(u"A2").PutValue(100);
worksheet.GetCells().Get(u"A3").PutValue(150);
worksheet.GetCells().Get(u"B1").PutValue(4);
worksheet.GetCells().Get(u"B2").PutValue(20);
worksheet.GetCells().Get(u"B3").PutValue(50);

// Adding a chart to the worksheet
int chartIndex = worksheet.GetCharts().Add(Aspose::Cells::Charts::ChartType::Column, 5, 0, 20, 8);

// Accessing the instance of the newly added chart
Chart chart = worksheet.GetCharts().Get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.GetNSeries().Add(u"A1:B3", true);

// Path of output image file
U16String outputChartImage = outDir + u"out1image.png";
chart.ToImage(outputChartImage, ImageType::Png);

// Path of output pdf file
U16String outputPdfFile = outDir + u"out1pdf.pdf";

// Saving chart to PDF
chart.ToPdf(outputPdfFile);

Aspose::Cells::Cleanup();

{{< /highlight >}}

##  **渲染图表**

Aspose.Cells API 支持将 Excel 图表转换为图像和 PDF 格式，无需任何其他工具或应用程序。为了提供渲染支持，Chart 类公开了具有大量重载的 ToImage 和 ToPdf 方法，以最适合应用程序的要求。

###  **将图表渲染为图像**

Chart.toImage 方法具有大量重载来支持简单和高级渲染。如果应用程序要求以默认尺寸渲染图表，我们建议您使用 Chart.toImage 方法，如下所示。

{{< highlight "cpp" >}}

// Path of output image file
U16String outputChartImage = outDir + u"out1image.png";

// Saving the chart to image file
chart.ToImage(outputChartImage, ImageType::Png);

{{< /highlight >}}

###  **渲染图至PDF**

为了将图表呈现为 PDF 格式，Aspose.Cells API 公开了 Chart.ToPdf 方法，能够将结果 PDF 存储在光盘路径或流上。

{{< highlight "cpp" >}}

// Path of output pdf file
U16String outputPdfFile = outDir + u"out1pdf.pdf";

// Saving chart to PDF
chart.ToPdf(outputPdfFile);

{{< /highlight >}}

##  **支持的渲染图表类型**

目前不支持渲染某些图表类型。此类图表类型包含****支持中的 N****下表的列。

|**图表类型**|**图表子类型**|**支持的**|
| :- | :- | :- |
|**柱子**|柱子|*是**|
| |列堆叠|*是**|
| |列100%堆积|*是**|
| |柱状3D簇状|*是**|
| |柱3D堆叠|*是**|
| |Column3D100PercentStacked|*是**|
| |柱三维|*是**|
|**酒吧**|酒吧|*是**|
| |条形堆叠|*是**|
| |条形100%堆叠|*是**|
| |Bar3D簇状|*是**|
| |酒吧3D堆叠|*是**|
| |Bar3D100百分比堆叠|*是**|
|**线**|线|*是**|
| |线堆叠|*是**|
| |线 100% 堆叠|*是**|
| |带数据标记的线|*是**|
| |带数据标记的线堆叠|*是**|
| |带数据标记的 Line100PercentStacked|*是**|
| |线三维|*是**|
|**馅饼**|馅饼|*是**|
| |饼图3D|*是**|
| |派派|*是**|
| |馅饼爆炸了|*是**|
| |饼图3D爆炸|*是**|
| |饼图栏|*是**|
|**分散**|分散|*是**|
| |通过带有数据标记的曲线连接的散点图|*是**|
| |不带数据标记的按曲线连接的散点图|*是**|
| |ScatterConnectedByLinesWithDataMarker|*是**|
| |不带数据标记的按行分散连接|*是**|
|**区域**|区域|*是**|
| |堆积面积|*是**|
| |面积100%堆叠|*是**|
| |三维区域|*是**|
| |区域3D堆叠|*是**|
| |Area3D100PercentStacked|*是**|
|**油炸圈饼**|油炸圈饼|*是**|
| |甜甜圈爆炸|*是**|
|**雷达**|雷达|*是**|
| |带数据标记的雷达|*是**|
| |雷达填充|*是**|
|**表面**|表面3D|N|
| |表面线框3D|N|
| |表面轮廓|N|
| |表面轮廓线框|N|
|**气泡**|气泡|*是**|
| |泡泡3D|N|
|库存|股票高低收盘|*是**|
| |股票开盘高低收盘|*是**|
| |股票成交量高低收盘|*是**|
| |股票成交量开盘高低收盘|*是**|
|**圆柱**|圆柱|*是**|
| |圆筒堆叠|*是**|
| |气缸100%堆叠|*是**|
| |圆柱棒|*是**|
| |圆柱形条堆叠|*是**|
| |圆柱形条100%堆叠|*是**|
| |圆柱3D|*是**|
|**锥体**|锥体|*是**|
| |圆锥堆叠|*是**|
| |锥体100%堆叠|*是**|
| |锥形棒|*是**|
| |锥形条堆叠|*是**|
| |锥形条100%堆叠|*是**|
| |圆锥柱3D|*是**|
|**金字塔**|金字塔|*是**|
| |金字塔堆积|*是**|
| |金字塔100%堆叠|*是**|
| |金字塔酒吧|*是**|
| |金字塔酒吧堆积|*是**|
| |金字塔条形图100%堆叠|*是**|
| |金字塔柱3D|*是**|
|**盒须**|盒须|Y|
|**漏斗**|漏斗|*是**|
|**帕累托线**|帕累托线|*是**|
|**旭日**|旭日|*是**|
|**树形图**|树形图|*是**|
|**瀑布**|瀑布|*是**|
|**直方图**|直方图|Y|
|**地图**|地图|*N**|

{{% alert color="primary" %}}

如果您尝试将不支持的图表类型渲染为图像或 PDF，您最终可能会得到 0 大小的图像或空白 PDF。

{{% /alert %}}
