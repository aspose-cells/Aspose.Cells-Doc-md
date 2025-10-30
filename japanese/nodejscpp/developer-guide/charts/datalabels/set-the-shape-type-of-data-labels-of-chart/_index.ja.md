---
title: Node.js経由でC++を使ったチャートのデータラベルのシェイプタイプを設定
linktitle: チャートのデータラベルのシェイプタイプを設定する
description: Aspose.Cells for Node.js via C++を使用してチャートのデータラベルのシェイプタイプを設定する方法を学びます。このガイドでは、利用可能なさまざまなシェイプタイプを説明し、見た目と使いやすさを向上させるための適切なシェイプの選択方法を示します。
keywords: Aspose.Cells for Node.js via C++、チャート作成、データラベル、シェイプタイプ、プレゼンテーション、使いやすさ。
type: docs
weight: 110
url: /ja/nodejs-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **可能な使用シナリオ**
`DataLabels.shapeType`プロパティを使用してチャートのデータラベルのシェイプタイプを変更できます。これは`DataLabelShapeType`列挙型の値を取り、データラベルのシェイプタイプを適宜変更します。その値の一部は

{{< highlight javascript >}}
 DataLabelShapeType.BentLineCallout
DataLabelShapeType.DownArrowCallout
DataLabelShapeType.Ellipse
DataLabelShapeType.LineCallout
DataLabelShapeType.Rect
etc.
{{< /highlight >}}

## **チャートのデータラベルの形状タイプを設定する**
以下のサンプルコードは、チャートのデータラベルのシェイプタイプを`DataLabelShapeType.WedgeEllipseCallout`に変更します。コードで使用されたサンプルExcelファイル（60489778.xlsx）と、それによって生成された出力Excelファイル（60489779.xlsx）をご覧ください。スクリーンショットは、このコードの効果を示すサンプルExcelファイルの様子です。

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **サンプルコード**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSetShapeTypeOfDataLabelsOfChart.xlsx");

// Load source Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Access first series
const series = chart.getNSeries().get(0);

// Set the shape type of data labels i.e. Speech Bubble Oval
series.getDataLabels().setShapeType(AsposeCells.DataLabelShapeType.WedgeEllipseCallout);

// Save the output Excel file
workbook.save(path.join(dataDir, "outputSetShapeTypeOfDataLabelsOfChart.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
