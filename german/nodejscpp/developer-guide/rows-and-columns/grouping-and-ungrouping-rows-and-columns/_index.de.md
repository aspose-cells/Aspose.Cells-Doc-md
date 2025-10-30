---
title: Gruppieren und Entgruppieren von Zeilen und Spalten mit Node.js via C++
linktitle: Gruppieren und Aufheben der Gruppierung von Zeilen und Spalten
type: docs
weight: 50
url: /de/nodejs-cpp/grouping-and-ungrouping-rows-and-columns/
description: Entdecken Sie, wie Sie Zeilen und Spalten in Excel mit Aspose.Cells for Node.js via C++ gruppieren und aufheben können.
--- 

## **Einführung**

In einer Microsoft Excel-Datei können Sie eine Gliederung für die Daten erstellen, um mit einem einzigen Mausklick Ebenen von Details anzuzeigen und auszublenden.

Klicken Sie auf die **Gliederungssymbole**, 1,2,3, + und -, um nur die Zeilen oder Spalten anzuzeigen, die Zusammenfassungen oder Überschriften für Abschnitte in einem Arbeitsblatt bereitstellen, oder verwenden Sie die Symbole, um Details unter einer einzelnen Zusammenfassung oder Überschrift anzuzeigen, wie unten in der Abbildung gezeigt:

|**Gruppieren von Zeilen und Spalten.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Gruppenverwaltung von Zeilen und Spalten**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) enthält eine [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection), die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) stellt eine [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung bereit, die alle Zellen im Arbeitsblatt repräsentiert.

Die [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung bietet mehrere Methoden zur Verwaltung von Zeilen oder Spalten in einem Arbeitsblatt, von denen einige im Folgenden ausführlicher besprochen werden.

### **Zeilen und Spalten gruppieren**

Es ist möglich, Zeilen oder Spalten zu gruppieren, indem die Methoden [**groupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#groupRows-number-number-boolean-) und [**groupColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#groupColumns-number-number-) der [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung aufgerufen werden. Beide Methoden nehmen die folgenden Parameter an:

- Erster Zeilen-/Spaltenindex, die erste Zeile oder Spalte in der Gruppe.
- Letzter Zeilen-/Spaltenindex, die letzte Zeile oder Spalte in der Gruppe.
- Ist versteckt, ein boolescher Parameter, der angibt, ob Zeilen/Spalten nach dem Gruppieren ausgeblendet werden sollen oder nicht.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileContent = fs.readFileSync(filePath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileContent);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows (from 0 to 5) and making them hidden by passing true
worksheet.getCells().groupRows(0, 5, true);

// Grouping first three columns (from 0 to 2) and making them hidden by passing true
worksheet.getCells().groupColumns(0, 2, true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Gruppeneinstellungen**

Microsoft Excel ermöglicht es Ihnen, Gruppeneinstellungen für die Anzeige zu konfigurieren:

- Zusammenfassungszeilen unterhalb von Details.
- Zusammenfassungsspalten rechts neben dem Detail.

Entwickler können diese Gruppierungseinstellungen mit der Eigenschaft [**getOutline()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getOutline--) der [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse konfigurieren.

### **Zusammenfassungszeilen unterhalb der Details**

Es ist möglich, festzulegen, ob Zusammenfassungszeilen unter der Detailansicht angezeigt werden sollen, indem die Eigenschaft [**getSummaryRowBelow()**](https://reference.aspose.com/cells/nodejs-cpp/outline/#getSummaryRowBelow--) der [**Outline**](https://reference.aspose.com/cells/nodejs-cpp/outline)-Klasse auf **true** oder **false** gesetzt wird.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows and first three columns
worksheet.getCells().groupRows(0, 5, true);
worksheet.getCells().groupColumns(0, 2, true);

// Setting SummaryRowBelow property to false
worksheet.getOutline().setSummaryRowBelow(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **Zusammenfassungsspalten rechts von den Details**

Entwickler können auch die Anzeige von Zusammenfassungs-Spalten rechts von den Details steuern, indem sie die Eigenschaft [**getSummaryColumnRight()**](https://reference.aspose.com/cells/nodejs-cpp/outline/#getSummaryColumnRight--) der [**Outline**](https://reference.aspose.com/cells/nodejs-cpp/outline)-Klasse auf **true** oder **false** setzen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows and first three columns
worksheet.getCells().groupRows(0, 5, true);
worksheet.getCells().groupColumns(0, 2, true);

worksheet.getOutline().setSummaryColumnRight(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Zeilen und Spalten entgruppieren**

Um gruppierte Zeilen oder Spalten aufzuheben, rufen Sie die Methoden [**ungroupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupRows-number-number-boolean-) und [**ungroupColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupColumns-number-number-) der [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung auf. Beide Methoden nehmen zwei Parameter an:

- Erster Zeilen- oder Spaltenindex, die erste Zeile/Spalte, die aufgehoben werden soll.
- Letzter Zeilen- oder Spaltenindex, die letzte Zeile/Spalte, die aufgehoben werden soll.

[**ungroupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupRows-number-number-boolean-) hat eine Überladung, die einen dritten Parameter vom Typ Boolean akzeptiert. Wird dieser auf **true** gesetzt, werden alle gruppierten Informationen entfernt. Andernfalls werden nur die äußeren Gruppierungsinformationen gelöscht.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading Excel file into buffer
const buffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with file content
const workbook = new AsposeCells.Workbook(buffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Ungrouping first six rows (from 0 to 5)
worksheet.getCells().ungroupRows(0, 5);

// Ungrouping first three columns (from 0 to 2)
worksheet.getCells().ungroupColumns(0, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
