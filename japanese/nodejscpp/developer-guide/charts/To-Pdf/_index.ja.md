---  
title: Node.js を使用した C++ 経由の PDF へのチャート作成  
linktitle: グラフをPDFに変換する  
description: Aspose.Cells for Node.js via C++ を使用してチャートを PDF ドキュメントに変換する方法を学びます。このガイドでは、Microsoft Excel のチャートをエクスポートし、PDFとして保存して配布や保存に役立てる方法を示します。  
keywords: Aspose.Cells for Node.js via C++、チャートをPDFに、Microsoft Excel、PDF変換、エクスポート、配布、アーカイブ。  
type: docs  
weight: 47  
url: /ja/nodejs-cpp/chart-to-pdf/  
---  

## **PDFへのチャートのレンダリング**

チャートをPDF形式にレンダリングするには、Aspose.Cells APIs が [**Chart.toPdf(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toPdf-string-) メソッドを公開しており、結果のPDFをディスクパスまたはStreamに保存することができます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Adding a new worksheet to the Workbook
const sheetIndex = workbook.getWorksheets().add();
// Obtaining the reference of the newly added worksheet by passing its index to WorksheetCollection
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);
// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Adding Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Converting chart to PDF
chart.toPdf(path.join(dataDir, "chartPDF_out.pdf"));
```

## **希望のページサイズでチャートPDFを作成**  
Aspose.Cellsを使用して目的のページサイズのチャートPDFを作成し、ページ内でチャートの位置を上、下、中央、左、右などに調整できます。さらに、出力されたチャートはStreamまたはディスクに作成可能です。サンプルコードでは、[サンプルExcelファイル](64716906.xlsx)を読み込み、最初のチャートにアクセスし、希望のページサイズで[出力PDF](64716907.pdf)に変換しています。このスクリーンショットは、コード内で指定された7x7のページサイズと、ハorizontal/Verticalに中央揃えされたチャートを示しています。

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)  
## **サンプルコード**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample Excel file containing the chart.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCreateChartPDFWithDesiredPageSize.xlsx"));

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet.
const chart = worksheet.getCharts().get(0);

// Create chart pdf with desired page size.
chart.toPdf(path.join(outputDir, "outputCreateChartPDFWithDesiredPageSize.pdf"), 7, 7, AsposeCells.PageLayoutAlignmentType.Center, AsposeCells.PageLayoutAlignmentType.Center);
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
