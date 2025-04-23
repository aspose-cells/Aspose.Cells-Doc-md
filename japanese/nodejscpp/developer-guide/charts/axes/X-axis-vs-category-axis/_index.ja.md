---
title: X軸とカテゴリ軸の違いを理解する方法[Node.js+C++]
linktitle: X軸 vs カテゴリ軸
description: Aspose.Cells for Node.js via C++におけるX軸とカテゴリ軸の違いを学びましょう。使い方やプロパティの違い、その設定方法について理解を深めることができます。
keywords: Aspose.Cells for Node.js via C++、X軸、カテゴリ軸、違い、用途、プロパティ、設定。
type: docs
weight: 180
url: /ja/nodejs-cpp/X-axis-vs-category-axis/
---

## **可能な使用シナリオ**
X軸には異なるタイプがあります。Y軸が値タイプの軸であるのに対し、X軸はカテゴリタイプの軸または値タイプの軸であることができます。値軸を使用すると、データは連続的に変化する数値データとして扱われ、マーカーは数値に応じて軸上の位置に配置されます。カテゴリ軸を使用すると、データは数値ではないテキストラベルの連続として扱われ、マーカーはシーケンス内の位置に応じて軸上の位置に配置されます。以下のサンプルは、値軸とカテゴリ軸の違いを示しています。
サンプルデータは以下の[サンプルテーブルファイル](sample.png)で表示されています。最初の列にはX軸データが含まれており、これはカテゴリまたは値として扱うことができます。数字は等間隔ではなく、数値の順序に従っているわけでもありません。

![todo:image_alt_text](sample.png)
## **Microsoft ExcelのようにX軸とカテゴリ軸を処理する**
このデータは二つのタイプのチャートに表示されます。一つはXY（散布図）チャートでX軸は値軸、もう一つは折れ線グラフでX軸はカテゴリ軸です。

![todo:image_alt_text](compare.png)
## **サンプルコード**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Put the sample values used in charts
worksheet.getCells().get("A2").putValue(1);
worksheet.getCells().get("A3").putValue(3);
worksheet.getCells().get("A4").putValue(2.5);
worksheet.getCells().get("A5").putValue(3.5);
worksheet.getCells().get("B1").putValue("Cats");
worksheet.getCells().get("C1").putValue("Dogs");
worksheet.getCells().get("D1").putValue("Fishes");
worksheet.getCells().get("B2").putValue(7);
worksheet.getCells().get("B3").putValue(6);
worksheet.getCells().get("B4").putValue(5);
worksheet.getCells().get("B5").putValue(4);
worksheet.getCells().get("C2").putValue(7);
worksheet.getCells().get("C3").putValue(5);
worksheet.getCells().get("C4").putValue(4);
worksheet.getCells().get("C5").putValue(3);
worksheet.getCells().get("D2").putValue(8);
worksheet.getCells().get("D3").putValue(7);
worksheet.getCells().get("D4").putValue(3);
worksheet.getCells().get("D5").putValue(2);

// Create Line Chart: X as Category Axis
let pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.LineWithDataMarkers, 6, 15, 20, 21);
// Retrieve the Chart object
let chart = worksheet.getCharts().get(pieIdx);
// Add Series
chart.getNSeries().add("B2:D5", true);
// Set the category data
chart.getNSeries().setCategoryData("=Sheet1!$A$2:$A$5");
// Set the first series name
chart.getNSeries().get(0).setName("Cats");
// Set the second series name
chart.getNSeries().get(1).setName("Dogs");
// Set the third series name
chart.getNSeries().get(2).setName("Fishes");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);

// Create XY (Scatter) Chart: X as Value Axis
pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.ScatterConnectedByLinesWithDataMarker, 6, 6, 20, 12);
// Retrieve the Chart object
chart = worksheet.getCharts().get(pieIdx);
// Add Series
chart.getNSeries().add("B2:D5", true);
// Set X values for series 
chart.getNSeries().get(0).setXValues("{1,3,2.5,3.5}");
chart.getNSeries().get(1).setXValues("{1,3,2.5,3.5}");
chart.getNSeries().get(2).setXValues("{1,3,2.5,3.5}");
// Set the first series name
chart.getNSeries().get(0).setName("Cats");
// Set the second series name
chart.getNSeries().get(1).setName("Dogs");
// Set the third series name
chart.getNSeries().get(2).setName("Fishes");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("XAxis.xlsx");
```
