---
title: Excel i PDF ye dönüştürürken Node.js kullanarak C++ ile Katı Izgara Çizgisi Render Etme
linktitle: Excel den PDF ye dönüştürürken Katı Izgara Çizgisi Çiz
type: docs
weight: 390
url: /tr/nodejs-cpp/render-solid-gridline-while-converting-excel-to-pdf/
description: Aspose.Cells for Node.js via C++ kullanarak Excel i PDF ye dönüştürürken katı ızgara çizgilerini nasıl gölgeleyeceğinizi öğrenin. 
keywords: PDF ye Katı ızgara çizgisi Yansıtmak için Node.js ve C++ kullanarak, Excel i PDF ye dönüştür, Node.js ve C++ kullanarak Katı ızgara çizgisi ile Excel i PDF ye dönüştür, PdfSaveOptions kullanarak Node.js ve C++ ile katı ızgara çizgisi 
---

Uyumluluk için, Aspose.Cells varsayılan olarak Excel'den PDF'ye dönüştürürken ızgara çizgilerini noktalı çizgi olarak çizer. Ancak, modern Excel günümüzde ızgara çizgilerini katı çizgi olarak çizer.

[PdfSaveOptions.gridlineTypes](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) seçeneği ile, Aspose.Cells for Node.js via C++ ızgara çizgilerini aynı zamanda katı çizgiler olarak da render edebilir.

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

{{< app/cells/assistant language="nodejs-cpp" >}}
