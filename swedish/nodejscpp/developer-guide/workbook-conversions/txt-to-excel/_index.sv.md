---  
title: Konvertera CSV, TSV och TXT till Excel med Node.js via C++  
linktitle: Konvertera CSV, TSV och TXT till Excel  
type: docs  
weight: 30  
url: /sv/nodejs-cpp/convert-csv-tsv-and-txt-to-excel/  
---  

{{% alert color="primary" %}}  
Med Aspose.Cells kan du konvertera CSV-filer till Excel, OpenOffice, PDF, JSON och många andra format.  
{{% /alert %}}  

## **Öppning av CSV-filer**  

Kommaseparerade värden (CSV) filer innehåller poster där värdena är separerade med kommatecken. Data lagras som en tabell där varje kolumn separeras med kommatecknet och citeras med dubbelcitat-tecknet. Om en fältvärde innehåller ett dubbelcitat-tecken escapas det med ett par av dubbelcitat-tecken. Du kan också använda Microsoft Excel för att exportera kalkylbladsdata till CSV.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions4 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Csv);
// Create a Workbook object and opening the file from its path
const wbCSV = new AsposeCells.Workbook(path.join(dataDir, "Book_CSV.csv"), loadOptions4);
console.log("CSV file opened successfully!");
```  

## **Öppna CSV-filer och ersätt ogiltiga tecken**  

När en CSV-fil med specialtecken öppnas i Excel, ersätts tecknen automatiskt. Samma gäller för Aspose.Cells API som demonstreras i kodexemplet nedan.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const filePath = path.join(sourceDir, "[20180220142533][ASPOSE_CELLS_TEST].csv");

const options = new AsposeCells.TxtLoadOptions();
options.setSeparator(",");
options.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData));
options.setCheckExcelRestriction(false);
options.setConvertNumericData(false);
options.setConvertDateTimeData(false);
// Load CSV file
const workbook = new AsposeCells.Workbook(filePath, options);

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
// Opening Tab Delimited Files
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions5 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.TabDelimited);

// Create a Workbook object and opening the file from its path
const wbTabDelimited = new AsposeCells.Workbook(path.join(dataDir, "Book1TabDelimited.txt"), loadOptions5);
console.log("Tab delimited file opened successfully!");
```  

### **Öppning av tabseparatorvärdefiler (TSV-filer)**  

Värden separerade med tabb (TSV) innehåller kalkylbladsdata men utan formatering. Det är samma sak som en Tab-separerad fil där data är arrangerad i rader och kolumner som i tabeller och kalkylblad.  

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

console.log("Cell Name: " + cell.getName() + " Value: " + cell.getStringValue());
```  

## **Fortsatta ämnen**  
- [Läs in eller importera CSV-fil med formler](/cells/sv/nodejs-cpp/load-or-import-csv-file-with-formulas/)  
- [Läsning av CSV-fil med flera teckentabeller](/cells/sv/nodejs-cpp/reading-csv-file-with-multiple-encodings/)  


