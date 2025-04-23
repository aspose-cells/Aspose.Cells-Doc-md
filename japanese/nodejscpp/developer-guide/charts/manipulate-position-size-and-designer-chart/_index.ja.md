---
title: 位置・サイズ・デザイナーチャートをNode.js経由で操作
linktitle: 位置、サイズ、およびデザインチャートを操作
description: Microsoft ExcelでAspose.Cells for Node.js via C++を使い、位置やサイズ、デザイナーチャートを効果的に操作する方法を学びましょう。当ガイドでは、これらのプロパティを調整してレイアウトや視覚化を改善する方法を示します。
keywords: Aspose.Cells for Node.js via C++、位置、サイズ、デザイナーチャート、Microsoft Excel、レイアウト、視覚化。
type: docs
weight: 45
url: /ja/nodejs-cpp/manipulate-position-size-and-designer-chart/
---

## **チャートの位置とサイズ**
時には、ワークシート内の新旧チャートの位置やサイズを変更したい場合があります。Aspose.Cellsは [Chart.getChartObject()](https://reference.aspose.com/cells/nodejs-cpp/chart/#getChartObject--) プロパティを提供してこれを実現します。これのサブプロパティを使用して、新しい **高さ** と **幅** でチャートのリサイズや、新しい **X** と **Y** の座標で再配置が可能です。

### **チャートの位置とサイズの制御**
チャートの位置（X、Y座標）またはサイズ（高さ、幅）を変更するには、これらのプロパティを使用します。

1. [Shape.getX()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getX--)
1. [Shape.getY()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getY--)
1. [Shape.getHeight()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getHeight--)
1. [Shape.getWidth()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getWidth--)

上記のAPIの使用例では、既存のワークブックにチャートが含まれる最初のワークシートをロードし、そのチャートのサイズ変更と位置変更をAspose.Cellsを使って行っています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "chart.xls");

// Loads the workbook which contains the chart
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(1);

// Load the chart from source worksheet
const chart = worksheet.getCharts().get(0);

// Resize the chart
chart.getChartObject().setWidth(400);
chart.getChartObject().setHeight(300);

// Reposition the chart
chart.getChartObject().setX(250);
chart.getChartObject().setY(150);

// Output the file
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **デザイナーチャートの操作**
テンプレートファイル内のチャートを操作・変更する必要がある場合もあります。Aspose.Cellsは、デザイナーチャートの内容や要素の操作を完全にサポートしており、データ、チャート内容、背景画像、書式設定を正確に保持します。

### **テンプレートファイル内のデザイナーチャートを操作する**
テンプレートファイルのデザイナーチャートを操作するには、チャート関連のAPIを使用してください。例えば、Worksheet.charts プロパティを使用して、テンプレートファイル内の既存のチャートコレクションを取得できます。

#### **チャートの作成**
次の例は、ピラミッドチャートの作成方法を示しています。このチャートを後で操作します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Pyramid, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

#### **チャートの操作**
次の例は、既存のチャートの操作方法を示しています。この例では、上記で作成したチャートを変更します。生成された出力では、1つのデータポイントの日付ラベルが 'United Kingdom, 30K' に設定されていることに注意してください。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "piechart.xls");

// Loads the existing file.
const workbook = new AsposeCells.Workbook(filePath);

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(1);
const chart = sheet.getCharts().get(0);

// Get the data labels in the data series of the third data point.
const dataLabels = chart.getNSeries().get(0).getPoints().get(2).getDataLabels();

// Change the text of the label.
dataLabels.setText("Unided Kingdom, 400K ");

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```

#### **デザイナーテンプレート内の折れ線グラフの操作**
この例では、折れ線グラフを操作します。既存のチャートにいくつかのデータシリーズを追加し、それらの線の色を変更します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Get the designer chart in the first worksheet.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Add the third data series to it.
chart.getNSeries().add("{60, 80, 10}", true);

// Add another data series (fourth) to it.
chart.getNSeries().add("{0.3, 0.7, 1.2}", true);

// Plot the fourth data series on the second axis.
chart.getNSeries().get(3).setPlotOnSecondAxis(true);

// Change the Border color of the second data series.
chart.getNSeries().get(1).getBorder().setColor(AsposeCells.Color.Green);

// Change the Border color of the third data series.
chart.getNSeries().get(2).getBorder().setColor(AsposeCells.Color.Red);

// Make the second value axis visible.
chart.getSecondValueAxis().setIsVisible(true);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```

