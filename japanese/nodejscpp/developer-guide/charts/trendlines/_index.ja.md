---
title: Node.js から C++ 経由でチャートのトレンドラインの式テキストを取得
description: Aspose.Cells for Node.js via C++ を使って、Microsoft Excel で作成したチャートのトレンドラインの方程式テキストを取得する方法を学びます。これにより、トレンドラインの方程式をアクセス、抽出し、さらなる分析や表示に利用できます。
keywords: Aspose.Cells for Node.js via C++、チャートトレンドライン、式テキスト、Microsoft Excel、データ分析、表示。
linktitle: トレンドライン
type: docs
weight: 110
url: /ja/nodejs-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ を使用してチャートのトレンドラインの式テキストを取得できます。Aspose.Cells は [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--) プロパティを提供しており、これを用いてトレンドラインの式テキストを返します。このプロパティを使うには、まず [**Chart.calculate()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#calculate--) メソッドを呼び出す必要があります。

{{% /alert %}}

以下のスクリーンショットは、トレンドライン付きのチャートと、その式テキストが赤色で表示されたものです。この式テキストは、以下のサンプルコードの [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--) プロパティを使用して取得します。

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## Node.js コードでチャートのトレンドラインの式テキストを取得

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "source.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Calculate the Chart first to get the Equation Text of Trendline
chart.calculate();

// Access the Trendline
const trendLine = chart.getNSeries().get(0).getTrendLines().get(0);

// Read the Equation Text of Trendline
console.log("Equation Text: " + trendLine.getDataLabels().getText());
```

## サンプルコードによって生成された出力

これは上記のサンプルコードのコンソール出力です。

{{< highlight javascript >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
