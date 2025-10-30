---
title: Node.js経由のC++で、チャートのデータラベルの折り返しを無効にする方法
description: Aspose.Cells for Node.js via C++を使って、チャート内のデータラベルのテキスト折り返しを無効にする方法を学びましょう。長いラベルが重ならないように防ぎ、読みやすくクリアなチャート表示を提供します。
keywords: Aspose.Cells for Node.js via C++、チャート作成、データラベル、テキスト折り返し、重なり、可読性、表示。
type: docs
weight: 70
url: /ja/nodejs-cpp/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013では、ユーザーはチャートのデータラベル内のテキストを折り返すか折り返さないかを選択できます。デフォルトでは、チャートのデータラベル内のテキストは折り返し状態になっています。

Aspose.Cellsは、[**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#isTextWrapped--)プロパティを提供しており、これをtrueまたはfalseに設定することで、データラベルのテキスト折り返しを有効または無効にできます。

{{% /alert %}}

次のコードサンプルは、チャートのデータラベルのテキスト折り返しを無効にする方法を示しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_wrap_label.xlsx");
// Load the sample Excel file inside the workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Disable the Text Wrapping of Data Labels in all Series
chart.getNSeries().get(0).getDataLabels().setIsTextWrapped(false);
chart.getNSeries().get(1).getDataLabels().setIsTextWrapped(false);
chart.getNSeries().get(2).getDataLabels().setIsTextWrapped(false);

// Save the workbook
workbook.save(path.join(dataDir, "Output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
