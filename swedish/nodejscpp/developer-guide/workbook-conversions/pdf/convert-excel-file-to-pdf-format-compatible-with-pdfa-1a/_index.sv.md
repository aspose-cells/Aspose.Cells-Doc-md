---  
title: Konvertera Excel fil till PDF format kompatibelt med PDF/A 1a med Node.js via C++  
linktitle: Konvertera Excel fil till PDF format kompatibelt med PDF/A 1a  
type: docs  
weight: 130  
url: /sv/nodejs-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/  
description: Lär dig hur du konverterar Excel filer till PDF/A kompatibla PDF filer med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  

PDF/A är en unik variant av PDF utformad för långsiktigt bevarande av dokument. PDF/A är en ISO-standardiserad version av Portable Document Format (PDF) som är ett arkivformat av PDF som inbäddar alla teckensnitt som används i dokumentet inom PDF-filen. PDF/A skiljer sig från PDF genom att förbjuda funktioner som teckensnittslänkning (i motsats till teckensnittsinbäddning) och kryptering. Aspose.Cells for Node.js via C++ gör det möjligt att spara Excel-filer till PDF/A-kompatibla PDF-filer (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab och PDF/A-3u stöds). Denna guide beskriver hur du sparar arbetsboken i Excel till PDF/A-kompatibla (PDF/A-1a) PDF-filer.  

## **Konvertera Excel-fil till PDF-format kompatibelt med PDF/A-1a**  

Utvecklare kan använda klassen [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) för att ställa in olika attribut för konverteringen. Att ställa in olika egenskaper för klassen [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) ger dig kontroll över utskrift, typsnitt, säkerhet och kompressionsinställningar för den valda PDF-filen. Den viktigaste egenskapen är [**PdfSaveOptions.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--), som gör att du kan spara Excel-filer till PDF/A-kompatibla PDF-filer.  

Följande exempel visar hur man konverterar en Excel-fil till PDF-format kompatibelt med PDF/A-1a. Se dess [output PDF](outputCompliancePdfA1a.pdf) samt skärmbilder för referens.  

## **Skärmdump**  

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)  

## **Exempelkod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and add some message inside it
const cell = ws.getCells().get("B5");
cell.putValue("This PDF format is compatible with PDFA-1a.");

// Create pdf save options and set its compliance to PDFA-1a
const opts = new AsposeCells.PdfSaveOptions();
opts.setCompliance(AsposeCells.PdfCompliance.PdfA1a);

// Save the output pdf
wb.save(path.join(outputDir, "outputCompliancePdfA1a.pdf"), opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
