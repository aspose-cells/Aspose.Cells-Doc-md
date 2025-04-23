---
title: チャートなしのExcelファイルをNode.jsとC++で読み込む
linktitle: グラフを含まないソースエクセルファイルを読み込む
type: docs
weight: 420
url: /ja/nodejs-cpp/load-source-excel-file-without-charts/
description: Aspose.Cells for Node.js via C++ を使って、チャートなしの Excel ファイルを読み込む方法を学びます。 
---

{{% alert color="primary" %}}

Aspose.Cellsでは、チャートのないExcelファイルを読み込むことが可能です。これには[**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--)プロパティを使用してください。

{{% /alert %}}

## **グラフを含まないスプレッドシートを読み込む**

以下のサンプルコードは、チャートなしのExcelファイルを読み込み、それを出力PDF形式で保存します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the load options and filter the data
const options = new AsposeCells.LoadOptions();

// Include everything except charts
options.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart));

// Load the workbook with specified load options
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart.xlsx"), options);

// Save the workbook in PDF format
workbook.save(path.join(dataDir, "ResultWithoutChart.pdf"), AsposeCells.SaveFormat.Pdf);
```
