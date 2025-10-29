---
title: 将图表转换为图片（C++版）
linktitle: 图表转为图像
type: docs
weight: 46
url: /zh/cpp/chart-to-image/
description: 学习如何使用 Aspose.Cells for C++ 将图表导出为 JPEG 或 PNG 等图像格式。我们的指南将演示如何从 Microsoft Excel 导出图表并将其保存为独立图片，以供进一步使用和操作。
keywords: Aspose.Cells for C++，图表转图片，Microsoft Excel，图像转换，导出，独立图片。
---

## **渲染图表**

Aspose.Cells APIs 支持将 Excel 图表转换为图像格式，无需任何额外的工具或应用程序。为了提供渲染支持，[**Chart**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/) 类公开了 [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/toimage/) 方法，具有多种重载，最适合应用需求。

### **将图表渲染为图像**

[**Chart.ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/toimage/) 方法具有多种重载，以支持简单和高级渲染。如果应用需求是在默认尺寸中渲染图表，建议使用如下 [**Chart.ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/toimage/) 方法：

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtain the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(4);
    worksheet.GetCells().Get(u"B2").PutValue(20);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Convert chart to image
    chart.ToImage(outDir + u"chartEMF_out.emf", ImageType::Emf);

    // Convert chart to Bitmap
    chart.ToImage(outDir + u"chartBMP_out.bmp", ImageType::Bmp);

    std::cout << "Chart converted to images successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

也可以使用高级设置将图表渲染为图片。Aspose.Cells APIs 提供了一个重载版本的 [**Chart.ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/toimage/) 方法，它接受 [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) 实例，让您可以指定分辨率、平滑模式、图像格式等参数。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int32_t sheetIndex = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(4);
    worksheet.GetCells().Get(u"B2").PutValue(20);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Add a chart to the worksheet
    int32_t chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Get the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Create an instance of ImageOrPrintOptions and set a few properties
    ImageOrPrintOptions options;
    options.SetVerticalResolution(300);
    options.SetHorizontalResolution(300);

    // Convert chart to image with additional settings
    chart.ToImage(outDir + u"chartPNG_out.png", options);

    std::cout << "Chart converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **支持的图表类型的渲染**

目前有一些不支持渲染的图表类型。这些图表类型在下表的**Supported**列中包含**N**。

|图表类型|图表子类型|支持
| :- | :- | :- |
|**Column**|Column|**Y**|
| |ColumnStacked|**Y**|
| |Column100PercentStacked|**Y**|
| |Column3DClustered|**Y**|
| |Column3DStacked|**Y**|
| |Column3D100PercentStacked|**Y**|
| |Column3D|**Y**|
|**Bar**|Bar|**Y**|
| |BarStacked|**Y**|
| |Bar100PercentStacked|**Y**|
| |Bar3DClustered|**Y**|
| |Bar3DStacked|**Y**|
| |Bar3D100PercentStacked|**Y**|
|**Line**|Line|**Y**|
| |LineStacked|**Y**|
| |Line100PercentStacked|**Y**|
| |LineWithDataMarkers|**Y**|
| |LineStackedWithDataMarkers|**Y**|
| |Line100PercentStackedWithDataMarkers|**Y**|
| |Line3D|**Y**|
|**Pie**|Pie|**Y**|
| |Pie3D|**Y**|
| |PiePie|**Y**|
| |PieExploded|**Y**|
| |Pie3DExploded|**Y**|
| |PieBar|**Y**|
|**Scatter**|Scatter|**Y**|
| |ScatterConnectedByCurvesWithDataMarker|**Y**|
| |ScatterConnectedByCurvesWithoutDataMarker|**Y**|
| |ScatterConnectedByLinesWithDataMarker|**Y**|
| |ScatterConnectedByLinesWithoutDataMarker|**Y**|
|**Area**|Area|**Y**|
| |AreaStacked|**Y**|
| |Area100PercentStacked|**Y**|
| |Area3D|**Y**|
| |Area3DStacked|**Y**|
| |Area3D100PercentStacked|**Y**|
|**Doughnut**|Doughnut|**Y**|
| |DoughnutExploded|**Y**|
|**Radar**|Radar|**Y**|
| |RadarWithDataMarkers|**Y**|
| |RadarFilled|**Y**|
|**Surface**|Surface3D|N|
| |SurfaceWireframe3D|N|
| |SurfaceContour|N|
| |SurfaceContourWireframe|N|
|**Bubble**|Bubble|**Y**|
| |Bubble3D|N|
|**Stock**|StockHighLowClose|**Y**|
| |StockOpenHighLowClose|**Y**|
| |StockVolumeHighLowClose|**Y**|
| |StockVolumeOpenHighLowClose|**Y**|
|**Cylinder**|Cylinder|**Y**|
| |CylinderStacked|**Y**|
| |Cylinder100PercentStacked|**Y**|
| |CylindricalBar|**Y**|
| |CylindricalBarStacked|**Y**|
| |CylindricalBar100PercentStacked|**Y**|
| |CylindricalColumn3D|**Y**|
|**Cone**|Cone|**Y**|
| |ConeStacked|**Y**|
| |Cone100PercentStacked|**Y**|
| |ConicalBar|**Y**|
| |ConicalBarStacked|**Y**|
| |ConicalBar100PercentStacked|**Y**|
| |ConicalColumn3D|**Y**|
|**Pyramid**|Pyramid|**Y**|
| |PyramidStacked|**Y**|
| |Pyramid100PercentStacked|**Y**|
| |PyramidBar|**Y**|
| |PyramidBarStacked|**Y**|
| |PyramidBar100PercentStacked|**Y**|
| |PyramidColumn3D|**Y**|
|**BoxWhisker**|BoxWhisker|Y|
|**Funnel**|Funnel|**Y**|
|**ParetoLine**|ParetoLine|**Y**|
|**Sunburst**|Sunburst|**Y**|
|**Treemap**|Treemap|**Y**|
|**Waterfall**|Waterfall|**Y**|
|**Histogram**|Histogram|Y|
|**Map**|Map|**N**|

{{% alert color="primary" %}}

如果尝试将不支持的图表类型渲染为图片或 PDF，可能会得到 0 大小的图片或空白 PDF。

{{% /alert %}}

## **高级主题**
- [将图表转换为PDF](/cells/zh/cpp/chart-to-pdf/)
{{< app/cells/assistant language="cpp" >}}
