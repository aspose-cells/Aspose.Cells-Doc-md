---
title: C++によるExcelチャートのタイトル管理
linktitle: タイトル
description: Microsoft Excelでチャートや軸のタイトルを追加・フォーマットする方法について学びます。Aspose.Cells for C++を使って、タイトルの種類設定、外観調整、軸タイトルの修正など、より良いデータ表現と明確さを実現します。
keywords: Aspose.Cells for C++, チャートタイトル, 軸タイトル, Microsoft Excel, データ表現, 外観
type: docs
weight: 50
url: /ja/cpp/chart-and-axis-titles/
---

{{% alert color="primary" %}}

Excelチャートには、2種類のタイトルがあります:
1. チャートタイトル 
1. 軸のタイトル

{{% /alert %}}

## **タイトルオプション**
Aspose.Cellsは、実行時にチャートのタイトルを管理することも可能です。[Title](https://reference.aspose.com/cells/cpp/aspose.cells.charts/title/)オブジェクトを使用して、タイトルのテキスト、フォント、塗りつぶしのフォーマットを変更できます。

|![todo:image_alt_text](chart_title.png)|

## **チャートや軸のタイトルの設定**
Microsoft Excelを使って、チャートとその軸のタイトルをWYSIWYG環境で設定できます。Aspose.Cellsは、開発者がチャートと軸のタイトルを実行時に設定できるようにします。すべてのチャートと軸には[Title](https://reference.aspose.com/cells/cpp/aspose.cells.charts/title/)プロパティがあり、タイトル設定に利用できます。以下は例です。

チャートと軸のタイトルを設定するコードスニペットを示します。

```cpp
#include <iostream>
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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(60);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Setting the foreground color of the plot area
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::Blue());

    // Setting the foreground color of the chart area
    chart.GetChartArea().GetArea().SetForegroundColor(Color::Yellow());

    // Setting the foreground color of the 1st SeriesCollection area
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color::Red());

    // Setting the foreground color of the area of the 1st SeriesCollection point
    chart.GetNSeries().Get(0).GetPoints().Get(0).GetArea().SetForegroundColor(Color::Cyan());

    // Filling the area of the 2nd SeriesCollection with a gradient
    chart.GetNSeries().Get(1).GetArea().GetFillFormat().SetOneColorGradient(Color::Lime(), 1, GradientStyleType::Horizontal, 1);

    // Setting the title of a chart
    chart.GetTitle().SetText(u"Title");

    // Setting the font color of the chart title to blue
    chart.GetTitle().GetFont().SetColor(Color::Blue());

    // Setting the title of category axis of the chart
    chart.GetCategoryAxis().GetTitle().SetText(u"Category");

    // Setting the title of value axis of the chart
    chart.GetValueAxis().GetTitle().SetText(u"Value");

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **上級トピック**
- [ODSファイルからチャートサブタイトルを読む](/cells/ja/cpp/read-chart-subtitle-from-ods-file/)
