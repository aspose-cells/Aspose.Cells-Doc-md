---
title: Laddning och hantering av Excel , OpenOffice , Json , Csv och Html filer
linktitle: Öppna filer
type: docs
weight: 20
url: /sv/nodejs-cpp/loading-saving-and-managing/
description: Med Aspose.Cells är det enkelt att skapa, öppna och hantera Excel , CSV , TSV , ODS , HTML , Numbers , Json , XML , Pdf , Jpg , Tiff , Bild , Mht och XPS filer med Node.js via C++.
---

{{% alert color="primary" %}}

Med Aspose.Cells är det enkelt att skapa, öppna och hantera Excel-filer, till exempel för att hämta data eller använda en designer mall för att snabba upp utvecklingsprocessen.

{{% /alert %}}

## **Skapa en ny arbetsbok**
Följande exempel skapar en ny arbetsbok från grunden.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const licensePath = path.join(dataDir, "Aspose.Cells.lic");

try {
// Create a License object
const license = new AsposeCells.License();

// Set the license of Aspose.Cells to avoid the evaluation limitations
license.setLicense(licensePath);
} catch (ex) {
console.log(ex.message);
}

// Instantiate a Workbook object that represents Excel file.
const wb = new AsposeCells.Workbook();

// When you create a new workbook, a default "Sheet1" is added to the workbook.
const sheet = wb.getWorksheets().get(0);

// Access the "A1" cell in the sheet.
const cell = sheet.getCells().get("A1");

// Input the "Hello World!" text into the "A1" cell
cell.putValue("Hello World!");

// Save the Excel file.
wb.save(path.join(dataDir, "MyBook_out.xlsx"));
```

## **Öppna och spara en fil**
Med Aspose.Cells är det enkelt att öppna, spara och hantera Excel-filer.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening through Path
// Creating a Workbook object and opening an Excel file using its file path
const workbook1 = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));
// Adding new sheet
const sheet = workbook1.getWorksheets().add("MySheet");
// Setting active sheet
workbook1.getWorksheets().setActiveSheetIndex(1);
// Setting values.
const cells = sheet.getCells();
// Setting text
cells.get("A1").putValue("Hello!");
// Setting number
cells.get("A2").putValue(1000);
// Setting Date Time
const cell = cells.get("A3");
cell.putValue(new Date());
const style = cell.getStyle();
style.setNumber(14);
cell.setStyle(style);
// Setting formula
cells.get("A4").setFormula("=SUM(A1:A3)");
// Saving the workbook to disk.
workbook1.save(path.join(dataDir, "dest.xlsx"));
```

## **Avancerade ämnen**
- [Olika sätt att öppna filer](/cells/sv/nodejs-cpp/different-ways-to-open-files/)
- [Filtrera Definierade namn vid inläsning av arbetsbok](/cells/sv/nodejs-cpp/filter-defined-names-while-loading-workbook/)
- [Filtrera objekt vid inläsning av arbetsbok eller arbetsblad](/cells/sv/nodejs-cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [Filtrering av datatyp vid inläsning av arbetsboken från mallfil](/cells/sv/nodejs-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Få varningar vid inläsning av Excel-fil](/cells/sv/nodejs-cpp/get-warnings-while-loading-excel-file/)
- [Ladda käll-Excel-fil utan diagram](/cells/sv/nodejs-cpp/load-source-excel-file-without-charts/)
- [Ladda specifika arbetsblad i en arbetsbok](/cells/sv/nodejs-cpp/load-specific-worksheets-in-a-workbook/)
- [Ladda arbetsbok med specificerad pappersstorlek](/cells/sv/nodejs-cpp/load-workbook-with-specified-printer-paper-size/)
- [Öppna filer från olika Microsoft Excel-versioner](/cells/sv/nodejs-cpp/opening-different-microsoft-excel-versions-files/)
- [Öppna filer med olika format](/cells/sv/nodejs-cpp/opening-files-with-different-formats/)
- [Optimera minnesanvändningen vid arbete med stora filer med stora dataset](/cells/sv/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Läsa Numbers-kalkylblad utvecklat av Apple Inc. med Aspose.Cells](/cells/sv/nodejs-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Stoppa konvertering eller laddning med hjälp av InterruptMonitor när det tar för lång tid](/cells/sv/nodejs-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Använda LightCells API](/cells/sv/nodejs-cpp/using-lightcells-api/)
- [Konvertera CSV till JSON](/cells/sv/nodejs-cpp/convert-csv-to-json/)
- [Konvertera Excel till JSON](/cells/sv/nodejs-cpp/convert-excel-to-json/)
- [Konvertera JSON till CSV](/cells/sv/nodejs-cpp/convert-json-to-csv/)
- [Konvertera JSON till Excel](/cells/sv/nodejs-cpp/convert-json-to-excel/)
- [Konvertera Excel till Html](/cells/sv/nodejs-cpp/convert-excel-to-html/)
{{< app/cells/assistant language="nodejs-cpp" >}}
