---
title: C++を使った一次・二次軸
linktitle: プライマリおよびセカンダリ軸
description: Aspose.Cells for C++の一次軸と二次軸を理解し操作する方法を学びます。ガイドでは、一次軸と二次軸の違いや、それらを効果的に設定・使用する方法について説明します。
keywords: Aspose.Cells for C++、一次軸、二次軸、理解、違い、設定、使用。
type: docs
weight: 190
url: /ja/cpp/primary-and-second-axis/
---

## **可能な使用シナリオ**
チャート内のデータ系列に数字が大幅に変動したり、データの種類が混在している場合（価格とボリュームなど）、1つ以上のデータ系列をセカンダリ垂直（値）軸にプロットします。セカンダリ垂直軸のスケールは、関連するデータ系列の値を表示します。セカンダリ軸は、列と折れ線グラフが組み合わさったチャートでうまく機能します。

## **Microsoft Excelのようにプライマリおよびセカンダリ軸を処理する**
新しいExcelファイルを作成し、最初のワークシートにチャートの値を配置するサンプルコードをご覧ください。 
次にチャートを追加し、セカンダリ軸を表示します。

![todo:image_alt_text](excel.png)

## **サンプルコード**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put the sample values used in a chart
    worksheet.GetCells().Get(u"A1").PutValue(u"Region");
    worksheet.GetCells().Get(u"A2").PutValue(u"Peking");
    worksheet.GetCells().Get(u"A3").PutValue(u"New York");
    worksheet.GetCells().Get(u"A4").PutValue(u"Paris");
    worksheet.GetCells().Get(u"B1").PutValue(u"Sales Volume");
    worksheet.GetCells().Get(u"C1").PutValue(u"Growth Rate");
    worksheet.GetCells().Get(u"B2").PutValue(100);
    worksheet.GetCells().Get(u"B3").PutValue(80);
    worksheet.GetCells().Get(u"B4").PutValue(140);
    worksheet.GetCells().Get(u"C2").PutValue(0.7);
    worksheet.GetCells().Get(u"C3").PutValue(0.8);
    worksheet.GetCells().Get(u"C4").PutValue(1.0);

    // Create a Scatter chart
    int pieIdx = worksheet.GetCharts().Add(ChartType::Scatter, 6, 6, 15, 11);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Add Series
    chart.GetNSeries().Add(u"B2:C4", true);

    // Set the category data
    chart.GetNSeries().SetCategoryData(u"=Sheet1!$A$2:$A$4");

    // Set the Second-Axis
    chart.GetNSeries().Get(1).SetPlotOnSecondAxis(true);

    // Show the Second-Axis
    chart.GetSecondValueAxis().SetIsVisible(true);

    // Set the second series ChartType to line
    chart.GetNSeries().Get(1).SetType(ChartType::Line);

    // Set the series name
    chart.GetNSeries().Get(0).SetName(u"Sales Volume");
    chart.GetNSeries().Get(1).SetName(u"Growth Rate");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the file
    workbook.Save(u"PrimaryandSecondaryAxis.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
