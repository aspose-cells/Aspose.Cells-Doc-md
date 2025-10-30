---  
title: Node.jsとC++を使用してExcelチャートのDataLabelsを管理する  
description: Aspose.Cells for Node.js via C++を使用してExcelチャートのデータラベルを効果的に管理する方法について学びましょう。この包括的ガイドは、ラベルの追加、削除、および修正を含むさまざまな管理タスクをカバーし、チャートの可読性と使いやすさを向上させます。  
keywords: Aspose.Cells for Node.js、Excelチャート、データラベル、管理、可読性、使いやすさ、追加、削除、修正。  
linktitle: データラベル  
type: docs  
weight: 50  
url: /ja/nodejs-cpp/insert-datalabels-to-chart/  
---  

{{% alert color="primary" %}}  

データラベルはチャートの重要な部分です。  
各シリーズの値、パーセンテージなどを簡単に把握できます。  

{{% /alert %}}  

## **データラベルオプション**  
Aspose.Cells for Node.js via C++では、DataLabelsオブジェクトを使用してチャートのデータラベルをランタイムで管理できます。簡単に移動、更新、フォーマットが可能です。  

|![todo:image_alt_text](chart_datalabels.png)|  

## **データラベルの管理**  
Aspose.CellsのDataLabelsを使用すると、チャートのデータラベルの管理は簡単です。  

 DataLabelsの管理方法例は次の通りです。  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

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

// Show value labels
chart.getNSeries().get(0).getDataLabels().setShowValue(true);
// Show series name labels
chart.getNSeries().get(1).getDataLabels().setShowSeriesName(true);
// Move labels to center
chart.getNSeries().get(1).getDataLabels().setPosition(AsposeCells.LabelPositionType.Center);

// Save the file
workbook.save("chart_datalabels.xlsx");
```  

## **高度なトピック**  
- [チャートシリーズのデータポイントにカスタムラベルを追加する](/cells/ja/nodejs-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)  
- [チャートのデータラベルのテキスト折り返しを無効にする](/cells/ja/nodejs-cpp/disable-text-wrapping-for-data-labels-of-the-chart/)  
- [テキストに合わせるようにチャートのデータラベルの形状をリサイズする](/cells/ja/nodejs-cpp/resize-chart-s-data-label-shape-to-fit-text/)  
- [チャートポイントのリッチテキストカスタムデータラベル](/cells/ja/nodejs-cpp/rich-text-custom-data-label-of-chart-point/)  
- [チャートのデータラベルの形状タイプを設定する](/cells/ja/nodejs-cpp/set-the-shape-type-of-data-labels-of-chart/)  
- [データラベルとしてセル範囲を表示する](/cells/ja/nodejs-cpp/showing-cell-range-as-the-data-labels/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
