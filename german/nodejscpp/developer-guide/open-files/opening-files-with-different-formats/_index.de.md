---
title: Öffnen von Dateien mit unterschiedlichen Formaten mit Node.js über C++
linktitle: Öffnen von Dateien mit verschiedenen Formaten
type: docs
weight: 30
url: /de/nodejs-cpp/opening-files-with-different-formats/
description: Die API Aspose.Cells for Node.js via C++ ermöglicht das Öffnen/Lesen verschiedener Formate wie XLSX, HTML, CSV, ODS, TSV, SXC, FODS usw.
keywords: Öffnen von XLSX Dateien, Öffnen von HTML Dateien, Lesen von FODS Dateien, Lesen von ODS Dateien, Lesen von SXC Dateien, Öffnen von CSV Dateien, Tabstopp Delimited, SpreadsheetML, TSV, MHTML
---

{{% alert color="primary" %}}

Mit Aspose.Cells können Sie Dateien in verschiedenen Formaten öffnen. **Aspose.Cells** kann eine Reihe von Dateiformaten wie Microsoft Excel Tabellen (XLS, XLSX, XLSM, XLSB), SpreadsheetML, Komma-getrennte Werte (CSV), Tabulator-getrennte oder TSV-Dateien usw. öffnen.

Wenn Sie alle unterstützten Dateiformate kennen müssen, verweisen Sie bitte auf die folgenden Seiten:
[Unterstützte Dateiformate](https://docs.aspose.com/cells/nodejs-cpp/supported-file-formats/)

{{% /alert %}}

## **Öffnen von Dateien mit verschiedenen Formaten**

Aspose.Cells ermöglicht Entwicklern, Tabellendateien mit verschiedenen Formaten wie SpreadsheetML, durch Kommas getrennte Werte (CSV), Tab- oder Tabstopp-getrennte Werte (TSV), ODS-Dateien zu öffnen. Um solche Dateien zu öffnen, können Entwickler die gleiche Methodik verwenden wie beim Öffnen von Dateien verschiedener Microsoft Excel-Versionen.

### **Öffnen von SpreadsheetML-Dateien**

SpreadsheetML-Dateien sind XML-Darstellungen von Tabellen, die alle Informationen darüber enthalten, z.B. Formatierung, Formeln usw. Seit Microsoft Excel XP steht eine XML-Exportoption zur Verfügung, die Ihre Tabellen in SpreadsheetML-Dateien exportiert.

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

### **Öffnen von HTML-Dateien**

Aspose.Cells ermöglicht es, eine HTML-Datei in ein Workbook-Objekt zu laden. Die HTML-Datei sollte Microsoft Excel orientiert sein, d.h., MS-Excel sollte sie öffnen können.

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

### **Öffnen von CSV-Dateien**

Comma Separated Values (CSV)-Dateien enthalten Datensätze, bei denen die Werte durch Kommas getrennt sind. Die Daten werden als Tabelle gespeichert, wobei jede Spalte durch das Kommazeichen getrennt und durch doppelte Anführungszeichen eingeschlossen ist. Wenn ein Feldwert ein doppelt-anklicken Zeichen enthält, wird es mit einem Paar doppelter Anführungszeichen maskiert. Sie können auch Microsoft Excel verwenden, um Tabellenkalkulationsdaten in CSV zu exportieren.

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

#### **Öffnen von CSV-Dateien und Ersetzen ungültiger Zeichen**

Wenn in Excel eine CSV-Datei mit Sonderzeichen geöffnet wird, werden die Zeichen automatisch ersetzt. Das gleiche passiert mit der Aspose.Cells API, was im unten stehenden Codebeispiel demonstriert wird.

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

### **Öffnen von Textdateien mit benutzerdefiniertem Trennzeichen**

Textdateien werden verwendet, um Tabellendaten ohne Formatierung zu halten. Die Datei ist eine Art reine Textdatei, die einige benutzerdefinierte Trennzeichen haben kann.

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

### **Öffnen von tabstoppgetrennten Dateien**

Tabulator-getrennte (Text)-Dateien enthalten Tabellenkalkulationsdaten, jedoch ohne jegliche Formatierung. Daten sind in Zeilen und Spalten angeordnet, ähnlich wie in Tabellen und Tabellenkalkulationen. Grundsätzlich ist eine tabulatorgetrennte Datei eine spezielle Art von einfachem Textfile mit einem Tabulator zwischen den Spalten.

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

### **Öffnen von tabstoppgetrennten Werten (TSV) Dateien**

Tabulator-getrennte (TSV)-Dateien enthalten Tabellenkalkulationsdaten, jedoch ohne jegliche Formatierung. Es ist identisch mit einer tabulatorgetrennten Datei, bei der Daten in Zeilen und Spalten wie in Tabellen und Tabellenkalkulationen angeordnet sind.

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

### **Öffnen von SXC Dateien**

StarOffice Calc ist ähnlich wie Microsoft Excel und unterstützt Formeln, Diagramme, Funktionen und Makros. Die mit dieser Software erstellten Tabellen werden mit der SXC-Erweiterung gespeichert. Die SXC-Datei wird auch für OpenOffice.org Calc-Tabellen verwendet. Aspose.Cells kann SXC-Dateien lesen, wie das folgende Codebeispiel zeigt.

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

### **Öffnen von FODS Dateien**

FODS-Dateien sind Tabellen, die im OpenDocument XML-Format gespeichert sind, ohne Kompression. Aspose.Cells kann FODS-Dateien lesen, wie im folgenden Codebeispiel gezeigt.

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
