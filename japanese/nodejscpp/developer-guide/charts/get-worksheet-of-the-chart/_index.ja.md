---
title: Node.jsとC++を使用してチャートのワークシートを取得する
linktitle: チャートのワークシートを取得
description: Aspose.Cells for Node.js via C++を使用してExcelチャートに関連付けられたワークシートを取得する方法を学び、チャートの基礎データに効率的にアクセスおよび操作します。
keywords: Aspose.Cells for Node.js、Excelチャート、ワークシート、データ操作、基礎データ、操作、Node.jsとC++
type: docs
weight: 1000
url: /ja/nodejs-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

時には、チャートの参照からワークシートにアクセスしたい場合があります。Aspose.Cellsは、チャートを含むワークシートの参照を返す[**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--)プロパティを提供しています。

{{% /alert %}}

以下の例は [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--) プロパティの使用例を示します。最初にワークシートの名前を出力し、その後最初のチャートにアクセスします。再びワークシート名を出力し、[**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--) プロパティを使用します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Access first worksheet of the workbook
const worksheet = workbook.getWorksheets().get(0);

// Print worksheet name
console.log("Sheet Name: " + worksheet.getName());

// Access the first chart inside this worksheet
const charts = worksheet.getCharts();
if (charts.getCount() > 0) {
const chart = charts.get(0);

// Access the chart's sheet and display its name again
console.log("Chart's Sheet Name: " + chart.getWorksheet().getName());
} else {
console.log("No charts available in the worksheet.");
}
```

以下はサンプルコードのコンソール出力です。同じワークシート名が2回印刷されることがわかります。

{{< highlight javascript >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
