---
title: Node.js経由でC++を使用して、フレームスクリプトとドキュメントプロパティのエクスポートを無効にする
linktitle: フレームスクリプトとドキュメントプロパティのエクスポートを無効にする
type: docs
weight: 310
url: /ja/nodejs-cpp/disable-exporting-frame-scripts-and-document-properties/
description: ExcelブックをHTMLに変換するときに、フレームスクリプトとドキュメントプロパティのエクスポートを無効にする方法についてAspose.Cells for Node.js via C++を使用して学びましょう。
--- 

{{% alert color="primary" %}}

Aspose.Cellsは、ExcelブックをHTMLに変換する際に、フレームスクリプトとドキュメントプロパティをエクスポートします。バージョン8.6.0のAspose.Cells for Node.js via C++では、これらのエクスポートを任意で無効にするオプションが導入されています。`HtmlSaveOptions.exportFrameScriptsAndProperties`プロパティを使用してください。

{{% /alert %}}

## **フレームスクリプトとドキュメントプロパティのエクスポートを無効にする**

以下のサンプルコードを使用すると、フレームスクリプトとドキュメントプロパティのエクスポートを無効にできます。ワークブックをHTMLに変換すると、出力ファイルにフレームスクリプトとドキュメントプロパティは含まれません。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the required workbook to convert
const filePath = path.join(dataDir, "Sample1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Disable exporting frame scripts and document properties
const options = new AsposeCells.HtmlSaveOptions();
options.setExportFrameScriptsAndProperties(false);

// Save workbook as HTML
workbook.save(path.join(dataDir, "output.out.html"), options);
```
