---
title: Laden und Verwalten von Excel , OpenOffice , Json , Csv und Html Dateien
linktitle: Dateien öffnen
type: docs
weight: 20
url: /de/nodejs-cpp/loading-saving-and-managing/
description: Mit Aspose.Cells ist es einfach, Excel , CSV , TSV , ODS , HTML , Numbers , Json , XML , Pdf , Jpg , Tiff , Bild , Mht und XPS Dateien mit Node.js über C++ zu erstellen, zu öffnen und zu verwalten.
---

{{% alert color="primary" %}}

Mit Aspose.Cells ist es einfach, Excel-Dateien zu erstellen, zu öffnen und zu verwalten, z.B. um Daten abzurufen oder eine Designer-Vorlage zu verwenden, um den Entwicklungsprozess zu beschleunigen.

{{% /alert %}}

## **Neue Arbeitsmappe erstellen**
Das folgende Beispiel erstellt ein neues Arbeitsbuch von Grund auf.

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

## **Eine Datei öffnen und speichern**
Mit Aspose.Cells ist es einfach, Excel-Dateien zu öffnen, zu speichern und zu verwalten.

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

## **Erweiterte Themen**
- [Verschiedene Möglichkeiten, Dateien zu öffnen](/cells/de/nodejs-cpp/different-ways-to-open-files/)
- [Definierte Namen filtern beim Laden der Arbeitsmappe](/cells/de/nodejs-cpp/filter-defined-names-while-loading-workbook/)
- [Objekte filtern beim Laden einer Arbeitsmappe oder eines Arbeitsblatts](/cells/de/nodejs-cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [Die Art der Daten filtern, während die Arbeitsmappe aus einer Vorlagendatei geladen wird](/cells/de/nodejs-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Warnungen beim Laden von Excel-Dateien erhalten](/cells/de/nodejs-cpp/get-warnings-while-loading-excel-file/)
- [Quell-Excel-Datei ohne Diagramme laden](/cells/de/nodejs-cpp/load-source-excel-file-without-charts/)
- [Bestimmte Arbeitsblätter in einer Arbeitsmappe laden](/cells/de/nodejs-cpp/load-specific-worksheets-in-a-workbook/)
- [Arbeitsmappe mit angegebener Druckerpapiergröße laden](/cells/de/nodejs-cpp/load-workbook-with-specified-printer-paper-size/)
- [Öffnen von verschiedenen Microsoft Excel-Versionen Dateien](/cells/de/nodejs-cpp/opening-different-microsoft-excel-versions-files/)
- [Öffnen von Dateien mit verschiedenen Formaten](/cells/de/nodejs-cpp/opening-files-with-different-formats/)
- [Optimierung des Speicherverbrauchs beim Arbeiten mit großen Dateien und umfangreichen Datensätzen](/cells/de/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Zahlen-Tabellenkalkulation von Apple Inc. mit Aspose.Cells lesen](/cells/de/nodejs-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [ Konvertierung oder Laden mit InterruptMonitor stoppen, wenn es zu lange dauert](/cells/de/nodejs-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Verwendung der LightCells-API](/cells/de/nodejs-cpp/using-lightcells-api/)
- [Konvertieren von CSV in JSON](/cells/de/nodejs-cpp/convert-csv-to-json/)
- [Excel nach JSON konvertieren](/cells/de/nodejs-cpp/convert-excel-to-json/)
- [JSON in CSV konvertieren](/cells/de/nodejs-cpp/convert-json-to-csv/)
- [JSON in Excel konvertieren](/cells/de/nodejs-cpp/convert-json-to-excel/)
- [Excel in Html umwandeln](/cells/de/nodejs-cpp/convert-excel-to-html/)
