---  
title: Node.jsを使ったC++によるカスタムチャート作成  
linktitle: チャートのカスタマイズ  
description: Aspose.Cells for Node.js via C++でチャートのカスタマイズ方法を学びます。ガイドでは、チャートレイアウトの変更、データ系列の追加とフォーマット、軸の調整、さまざまなフォーマットオプションの適用方法を解説します。  
keywords: Aspose.Cells for Node.js via C++、チャート作成、カスタマイズ、レイアウト、データ系列、軸、フォーマット、外観、使いやすさ。  
type: docs  
weight: 40  
url: /ja/nodejs-cpp/customizing-charts/  
---  


## **カスタムチャートの作成**  

これまで、チャートについて議論してきた際は、標準の書式設定が施された標準的なチャートを見てきました。我々はデータソースを定義し、いくつかのプロパティを設定するだけで、チャートはデフォルトのフォーマット設定で作成されます。しかし、Aspose.Cells APIは、開発者が独自のフォーマット設定を持つカスタムチャートを作成できる機能もサポートしています。  

開発者は、Aspose.Cellsを使用して実行時にカスタムチャートを作成できます。  

チャートはデータ系列で構成されています。Aspose.Cellsにおける各データ系列は [**Series**](https://reference.aspose.com/cells/nodejs-cpp/series) オブジェクトで表され、[**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection) オブジェクトは [**Series**](https://reference.aspose.com/cells/nodejs-cpp/series) オブジェクトのコレクションとして機能します。カスタムチャートを作成する際、開発者は異なるデータ系列（[**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection) オブジェクトに収集された）に対して異なる種類のチャートを使用する自由があります。  

以下の例コードは、カスタムチャートの作成方法を示しています。この例では、最初のデータ系列には列チャートを使用し、2番目のデータ系列には折れ線グラフを使用しています。その結果、ワークシートには列チャートと折れ線グラフが組み合わされたチャートが追加されます。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("A4").putValue(110);
worksheet.getCells().get("B1").putValue(260);
worksheet.getCells().get("B2").putValue(12);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(100);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Setting the chart type of 2nd NSeries to display as line chart
chart.getNSeries().get(1).setType(AsposeCells.ChartType.Line);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  

現在、Aspose.Cellsはパイチャート、ラインチャート、カラムチャート、およびカラム積み上げチャートを組み合わせたカスタムチャートのみをサポートしていますが、今後のリリースでさらに多くのチャートがサポートされる予定です。  

{{% /alert %}}  

