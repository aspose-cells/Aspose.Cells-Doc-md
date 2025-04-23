---
title: チャート凡例のエントリの塗りつぶしを「なし」に設定する方法（Aspose.Cells for Node.js via C++使用）
linktitle: Aspose.Cellsを使用して、チャートの凡例エントリの塗りつぶしのテキストを無効に設定する
description: Aspose.Cells for Node.js via C++を使ってチャート凡例のエントリの塗りつぶしを「なし」に設定する方法を学びましょう。このガイドでは、Microsoft Excelのチャートの凡例エントリの塗りつぶし色を変更して、見た目とカスタマイズ性を向上させる方法を紹介します。
keywords: Aspose.Cells for Node.js via C++、チャート凡例のエントリの塗りつぶし、Microsoft Excel、ビジュアライゼーション、カスタマイズ。
type: docs
weight: 320
url: /ja/nodejs-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

チャートの凡例エントリの塗りつぶしを「なし」に設定して、凡例内に表示されないようにする場合は、[**LegendEntry.isTextNoFill()**](https://reference.aspose.com/cells/nodejs-cpp/legendentry/#isTextNoFill--)を**true**に設定してください。

{{% /alert %}}

次のサンプルコードは、チャートの2番目の凡例エントリの塗りつぶしのテキストを無効に設定します。このコードで使用される [サンプルExcelファイル](5115219.xlsx) とその生成される [出力Excelファイル](5115217.xlsx) をダウンロードして参照してください。

次のスクリーンショットは、このコードが[sample excel file](5115219.xlsx)に与える影響を示しています。

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Sample.xlsx"));

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the first chart inside the sheet
const chart = sheet.getCharts().get(0);

// Set text of second legend entry fill to none
chart.getLegend().getLegendEntries().get(1).setIsTextNoFill(true);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "ChartLegendEntry_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
