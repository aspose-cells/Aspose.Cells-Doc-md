---
title: C++によるZ軸の設定
linktitle: Z軸
description: Aspose.Cells for C++でZ軸の操作方法を学びます。スケールやラベルの設定、カスタマイズ方法を理解し、チャートの見栄えを向上させます。
keywords: Aspose.Cells for C++、Z軸、チャート作成、設定、カスタマイズ、スケール、ラベル
type: docs
weight: 210
url: /ja/cpp/z-axis/
---

## **可能な使用シナリオ**
3-D列や3-Dコーン、または3-Dピラミッドなどの一部の3-Dチャートには深度（系列）軸として知られるZ軸があります。この軸の間隔、軸ラベル、およびその他の操作を指定することができます。

## **Microsoft Excelのようにプライマリおよびセカンダリ軸を処理する**
以下のサンプルコードは、新しいExcelファイルを作成し、最初のワークシートにグラフの値を配置します。その後、チャートを追加し、タイプをColumn3Dに設定します。これによりZ軸（奥行き軸）も確認できます。 

![todo:image_alt_text](excel.png)

## **サンプルコード**
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put values to cells for creating chart
    worksheet.GetCells().Get(u"A1").PutValue(u"A");
    worksheet.GetCells().Get(u"B1").PutValue(u"B");
    worksheet.GetCells().Get(u"C1").PutValue(u"C");
    worksheet.GetCells().Get(u"A2").PutValue(2);
    worksheet.GetCells().Get(u"A3").PutValue(1);
    worksheet.GetCells().Get(u"B2").PutValue(2);
    worksheet.GetCells().Get(u"B3").PutValue(3);
    worksheet.GetCells().Get(u"C2").PutValue(2);
    worksheet.GetCells().Get(u"C3").PutValue(3);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column3D, 9, 6, 25, 16);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Calculate the chart
    chart.Calculate();

    // Add SeriesCollection (chart data source) to the chart ranging from "A2" cell to "C3"
    chart.SetChartDataRange(u"A2:C3", true);

    // Hide the CategoryAxis axis
    chart.GetCategoryAxis().SetIsVisible(false);

    // Hide the ValueAxis axis
    chart.GetValueAxis().SetIsVisible(false);

    // Save the file
    workbook.Save(u"ZAxis.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```
