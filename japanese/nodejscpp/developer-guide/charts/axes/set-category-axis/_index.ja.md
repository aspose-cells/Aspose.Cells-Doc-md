---
title: Node.jsとC++を使用したカテゴリ軸の設定方法
linktitle: カテゴリ軸の設定方法
description: Aspose.Cells for Node.js via C++でカテゴリ軸を設定する方法を学びましょう。ガイドは、カテゴリ軸の範囲の定義、プロパティの調整、ラベルのフォーマットについて説明します。
keywords: Aspose.Cells for Node.js via C++、カテゴリ軸、設定、範囲、プロパティ、フォーマット。
type: docs
weight: 205
url: /ja/nodejs-cpp/how-to-set-category-axis/
---

## **可能な使用シナリオ**
ワークシート内にチャートを作成した後、そのチャートのカテゴリ軸を設定できます。この記事では、Aspose.Cellsを使用したExcelチャートのカテゴリ軸設定方法をサンプルコードとともに紹介します。

## **サンプルコードの手順**

1. 新しいブックを作成します。

2. 最初のワークシートで新しいチャートを作成します。

3. 最初のワークシートのセルにいくつかの値を追加します。

4. これでカテゴリ軸を設定できます。セルデータを使用する方法と文字列を直接使用する二つの方法がサンプルコードで示されています。

5. 値軸を設定し、結果を確認するためにワークブックを保存します。

## **サンプルコード**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Your local test path
const dataDir = ""; // Update with your path

// Create a new workbook
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CHART");

// Add a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 8, 0, 20, 10);
const chart = worksheet.getCharts().get(chartIndex);

// Add some values to cells
worksheet.getCells().get("A1").putValue("Sales");
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("A4").putValue(130);
worksheet.getCells().get("A5").putValue(160);
worksheet.getCells().get("A6").putValue(150);
worksheet.getCells().get("B1").putValue("Days");
worksheet.getCells().get("B2").putValue(1);
worksheet.getCells().get("B3").putValue(2);
worksheet.getCells().get("B4").putValue(3);
worksheet.getCells().get("B5").putValue(4);
worksheet.getCells().get("B6").putValue(5);

// Some values in string
const Sales = "100,150,130,160,150";
const Days = "1,2,3,4,5";

// Set Category Axis Data with string
chart.getNSeries().setCategoryData(`{${Days}}`);
// Or you can set Category Axis Data with data in cells
// chart.getNSeries().setCategoryData("B2:B6");

// Add Series to the chart
chart.getNSeries().add("Demand1", true);
// Set value axis with string 
chart.getNSeries().get(0).setValues(`{${Sales}}`);
chart.getNSeries().add("Demand2", true);
// Set value axis with data in cells
chart.getNSeries().get(1).setValues("A2:A6");

// Set some Category Axis properties
chart.getCategoryAxis().getTickLabels().setRotationAngle(45);
chart.getCategoryAxis().getTickLabels().getFont().setSize(8);
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);

// Save the workbook to view the result file
workbook.save(path + "Output.xlsx");
```
