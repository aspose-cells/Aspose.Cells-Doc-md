---  
title: Rendera en PDF sida per Excel Arbetsblad  Excel till PDF konvertering med Node.js via C++  
linktitle: Rendera en PDF sida per Excel ark  Konvertering av Excel till PDF  
type: docs  
weight: 100  
url: /sv/nodejs-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/  
---  

{{% alert color="primary" %}}  

När du arbetar med stora Microsoft Excel-filer (t.ex. en arbetsbok som har många blad, varje med 50 kolumner och 300 eller fler rader med data), kan du vilja att PDF-utdata visar ett blad per sida, oavsett storleken på bladet. Detta innebär att varje sida sannolikt kommer att ha en radikalt olika sidstorlek. Detta kan uppnås med Aspose.Cells for Node.js via C++.  

{{% /alert %}}  

Se följande exempel på kod som konverterar en Excel-fil med flera kalkylblad till PDF.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Initialize a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "input.xlsx"));

// Implement one page per worksheet option
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setOnePagePerSheet(true);

// Save the PDF file
workbook.save(path.join(dataDir, "OutputFile.out.pdf"), pdfSaveOptions);
```  

{{% alert color="primary" %}}  

Om [PdfSaveOptions.getOnePagePerSheet()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOnePagePerSheet--) inställningen är satt till **sant**, kommer allt bladinnehåll att renderas på en PDF-sida.  

{{% /alert %}} {{% alert color="primary" %}}  

Om ditt kalkylblad innehåller formler är det bäst att ringa [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) precis innan du renderar kalkylbladet till PDF. Detta säkerställer att de formelberoende värdena omberäknas och att de korrekta värdena visas i PDFen.  

{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
