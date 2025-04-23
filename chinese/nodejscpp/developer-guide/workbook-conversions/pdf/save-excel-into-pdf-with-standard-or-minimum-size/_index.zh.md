---
title: 使用 Node.js 和 C++ 将 Excel 保存为标准或最小尺寸的 PDF
linktitle: 使用标准大小或最小大小将Excel保存为PDF
type: docs
weight: 340
url: /zh/nodejs-cpp/save-excel-into-pdf-with-standard-or-minimum-size/
description: 学习如何使用 Aspose.Cells for Node.js via C++ 以标准或最小尺寸将 Excel 文件保存为 PDF。
---

{{% alert color="primary" %}} 

默认情况下，Aspose.Cells 将 Excel 内容保存为标准尺寸的 PDF。但你也可以使用 [PdfSaveOptions.getOptimizationType()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOptimizationType--) 属性来保存为最小尺寸。该属性接受以下值：

- PdfOptimizationType.Standard
- PdfOptimizationType.MinimumSize

{{% /alert %}} 

## **使用 Aspose.Cells for Node.js via C++ 将 Excel 保存为标准或最小尺寸的 PDF**
以下示例代码展示了如何使用 [PdfSaveOptions.getOptimizationType()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOptimizationType--) 属性，将 Excel 保存为标准或最小尺寸的 PDF。

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
