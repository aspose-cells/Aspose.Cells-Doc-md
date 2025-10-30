---
title: Node.jsを使ってODSファイルからチャートのサブタイトルを読む方法
linktitle: ODSファイルからチャートサブタイトルを読む
description: Aspose.Cells for Node.js via C++を使ってOpenDocument Spreadsheet（ODS）ファイルからチャートのサブタイトルを取得する方法を学びましょう。ガイドは、チャートのサブタイトルの抽出とアクセス方法を示し、さらなる分析や表示に役立ちます。
keywords: Aspose.Cells for Node.js via C++、チャートのサブタイトルの読み取り、OpenDocument Spreadsheet、ODSファイル、チャート抽出、データ分析。
type: docs
weight: 160
url: /ja/nodejs-cpp/read-chart-subtitle-from-ods-file/
---

## **ODSファイルからチャートサブタイトルを読む**

Aspose.Cellsは、[**Chart.getSubTitle()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getSubTitle--)プロパティを使用してODSファイル内のチャートサブタイトルを読むことができます。以下のサンプルコードは[サンプルODSファイル](89620481.ods)をロードし、[**Chart.getSubTitle()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getSubTitle--)プロパティを使用してチャートのサブタイトルを読み取り、コンソールウィンドウに出力します。

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Load excel file containing charts
const filePath = path.join(sourceDir, "SampleChart.ods");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

console.log("Chart Subtitle: " + chart.getSubTitle().getText());
```

## **コンソール出力**

{{< highlight javascript >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
