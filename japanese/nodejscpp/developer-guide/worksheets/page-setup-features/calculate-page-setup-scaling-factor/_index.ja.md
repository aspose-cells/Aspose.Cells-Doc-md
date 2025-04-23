---
title: Node.jsとC++を使用してページ設定の拡大縮小率を計算する。
linktitle: ページ設定スケーリングファクターを計算します
type: docs
weight: 300
url: /ja/nodejs-cpp/calculate-page-setup-scaling-factor/
description: この記事では、Node.js APIとC++を使い、Excelシートのページ設定の拡大縮小比率をプログラム的に計算するためのサンプルコードを提供します。
keywords: Excelのページ設定の幅と高さをNode.jsとC++を使用して計算します。
---

{{% alert color="primary" %}}

**Fit to n page(s) wide by m tall**オプションを利用したページ設定の拡大縮小率は、Microsoft Excelが計算します。同じ値は[**SheetRender.getPageScale()**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#getPageScale--)プロパティを使用して取得できます。このプロパティはパーセンテージに変換可能な倍精度浮動小数点値を返します。例：0.5なら拡大縮小率は50%。

{{% /alert %}}

次のサンプルコードは、[**SheetRender.getPageScale()**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#getPageScale--) プロパティを使用してページ設定のスケーリングファクターを計算する方法を示しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some data in these cells
worksheet.getCells().get("A4").putValue("Test");
worksheet.getCells().get("S4").putValue("Test");

// Set paper size
worksheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);

// Set fit to pages wide as 1
worksheet.getPageSetup().setFitToPagesWide(1);

// Calculate page scale via sheet render
const sr = new AsposeCells.SheetRender(worksheet, new AsposeCells.ImageOrPrintOptions());

// Convert page scale double value to percentage
const strPageScale = (sr.getPageScale() * 100).toFixed(0) + "%";

// Write the page scale value
console.log(strPageScale);
```
