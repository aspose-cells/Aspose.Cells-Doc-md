---
title: 使用 C++ 进行 Excel 转 PDF 时渲染实线格线
linktitle: 将 Excel 转为 PDF 时渲染实线格线
type: docs
weight: 390
url: /zh/nodejs-cpp/render-solid-gridline-while-converting-excel-to-pdf/
description: 了解如何在使用 Aspose.Cells for Node.js via C++ 转换 Excel 为 PDF 时渲染实线格线。 
keywords: 在Node.js通过C++渲染实线格线到PDF，Excel转PDF支持实线格线Node.js通过C++，PdfSaveOptions支持实线格线Node.js via C++ 
---

为了兼容旧版本，Aspose.Cells 在将 Excel 转为 PDF 时默认以虚线渲染格线。然而，现代 Excel 现在渲染格线为实线。

使用 [PdfSaveOptions.gridlineTypes](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) 选项，Aspose.Cells for Node.js via C++ 也可以将格线渲染为实线。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create an empty Workbook
const wb = new AsposeCells.Workbook();

// Prepare data
wb.getWorksheets().get(0).getCells().get("D9").putValue("gridline");

// Enable to print gridline
wb.getWorksheets().get(0).getPageSetup().setPrintGridlines(true);

// Set to render gridline as solid line
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setGridlineType(AsposeCells.GridlineType.Hair);

// Save the pdf file with PdfSaveOptions
wb.save(path.join(dataDir, "test_Cs.pdf"), pdfSaveOptions);
```

![solid-gridline.png](solid-gridline.png)

