---
title: Verschiedene Möglichkeiten, Dateien mit Node.js via C++ zu öffnen
linktitle: Verschiedene Möglichkeiten, Dateien zu öffnen
type: docs
weight: 10
url: /de/nodejs-cpp/different-ways-to-open-files/
description: Dieser Artikel erklärt, wie eine Excel Datei mit der Aspose.Cells for Node.js via C++ API geöffnet werden kann.
keywords: Node.js eine Excel Datei ohne Excel öffnen – Wie öffne ich eine Excel Datei mit Node.js?
---

{{% alert color="primary" %}}

Mit Aspose.Cells ist es einfach, Dateien zu öffnen, beispielsweise um Daten abzurufen oder einen Designer-Template zu verwenden, um den Entwicklungsprozess zu beschleunigen.

{{% /alert %}}

## **Wie man eine Excel-Datei über einen Pfad öffnet**

Entwickler können eine Microsoft Excel-Datei öffnen, indem sie den Dateipfad auf dem lokalen Computer in den Konstruktor der [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Klasse übergeben. Einfach den Pfad als *String* im Konstruktor übergeben. Aspose.Cells erkennt automatisch den Dateityp.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Opening through Path
// Creating a Workbook object and opening an Excel file using its file path
const workbook1 = new AsposeCells.Workbook(filePath);
console.log("Workbook opened using path successfully!");
```

## **Wie man eine Excel-Datei über einen Stream öffnet**

Es ist auch einfach, eine Excel-Datei als Stream zu öffnen. Verwenden Sie dazu eine überladene Version des Konstruktors, der das *Stream*-Objekt enthält, das die Datei enthält.

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book2.xls");
// Opening through Stream
// Create a Stream object
const fstream = fs.createReadStream(filePath);

// Creating a Workbook object, open the file from a Stream object
// That contains the content of file and it should support seeking
const chunks = [];
fstream.on('data', (chunk) => {
chunks.push(chunk);
```

## **Wie man eine Datei nur mit Daten öffnet**

Um eine Datei nur mit Daten zu öffnen, verwenden Sie die Klassen [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) und [**LoadFilter**](https://reference.aspose.com/cells/nodejs-cpp/loadfilter), um die entsprechenden Attribute und Optionen der Klassen für die zu ladende Vorlage festzulegen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load only specific sheets with data and formulas
// Other objects, items etc. would be discarded

// Instantiate LoadOptions specified by the LoadFormat
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);

// Set LoadFilter property to load only data & cell formatting
loadOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData));

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"), loadOptions);
console.log("File data imported successfully!");
```

## **Wie man nur sichtbare Blätter lädt**

Beim Laden einer [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) ist es manchmal ausreichend, nur die Daten in sichtbaren Arbeitsblättern einer Arbeitsmappe zu benötigen. Aspose.Cells erlaubt es, Daten in unsichtbaren Arbeitsblättern beim Laden einer Arbeitsmappe zu überspringen. Dazu erstellen Sie eine benutzerdefinierte Funktion, die von der Klasse [**LoadFilter**](https://reference.aspose.com/cells/nodejs-cpp/loadfilter) erbt, und übergeben die Instanz an die [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--)-Eigenschaft.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sampleFile = "output.xlsx";
const samplePath = path.join(dataDir, sampleFile);

// Create a sample workbook
// and put some data in first cell of all 3 sheets
const createWorkbook = new AsposeCells.Workbook();
createWorkbook.getWorksheets().get("Sheet1").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().add("Sheet2").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().add("Sheet3").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().get("Sheet3").setIsVisible(false);
createWorkbook.save(samplePath);

// Load the sample workbook
const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setLoadFilter(new AsposeCells.LoadFilter()); // Corrected line by defining LoadFilter properly

const loadWorkbook = new AsposeCells.Workbook(samplePath, loadOptions);
console.log(`Sheet1: A1: ${loadWorkbook.getWorksheets().get("Sheet1").getCells().get("A1").getValue()}`);
console.log(`Sheet1: A2: ${loadWorkbook.getWorksheets().get("Sheet2").getCells().get("A1").getValue()}`);
console.log(`Sheet1: A3: ${loadWorkbook.getWorksheets().get("Sheet3").getCells().get("A1").getValue()}`);
```

Hier ist die Implementierung der in der obigen Codezeile referenzierten *CustomLoad*-Klasse.

```javascript
const { Workbook, LoadDataFilterOptions } = require("aspose.cells.node");

class CustomLoad {
startSheet(sheet) {
if (sheet.isVisible()) {
// Load everything from visible worksheet
this.loadDataFilterOptions = LoadDataFilterOptions.All;
} else {
// Load nothing
this.loadDataFilterOptions = LoadDataFilterOptions.Structure;
}
}
}
```

{{% alert color="primary" %}}

Eine Ausnahme wird ausgelöst, wenn versucht wird, Nicht-Excel-Formate (z.B. PPT/PPTX, DOC/DOCX usw.) mit Aspose.Cells zu öffnen.

{{% /alert %}} 

{{% alert color="primary" %}}

Es besteht die Wahrscheinlichkeit, dass der [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Konstruktor beim Laden großer Tabellenkalkulationen eine *OutOfMemoryError* auslösen kann. Diese Ausnahme deutet darauf hin, dass der verfügbaren Speicher nicht ausreicht, um die Tabelle vollständig in den Speicher zu laden; daher muss die Tabelle beim Laden die Speicherpräferenzen aktiviert haben.

{{% /alert %}}

