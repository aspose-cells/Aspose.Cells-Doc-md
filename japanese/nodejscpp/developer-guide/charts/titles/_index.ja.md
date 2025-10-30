---
title: Excelチャートのタイトル管理をNode.js via C++で行う
description: Microsoft Excelでチャートや軸のタイトルを追加・フォーマットする方法をAspose.Cells for Node.js via C++で学びます。さまざまなタイトルの設定方法や見た目の調整、軸タイトルの修正方法を実例とともに解説します。
keywords: Aspose.Cells for Node.js via C++、チャートタイトル、軸タイトル、Microsoft Excel、データ表現、外観。
linktitle: タイトル
type: docs
weight: 50
url: /ja/nodejs-cpp/chart-and-axis-titles/
---

{{% alert color="primary" %}}

Excelチャートには、2種類のタイトルがあります:
1. チャートタイトル 
1. 軸のタイトル

{{% /alert %}}

## **タイトルオプション**
Aspose.Cells for Node.js via C++は、チャートのタイトルをランタイムで管理することも可能です。`Title`オブジェクトを使って、タイトルのテキスト、フォント、塗りつぶしのフォーマットを変更できます。

|![todo:image_alt_text](chart_title.png)|

## **チャートや軸のタイトルの設定**
Microsoft Excelを使えば、WYSIWYG環境でチャートと軸のタイトルを設定できます。Aspose.Cells for Node.js via C++は、開発者が実行時にチャートと軸のタイトルを設定できるようにします。すべてのチャートと軸は`Title`プロパティを持ち、タイトルの設定に利用できます。例を以下に示します。

次のコードスニペットは、チャートと軸にタイトルを設定する方法を示しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(60);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Setting the foreground color of the plot area
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.Blue);

// Setting the foreground color of the chart area
chart.getChartArea().getArea().setForegroundColor(AsposeCells.Color.Yellow);

// Setting the foreground color of the 1st SeriesCollection area
chart.getNSeries().get(0).getArea().setForegroundColor(AsposeCells.Color.Red);

// Setting the foreground color of the area of the 1st SeriesCollection point
chart.getNSeries().get(0).getPoints().get(0).getArea().setForegroundColor(AsposeCells.Color.Cyan);

// Filling the area of the 2nd SeriesCollection with a gradient
chart.getNSeries().get(1).getArea().getFillFormat().setOneColorGradient(AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1);

// Setting the title of a chart
chart.getTitle().setText("Title");

// Setting the font color of the chart title to blue
chart.getTitle().getFont().setColor(AsposeCells.Color.Blue);

// Setting the title of category axis of the chart
chart.getCategoryAxis().getTitle().setText("Category");

// Setting the title of value axis of the chart
chart.getValueAxis().getTitle().setText("Value");

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **高度なトピック**
- [ODSファイルからチャートサブタイトルを読む](/cells/ja/nodejs-cpp/read-chart-subtitle-from-ods-file/)
{{< app/cells/assistant language="nodejs-cpp" >}}
