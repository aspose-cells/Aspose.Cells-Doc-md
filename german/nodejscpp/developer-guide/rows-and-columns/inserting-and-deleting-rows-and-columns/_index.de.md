---
title: Einfügen und Löschen von Zeilen und Spalten einer Excel Datei
linktitle: Einfügen und Löschen von Zeilen und Spalten
type: docs
weight: 70
url: /de/nodejs-cpp/inserting-and-deleting-rows-and-columns/
description: Dieser Artikel zeigt, wie Zeilen und Spalten mit der Aspose.Cells for Node.js via C++ API eingefügt und gelöscht werden können.
keywords: Aspose.Cells Node.js via C++ verwalten Zeilen und Spalten, Zeilen und Spalten einfügen, Zeilen und Spalten löschen
---

## **Einführung**

Beim Erstellen eines neuen Arbeitsblatts von Grund auf oder bei der Arbeit an einem vorhandenen Arbeitsblatt müssen möglicherweise zusätzliche Zeilen oder Spalten hinzugefügt werden, um mehr Daten aufzunehmen. Umgekehrt können auch Zeilen oder Spalten von bestimmten Positionen im Arbeitsblatt gelöscht werden. 
Um diese Anforderungen zu erfüllen, bietet Aspose.Cells for Node.js via C++ eine sehr einfache Reihe von Klassen und Methoden, die im Folgenden diskutiert werden.

### **Zeilen und Spalten verwalten**

Aspose.Cells for Node.js via C++ bietet eine Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)-, die Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse bietet eine [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-Sammlung, die alle Zellen im Arbeitsblatt enthält.

Die [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-Sammlung bietet mehrere Methoden zur Verwaltung von Zeilen und Spalten in einem Arbeitsblatt. Einige davon werden im Folgenden besprochen.

{{% alert color="primary" %}}

Wenn Zeilen oder Spalten hinzugefügt werden, verschiebt sich der Inhalt im Arbeitsblatt nach unten oder nach rechts, und wenn Zeilen oder Spalten entfernt werden, verschiebt sich der Inhalt nach oben oder nach links.

{{% /alert %}}


## **Zeilen und Spalten einfügen**

### **Wie man eine Zeile einfügt**

Fügen Sie eine Zeile in das Arbeitsblatt an einer beliebigen Stelle ein, indem Sie die Methode [**insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) der Sammlung [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) aufrufen. Die Methode [**insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) übernimmt den Index der Zeile, an der die neue Zeile eingefügt wird.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Inserting a row into the worksheet at 3rd position
worksheet.getCells().insertRow(2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

### **Wie man mehrere Zeilen einfügt**

Um mehrere Zeilen in ein Arbeitsblatt einzufügen, rufen Sie die Methode [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) der Sammlung [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) auf. Die Methode [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) übernimmt zwei Parameter:

- Zeilenindex, der Index der Zeile, ab der die neuen Zeilen eingefügt werden.
- Anzahl der Zeilen, die insgesamt eingefügt werden müssen.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

const fileData = fs.readFileSync(filePath);
const workbook = new AsposeCells.Workbook(fileData);

const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().insertRows(2, 10);

workbook.save(path.join(dataDir, "output.out.xls"));
```

### **Wie man eine Zeile mit Formatierung einfügt**

Um eine Zeile mit Formatierungsoptionen einzufügen, verwenden Sie die Überladung von [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-), die [**InsertOptions**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions) als Parameter akzeptiert. Setzen Sie die [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/)-Eigenschaft der Klasse [**InsertOptions**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions) mit der [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/)-Enumeration. Die [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/)-Enumeration hat drei unten aufgeführte Elemente.

- SameAsAbove: Formatiert die Zeile wie die darüber liegende Zeile.
- SameAsBelow: Formatiert die Zeile wie die unterhalb liegende Zeile.
- Löschen: Löscht das Format.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "book1.xls");
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting Formatting options
const insertOptions = new AsposeCells.InsertOptions();
insertOptions.setCopyFormatType(AsposeCells.CopyFormatType.SameAsAbove);

// Inserting a row into the worksheet at 3rd position
worksheet.getCells().insertRows(2, 1, insertOptions);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "InsertingARowWithFormatting.out.xls"));
```

### **Wie man eine Spalte einfügt**

Entwickler können auch eine Spalte in das Arbeitsblatt an beliebiger Stelle einfügen, indem sie die Methode [**insertColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertColumn-number-boolean-) der Sammlung [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) aufrufen. Die Methode [**insertColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertColumn-number-boolean-) erfordert den Index der Spalte, in die die neue Spalte eingefügt werden soll.

```javascript
const fs = require('fs');
const path = require('path');
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

// Inserting a column into the worksheet at 2nd position
worksheet.getCells().insertColumn(1);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **Zeilen und Spalten löschen**

### **Wie man mehrere Zeilen löscht**

Um mehrere Zeilen aus einem Arbeitsblatt zu löschen, rufen Sie die Methode [**deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) der Sammlung [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) auf. Die Methode [**deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) erfordert zwei Parameter:

- Zeilenindex, der Index der Zeile, ab der die Zeilen gelöscht werden.
- Anzahl der Zeilen, die insgesamt gelöscht werden müssen.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Read file contents as Uint8Array
const fileContent = fs.readFileSync(filePath);
const fileBuffer = new Uint8Array(fileContent);

// Instantiating a Workbook object with file buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Deleting 10 rows from the worksheet starting from 3rd row
worksheet.getCells().deleteRows(2, 10);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```


### **Wie man eine Spalte löscht**

Um eine Spalte aus dem Arbeitsblatt an beliebiger Stelle zu löschen, rufen Sie die Methode [**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteColumn-number-boolean-) der Sammlung [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) auf. Die Methode [**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteColumn-number-boolean-) erfordert den Index der zu löschenden Spalte.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fs.readFileSync(filePath));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Deleting a column from the worksheet at 5th position
worksheet.getCells().deleteColumn(4);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));

// Closing resources is handled automatically by Node.js, no specific close needed.
```
