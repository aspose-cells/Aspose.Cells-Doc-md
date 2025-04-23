---
title: Resampling tillagda bilder  Excel till PDF konvertering med Node.js via C++
linktitle: Resampling tillagda bilder
type: docs
weight: 150
url: /sv/nodejs-cpp/resampling-added-images-excel-to-pdf-conversion/
description: Lär dig hur man komprimerar bilder som lagts till i Excel filer för att minska PDF storleken och förbättra konverteringsprestandan med Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

När du arbetar med stora Microsoft Excel-filer med många bilder kan du behöva komprimera tillagda bilder för att minska utdatafilens storlek och förbättra den totala konverteringsprestandan. Aspose.Cells for Node.js via C++ stöder återprovning av tillagda bilder för att minska utdata-PDF-filens storlek och förbättra prestandan något.

{{% /alert %}}

Se följande exempelkod som beskriver hur man utför uppgiften med hjälp av Aspose.Cells API. Exemplet konverterar en Microsoft Excel-fil till en PDF-fil samtidigt som bilderna i filen komprimeras.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Initialize a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "input.xlsx"));

// Instantiate the PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
// Set Image Resample properties
pdfSaveOptions.setImageResample(300, 70);

// Save the PDF file
workbook.save(path.join(dataDir, "OutputFile_out_pdf"), pdfSaveOptions);
```

{{% alert color="primary" %}}

Genom att använda alternativet [**setImageResample(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#setImageResample-number-number-) minimerar storleken på utdata-PDF men kan påverka bildkvaliteten något.

{{% /alert %}} {{% alert color="primary" %}}

Om ditt kalkylblad innehåller formler, är det bäst att anropa [**workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) strax innan du renderar kalkylbladet till PDF-format. Genom att göra det säkerställs att formelberoende värden beräknas om och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}
