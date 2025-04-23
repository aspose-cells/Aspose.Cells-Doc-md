---
title: HTML保存時に非表示のワークシート内容のエクスポートを防止する方法
linktitle: HTMLに保存する際に非表示のワークシートコンテンツをエクスポートしないようにする
type: docs
weight: 210
url: /ja/nodejs-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Aspose.Cells for Node.js via C++を使って、非表示のワークシート内容のエクスポートを防ぐ方法を学びます。
---

{{% alert color="primary" %}}

ExcelワークブックをHTMLに保存できます。ただし、ワークブックに非表示のワークシートが含まれている場合、Aspose.Cellsはデフォルトでは非表示のワークシートのコンテンツをHTML出力（_files）ディレクトリにエクスポートします。この方法で非表示のワークシートのコンテンツをエクスポートすることは適切ではありません。たとえば、非表示のワークシートにHTML出力ディレクトリにエクスポートされてはならない画像が含まれている場合などです。

{{% /alert %}}

Aspose.Cells for Node.js via C++は、[**HtmlSaveOptions.getExportHiddenWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportHiddenWorksheet--)プロパティを提供します。デフォルトでは**true**に設定されており、非表示のワークシートもHTMLにエクスポートされます。これを**false**に設定すると、非表示のシートはエクスポートされません。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "WorkbookWithHiddenContent.xlsx"));

// Do not export hidden worksheet contents
const options = new AsposeCells.HtmlSaveOptions();
options.setExportHiddenWorksheet(false);

// Save the workbook
workbook.save(path.join(dataDir, "HtmlWithoutHiddenContent_out.html"), options);
```

