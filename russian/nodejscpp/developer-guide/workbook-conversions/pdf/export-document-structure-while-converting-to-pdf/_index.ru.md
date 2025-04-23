---
title: Экспорт структуры документа при преобразовании в PDF с помощью Node.js через C++
linktitle: Экспорт структуры документа при конвертации в PDF
type: docs
weight: 360
url: /ru/nodejs-cpp/export-document-structure-while-converting-to-pdf/
description: Узнайте, как экспортировать структуру документа при преобразовании файла Excel в тегированный PDF с помощью Aspose.Cells for Node.js via C++. 
---

Функции структурной логики PDF предоставляют механизм включения информации о структуре содержимого документа в PDF-файл. Aspose.Cells for Node.js via C++ сохраняет информацию о структуре из документа Microsoft Excel, такую как ячейка, строка, таблица, лист, изображение, фигура, шапка/подвал и т.д.

С помощью опции [PdfSaveOptions.getExportDocumentStructure()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getExportDocumentStructure--) вы можете сохранять в тегированный PDF с экспортированной структурой документа.

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

