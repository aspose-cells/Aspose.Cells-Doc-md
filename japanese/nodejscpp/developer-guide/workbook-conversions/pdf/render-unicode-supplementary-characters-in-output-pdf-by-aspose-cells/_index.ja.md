---
title: Aspose.Cells for Node.js via C++によるUnicode補助字符の出力PDFへのレンダリング
linktitle: Aspose.Cells による出力PDFでUnicode補助文字をレンダリングする
type: docs
weight: 350
url: /ja/nodejs-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Aspose.Cells for Node.js via C++を使用してUnicode補助字符を出力PDFにレンダリングする方法を学びましょう。 
---

{{% alert color="primary" %}}

通常のUnicode文字は2バイトであり、Unicode補助文字は4バイトです。Aspose.Cells はこれらの4バイトのUnicode文字のレンダリングをサポートしています。

Unicode文字標準では、補助文字はU+10000からU+10FFFFまでのコードポイントが割り当てられています。つまり、これらはU+FFFFよりも大きいUnicode文字です。

- UTF-8では、これらの文字はそれぞれ4バイトです。
- UTF-16では、これらの文字は2つのサロゲート（16ビットユニット）が必要です。

{{% /alert %}}

## Aspose.Cells for Node.js via C++を使用した出力PDFへのUnicode補助字符のレンダリング

以下のスクリーンショットは、Aspose.Cellsが[source excel file](5115563.xlsx)を[output PDF](5115564.pdf)にレンダリングした様子を示しています。すべてのUnicode補助字符がMicrosoft Excelと同じように正確にレンダリングされているのがわかります。

![todo:image_alt_text](output.png)

## サンプルコード

[ソースExcelファイル](5115563.xlsx)を[出力PDF](5115564.pdf)に変換するためのサンプルコードを使用できます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source excel file containing Unicode Supplementary characters
const workbook = new AsposeCells.Workbook(path.join(dataDir, "unicode-supplementary-characters.xlsx"));

// Save the workbook
workbook.save(path.join(dataDir, "RenderUnicodeInOutput_out.pdf"));
```
