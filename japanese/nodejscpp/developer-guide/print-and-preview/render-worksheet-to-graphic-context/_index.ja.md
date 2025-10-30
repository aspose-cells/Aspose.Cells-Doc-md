---
title: Node.jsとC++を使用したワークシートのグラフィックコンテキストへのレンダリング
linktitle: グラフィックコンテキストにワークシートをレンダリングする
type: docs
weight: 300
url: /ja/nodejs-cpp/render-worksheet-to-graphic-context/
description: Aspose.Cells for Node.js via C++を使用してワークシートをグラフィックコンテキストにレンダリングする方法を学びます。これには、画像ファイル、画面、プリンタへのレンダリングが含まれます。
---

{{% alert color="primary" %}}

Aspose.Cellsは、ワークシートをグラフィックコンテキストにレンダリングする機能を備えています。グラフィックコンテキストは画像ファイル、画面、プリンタなど何でも構いません。以下のいずれかの方法を使用してワークシートをグラフィックコンテキストにレンダリングしてください。

- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)
- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)

{{% /alert %}}

以下のコードは、Aspose.Cellsを使用してワークシートをグラフィックコンテキストにレンダリングする方法を示しています。コードを実行すると、ワークシート全体が出力され、残りの空きスペースは青色で塗りつぶされ、画像は**OutputImage_out_.png**として保存されます。任意のExcelファイルを使用して試すことができます。コード内のコメントも参照してください。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleBook.xlsx");
// Create workbook object from source file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create empty image buffer
const bmpOptions = new AsposeCells.ImageOrPrintOptions();
bmpOptions.setOnePagePerSheet(true);

// Render worksheet to image
const sheetRender = new AsposeCells.SheetRender(worksheet, bmpOptions);
sheetRender.toImage(0, dataDir + "/OutputImage_out.png");

// Save the image in Png format
```
{{< app/cells/assistant language="nodejs-cpp" >}}
