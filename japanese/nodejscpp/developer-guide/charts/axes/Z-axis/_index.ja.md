---
title: Z軸に関する情報【Node.js+C++】
description: Aspose.Cells for Node.js via C++におけるZ軸の扱い方を学びましょう。スケールやラベルなどの設定とカスタマイズ方法についてガイドします。
keywords: Aspose.Cells for Node.js via C++、Z軸、チャート作成、設定、カスタマイズ、スケール、ラベル。
type: docs
weight: 210
url: /ja/nodejs-cpp/z-axis/
---

## **可能な使用シナリオ**
3D柱、3D円錐、3Dピラミッドなどの一部の3Dチャートには深さ（シリーズ）軸、別名Z軸があります。これを変更可能で、ティックマークの間隔や軸のラベルなどを指定できます。

## **プライマリとセカンダリ軸の扱い【Microsoft Excelと同等】**
次のサンプルコードをご覧ください。新しいExcelファイルを作成し、最初のワークシートにチャートの値を設定します。次に、チャートを追加し、チャートタイプをColumn3Dに設定します。すると、Z軸（深さ軸）も表示されます。 

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
// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Put values to cells for creating chart
worksheet.getCells().get("A1").putValue("A");
worksheet.getCells().get("B1").putValue("B");
worksheet.getCells().get("C1").putValue("C");
worksheet.getCells().get("A2").putValue(2);
worksheet.getCells().get("A3").putValue(1);
worksheet.getCells().get("B2").putValue(2);
worksheet.getCells().get("B3").putValue(3);
worksheet.getCells().get("C2").putValue(2);
worksheet.getCells().get("C3").putValue(3);
// Add a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column3D, 9, 6, 25, 16);
// Access the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Calculate the chart
chart.calculate();
// Add SeriesCollection (chart data source) to the chart ranging from "A2" cell to "C3"
chart.setChartDataRange("A2:C3", true);
// Hide the CategoryAxis axis
chart.getCategoryAxis().setIsVisible(false);
// Hide the ValueAxis axis
chart.getValueAxis().setIsVisible(false);
// Save the file
workbook.save("ZAxis.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
