---
title: Node.jsを通じたC++を使用して列幅をemやパーセントのスケーラブルユニットに設定する
linktitle: 列幅をemやパーセントのようなスケーラブルユニットに設定します
type: docs
weight: 130
url: /ja/nodejs-cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Aspose.Cells for Node.js via C++で、列幅をemやパーセントのようなスケーラブルユニットに設定する方法を学びます。生成されたHTMLテーブルの見栄えを改善します。
---

スプレッドシートからHTMLファイルを生成するのは非常に一般的です。列のサイズは「pt」で定義され、多くの場合で機能します。ただし、この固定サイズが不要な場合もあります。たとえば、コンテナパネルの幅が600pxの場合、そのHTMLページが表示される場所では、生成されたテーブルの幅が大きいと横スクロールバーが出る場合があります。この固定サイズをemやパーセントのようなスケーラブルユニットに変更して、より良いプレゼンテーションを実現する必要があります。以下のサンプルコードでは、[**HtmlSaveOptions.getWidthScalable()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getWidthScalable--)を**true**に設定することでスケーラブルな幅の作成が可能です。

サンプルのソースファイルと出力ファイルは以下のリンクからダウンロードできます：

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample source file
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleForScalableColumns.xlsx");
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Specify Html Save Options
const options = new AsposeCells.HtmlSaveOptions();

// Set the property for scalable width
options.setWidthScalable(true);

// Specify image save format
options.setExportImagesAsBase64(true);

// Save the workbook in Html format with specified Html Save Options
const outputFilePath = path.join(dataDir, "outsampleForScalableColumns.html");
workbook.save(outputFilePath, options);
```
