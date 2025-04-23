---
title: C++でTreeMapチャートを作成する方法
description: Aspose.Cells for C++でツリーマップチャートを作成する方法を学びます。ガイドは、色、ラベル、データ表現など、ツリーマップチャートのさまざまなプロパティやフォーマットオプションを理解するのに役立ちます。
keywords: Aspose.Cells for C++、ツリーマップチャート、作成、プロパティ、フォーマット、色、ラベル、データ表現、円形チャート、階層型チャート。
type: docs
weight: 161
url: /ja/cpp/creating-treemap-chart/
---

## **可能な使用シナリオ**
ツリーマップチャートは、データを階層ビューで表し、店舗の売れ筋商品などのパターンを簡単に把握できます。ツリーのブランチは長方形で表され、各サブブランチは小さな長方形として表示されます。ツリーマップチャートは、色と近接性でカテゴリを表示し、他のチャートタイプでは難しい大量のデータを簡単に表示できます。

![todo:image_alt_text](sample.png)
## **ツリーマップチャート**
以下のコードを実行すると、下記のツリーマップチャートが表示されます。

![todo:image_alt_text](result.png)
## **サンプルコード**
下記のサンプルコードは、[サンプルExcelファイル](treemap.xlsx)を読み込み、[出力Excelファイル](out.xlsx)を生成します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"treemap.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a Treemap chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::Treemap, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"TreeMap Chart");

    // Add series data range (D2:F13, actually)
    chart.GetNSeries().Add(u"D2:F13", true);

    // Set category data (A2:C13 is incorrect)
    chart.GetNSeries().SetCategoryData(u"A2:C13");

    // Show the DataLabels with category names
    chart.GetNSeries().Get(0).GetDataLabels().SetShowCategoryName(true);

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
