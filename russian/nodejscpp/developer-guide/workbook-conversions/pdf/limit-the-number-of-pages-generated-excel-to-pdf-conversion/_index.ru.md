---
title: Ограничить количество создаваемых страниц  Преобразование Excel в PDF с помощью Node.js и C++
linktitle: Ограничение количества сгенерированных страниц при преобразовании Excel в PDF
type: docs
weight: 180
url: /ru/nodejs-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Узнайте, как ограничить количество страниц при преобразовании электронной таблицы Excel в PDF с помощью Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

 Иногда вы хотите распечатать диапазон страниц в выходной PDF-файл. Aspose.Cells for Node.js via C++ позволяет установить лимит на количество создаваемых страниц при преобразовании файла Excel в формат PDF.

{{% /alert %}}

## **Ограничение количества сгенерированных страниц**

В следующем примере показано, как отображать диапазон страниц (3 и 4) в файле Microsoft Excel в формате PDF.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "TestBook.xlsx"));
// Instantiate the PdfSaveOption
const options = new AsposeCells.PdfSaveOptions();

// Print only Page 3 and Page 4 in the output PDF
// Starting page index (0-based index)
options.setPageIndex(3);
// Number of pages to be printed
options.setPageCount(2);

// Save the PDF file
workbook.save(path.join(dataDir, "outPDF1.out.pdf"), options);
```

{{% alert color="primary" %}}

 Если в таблице есть формулы, лучше всего вызвать [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) непосредственно перед рендерингом в PDF. Это гарантирует, что значения, зависящие от формул, будут перерасчитаны, и в выходном файле будут отображаться правильные значения.

{{% /alert %}}
