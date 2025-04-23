---
title: Excel in CSV, TSV und Txt mit Node.js via C++ umwandeln
linktitle: Als CSV, TSV und Txt speichern
type: docs
weight: 40
url: /de/nodejs-cpp/convert-excel-to-csv-tsv-and-txt/
description: Erfahren Sie, wie Sie Excel Dateien mithilfe von Aspose.Cells for Node.js via C++ in CSV, TSV und TXT Formate umwandeln.
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht die Konvertierung von Excel-, ODS-, JSON- und anderen Formatdateien in CSV, TSV und TXT.

{{% /alert %}}

## **Arbeitsmappe in Text- oder CSV-Format speichern**

Manchmal möchten Sie ein Arbeitsbuch mit mehreren Arbeitsblättern in Textformat umwandeln oder speichern. Für Textformate (zum Beispiel TXT, TabDelim, CSV usw.) speichern sowohl Microsoft Excel als auch Aspose.Cells standardmäßig nur den Inhalt des aktiven Arbeitsblatts.

Das folgende Code-Beispiel erklärt, wie man ein vollständiges Arbeitsbuch in Textformat speichert. Laden Sie das Quellarbeitsbuch, das jede Microsoft Excel- oder OpenOffice-Tabellendatei (also XLS, XLSX, XLSM, XLSB, ODS usw.) mit beliebiger Anzahl an Arbeitsblättern sein kann.

Beim Ausführen des Codes werden die Daten aller Blätter in der Arbeitsmappe in das TXT-Format konvertiert

Sie können das gleiche Beispiel anpassen, um Ihre Datei als CSV zu speichern. Standardmäßig ist [**TxtSaveOptions.getSeparator()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getSeparator--) ein Komma, geben Sie also keinen Separator an, wenn Sie im CSV-Format speichern.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Text save options. You can use any type of separator
const opts = new AsposeCells.TxtSaveOptions();
opts.setSeparator('\t');
opts.setExportAllSheets(true);

// Save entire workbook data into file
workbook.save(path.join(dataDir, "out.txt"), opts);
```

## **Textdateien mit benutzerdefiniertem Trennzeichen speichern**

Textdateien enthalten Tabellendaten ohne Formatierung

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath);

// Instantiate Text File's Save Options
const options = new AsposeCells.TxtSaveOptions();

// Specify the separator
options.setSeparator(";");

// Save the file with the options
wb.save(path.join(dataDir, "output.csv"), options);
```


## **Erweiterte Themen**
- [Trennzeichen für leere Zeilen beim Exportieren von Tabellenkalkulationen im CSV-Format beibehalten](/cells/de/nodejs-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Führende leere Zeilen und Spalten beim Export von Tabellenkalkulationen in das CSV-Format abschneiden](/cells/de/nodejs-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
