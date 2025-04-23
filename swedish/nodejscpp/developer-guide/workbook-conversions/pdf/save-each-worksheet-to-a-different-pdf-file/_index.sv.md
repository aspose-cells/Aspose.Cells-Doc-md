---  
title: Spara varje kalkylblad till en separat PDF med Node.js via C++  
linktitle: Spara varje kalkylblad i en separat PDF fil  
type: docs  
weight: 130  
url: /sv/nodejs-cpp/save-each-worksheet-to-a-different-pdf-file/  
---  

{{% alert color="primary" %}}  
Aspose.Cells stöder konvertering av XLS-filer (som innehåller bilder, diagram etc.) till PDF-dokument. Aspose.Cells for Node.js via C++ kan fungera självständigt för att konvertera ett kalkylblad till PDF, och du behöver inte använda Aspose.PDF för Node.js via C++ för konverteringen. Konverteringen kräver inte att programvaran skapar eller använder några tillfälliga filer eftersom hela processen kan göras i minnet.  
{{% /alert %}}  

## **Spara varje arbetsblad i en separat PDF-fil**  
Om du behöver spara varje arbetsblad i din mall-Excel-fil för att generera olika PDF-filer kan du enkelt göra detta. Du kan försöka att ställa in ett arbetsbladsvänteläge till [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/nodejs-cpp/pdfs saveoptions/#sheetSet) åt gången för att rendera till PDF.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Get the Excel file path
const filePath = path.join(dataDir, "input.xlsx");

// Instantiate a new workbook and open the Excel file from its location
const workbook = new AsposeCells.Workbook(filePath);

// Get the count of the worksheets in the workbook
const sheetCount = workbook.getWorksheets().getCount();

// Define PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Take PDFs of each sheet
for (let j = 0; j < sheetCount; j++) {
const ws = workbook.getWorksheets().get(j);

// set worksheet to output
const sheetSet = new AsposeCells.SheetSet([ws.getIndex()]);
pdfSaveOptions.setSheetSet(sheetSet);

workbook.save(path.join(dataDir, `worksheet-${ws.getName()}.out.pdf`), pdfSaveOptions);
}
```  

{{% alert color="primary" %}}  
Om ditt kalkylblad innehåller formler, är det bäst att anropa [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) strax innan du renderar kalkylbladet till PDF-format. Genom att göra det säkerställs att formelberoende värden beräknas om och de korrekta värdena renderas i PDF-filen.  
{{% /alert %}}  

