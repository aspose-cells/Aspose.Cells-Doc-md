---
title: Öppna filer med olika format med Node.js via C++
linktitle: Öppning av filer med olika format
type: docs
weight: 30
url: /sv/nodejs-cpp/opening-files-with-different-formats/
description: Aspose.Cells for Node.js via C++ API tillåter dig att öppna/läsa olika format som XLSX, HTML, CSV, ODS, TSV, SXC, FODS, etc.
keywords: öppna xlsx filer, öppna html filer, läsa in fods filer, läsa in ods filer, läsa in sxc filer, öppna csv filer, tabulerad, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

Med Aspose.Cells kan du öppna filer med olika format. **Aspose.Cells** kan öppna ett antal filformat, såsom Microsoft Excel kalkblad (XLS, XLSX, XLSM, XLSB), SpreadsheetML, kommaseparerade värden (CSV), tabbavgränsade eller tabbseparerade värden (TSV), etc.

Om du behöver veta alla stödda filformat, se följande sidor:
[Stödda filformat](https://docs.aspose.com/cells/nodejs-cpp/supported-file-formats/)

{{% /alert %}}

## **Öppna filer med olika format**

Aspose.Cells gör det möjligt för utvecklare att öppna kalkylbladsfiler med olika format som SpreadsheetML, kommaseparerade värden (CSV), Tab Delimited eller Tab-separerade värden (TSV), ODS-filer. För att öppna sådana filer kan utvecklare använda samma metod som de använder för att öppna filer för olika versioner av Microsoft Excel.

### **Öppning av SpreadsheetML Filer**

SpreadsheetML-filer är XML-representationer av kalkblad inklusive all information om det, såsom formatering, formler, etc. Sedan Microsoft Excel XP har ett XML-exportalternativ som exporterar dina kalkblad till SpreadsheetML-filer.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening SpreadsheetML Files
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions3 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.SpreadsheetML);

// Create a Workbook object and opening the file from its path
const wbSpreadSheetML = new AsposeCells.Workbook(path.join(dataDir, "Book3.xml"), loadOptions3);
console.log("SpreadSheetML file opened successfully!");
```

### **Öppning av HTML filer**

Aspose.Cells tillåter dig att öppna en HTML-fil i ett Workbook-objekt. HTML-filen bör vara Microsoft Excel-orienterad, det vill säga, MS-Excel ska kunna öppna den.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.html");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath, loadOptions);

// Save the MHT file
wb.save(`${filePath}output.xlsx`);
```

### **Öppning av CSV-filer**

Komma-separerade värden (CSV) filer innehåller poster där värdena separeras med kommatecken. Data lagras som en tabell där varje kolumn är separerad av kommatecknet och citerad med dubbla citattecken. Om ett fält innehåller ett dubbelt citattecken, är det undkommet med ett par dubbla citattecken. Du kan också använda Microsoft Excel för att exportera kalkylbladdata till CSV.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book_CSV.csv");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions4 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Csv);

// Create a Workbook object and opening the file from its path
const wbCSV = new AsposeCells.Workbook(filePath, loadOptions4);
console.log("CSV file opened successfully!");
```

#### **Öppna CSV-filer och ersätt ogiltiga tecken**

När en CSV-fil med specialtecken öppnas i Excel, ersätts tecknen automatiskt. Samma gäller för Aspose.Cells API som demonstreras i kodexemplet nedan.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const filePath = path.join(sourceDir, "[20180220142533][ASPOSE_CELLS_TEST].csv");

const loadOptions = new AsposeCells.TxtLoadOptions();
loadOptions.setSeparator(';');
loadOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData));
loadOptions.setCheckExcelRestriction(false);
loadOptions.setConvertNumericData(false);
loadOptions.setConvertDateTimeData(false);

// Load CSV file
const workbook = new AsposeCells.Workbook(filePath, loadOptions);


console.log(workbook.getWorksheets().get(0).getName()); // (20180220142533)(ASPOSE_CELLS_T
console.log(workbook.getWorksheets().get(0).getName().length); // 31
console.log("CSV file opened successfully!");
```

### **Öppning av Textfiler med Anpassad Separator**

Textfiler används för att hålla kalkylbladsdata utan formatering. Filen är en typ av vanlig textfil som kan ha några anpassade separatorer.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book11.csv");

// Instantiate Text File's LoadOptions
const txtLoadOptions = new AsposeCells.TxtLoadOptions();

// Specify the separator
txtLoadOptions.setSeparator(",");

// Specify the encoding type
txtLoadOptions.setEncoding(AsposeCells.EncodingType.UTF8);

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath, txtLoadOptions);

// Save file
wb.save(path.join(dataDir, "output.txt"));
```

### **Öppning av tabbehållna filer**

Tab-separerade (Text) filer innehåller kalkylbladsdata men utan formatering. Data är arrangerad i rader och kolumner som i tabeller och kalkylblad. En fil med tab-separering är i princip en speciell typ av platt textfil med ett tab-tecken mellan varje kolumn.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1TabDelimited.txt");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions5 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.TabDelimited);

// Create a Workbook object and opening the file from its path
const wbTabDelimited = new AsposeCells.Workbook(filePath, loadOptions5);
console.log("Tab delimited file opened successfully!");
```

### **Öppning av tabseparatorvärdefiler (TSV-filer)**

Tab-separerade värden (TSV)-filer innehåller kalkbladdata men utan någon formatering. Det är detsamma som en Tab-betalad fil där data är ordnad i rader och kolumner som i tabeller och kalkblad.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Tsv);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleTSVFile.tsv"), loadOptions);

// Using the Sheet 1 in Workbook
const worksheet = workbook.getWorksheets().get(0);

// Accessing a cell using its name
const cell = worksheet.getCells().get("C3");

console.log(`Cell Name: ${cell.getName()} Value: ${cell.getStringValue()}`);
```

### **Öppning av SXC-filer**

StarOffice Calc liknar Microsoft Excel och stöder formler, diagram, funktioner och makron. Kalkbladen som skapas med denna programvara sparas med SXC-ändelsen. SXC-filen används också för OpenOffice.org Calc kalkbladsfiler. Aspose.Cells kan läsa SXC-filer som visas i följande kodexempel.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Sxc);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleSXC.sxc"), loadOptions);

// Using the Sheet 1 in Workbook
const worksheet = workbook.getWorksheets().get(0);

// Accessing a cell using its name
const cell = worksheet.getCells().get("C3");

console.log(`Cell Name: ${cell.getName()} Value: ${cell.getStringValue()}`);
```

### **Öppning av FODS-filer**

FODS-fil är ett kalkblad sparat i OpenDocument XML utan någon komprimering. Aspose.Cells kan läsa FODS-filer som demonstreras i följande kodexempel.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Fods);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleFods.fods"), loadOptions);

console.log("FODS file opened successfully!");
```

{{< app/cells/assistant language="nodejs-cpp" >}}
