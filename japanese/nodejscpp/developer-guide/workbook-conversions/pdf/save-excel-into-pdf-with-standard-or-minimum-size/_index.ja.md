---
title: Node.js経由のC++を使用してExcelを標準または最小サイズのPDFに保存
linktitle: Excelを標準サイズまたは最小サイズのPDFに保存する
type: docs
weight: 340
url: /ja/nodejs-cpp/save-excel-into-pdf-with-standard-or-minimum-size/
description: Aspose.Cells for Node.js via C++を使用して、Excelファイルを標準または最小サイズのPDFに保存する方法を学びます。
---

{{% alert color="primary" %}} 

デフォルトでは、Aspose.CellsはExcelを標準サイズのPDFに保存します。ただし、[PdfSaveOptions.getOptimizationType()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOptimizationType--) プロパティを使用して最小サイズで保存することも可能です。以下の値を受け入れます：

- PdfOptimizationType.Standard
- PdfOptimizationType.MinimumSize

{{% /alert %}} 

## **Aspose.Cells for Node.js via C++を使用してExcelを標準または最小サイズのPDFに保存**
以下のサンプルコードは、[PdfSaveOptions.getOptimizationType()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOptimizationType--) プロパティを使用してExcelを標準または最小サイズのPDFに保存する方法を示しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleBook.xlsx");
// Load excel file into workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Save into Pdf with Minimum size
const opts = new AsposeCells.PdfSaveOptions();
opts.setOptimizationType(AsposeCells.PdfOptimizationType.MinimumSize);

workbook.save(path.join(dataDir, "OptimizedOutput_out.pdf"), opts);
```
