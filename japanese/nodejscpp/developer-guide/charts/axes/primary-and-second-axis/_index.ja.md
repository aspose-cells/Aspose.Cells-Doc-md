---
title: Node.jsとC++を使用したプライマリとセカンダリ軸の設定
description: Aspose.Cells for Node.js via C++におけるプライマリおよびセカンダリ軸を理解し、それらを効果的に設定・使用する方法を学びましょう。違いを理解するのに役立ちます。
keywords: Aspose.Cells for Node.js via C++、プライマリ軸、セカンダリ軸、理解、違い、設定、使用。
type: docs
weight: 190
url: /ja/nodejs-cpp/primary-and-second-axis/
---

## **可能な使用シナリオ**
チャート内のデータ系列に数字が大幅に変動したり、データの種類が混在している場合（価格とボリュームなど）、1つ以上のデータ系列をセカンダリ垂直（値）軸にプロットします。セカンダリ垂直軸のスケールは、関連するデータ系列の値を表示します。セカンダリ軸は、列と折れ線グラフが組み合わさったチャートでうまく機能します。

## **Microsoft Excelのようにプライマリおよびセカンダリ軸を処理する**
新しいExcelファイルを作成し、最初のワークシートにチャートの値を配置するサンプルコードをご覧ください。 
次にチャートを追加し、セカンダリ軸を表示します。

![todo:image_alt_text](excel.png)

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

// Put the sample values used in a chart
worksheet.getCells().get("A1").putValue("Region");
worksheet.getCells().get("A2").putValue("Peking");
worksheet.getCells().get("A3").putValue("New York");
worksheet.getCells().get("A4").putValue("Paris");
worksheet.getCells().get("B1").putValue("Sales Volume");
worksheet.getCells().get("C1").putValue("Growth Rate");
worksheet.getCells().get("B2").putValue(100);
worksheet.getCells().get("B3").putValue(80);
worksheet.getCells().get("B4").putValue(140);
worksheet.getCells().get("C2").putValue(0.7);
worksheet.getCells().get("C3").putValue(0.8);
worksheet.getCells().get("C4").putValue(1.0);

// Create a Scatter chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Scatter, 6, 6, 15, 11);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Add Series
chart.getNSeries().add("B2:C4", true);
// Set the category data
chart.getNSeries().setCategoryData("=Sheet1!$A$2:$A$4");
// Set the Second-Axis
chart.getNSeries().get(1).setPlotOnSecondAxis(true);
// Show the Second-Axis
chart.getSecondValueAxis().setIsVisible(true);
// Set the second series ChartType to line
chart.getNSeries().get(1).setType(AsposeCells.ChartType.Line);
// Set the series name
chart.getNSeries().get(0).setName("Sales Volume");
chart.getNSeries().get(1).setName("Growth Rate");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Fill the PlotArea area with nothing
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the file
workbook.save("PrimaryandSecondaryAxis.xlsx");
```
