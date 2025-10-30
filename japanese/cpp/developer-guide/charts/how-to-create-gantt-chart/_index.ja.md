---
title: C++でガントチャートを作成する方法
linktitle: ガントチャートの作成方法
type: docs
weight: 72
url: /ja/cpp/how-to-create-gantt-chart/
description: Aspose.Cells for C++ APIを使ったガントチャート作成方法を学びます。
keywords: C++でガントチャートを作成し、追加し、挿入する方法
---

## **ガントチャートとは何ですか**

ガントチャートは、プロジェクトスケジュールを示す棒グラフの一種です。各作業やアクティビティの開始・終了日を示し、その長さは期間に対応しています。タスク間の依存関係も示し、プロジェクトマネージャーが作業の順序を視覚化できるようにします。広くプロジェクト管理に利用され、計画・スケジューリング・進行状況の追跡に役立ちます。

## **Excelでガントチャートを作成する方法**

Excelでガントチャートを作成するには、次の手順に従います:
1. ガントチャート用のデータを追加します。 
<br>
<img src="00.png" width=50% />
1. データを選択し、「挿入」→「グラフ」→「積み上げ縦棒グラフ」→「積み上げ横棒グラフ」を選びます。例として、B1:B7を選択し、「積み上げ縦棒」グラフを挿入します。
<br>
<img src="1.png" width=50% />

1. グラフを選択し、「データの追加」を選択します。次に、**系列名**と**系列値**を以下のように設定します。
<br>
<img src="2.png" width=50% />

1. グラフを選択し、**横軸（カテゴリ）軸ラベルの編集**を行います。
<br>
<img src="3.png" width=50% />

1. Y軸の**軸の書式設定**で、**逆順にカテゴリ**を選択します。
1. **青い系列**を選択し、「塗りつぶし→塗りつぶしなし」を設定します。
1. X軸についても**軸の書式設定**を行い、**最小値**と**最大値**を設定します（例：2019年1月5日：43470、2019年1月30日：43494）。
<br>
<img src="4.png" width=50% />

1. グラフに**データラベルを追加**すると、ガントチャートが完成します。
<br>
<img src="0.png" width=50% />


## **Aspose.Cellsでガントチャートを追加する方法**
以下のサンプルコードをご覧ください。サンプルExcelファイル（sample.xlsx）を読み込み、サンプルデータが含まれています。その後、初期データに基づいた積み上げ棒グラフを作成し、関連する設定を行います。最後に、Excelファイル（結果のxlsx）として保存します。以下のスクリーンショットは、Aspose.Cellsが作成したガントチャートです。
<br>
<img src="5.png" width=60% />

### **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create BarStacked Chart
    int32_t chartIndex = worksheet.GetCharts().Add(ChartType::BarStacked, 5, 6, 20, 15);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Set the chart title name
    chart.GetTitle().SetText(u"Gantt Chart");

    // Set the chart title visibility
    chart.GetTitle().SetIsVisible(true);

    // Set data range
    chart.SetChartDataRange(u"B1:B6", true);

    // Add series data range
    chart.GetNSeries().Add(u"C2:C6", true);

    // No fill for one series
    chart.GetNSeries().Get(0).GetArea().GetFillFormat().SetFillType(FillType::None);

    // Set the Horizontal(Category) Axis
    chart.GetNSeries().SetCategoryData(u"A2:A6");

    // Reverse the Horizontal(Category) Axis
    chart.GetCategoryAxis().SetIsPlotOrderReversed(true);

    // Set the value axis's MinValue and MaxValue
    chart.GetValueAxis().SetMinValue(worksheet.GetCells().Get(u"B2").GetValue());
    chart.GetValueAxis().SetMaxValue(worksheet.GetCells().Get(u"D6").GetValue());

    // Set the PlotArea with no fill
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Show the DataLabels
    chart.GetNSeries().Get(1).GetDataLabels().SetShowValue(true);

    // Disable the Legend
    chart.SetShowLegend(false);

    // Save the result
    workbook.Save(u"result.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{< app/cells/assistant language="cpp" >}}
