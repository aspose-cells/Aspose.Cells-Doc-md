---
title: Node.js経由でC++を使ったダイナミックローリングチャートの作成方法
linktitle: 動的ローリングチャートの作成方法
description: Aspose.Cells for Node.js via C++を使用したダイナミックローリングチャートの作成方法を学びます。ガイドは、スムーズなデータ遷移とローリング平均を実装し、連続性と最新状態を保つチャートの作り方を示します。
keywords: Aspose.Cells for Node.js、ダイナミックローリングチャート、データ遷移、スムース平均、連続表示、更新されたビジュアライゼーション。
type: docs
weight: 74
url: /ja/nodejs-cpp/create-dynamic-rolling-chart/
---

## **可能な使用シナリオ**
動的ローリングチャートとは、データポイントが常にシフトして更新されるグラフィカルな表現を指します。このタイプのチャートは継続的に自動更新され、新しいデータポイントが追加されると古いデータポイントは破棄されます。

動的ローリングチャートは、リアルタイムやストリーミングデータのトレンドやパターンを可視化するために一般的に使用されます。株式市場の分析、気象モニタリング、またはライブパフォーマンスの追跡など、時間的な側面や時間の経過に伴う変化が重要なシナリオで特に有用です。

これらのチャートは通常、アニメーションや自動スクロールのメカニズムを使用して、常に最新の情報が表示されるようにしています。ローリングウィンドウの長さは、過去の1時間、1日、または1週間など、特定の時間期間を表示するようにカスタマイズできます。

要約すると、動的なローリングチャートは、古いデータを破棄しながら最新のデータポイントを表示する連続的に更新されるグラフ表現であり、ユーザーがリアルタイムのトレンドやパターンを観察することができます。

## **Aspose Cellsを使用して動的なローリングチャートを作成する**
次の段落では、Aspose.Cellsを使用して動的なローリングチャートを作成する方法を示します。例のコードと、このコードで作成されたExcelファイルも表示します。

## **サンプルコード**
次のサンプルコードは[DynamicRollingChart.xlsx]を生成します。

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
sheet.getCells().get("A1").putValue("Month");
sheet.getCells().get("A2").putValue(1);
sheet.getCells().get("A3").putValue(2);
sheet.getCells().get("A4").putValue(3);
sheet.getCells().get("A5").putValue(4);
sheet.getCells().get("A6").putValue(5);
sheet.getCells().get("A7").putValue(6);
sheet.getCells().get("A8").putValue(7);

sheet.getCells().get("B1").putValue("Sales");
sheet.getCells().get("B2").putValue(50);
sheet.getCells().get("B3").putValue(45);
sheet.getCells().get("B4").putValue(55);
sheet.getCells().get("B5").putValue(60);
sheet.getCells().get("B6").putValue(55);
sheet.getCells().get("B7").putValue(65);
sheet.getCells().get("B8").putValue(70);

// Set the dynamic range for the chart's data source.
let index = sheets.getNames().add("Sheet1!ChtData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)");

// Set the dynamic range for the chart's data labels.
index = sheets.getNames().add("Sheet1!ChtLabels");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Line, 10, 3, 25, 10);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("Sales", true);
chart.getNSeries().get(0).setValues("Sheet1!ChtData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicRollingChart.xlsx"));
```

## **メモ**
生成されたファイルでは、列Aと列Bにデータを追加できます。これに対し、チャートは最新の5つのデータセットを動的にカウントします。これは、例のコードの「OFFSET」式を使用して行います。

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

数式の中の数値「-5」を「-10」に変更してみると、動的チャートは最新の10つのデータセットをカウントします。これでAspose.Cellsを使用して動的なローリングチャートを作成しました。
{{< app/cells/assistant language="nodejs-cpp" >}}
