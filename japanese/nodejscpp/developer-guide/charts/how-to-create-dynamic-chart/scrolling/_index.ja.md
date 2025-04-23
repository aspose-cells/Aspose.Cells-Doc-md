---
title: Node.jsを使用したC++によるダイナミックスクロールチャートの作成方法
linktitle: 動的なスクロールチャートの作成方法
description: Aspose.Cells for Node.js via C++を使用してダイナミックスクロールチャートを作成する方法を学びましょう。ステップバイステップのガイドでは、スムースなデータ遷移と自動スクロールを実現し、継続的で更新された表示を行う方法を示します。
keywords: Aspose.Cells for Node.js、ダイナミックスクロールチャート、データ遷移、スムーススクロール、連続表示、更新ビジュアライゼーション。
type: docs
weight: 75
url: /ja/nodejs-cpp/create-dynamic-scrolling-chart/
---

## **可能な使用シナリオ**
動的スクロールチャートは、時間の経過とともに変化するデータを表示するためのグラフ表現の一種です。リアルタイムのデータ表示を提供するよう設計されており、ユーザーが連続的な更新やトレンドを追跡できます。新しいデータが追加されると、チャートは自動的に更新され、最新の情報を表示します。

動的スクロールチャートは、ファイナンス、株式市場分析、気象追跡、ソーシャルメディア分析など、さまざまな産業で一般的に使用されます。リアルタイム情報に基づいた、データパターンの視覚化と分析をユーザーが行い、的確な意思決定を行うことができます。

これらのチャートは通常、インタラクティブであり、ユーザーがズームインまたはズームアウト、過去のデータをスクロール、時間間隔を調整することができます。通常、複数のデータシリーズをサポートし、異なるメトリクスおよび相関を包括的に表示します。

全体として、動的スクロールチャートは、時系列データのモニタリングと分析に貴重なツールであり、リアルタイムの意思決定を容易にし、データの可視化能力を向上させるものです。

## **Aspose.Cellsを使用してダイナミックスクロールチャートを作成する**
次の段落では、Aspose.Cells for Node.js via C++を使ったダイナミックスクロールチャートの作成方法をご紹介します。例のコードと、このコードで作成されたExcelファイルも示します。

## **サンプルコード**
次のサンプルコードは[DynamicScrollingChart.xlsx]を生成します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Your local test path
const localPath = "";

// Create a new workbook and access the first worksheet.
const workbook = new AsposeCells.Workbook();
const sheets = workbook.getWorksheets();
const sheet = sheets.get(0);

// Populate the data for the chart. Add values to cells and set series names.
sheet.getCells().get("A1").putValue("Day");
sheet.getCells().get("B1").putValue("Sales");
// In this example, we will add 30 days of data
const allDays = 30;
const showDays = 10;
let currentDay = 1;

for (let i = 0; i < allDays; i++) {
const cellA = `A${i + 2}`;
const cellB = `B${i + 2}`;
sheet.getCells().get(cellA).putValue(i + 1);
sheet.getCells().get(cellB).putValue(50 * (i % 2) + 20 * (i % 3) + 10 * Math.floor(i / 3));
}

// This is the Dynamic Scrolling Control Data
sheet.getCells().get("G19").putValue("Start Day");
sheet.getCells().get("G20").putValue(currentDay);
sheet.getCells().get("H19").putValue("Show Days");
sheet.getCells().get("H20").putValue(showDays);

// Set the dynamic range for the chart's data source. 
let index = sheets.getNames().add("Sheet1!ChtScrollData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

// Set the dynamic range for the chart's data labels. 
index = sheets.getNames().add("Sheet1!ChtScrollLabels");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

// Add a ScrollBar for the Dynamic Scrolling Chart
const bar = sheet.getShapes().addScrollBar(2, 0, 3, 0, 200, 30);
bar.setMin(0);
bar.setMax(allDays - showDays);
bar.setCurrentValue(currentDay);
bar.setLinkedCell("$G$20");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Line, 2, 4, 15, 10);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("Sales", true);
chart.getNSeries().get(0).setValues("Sheet1!ChtScrollData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtScrollLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicScrollingChart.xlsx"));
```

## **メモ**
生成されたファイルでは、スクロールバーを操作できます。このとき、チャートは最新の10つのデータセットを動的にカウントします。これは、例のコードの「OFFSET」式を使用して行います。

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

セル "Sheet1!$H$20"の数値"10"を"15"に変更してみると、ダイナミックチャートが最新の15セットのデータをカウントします。これでAspose.Cells for Node.js via C++を使用したダイナミックスクロールチャートの作成に成功しました。
