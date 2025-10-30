---
title: Döküman Yapısını PDF ye Dönüştürürken Dışa Aktar (Node.js C++)
linktitle: PDF ye Dönüştürürken Belge Yapısını Dışa Aktar
type: docs
weight: 360
url: /tr/nodejs-cpp/export-document-structure-while-converting-to-pdf/
description: Aspose.Cells for Node.js via C++ kullanarak, Excel dosyasını etiketlenmiş PDF ye dönüştürürken döküman yapısını nasıl dışa aktaracağınızı öğrenin. 
---

PDF mantıksal yapı olanakları, belge içeriği yapısı hakkında bilgi içermeyi sağlar. Aspose.Cells for Node.js via C++, bir Microsoft Excel belgesinden hücre, satır, tablo, çalışma sayfası, resim, şekil, başlık / altbilgi gibi yapı bilgilerini korur.

Seçenek [PdfSaveOptions.getExportDocumentStructure()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getExportDocumentStructure--) ile, belge yapısı dışa aktarılan bir etiketlenmiş PDF'ye kaydedebilirsiniz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "document-structure-example.xlsx");
// Open the excel file with image, shape, chart, etc.
const wb = new AsposeCells.Workbook(filePath);

// Set to export document structure.
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setExportDocumentStructure(true);

// Save the pdf file with PdfSaveOptions
wb.save("output.pdf", pdfSaveOptions);
```

{{< app/cells/assistant language="nodejs-cpp" >}}
