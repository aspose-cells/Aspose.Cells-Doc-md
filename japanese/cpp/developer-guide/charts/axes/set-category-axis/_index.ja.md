---
title: C++を使ったカテゴリ軸の設定方法
linktitle: カテゴリ軸の設定方法
description: Aspose.Cells for C++でカテゴリ軸を設定する方法を学びます。ガイドでは、カテゴリ軸の範囲の定義、プロパティの調整、ラベルのフォーマット方法について説明します。
keywords: Aspose.Cells for C++、カテゴリ軸、設定、範囲、プロパティ、フォーマット
type: docs
weight: 205
url: /ja/cpp/how-to-set-category-axis/
---

## **可能な使用シナリオ**
ワークシート内にチャートを作成した後、そのチャートのカテゴリ軸を設定できます。この記事では、Aspose.Cellsを使用したExcelチャートのカテゴリ軸設定方法をサンプルコードとともに紹介します。

## **サンプルコードの手順**

1. 新しいブックを作成します。

2. 最初のワークシートで新しいチャートを作成します。

3. 最初のワークシートのセルにいくつかの値を追加します。

4. これでカテゴリ軸を設定できます。セルデータを使う方法と文字列を直接使う方法の2つをサンプルコードで示します。

5. 値軸を設定し、結果を確認するためにワークブックを保存します。

## **サンプルコード**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Your local test path
    U16String path = u"";

    // Create a new workbook
    Workbook workbook;
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);
    worksheet.SetName(u"CHART");

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 8, 0, 20, 10);
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add some values to cells
    worksheet.GetCells().Get(u"A1").PutValue(u"Sales");
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"A4").PutValue(130);
    worksheet.GetCells().Get(u"A5").PutValue(160);
    worksheet.GetCells().Get(u"A6").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(u"Days");
    worksheet.GetCells().Get(u"B2").PutValue(1);
    worksheet.GetCells().Get(u"B3").PutValue(2);
    worksheet.GetCells().Get(u"B4").PutValue(3);
    worksheet.GetCells().Get(u"B5").PutValue(4);
    worksheet.GetCells().Get(u"B6").PutValue(5);

    // Some values in string
    U16String Sales = u"100,150,130,160,150";
    U16String Days = u"1,2,3,4,5";

    // Set Category Axis Data with string
    chart.GetNSeries().SetCategoryData(u"{" + Days + u"}");
    // Or you can set Category Axis Data with data in cells, try it!
    // chart.GetNSeries().SetCategoryData(u"B2:B6");

    // Add Series to the chart
    chart.GetNSeries().Add(u"Demand1", true);
    // Set value axis with string 
    chart.GetNSeries().Get(0).SetValues(u"{" + Sales + u"}");
    chart.GetNSeries().Add(u"Demand2", true);
    // Set value axis with data in cells
    chart.GetNSeries().Get(1).SetValues(u"A2:A6");

    // Set some Category Axis properties
    chart.GetCategoryAxis().GetTickLabels().SetRotationAngle(45);
    chart.GetCategoryAxis().GetTickLabels().GetFont().SetSize(8);
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Save the workbook to view the result file
    workbook.Save(path + u"Output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
