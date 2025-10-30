---
title: Node.jsとC++を利用したガントチャートの作成方法
linktitle: ガントチャートの作成方法
type: docs
weight: 72
url: /ja/nodejs-cpp/how-to-create-gantt-chart/
description: Aspose.Cells for Node.js via C++ APIを使用したガントチャートの作り方を学びましょう。
keywords: Node.jsでガントチャートを作成、ガントチャートを追加、挿入
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

1. チャートを選択し、「データの選択」 -> 「追加」をクリックし、「シリーズ名」と「シリーズ値」を設定します。
<br>
<img src="2.png" width=50% />

1. グラフを選択し、**横軸（カテゴリ）軸ラベルの編集**を行います。
<br>
<img src="3.png" width=50% />

1. Y軸の**軸の書式設定**で、**逆順にカテゴリ**を選択します。
1. 「ブルーシリーズ」を選択し、「塗りつぶし -> 塗りつぶしなし」を設定します。
1. X軸の「軸の書式設定」を行い、「最小値」と「最大値」を設定します（例：1/5/2019:43470、1/30/2019:43494）。
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

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Create BarStacked Chart
const i = worksheet.getCharts().add(AsposeCells.ChartType.BarStacked, 5, 6, 20, 15);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(i);
// Set the chart title name 
chart.getTitle().setText("Gantt Chart");
// Set the chart title is Visible
chart.getTitle().setIsVisible(true);
// Set data range
chart.setChartDataRange("B1:B6", true);
// Add series data range
chart.getNSeries().add("C2:C6", true);
// No fill for one serie
chart.getNSeries().get(0).getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Set the Horizontal(Category) Axis
chart.getNSeries().setCategoryData("A2:A6");
// Reverse the Horizontal(Category) Axis
chart.getCategoryAxis().setIsPlotOrderReversed(true);
// Set the value axis's MinValue and MaxValue
const minValue = parseFloat(worksheet.getCells().get("B2").getValue());
const maxValue = parseFloat(worksheet.getCells().get("D6").getValue());
chart.getValueAxis().setMinValue(isNaN(minValue) ? 0 : minValue);
chart.getValueAxis().setMaxValue(isNaN(maxValue) ? 0 : maxValue);
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Show the DataLabels
chart.getNSeries().get(1).getDataLabels().setShowValue(true);
// Disable the Legend
chart.setShowLegend(false);
// Save the result
workbook.save("result.xlsx");
```

{{< app/cells/assistant language="nodejs-cpp" >}}
