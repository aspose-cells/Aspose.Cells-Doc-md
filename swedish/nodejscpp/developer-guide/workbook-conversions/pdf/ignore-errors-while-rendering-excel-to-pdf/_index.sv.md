---  
title: Ignorera fel vid rendering av Excel till PDF med Node.js via C++  
linktitle: Ignorera fel vid rendering av Excel till PDF  
type: docs  
weight: 80  
url: /sv/nodejs-cpp/ignore-errors-while-rendering-excel-to-pdf/  
description: Lär dig hur du ignorerar fel under konvertering av Excel filer till PDF med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  

Ibland när du konverterar din Excel-fil till PDF uppstår fel eller undantag och konverteringsprocessen avbryts. Du kan ignorera alla dessa fel under konverteringsprocessen genom att använda [**PdfSaveOptions.getIgnoreError()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getIgnoreError--) egenskapen. På detta sätt kommer konverteringsprocessen att slutföras smidigt utan att kasta något fel eller undantag, men datatapp kan inträffa. Använd därför denna egenskap bara om datatapp inte är kritiskt för dig.  

## **Ignorera fel vid rendering av Excel till PDF**  

Följande kod laddar [exempel Excel-fil](55541778.xlsx), men filen är felaktig och kastar ett fel under [konvertering till PDF](55541779.pdf) i 17.11, men eftersom vi använder [**PdfSaveOptions.getIgnoreError()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getIgnoreError--) egenskapen, kastas inget fel. Men en *rundad röd pil-liknande form* som visas i skärmdumpen förloras.  

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)  

## **Exempelkod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleErrorExcel2Pdf.xlsx");
// Load the Sample Workbook that throws Error on Excel2Pdf conversion
const wb = new AsposeCells.Workbook(filePath);

// Specify Pdf Save Options - Ignore Error
const opts = new AsposeCells.PdfSaveOptions();
opts.IgnoreError = true;

// Save the Workbook in Pdf with Pdf Save Options
wb.save("outputErrorExcel2Pdf.pdf", opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
