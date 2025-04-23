---
title: Verstecken und Anzeigen von Zeilen und Spalten mit Node.js via C++
linktitle: Zeilen und Spalten ausblenden und anzeigen
type: docs
weight: 60
url: /de/nodejs-cpp/hiding-and-showing-rows-and-columns/
description: Lernen Sie, wie Sie Zeilen und Spalten in einem Arbeitsblatt mit Aspose.Cells for Node.js via C++ ausblenden und anzeigen.
---

{{% alert color="primary" %}}

Manchmal macht es Sinn, bestimmte Zeilen oder Spalten in einem Arbeitsblatt zu verstecken und später anzuzeigen. Microsoft Excel bietet diese Funktion und auch Aspose.Cells.

{{% /alert %}}

## **Steuerung der Sichtbarkeit von Zeilen und Spalten**

Aspose.Cells for Node.js via C++ bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) enthält eine [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection), die Entwicklern Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) stellt eine [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung bereit, die alle Zellen im Arbeitsblatt enthält. Die [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung bietet mehrere Methoden zur Verwaltung von Zeilen oder Spalten in einem Arbeitsblatt. Einige davon werden im Folgenden besprochen.

### **Verbergen von Zeilen und Spalten**

Entwickler können eine Zeile oder Spalte ausblenden, indem sie die Methoden [**hideRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRow-number-) und [**hideColumn(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumn-number-) der [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) Sammlung aufrufen. Beide Methoden nehmen den Zeilen- und Spaltenindex als Parameter, um die spezifische Zeile oder Spalte auszublenden.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fileBuffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with Uint8Array
const workbook = new AsposeCells.Workbook(new Uint8Array(fileBuffer));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the 3rd row of the worksheet
worksheet.getCells().hideRow(2);

// Hiding the 2nd column of the worksheet
worksheet.getCells().hideColumn(1);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

{{% alert color="primary" %}}

Es ist auch möglich, eine Zeile oder Spalte auszublenden, indem die Zeilenhöhe oder Spaltenbreite auf 0 gesetzt wird.

{{% /alert %}}

### **Anzeigen von Zeilen und Spalten**

Entwickler können jede ausgeblendete Zeile oder Spalte anzeigen, indem sie die Methoden [**unhideRow(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRow-number-number-) und [**unhideColumn(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumn-number-number-) der [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) Sammlung jeweils aufrufen. Beide Methoden nehmen zwei Parameter:

- **Zeilen- oder Spaltenindex** - der Index einer Zeile oder Spalte, der verwendet wird, um die spezifische Zeile oder Spalte anzuzeigen.
- **Zeilenhöhe oder Spaltenbreite** - die Zeilenhöhe oder Spaltenbreite, die der Zeile oder Spalte nach dem Ausblenden zugewiesen wird.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Read the Excel file into a Buffer (Uint8Array)
const fileBuffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with file buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unhiding the 3rd row and setting its height to 13.5
worksheet.getCells().unhideRow(2, 13.5);

// Unhiding the 2nd column and setting its width to 8.5
worksheet.getCells().unhideColumn(1, 8.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

{{% alert color="primary" %}}

Beim Anzeigen einer verborgenen Spalte, die zuvor auf eine bestimmte Breite eingestellt war oder auf ihre ursprüngliche Breite zurückgesetzt werden soll, können Sie die Spalte mit einer negativen Breite sichtbar machen. Beispiel: worksheet.cells.unhideColumn(5, -1)

{{% /alert %}}

### **Mehrere Zeilen und Spalten verstecken**

Entwickler können mehrere Zeilen oder Spalten gleichzeitig ausblenden, indem sie die Methoden [**hideRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRows-number-number-) und [**hideColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumns-number-number-) der [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) Sammlung aufrufen. Beide Methoden nehmen den Startindex der Zeile oder Spalte und die Anzahl der Zeilen oder Spalten, die ausgeblendet werden sollen, als Parameter.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fileStream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fileStream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding 3, 4, and 5 rows in the worksheet
worksheet.getCells().hideRows(2, 3);

// Hiding 2 and 3 columns in the worksheet
worksheet.getCells().hideColumns(1, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "outputxls"));
```

{{% alert color="primary" %}}

Es ist auch möglich, die [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Klasse mit den [**unhideRows(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRows-number-number-number-)- und [**unhideColumns(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumns-number-number-number-)-Methoden zu verwenden, um mehrere Zeilen und Spalten sichtbar zu machen.

{{% /alert %}}
