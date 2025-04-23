---
title: Arbeitsblätter mit Node.js über C++ kopieren und verschieben
linktitle: Arbeitsblätter kopieren und verschieben
type: docs
weight: 10
url: /de/nodejs-cpp/copying-and-moving-worksheets/
description: Dieser Artikel enthält Beispielcode und beschreibt, wie Sie Arbeitsblätter programmgesteuert innerhalb einer Excel Arbeitsmappe und zwischen Excel Arbeitsmappen mit der Node.js API und C++ kopieren und verschieben.
keywords: Arbeitsblatt kopieren Node.js, Arbeitsblatt verschieben Node.js
---

{{% alert color="primary" %}}

Manchmal benötigen Sie eine Reihe von Arbeitsblättern mit gemeinsamer Formatierung und Daten. Wenn Sie beispielsweise mit vierteljährlichen Budgets arbeiten, möchten Sie möglicherweise eine Arbeitsmappe erstellen, die Tabellenblätter mit denselben Spaltenüberschriften, Zeilenüberschriften und Formeln enthält. Es gibt eine Möglichkeit, das zu tun: Indem Sie ein Blatt erstellen und es dann kopieren.

Aspose.Cells for Node.js via C++ unterstützt das Kopieren und Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen. Arbeitsblätter mit Daten, Formatierungen, Tabellen, Matrizen, Diagrammen, Bildern und anderen Objekten werden mit höchster Präzision kopiert.

{{% /alert %}}

## **Verschieben oder Kopieren von Blättern mit Microsoft Excel**

Im Folgenden sind die Schritte für das Kopieren und Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen in Microsoft Excel aufgeführt.

1. Um Blätter zu einem anderen Arbeitsmappen zu verschieben oder zu kopieren, öffnen Sie die Arbeitsmappe, die die Blätter empfangen wird.
1. Wechseln Sie zum Arbeitsmappe, die die Blätter enthält, die Sie verschieben oder kopieren möchten, und wählen Sie dann die Blätter aus.
1. Klicken Sie im **Bearbeiten** Menü auf **Blatt verschieben oder kopieren**.
1. Klicken Sie im Dialogfeld **Zu Arbeitsbuch** auf das Arbeitsbuch, um die Blätter zu empfangen.
1. Um die ausgewählten Blätter in ein neues Arbeitsbuch zu verschieben oder zu kopieren, klicken Sie auf **Neues Buch**.
1. Wählen Sie im Feld 'Vor Blatt' das Blatt aus, vor dem Sie die verschobenen oder kopierten Blätter einfügen möchten.
1. Um die Blätter zu kopieren anstatt sie zu verschieben, aktivieren Sie das Kontrollkästchen **Kopie erstellen**.

### **Arbeitsblätter innerhalb einer Arbeitsmappe mit Aspose.Cells for Node.js via C++ kopieren**

Aspose.Cells stellt eine überladene Methode, [**Aspose.Cells.WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#addCopy-number-), bereit, die verwendet wird, um ein Arbeitsblatt zur Sammlung hinzuzufügen und Daten von einem vorhandenen Arbeitsblatt zu kopieren. Eine Version der Methode nimmt den Index des Quellarbeitsblatts als Parameter an. Die andere Version nimmt den Namen des Quellarbeitsblatts an.

Das folgende Beispiel zeigt, wie ein vorhandenes Arbeitsblatt innerhalb einer Arbeitsmappe kopiert wird.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xls");

// Open an existing Excel file.
const wb = new AsposeCells.Workbook(inputPath);

// Create a Worksheets object with reference to
// the sheets of the Workbook.
const sheets = wb.getWorksheets();

// Copy data to a new sheet from an existing
// sheet within the Workbook.
sheets.addCopy("Sheet1");

// Save the Excel file.
wb.save(path.join(dataDir, "CopyWithinWorkbook_out.xls"));
```

### **Arbeitsblätter zwischen Arbeitsmappen kopieren**

Aspose.Cells bietet eine Methode, [**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#copy-worksheet-), mit der Daten und Formatierungen von einem Quellarbeitsblatt auf ein anderes Arbeitsblatt innerhalb oder zwischen Arbeitsmappen kopiert werden. Die Methode nimmt das Quellarbeitsblatt-Objekt als Parameter.

Das folgende Beispiel zeigt, wie ein Arbeitsblatt von einer Arbeitsmappe in eine andere kopiert wird.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xls");

// Create a Workbook.
// Open a file into the first book.
const excelWorkbook0 = new AsposeCells.Workbook(inputPath);

// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook();

// Copy the first sheet of the first book into second book.
excelWorkbook1.getWorksheets().get(0).copy(excelWorkbook0.getWorksheets().get(0));

// Save the file.
excelWorkbook1.save(path.join(dataDir, "CopyWorksheetsBetweenWorkbooks_out.xls"));
```

Das folgende Beispiel zeigt, wie ein Arbeitsblatt von einer Arbeitsmappe in eine andere kopiert wird.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook.
const excelWorkbook0 = new AsposeCells.Workbook();

// Get the first worksheet in the book.
const ws0 = excelWorkbook0.getWorksheets().get(0);

// Put some data into header rows (A1:A4)
for (let i = 0; i < 5; i++) {
ws0.getCells().get(i, 0).putValue(`Header Row ${i}`);
}

// Put some detail data (A5:A999)
for (let i = 5; i < 1000; i++) {
ws0.getCells().get(i, 0).putValue(`Detail Row ${i}`);
}

// Define a pagesetup object based on the first worksheet.
const pagesetup = ws0.getPageSetup();

// The first five rows are repeated in each page...
// It can be seen in print preview.
pagesetup.setPrintTitleRows("$1:$5");

// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook();

// Get the first worksheet in the book.
const ws1 = excelWorkbook1.getWorksheets().get(0);

// Name the worksheet.
ws1.setName("MySheet");

// Copy data from the first worksheet of the first workbook into the
// first worksheet of the second workbook.
ws1.copy(ws0);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "CopyWorksheetFromWorkbookToOther_out.xls"));
```

### **Arbeitsblätter innerhalb einer Arbeitsmappe verschieben**

Aspose.Cells stellt die Methode [**Aspose.Cells.Worksheet.moveTo()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#moveto-number-) bereit, um ein Arbeitsblatt an eine andere Stelle in derselben Tabelle zu verschieben. Die Methode nimmt den Zielarbeitsblattindex als Parameter.

Das folgende Beispiel zeigt, wie ein Arbeitsblatt an einen anderen Ort innerhalb der Arbeitsmappe verschoben wird.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "sample1.xlsx");

// Open an existing excel file.
const wb = new AsposeCells.Workbook(inputPath);

// Create a Worksheets object with reference to the sheets of the Workbook.
const sheets = wb.getWorksheets();

// Get the first worksheet.
const worksheet = sheets.get(0);

// Move the first sheet to the third position in the workbook.
worksheet.moveTo(2);

// Save the excel file.
wb.save(path.join(dataDir, "MoveWorksheet_out.xls"));
```
