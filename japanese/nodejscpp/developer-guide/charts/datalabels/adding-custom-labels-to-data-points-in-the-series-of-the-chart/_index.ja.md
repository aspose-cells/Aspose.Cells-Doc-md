---  
title: Node.js経由のC++を使った、チャートの系列内のデータポイントにカスタムラベルを追加する方法  
linktitle: チャートのシリーズのデータポイントにカスタムラベルを追加  
description: Aspose.Cells for Node.js via C++を使用して、チャートの系列内のデータポイントにカスタムラベルを追加する方法を学びましょう。このガイドでは、ラベルの外観、位置、フォーマットの変更方法を示し、データソースとリンクさせて正確な表現を行う方法も解説します。  
keywords: Aspose.Cells for Node.js、チャート作成、カスタムラベル、データポイント、系列、外観、位置、フォーマット、データソース、表現。  
type: docs  
weight: 100  
url: /ja/nodejs-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/  
---  

{{% alert color="primary" %}}  

チャートのシリーズのデータポイントにカスタムラベルを追加できます。Aspose.Cellsでは、これらのカスタムラベルを追加するための[**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--)プロパティを提供しています。この記事では、このプロパティを使用して、チャートのシリーズのデータポイントにカスタムラベルを追加する方法について説明します。

{{% /alert %}}  

 以下のコードは、「ラインで接続された散布図」と「データマーカー付き」のチャートを作成し、その後、シリーズ内のデータポイントに**カスタムラベル**を追加します。各カスタムラベルは**シリーズ名**と**ポイント名**を表示します。別のテキストに置き換えることも可能です。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Put data
sheet.getCells().get(0, 0).putValue(1);
sheet.getCells().get(0, 1).putValue(2);
sheet.getCells().get(0, 2).putValue(3);

sheet.getCells().get(1, 0).putValue(4);
sheet.getCells().get(1, 1).putValue(5);
sheet.getCells().get(1, 2).putValue(6);

sheet.getCells().get(2, 0).putValue(7);
sheet.getCells().get(2, 1).putValue(8);
sheet.getCells().get(2, 2).putValue(9);

// Generate the chart
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.ScatterConnectedByLinesWithDataMarker, 5, 1, 24, 10);
const chart = sheet.getCharts().get(chartIndex);

chart.getTitle().setText("Test");
chart.getCategoryAxis().getTitle().setText("X-Axis");
chart.getValueAxis().getTitle().setText("Y-Axis");

chart.getNSeries().setCategoryData("A1:C1");

// Insert series
chart.getNSeries().add("A2:C2", false);

let series = chart.getNSeries().get(0);

let pointCount = series.getPoints().getCount();
for (let i = 0; i < pointCount; i++) {
const pointIndex = series.getPoints().get(i);
pointIndex.getDataLabels().setText("Series 1" + "\n" + "Point " + i);
}

// Insert series
chart.getNSeries().add("A3:C3", false);

series = chart.getNSeries().get(1);

pointCount = series.getPoints().getCount();
for (let i = 0; i < pointCount; i++) {
const pointIndex = series.getPoints().get(i);
pointIndex.getDataLabels().setText("Series 2" + "\n" + "Point " + i);
}

workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
