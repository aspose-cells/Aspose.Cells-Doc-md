---
title: Verschiedene Möglichkeiten, Dateien mit Node.js über C++ zu speichern
linktitle: Dateien speichern
type: docs
weight: 40
url: /de/nodejs-cpp/different-ways-to-save-files/
description: Aspose.Cells for Node.js via C++ kann Dateien in verschiedene Formate speichern, darunter PDF, HTML, DOCX, PPTX, JSON und MHTML.
keywords: Aspose.Cells speichert Excel in PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML und mehr mit Node.js über C++.
---

{{% alert color="primary" %}}

Mit Aspose.Cells ist es möglich, Dateien zu erstellen und zu speichern. Dieser Artikel erklärt die verschiedenen Möglichkeiten, wie Dateien gespeichert werden können.

{{% /alert %}}

## **Verschiedene Möglichkeiten, Dateien zu speichern**

Aspose.Cells stellt die [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) bereit, die eine Microsoft Excel-Datei repräsentiert und die Eigenschaften sowie Methoden zum Arbeiten mit Excel-Dateien bietet. Die [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Klasse bietet die [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)-Methode zum Speichern von Excel-Dateien. Die [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)-Methode hat viele Überladungen, um Dateien auf unterschiedliche Weisen zu speichern.

Das Dateiformat, in das die Datei gespeichert wird, wird durch die [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)-Aufzählung festgelegt.

|**Dateiformat-Typen**|**Beschreibung**|
| :- | :- |
|CSV|Repräsentiert eine CSV-Datei|
|Excel97To2003|Stellt eine Excel 97 - 2003-Datei dar|
|Xlsx|Repräsentiert eine Excel 2007 XLSX Datei|
|Xlsm|Repräsentiert eine Excel 2007 XLSM Datei|
|Xltx|Repräsentiert eine Excel 2007 Vorlagen XLTX Datei|
|Xltm|Repräsentiert eine Excel 2007 makrofähige XLTM Datei|
|Xlsb|Repräsentiert eine Excel 2007 binäre XLSB Datei|
|SpreadsheetML|Repräsentiert eine Tabellenkalkulation XML-Datei|
|TSV|Repräsentiert eine durch Tabulatoren getrennte Werte-Datei|
|TabDelimited|Stellt eine tabulatorgetrennte Textdatei dar|
|ODS|Repräsentiert eine ODS-Datei|
|Html|Repräsentiert HTM L-Datei(en)|
|MHtml|Repräsentiert eine MHTML Datei(en)|
|Pdf|Repräsentiert eine PDF-Datei|
|XPS|Repräsentiert ein XPS-Dokument|
|TIFF|Repräsentiert das Dateiformat für markierte Bilddatei (TIFF)|

## **Wie man Datei in verschiedenen Formaten speichert**

Um Dateien an einem Speicherort zu speichern, geben Sie beim Aufrufen der [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Methode des [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)-Objekts den Dateinamen (einschließlich Speicherpfad) und das gewünschte Dateiformat (aus der [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)-Aufzählung) an.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save in Excel 97 to 2003 format
workbook.save(path.join(dataDir, ".output.xls"));
// OR
workbook.save(path.join(dataDir, ".output.xls"), new AsposeCells.XlsSaveOptions());

// Save in Excel 2007 xlsx format
workbook.save(path.join(dataDir, ".output.xlsx"), AsposeCells.SaveFormat.Xlsx);

// Save in Excel 2007 xlsb format
workbook.save(path.join(dataDir, ".output.xlsb"), AsposeCells.SaveFormat.Xlsb);

// Save in ODS format
workbook.save(path.join(dataDir, ".output.ods"), AsposeCells.SaveFormat.Ods);

// Save in Pdf format
workbook.save(path.join(dataDir, ".output.pdf"), AsposeCells.SaveFormat.Pdf);

// Save in Html format
workbook.save(path.join(dataDir, ".output.html"), AsposeCells.SaveFormat.Html);

// Save in SpreadsheetML format
workbook.save(path.join(dataDir, ".output.xml"), AsposeCells.SaveFormat.SpreadsheetML);
```

## **Wie man eine Arbeitsmappe als PDF speichert**
Das Portable Document Format (PDF) ist ein von Adobe in den 1990er Jahren entwickeltes Dokumentenformat. Ziel dieses Formats war die Einführung eines Standards für die Darstellung von Dokumenten und anderen Referenzmaterialien in einem Format, das unabhängig von Anwendungssoftware, Hardware und Betriebssystem ist. PDF kann Informationen wie Text, Bilder, Hyperlinks, Formularfelder, Rich Media, digitale Signaturen, Anhänge, Metadaten, Geodaten und 3D-Objekte enthalten, die Teil des Quell Dokuments werden können.

Der folgende Code zeigt, wie man ein Arbeitsblatt mit Aspose.Cells als PDF speichert:
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Set value to Cell.
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Hello World!");

const saveFilePath = path.join(dataDir, "pdf1.pdf");
workbook.save(saveFilePath);

// Save as Pdf format compatible with PDFA-1a
const saveOptions = new AsposeCells.PdfSaveOptions();
saveOptions.setCompliance(AsposeCells.PdfCompliance.PdfA1a);

const pdfAFilePath = path.join(dataDir, "pdfa1a.pdf");
workbook.save(pdfAFilePath, saveOptions);
```

## **Wie man eine Arbeitsmappe im Text- oder CSV-Format speichert**

Manchmal möchten Sie eine Arbeitsmappe mit mehreren Arbeitsblättern in Textformat konvertieren oder speichern. Für Textformate (zum Beispiel TXT, TabDelim, CSV usw.) speichern sowohl Microsoft Excel als auch Aspose.Cells standardmäßig nur den Inhalt des aktiven Arbeitsblatts.

Das folgende Codebeispiel erklärt, wie man ein gesamtes Arbeitsblatt in Textformat speichert. Laden Sie das Quell-Arbeitsblatt, das jede Microsoft Excel- oder OpenOffice-Tabellendatei sein kann (z.B. XLS, XLSX, XLSM, XLSB, ODS etc.), mit beliebiger Anzahl von Arbeitsblättern.

Beim Ausführen des Codes werden die Daten aller Blätter in der Arbeitsmappe in das TXT-Format konvertiert

Sie können dasselbe Beispiel anpassen, um Ihre Datei als CSV zu speichern. Standardmäßig ist [**TxtSaveOptions.getSeparator()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getSeparator--) das Komma, daher geben Sie keinen Trenner an, wenn Sie im CSV-Format speichern. Bitte beachten Sie: Wenn Sie die Evaluierungsversion verwenden und selbst wenn die [**TxtSaveOptions.getExportAllSheets()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getExportAllSheets--)-Eigenschaft auf true gesetzt ist, wird die Anwendung immer nur ein Arbeitsblatt exportieren.

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

## **Wie man eine Datei in Textdateien mit benutzerdefiniertem Trennzeichen speichert**

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

## **Wie man eine Datei in einen Stream speichert**

Um Dateien in einen Stream zu speichern, erstellen Sie ein *MemoryStream* oder *FileStream*-Objekt und speichern Sie die Datei in dieses Stream-Objekt, indem Sie die [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Methode des [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)-Objekts aufrufen. Geben Sie das gewünschte Dateiformat mit der [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)-Aufzählung an, wenn Sie die [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)-Methode aufrufen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

async function downloadExcel(req, res) {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);
// Save the workbook to a memory stream
const stream = workbook.save(AsposeCells.SaveFormat.Xlsx);

// Set the content type and file name
const contentType = "application/octet-stream";
const fileName = "output.xlsx";

// Set the response headers
res.setHeader("Content-Disposition", `attachment; filename="${fileName}"`);
res.setHeader("Content-Type", contentType);

// Write the file contents to the response body stream
res.send(stream);
}
```

## **Wie man eine Excel-Datei in Html- und Mht-Dateien speichert**
Aspose.Cells kann eine Excel-Datei, JSON, CSV oder andere Dateien einfach speichern, die von Aspose.Cells als .html- und .mht-Dateien geladen werden können.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to mhtml format
workbook.save("out.mht");
```


## **Wie man eine Excel-Datei in das OpenOffice-Format (ODS, SXC, FODS, OTS) speichert**
Wir können die Dateien im OpenOffice-Format speichern: ODS, SXC, FODS, OTS usw.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xlsx"));
// Save as ods file 
workbook.save("Out.ods");
// Save as sxc file 
workbook.save("Out.sxc");
// Save as fods file 
workbook.save("Out.fods");
```

## **Wie man eine Excel-Datei in JSON- oder XML-Dateien speichert**

JSON (JavaScript Object Notation) ist ein offenes Standarddateiformat zum Austausch von Daten, das menschenlesbaren Text zur Speicherung und Übertragung von Daten verwendet. JSON-Dateien werden mit der Erweiterung .json gespeichert. JSON erfordert weniger Formatierung und ist eine gute Alternative für XML. JSON leitet sich von JavaScript ab, ist jedoch ein sprachunabhängiges Datenformat. Die Generierung und Analyse von JSON wird von vielen modernen Programmiersprachen unterstützt. application/json ist der Medientyp, der für JSON verwendet wird.

Aspose.Cells unterstützt das Speichern von Dateien als JSON oder XML.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save(path.join(dataDir, "book1.json"));
```


## **Erweiterte Themen**
- [Anpassen des Arbeitsmappe-Komprimierungsgrads](/cells/de/nodejs-cpp/adjust-workbook-compression-level/)
- [Arbeitsmappe im Strict Open XML-Tabellenkalkulationsformat speichern](/cells/de/nodejs-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Speichern der Datei im Antwortobjekt](/cells/de/nodejs-cpp/saving-file-to-response-object/)
