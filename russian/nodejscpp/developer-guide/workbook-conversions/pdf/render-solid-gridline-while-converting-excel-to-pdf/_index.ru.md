---
title: Отрисовка сплошной сетки при преобразовании Excel в PDF с помощью Node.js через C++
linktitle: Отрисовка сплошной сетки при преобразовании Excel в PDF
type: docs
weight: 390
url: /ru/nodejs-cpp/render-solid-gridline-while-converting-excel-to-pdf/
description: Узнайте, как отображать сплошные линии сетки при преобразовании Excel в PDF с помощью Aspose.Cells for Node.js via C++. 
keywords: Отрисовка сплошной линии сетки в PDF через Node.js с помощью C++, преобразование Excel в PDF с сплошной линией сетки через Node.js с помощью C++, PdfSaveOptions для сплошной линии сетки в Node.js через C++ 
---

Для совместимости с более старыми версиями Aspose.Cells по умолчанию рисует сетки пунктирными линиями при преобразовании Excel в PDF. Однако современные Excel отображают сетки как сплошные линии.

С опцией [PdfSaveOptions.gridlineTypes](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) Aspose.Cells for Node.js via C++ также может отображать сетки как сплошные линии.

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

