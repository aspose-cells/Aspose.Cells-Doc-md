---
title: ExcelチャートのDataLabelsをC++で管理する
linktitle: データラベル
type: docs
weight: 50
url: /ja/cpp/insert-datalabels-to-chart/
description: Aspose.Cells for C++を使ったExcelチャートのデータラベル管理方法について学びます。ガイドは、ラベルの追加、削除、変更など、チャートの可読性と操作性を向上させるさまざまな管理タスクをカバーします。
keywords: Aspose.Cells for C++、Excelチャート、データラベル、管理、可読性、使いやすさ、追加、削除、変更。
---

{{% alert color="primary" %}}

 DataLabelsはチャートの重要な部分です。各系列の値や割合などを簡単に知ることができます。

{{% /alert %}}

## **データラベルオプション**
 Aspose.Cellsでは、Runtime時に[DataLabels](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/)オブジェクトを使用して、チャートのデータラベルを管理することも可能です。ラベルの移動、更新、フォーマットも簡単に行えます。

|![todo:image_alt_text](chart_datalabels.png)|

## **データラベルの管理**
 Aspose.Cellsの[DataLabels](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/)を使えば、チャートのデータラベルを簡単に管理できます。

 DataLabelsの管理方法例は次の通りです。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

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

    // Show value labels
    chart.GetNSeries().Get(0).GetDataLabels().SetShowValue(true);

    // Show series name labels
    chart.GetNSeries().Get(1).GetDataLabels().SetShowSeriesName(true);

    // Move labels to center
    chart.GetNSeries().Get(1).GetDataLabels().SetPosition(LabelPositionType::Center);

    // Save the file
    workbook.Save(u"chart_datalabels.xlsx");

    Aspose::Cells::Cleanup();
}
```

## ** 高度なトピック**
- [チャートシリーズのデータポイントにカスタムラベルを追加する](/cells/ja/cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)
- [チャートのデータラベルのテキスト折り返しを無効にする](/cells/ja/cpp/disable-text-wrapping-for-data-labels-of-the-chart/)
- [テキストに合わせるようにチャートのデータラベルの形状をリサイズする](/cells/ja/cpp/resize-chart-s-data-label-shape-to-fit-text/)
- [チャートポイントのリッチテキストカスタムデータラベル](/cells/ja/cpp/rich-text-custom-data-label-of-chart-point/)
- [チャートのデータラベルの形状タイプを設定する](/cells/ja/cpp/set-the-shape-type-of-data-labels-of-chart/)
- [データラベルとしてセル範囲を表示する](/cells/ja/cpp/showing-cell-range-as-the-data-labels/)
