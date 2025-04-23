---
title: Node.js経由のC++を使ったExcelのPDF変換中にソリッドグリッドラインをレンダリング
linktitle: ExcelをPDFに変換時にソリッドグリッドラインをレンダリング
type: docs
weight: 390
url: /ja/nodejs-cpp/render-solid-gridline-while-converting-excel-to-pdf/
description: Aspose.Cells for Node.js via C++を使用してExcelをPDFに変換するときにソリッドグリッドラインをレンダリングする方法を学びましょう。 
keywords: Node.js経由のC++でソリッドグリッドラインをPDFにレンダリング、ExcelからPDFに変換、PdfSaveOptionsを使用したソリッドグリッドラインの実現 
---

互換性のために、古いバージョンのAspose.CellsはExcelをPDFに変換する際にグリッドラインを点線としてレンダリングします。しかし、現代のExcelはグリッドラインを実線としてレンダリングします。

[PdfSaveOptions.gridlineTypes](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)オプションを使うと、Aspose.Cells for Node.js via C++はグリッドラインを実線としてレンダリングすることも可能です。

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

