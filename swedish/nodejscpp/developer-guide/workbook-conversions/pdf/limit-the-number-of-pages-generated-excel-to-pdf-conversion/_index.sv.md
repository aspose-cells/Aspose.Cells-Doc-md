---
title: Begränsa antalet genererade sidor  Excel till PDF konvertering med Node.js via C++
linktitle: Begränsa antalet genererade sidor  Excel till PDF konvertering
type: docs
weight: 180
url: /sv/nodejs-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Lär dig hur du begränsar antalet sidor som genereras vid konvertering av ett Excel ark till PDF med Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Ibland vill du skriva ut ett sidintervall till en utgångs-PDF-fil. Aspose.Cells for Node.js via C++ kan ställa in en gräns för hur många sidor som skapas vid konvertering av ett Excel-ark till PDF-format.

{{% /alert %}}

## **Begränsning av antalet genererade sidor**

Följande exempel visar hur man renderar en rad sidor (3 och 4) i en Microsoft Excel-fil till PDF.

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

Om kalkylbladet innehåller formler är det bäst att anropa [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) precis innan du renderar det till PDF. Det säkerställer att värden som är beroende av formler omberäknas och att de rätta värdena visas i output-filen.

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
