---
title: Undvik tom sida i utdata PDF när det inte finns något att skriva ut med Node.js via C++
linktitle: Undvik tomt sida i utdata PDF när det finns inget att skriva ut
type: docs
weight: 30
url: /sv/nodejs-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Lär dig hur du undviker tomma sidor i utdata PDF när det inte finns någonting att skriva ut med Aspose.Cells for Node.js via C++.
---

## **Möjliga användningsscenario**

 När Excel-filen är tom och användaren sparar den som PDF med Aspose.Cells for Node.js via C++ produceras en tom sida i utdata-PDF:en. Ibland är denna standardbeteende oönskat. Aspose.Cells tillhandahåller [**PdfSaveOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOutputBlankPageWhenNothingToPrint--) egenskapen för att hantera detta problem. Om du ställer in den till **false**, kommer ett undantag att inträffa när det inte finns något att skriva ut i PDF:en.

## **Undvik tom sida i utmatnings-PDF när det inte finns något att skriva ut**

 Följande kodexempel skapar en tom arbetsbok och sparar den som PDF efter att ha ställt in [**PdfSaveOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOutputBlankPageWhenNothingToPrint--) egenskapen till **false**. Eftersom det inte finns något att skriva ut i PDF:en, inträffar ett undantag som visas nedan.

## **Exempelkod**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Create Pdf save options.
const opts = new AsposeCells.PdfSaveOptions();

// Default value of OutputBlankPageWhenNothingToPrint is true.
// Setting false means - Do not output blank page when there is nothing to print.
opts.setOutputBlankPageWhenNothingToPrint(false);

// Save workbook to Pdf format, it will throw exception because workbook has nothing to print.
const ms = new Uint8Array();

try {
// Save to Pdf format. It will throw exception.
wb.save(ms, opts);
} catch (ex) {
console.error("Exception Message: " + ex.message + "\r\n");
}
```

## **Undantag**

{{< highlight javascript >}}

 exception was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
