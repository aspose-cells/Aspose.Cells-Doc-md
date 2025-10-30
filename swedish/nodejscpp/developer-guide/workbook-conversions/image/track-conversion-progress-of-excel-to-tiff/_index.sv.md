---
title: Spåra konverteringsprocessen av Excel till TIFF med Node.js via C++
linktitle: Följ konverteringsframstegen från Excel till TIFF
type: docs
weight: 190
url: /sv/nodejs-cpp/track-conversion-progress-of-excel-to-tiff/
description: Lär dig hur du spårar konverteringsframen för Excelfiler till TIFF med Aspose.Cells for Node.js via C++. Förbättra användarupplevelsen under konverteringen.
---

## **Möjliga användningsscenario**

Ibland kan det ta tid att konvertera stora Excel-filer. Under denna tid kan du visa konverteringsframstegen för dokumentet istället för bara en laddningsskärm för att öka användarvänligheten i din applikation. Aspose.Cells for Node.js via C++ stöder spårning av konverteringsprocessen genom att tillhandahålla gränssnittet [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback). Gränssnittet [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback) ger [**pageStartSaving(PageStartSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageStartSaving-pagestartsavingargs-) och [**pageEndSaving(PageEndSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageEndSaving-pageendsavingargs-)-metoder som du kan implementera i din egen klass. Du kan också kontrollera vilka sidor som renderas som demonstreras i den anpassade klassen *TestPageSavingCallback*.

## **Spåra konverteringsframsteg för Excel till TIFF**

Följande kod exempel laddar [käll excelfilen](95584311.xlsx) och skriver ut dess konverteringsframsteg i konsolen med hjälp av den anpassade klassen *TestPageSavingCallback* som implementerar [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback)-gränssnittet. Utdatafilen som genereras är bifogad för din referens.

[Output File](95584312.tiff)

## **Exempelkod**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleUseWorkbookRenderForImageConversion.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const opts = new AsposeCells.ImageOrPrintOptions();

// Define TestTiffPageSavingCallback
class TestTiffPageSavingCallback {
// Implement required methods for the callback here
}

opts.setPageSavingCallback(new TestTiffPageSavingCallback());
opts.setImageType(AsposeCells.ImageType.Tiff);

const wr = new AsposeCells.WorkbookRender(workbook, opts);
wr.toImage(path.join(outputDir, "DocumentConversionProgressForTiff_out.tiff"));
```

Nedan är koden för den anpassade klassen *TestTiffPageSavingCallback*.

```javascript
const AsposeCells = require("aspose.cells.node");

class TestTiffPageSavingCallback {
pageStartSaving(args) {
console.log(`Start saving page index ${args.pageIndex} of pages ${args.pageCount}`);

// Don't output pages before page index 2.
if (args.pageIndex < 2) {
args.setIsToOutput(false);
}
}

pageEndSaving(args) {
console.log(`End saving page index ${args.pageIndex} of pages ${args.pageCount}`);

// Don't output pages after page index 8.
if (args.pageIndex >= 8) {
args.setHasMorePages(false);
}
}
}
```

## **Konsoloutput**

{{< highlight java >}}

Start saving page index 0 of pages 10</br>
End saving page index 0 of pages 10</br>
Start saving page index 1 of pages 10</br>
End saving page index 1 of pages 10</br>
Start saving page index 2 of pages 10</br>
End saving page index 2 of pages 10</br>
Start saving page index 3 of pages 10</br>
End saving page index 3 of pages 10</br>
Start saving page index 4 of pages 10</br>
End saving page index 4 of pages 10</br>
Start saving page index 5 of pages 10</br>
End saving page index 5 of pages 10</br>
Start saving page index 6 of pages 10</br>
End saving page index 6 of pages 10</br>
Start saving page index 7 of pages 10</br>
End saving page index 7 of pages 10</br>
Start saving page index 8 of pages 10</br>
End saving page index 8 of pages 10</br>

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
