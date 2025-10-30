---
title: Node.jsをC++経由でExcelチャートの凡例を管理
description: Microsoft Excelでチャートの凡例を効果的に利用・カスタマイズするためにAspose.Cells for Node.js via C++を使用する方法を学びましょう。包括的なガイドでは、凡例の機能、アクセス方法、変更方法、さらには凡例を使った可視化とデータ理解の向上について説明します。
keywords: Aspose.Cells for Node.js via C++、チャート凡例、Microsoft Excel、可視化、データ理解。
linktitle: 凡例
type: docs
weight: 50
url: /ja/nodejs-cpp/chart-legend/
---

## **凡例オプション**
Aspose.Cells for Node.js via C++は、実行時にチャートの凡例を管理することも可能です。 [Legend](https://reference.aspose.com/cells/nodejs-cpp/legend/) オブジェクトは移動、更新、書式設定ができます。

|![todo:image_alt_text](chart_legend.png)|

## **チャートの凡例の設定**
Aspose.Cellsの [Legend](https://reference.aspose.com/cells/nodejs-cpp/legend/) を利用して、チャートの凡例を簡単に管理できます。

凡例管理のためのコードスニペットは次のとおりです：


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

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

// Setting the title of a chart
chart.getTitle().setText("Title");

// Setting the font color of the chart title to blue
chart.getTitle().getFont().setColor(AsposeCells.Color.Blue);

// Move the legend to left
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Left);

// Set font color of the legend
chart.getLegend().getFont().setColor(AsposeCells.Color.Blue);

// Save the file
workbook.save("chart_legend.xlsx");
```

## **高度なトピック**
- [Aspose.Cellsを使用して、チャートの凡例エントリの塗りをなしに設定する方法を説明します。](/cells/ja/nodejs-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/)
{{< app/cells/assistant language="nodejs-cpp" >}}
