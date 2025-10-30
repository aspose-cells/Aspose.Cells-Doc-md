---  
title: Spåra dokumentkonverteringsframsteg med Node.js via C++  
linktitle: Spåra dokumentkonverteringsframsteg  
type: docs  
weight: 970  
url: /sv/nodejs-cpp/track-document-conversion-progress/  
description: Lär dig spåra konverteringsprogressen för dokument i Excel filer med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  

Ibland kan det ta tid att konvertera stora Excel-filer. Under denna tid kan du visa konverteringsframstegen för dokumentet istället för bara en laddningsskärm för att öka användarvänligheten i din applikation. Aspose.Cells for Node.js via C++ stöder spårning av konverteringsprocessen genom att tillhandahålla gränssnittet [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback). Gränssnittet [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback) ger [**IPageSavingCallback.pageStartSaving(PageStartSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageStartSaving-pagestartsavingargs-) och [**IPageSavingCallback.pageEndSaving(PageEndSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageEndSaving-pageendsavingargs-)-metoder som du kan implementera i din egen klass. Du kan också kontrollera vilka sidor som renderas som demonstreras i den anpassade klassen *TestPageSavingCallback*.  

## **Spåra Dokumentkonverteringsframsteg**  

Följande kodexempel laddar [källexcel-filen](94896151.xlsx) och skriver ut dess konverteringsframsteg i konsolen med hjälp av den anpassade klassen *TestPageSavingCallback* som implementerar [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback)-gränssnittet.  

## **Exempelkod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Define TestPageSavingCallback class
class TestPageSavingCallback {
// Implement the required methods of this callback as needed
onPageSaving(pageIndex, fileName) {
console.log(`Saving page ${pageIndex} to ${fileName}`);
}
}

const workbook = new AsposeCells.Workbook(path.join(sourceDir, "PagesBook1.xlsx"));

const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setPageSavingCallback(new TestPageSavingCallback());

workbook.save(path.join(outputDir, "DocumentConversionProgress.pdf"), pdfSaveOptions);
```  

Följande är koden för den anpassade klassen *TestPageSavingCallback*.  

```javascript
const AsposeCells = require("aspose.cells.node");

class TestPageSavingCallback {
pageStartSaving(args) {
console.log(`Start saving page index ${args.getPageIndex()} of pages ${args.getPageCount()}`);

// don't output pages before page index 2.
if (args.getPageIndex() < 2) {
args.setIsToOutput(false);
}
}

pageEndSaving(args) {
console.log(`End saving page index ${args.getPageIndex()} of pages ${args.getPageCount()}`);

// don't output pages after page index 8.
if (args.getPageIndex() >= 8) {
args.setHasMorePages(false);
}
}
}
```  

## **Konsoloutput**  

{{< highlight java >}}  

Start saving page index 0 of pages 11</br>  
End saving page index 0 of pages 11</br>  
Start saving page index 1 of pages 11</br>  
End saving page index 1 of pages 11</br>  
Start saving page index 2 of pages 11</br>  
End saving page index 2 of pages 11</br>  
Start saving page index 3 of pages 11</br>  
End saving page index 3 of pages 11</br>  
Start saving page index 4 of pages 11</br>  
End saving page index 4 of pages 11</br>  
Start saving page index 5 of pages 11</br>  
End saving page index 5 of pages 11</br>  
Start saving page index 6 of pages 11</br>  
End saving page index 6 of pages 11</br>  
Start saving page index 7 of pages 11</br>  
End saving page index 7 of pages 11</br>  
Start saving page index 8 of pages 11</br>  
End saving page index 8 of pages 11  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
