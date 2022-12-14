---
title: 图表渲染
type: docs
weight: 30
url: /zh/cpp/chart-rendering/
---
## **创建图表**

Aspose.Cells API 支持创建真实的 Excel 图表，详见主题[创建和自定义 Excel 图表](/cells/zh/cpp/creating-and-customizing-charts/).为了演示如何使用 Aspose.Cells API 以图像和 PDF 格式呈现图表，我们将按照以下代码段创建 Column 类型的图表。

{{< highlight "cpp" >}}

     // Create a new workbook

	intrusive_ptr<IWorkbook> workbook = Factory::CreateIWorkbook();

	// Get first worksheet which is created by default

	intrusive_ptr<IWorksheet> worksheet = workbook->GetIWorksheets()->GetObjectByIndex(0);

	// Adding sample values to cells

	worksheet->GetICells()->GetObjectByIndex(new String("A1"))->PutValue(50);

	worksheet->GetICells()->GetObjectByIndex(new String("A2"))->PutValue(100);

	worksheet->GetICells()->GetObjectByIndex(new String("A3"))->PutValue(150);

	worksheet->GetICells()->GetObjectByIndex(new String("B1"))->PutValue(4);

	worksheet->GetICells()->GetObjectByIndex(new String("B2"))->PutValue(20);

	worksheet->GetICells()->GetObjectByIndex(new String("B3"))->PutValue(50);

	// Adding a chart to the worksheet

	int chartIndex = worksheet->GetICharts()->Add(Aspose::Cells::Charts::ChartType::ChartType_Column, 5, 0, 20, 8);

	// Accessing the instance of the newly added chart

	intrusive_ptr<Aspose::Cells::Charts::IChart> chart = worksheet->GetICharts()->GetObjectByIndex(chartIndex);

	// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"

	chart->GetNISeries()->Add(new String("A1:B3"), true);

{{< /highlight >}}

## **渲染图**

Aspose.Cells API 支持将 Excel 图表转换为图像和 PDF 格式，而无需任何其他工具或应用程序。为了提供渲染支持，Chart 类公开了具有大量重载的 ToImage 和 ToPdf 方法，以最好地满足应用程序的要求。

### **将图表渲染为图像**

Chart.toImage 方法具有大量重载以支持简单和高级渲染。如果应用程序要求以默认尺寸呈现图表，我们建议您使用 Chart.toImage 方法，如下所示。

{{< highlight "cpp" >}}

 // Output directory path

StringPtr outDir = new String("..\\Data\\02_OutputDirectory\\");

// Path of output image file

StringPtr outputChartImage = outDir->StringAppend(new String("out1image.png"));

// Saving the chart to image file

chart->ToImage(outputChartImage, Aspose::Cells::System::Drawing::Imaging::ImageFormat::GetPng());

{{< /highlight >}}

### **将图表渲染为 PDF**

为了将图表呈现为 PDF 格式，Aspose.Cells API 公开了 Chart.ToPdf 方法，能够将生成的 PDF 存储在磁盘路径或流中。

{{< highlight "cpp" >}}

 // Path of output pdf file

StringPtr outputPdfFile = outDir->StringAppend(new String("out1pdf.pdf"));

// Saving chart to PDF

chart->ToPdf(outputPdfFile);

{{< /highlight >}}

## **支持的渲染图表类型**

有一些图表类型当前不支持渲染。此类图表类型包含**N** 在**支持下表的**列。

|**图表类型**|**图表子类型**|**支持的**|
|:- |:- |:- |
|**柱子**|柱子|**Y**|
||列堆叠|**Y**|
||列 100% 堆叠|**Y**|
||Column3D簇状|**Y**|
||列 3D 堆叠|**Y**|
||Column3D100PercentStacked|**Y**|
||立柱三维|**Y**|
|**酒吧**|酒吧|**Y**|
||酒吧堆叠|**Y**|
||Bar100Percent 堆叠|**Y**|
||Bar3DClustered|**Y**|
||Bar3D堆叠|**Y**|
||Bar3D100PercentStacked|**Y**|
|**线**|线|**Y**|
||线堆叠|**Y**|
||Line100Percent 堆叠|**Y**|
||带数据标记的线|**Y**|
||LineStackedWithDataMarkers|**Y**|
||Line100PercentStackedWithDataMarkers|**Y**|
||直线三维|**Y**|
|**馅饼**|馅饼|**Y**|
||Pie3D|**Y**|
||派派|**Y**|
||馅饼爆炸|**Y**|
||饼图3D分解|**Y**|
||馅饼吧|**Y**|
|**分散**|分散|**Y**|
||ScatterConnectedByCurvesWithDataMarker|**Y**|
||ScatterConnectedByCurvesWithoutDataMarker|**Y**|
||ScatterConnectedByLinesWithDataMarker|**Y**|
||ScatterConnectedByLinesWithoutDataMarker|**Y**|
|**区域**|区域|**Y**|
||面积堆叠|**Y**|
||面积 100% 堆叠|**Y**|
||三维区域|**Y**|
||Area3D堆叠|**Y**|
||Area3D100PercentStacked|**Y**|
|**甜甜圈**|甜甜圈|**Y**|
||甜甜圈爆炸|**Y**|
|**雷达**|雷达|**Y**|
||带数据标记的雷达|**Y**|
||雷达填充|**Y**|
|**表面**|Surface3D|否|
||表面线框3D|否|
||表面轮廓|否|
||表面轮廓线框|否|
|**气泡**|气泡|**Y**|
||泡泡3D|否|
|库存|股价高低收盘|**Y**|
||股票开高低收|**Y**|
||StockVolumeHighLow关闭|**Y**|
||StockVolumeOpenHighLowClose|**Y**|
|**圆柱**|圆柱|**Y**|
||圆柱叠层|**Y**|
||圆柱100%堆叠|**Y**|
||圆柱棒|**Y**|
||圆柱形条堆叠|**Y**|
||CylindricalBar100PercentStacked|**Y**|
||圆柱3D|**Y**|
|**锥体**|锥体|**Y**|
||圆锥堆叠|**Y**|
||Cone100Percent堆叠|**Y**|
||锥形棒|**Y**|
||锥形条堆叠|**Y**|
||ConicalBar100PercentStacked|**Y**|
||锥形柱3D|**Y**|
|**金字塔**|金字塔|**Y**|
||金字塔堆叠|**Y**|
||金字塔100%堆积|**Y**|
||金字塔酒吧|**Y**|
||金字塔酒吧堆叠|**Y**|
||PyramidBar100PercentStacked|**Y**|
||金字塔柱3D|**Y**|
|**盒须**|盒须|是|
|**漏斗**|漏斗|**Y**|
|**帕累托线**|帕累托线|**Y**|
|**森伯斯特**|森伯斯特|**Y**|
|**树形图**|树形图|**Y**|
|**瀑布**|瀑布|**Y**|
|**直方图**|直方图|是|
|**地图**|地图|**N**|

{{% alert color="primary" %}}

如果您尝试将不受支持的图表类型呈现为图像或 PDF，您最终可能会得到大小为 0 的图像或空白 PDF。

{{% /alert %}}
