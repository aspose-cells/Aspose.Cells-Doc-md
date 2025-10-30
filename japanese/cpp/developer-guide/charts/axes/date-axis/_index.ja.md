---
title: C++を使った日付軸の設定
linktitle: 日付軸
description: Aspose.Cells for C++で日付軸を管理する方法を学びます。ガイドは、さまざまな日付フォーマット、時間スケール、ティックラベルの頻度の取り扱い方を理解するのに役立ちます。
keywords: Aspose.Cells for C++、日付軸、管理、日付フォーマット、時間スケール、ティックラベルの頻度。
type: docs
weight: 200
url: /ja/cpp/date-axis/
---

## **可能な使用シナリオ**
作成するチャートが日付を使用している場合、そしてチャートの横軸（カテゴリ軸）にプロットされている場合、Aspose.Cellsは自動的にカテゴリ軸を日付（タイムスケール）軸に変更します。
日付軸は、特定の間隔や基本単位（日数、月、年など）で、ワークシートの日付を年代順に表示します。ワークシート上の日付が順次に並んでいない場合や基本単位が同じでない場合でも、表示されます。
デフォルトでは、Aspose.Cellsは、ワークシートデータ内の任意の2つの日付間の最小差に基づいて日付軸の基本単位を決定します。例えば、株価データの最小日差が7日間の場合、Aspose.Cellsは基本単位を「日」に設定しますが、より長い期間のパフォーマンスを見る場合には、月または年に変更可能です。

## **Microsoft Excelのように日付軸を処理する**
新しいExcelファイルを作成し、最初のワークシートにチャートの値を配置するサンプルコードをご覧ください。 
その後、チャートを追加し、[**Axis**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/)の種類を設定します。 
[**TimeScale**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/categorytype/)のタイプを設定し、その後基本単位を日に設定します。

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

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add the sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(u"Date");

    // 14 means datetime format
    Style style = worksheet.GetCells().GetStyle();
    style.SetNumber(14);

    // Put values to cells for creating chart
    worksheet.GetCells().Get(u"A2").SetStyle(style);
    worksheet.GetCells().Get(u"A2").PutValue(Date{2022, 6, 26, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"A3").SetStyle(style);
    worksheet.GetCells().Get(u"A3").PutValue(Date{2022, 5, 22, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"A4").SetStyle(style);
    worksheet.GetCells().Get(u"A4").PutValue(Date{2022, 8, 3, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"B1").PutValue(u"Price");
    worksheet.GetCells().Get(u"B2").PutValue(40);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(60);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 9, 6, 21, 13);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.SetChartDataRange(u"A1:B4", true);

    // Set the Axis type to Date time
    chart.GetCategoryAxis().SetCategoryType(CategoryType::TimeScale);

    // Set the base unit for CategoryAxis to days
    chart.GetCategoryAxis().SetBaseUnitScale(TimeUnit::Days);

    // Set the direction for the axis text to be vertical
    chart.GetCategoryAxis().GetTickLabels().SetDirectionType(ChartTextDirectionType::Vertical);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Set max value of Y axis
    chart.GetValueAxis().SetMaxValue(70);

    // Set major unit
    chart.GetValueAxis().SetMajorUnit(10);

    // Save the file
    workbook.Save(u"DateAxis.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
