---
title: Belirtilen çalışma sayfalarını PDF ye kaydetmek Node.js ve C++ kullanarak
linktitle: Belirtilen Çalışma Sayfalarını PDF Olarak Kaydet
type: docs
weight: 140
url: /tr/nodejs-cpp/save-specified-worksheets-to-pdf/
description: Aspose.Cells for Node.js via C++ kullanarak belirli çalışma sayfalarını PDF ye nasıl kaydedeceğinizi öğrenin. 
---


Varsayılan olarak, Aspose.Cells bütün **görünen** çalışma sayfalarını bir PDF dosyasına kaydeder. [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--) seçeneğiyle, belirli çalışma sayfalarını PDF'ye kaydedebilirsiniz. Örneğin, etkin çalışma sayfasını PDF'ye, tüm çalışma sayfalarını (görünen ve gizli çalışma sayfaları dahil) PDF'ye, özel çoklu çalışma sayfalarını PDF'ye kaydedebilirsiniz.

## **Etkin Çalışma Sayfasını PDF Olarak Kaydet**

 Sadece aktif sayfayı PDF'ye aktarmak istiyorsanız, bunu [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--) seçeneğine [**SheetSet.getActive()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getActive--) geçirerek başarabilirsiniz.

 Kaynak dosyanın aktif sayfası [sheetset-example.xlsx](sheetset-example.xlsx) dosyasındaki `Sheet2` sayfasıdır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sheetset-example.xlsx");

// Open the template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Set active sheet to output
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setSheetSet(AsposeCells.SheetSet.getActive());

// Save the pdf file with PdfSaveOptions
workbook.save("output.pdf", pdfSaveOptions);
```

## ** Tüm Çalışma Sayfalarını PDF'ye Kaydet**

[**SheetSet.getVisible()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getVisible--) çalışma kitabında görünür sayfaları, [**SheetSet.getAll()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getAll--) ise görünür ve gizli/görülemez sayfaları dahil olmak üzere tüm sayfaları gösterir. Tüm sayfaları PDF'ye aktarmak istiyorsanız, sadece [**SheetSet.getAll()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getAll--) ile [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--) seçeneğine geçebilirsiniz.

Kaynak dosya [sheetset-example.xlsx](sheetset-example.xlsx) gizli Sheet3 sayfası dahil olmak üzere dört sayfayı içerir.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sheetset-example.xlsx");

// Open the template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Set all sheets to output
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setSheetSet(AsposeCells.SheetSet.getAll());

// Save the pdf file with PdfSaveOptions
workbook.save("output.pdf", pdfSaveOptions);
```

## **Belirtilen Çalışsayfalarını PDF olarak kaydet**

 İstenen / özelleştirilmiş çoklu sayfayı PDF'ye aktarmak istiyorsanız, bunu [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--) seçeneğine birden çok sayfa dizisi geçirerek başarabilirsiniz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sheetset-example.xlsx");

// Open the template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Set custom multiple sheets(Sheet1, Sheet3) to output
const sheetSet = new AsposeCells.SheetSet([0, 2]);
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setSheetSet(sheetSet);

// Save the pdf file with PdfSaveOptions
workbook.save("output.pdf", pdfSaveOptions);
```

## ** Çalışma Sayfalarını PDF'ye Yeniden Sırala**

Kaynak dosyayı değiştirmeden sayfaları (örneğin tersine sıralı) PDF'ye yeniden sıralamak istiyorsanız, bunu [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--) seçeneğine sıralanmış sayfa indeksleri geçirerek başarabilirsiniz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sheetset-example.xlsx");
// Open the template excel file
const wb = new AsposeCells.Workbook(filePath);

// Reorder sheets(Sheet1, Sheet2, Sheet3, Sheet4) to sheets(Sheet4, Sheet3, Sheet2, Sheet1)
const sheetSet = new AsposeCells.SheetSet([3, 2, 1, 0]);
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setSheetSet(sheetSet);

// Save the pdf file with PdfSaveOptions
wb.save("output.pdf", pdfSaveOptions);
```

{{% alert color="primary" %}} 

Eğer elektronik tablonuz formüller içeriyorsa, PDF formatına dönüştürmeden hemen önce [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) çağrısını yapmanız en iyisidir. Böyle yaparak formüle bağımlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.

{{% /alert %}}
