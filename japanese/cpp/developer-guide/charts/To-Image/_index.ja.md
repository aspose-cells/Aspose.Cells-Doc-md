---
title: チャートを画像に変換（C++）
linktitle: グラフをイメージに変換する
type: docs
weight: 46
url: /ja/cpp/chart-to-image/
description: Aspose.Cells for C++を使用して、チャートをJPEGやPNGなどの画像フォーマットに変換する方法について学びます。Microsoft Excelからチャートをエクスポートし、単体の画像として保存・操作する方法を示します。
keywords: Aspose.Cells for C++, チャートを画像に変換, Microsoft Excel, 画像変換, エクスポート, 単体画像
---

## **チャートのレンダリング**

Aspose.Cells APIは、追加のツールやアプリケーションを必要とせずにExcelチャートを画像形式に変換できます。レンダリングサポートのために、[**Chart**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/)クラスには多様なオーバーロードを持つ[**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/toimage/)メソッドが公開されており、用途に合った設定が可能です。

### **画像へのチャートのレンダリング**

[**Chart.ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/toimage/) メソッドには、シンプルなレンダリングから高度なレンダリングをサポートするためのさまざまなオーバーロードがあります。アプリケーションの要件がチャートをデフォルトの寸法でレンダリングする場合は、次のように [**Chart.ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/toimage/) メソッドを使用することをお勧めします。

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

高度な設定でチャートを画像にレンダリングすることも可能です。Aspose.Cells APIは、 resolution、smoothing mode、画像形式などのパラメータを指定できる[**Chart.ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/toimage/)メソッドのオーバーロードを提供しています。

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

## **レンダリングにサポートされているチャートの種類**

現在は描画に対応していないチャートタイプもいくつかあります。そうしたチャートタイプには、以下の表の**サポート**列に**N**が含まれています。

|チャートタイプ|チャートサブタイプ|サポートされているかどうか|
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

サポート外のチャートタイプを画像やPDFに変換しようとすると、サイズが0の画像や空白のPDFになる場合があります。

{{% /alert %}}

## **高度なトピック**
- [グラフをPDFに変換する](/cells/ja/cpp/chart-to-pdf/)
