---  
title: Zeilen in einem Excel Arbeitsblatt mit Node.js über C++ einfügen oder löschen  
linktitle: Ein oder Löschen von Zeilen in einem Excel Arbeitsblatt  
type: docs  
weight: 20  
url: /de/nodejs-cpp/insert-or-delete-rows-in-an-excel-worksheet/  
description: Dieser Artikel bietet Node.js Code, der C++ verwendet, um Zeilen in einem Excel Arbeitsblatt einzufügen und zu löschen.  
keywords: node.js Zeilen in Excel Arbeitsblatt einfügen oder löschen, node.js Zeilen in Excel einfügen oder löschen, node.js Zeilen in Excel einfügen, node.js Zeilen in Excel löschen, Zeilen in Excel Arbeitsblatt mit node.js einfügen oder löschen, Zeilen in Excel mit node.js einfügen oder löschen, Zeilen in Excel mit node.js einfügen, Zeilen in Excel mit node.js löschen  
---  

{{% alert color="primary" %}}  

Beim Erstellen eines neuen Arbeitsblatts oder bei der Arbeit mit einem bestehenden Arbeitsblatt könnte es notwendig sein, zusätzliche Zeilen oder Spalten hinzuzufügen, um Daten aufzunehmen. Manchmal ist es auch notwendig, Zeilen oder Spalten an bestimmten Stellen im Arbeitsblatt zu löschen.  

{{% /alert %}}  

Aspose.Cells for Node.js via C++ bietet zwei Methoden zum Einfügen und Löschen von Zeilen: [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) und [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-). Diese Methoden sind für optimale Leistung ausgelegt und erledigen die Aufgabe sehr schnell.  

Um eine Anzahl von Zeilen einzufügen oder zu entfernen, empfehlen wir, immer die Methoden [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) und [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) anstelle der Methoden [**Cells.insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) oder [**Cells.deleteRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRow-number-) in einer Schleife zu verwenden.  

Aspose.Cells arbeitet genauso wie Microsoft Excel. Wenn Zeilen oder Spalten hinzugefügt werden, wird der Inhalt des Arbeitsblatts nach unten und nach rechts verschoben. Wenn Zeilen oder Spalten entfernt werden, wird der Inhalt des Arbeitsblatts nach oben oder nach links verschoben. Referenzen in anderen Arbeitsblättern und Zellen werden aktualisiert, wenn Zeilen hinzugefügt oder entfernt werden.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object.
// Load a template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xlsx"));

// Get the first worksheet in the book.
const sheet = workbook.getWorksheets().get(0);

// Insert 10 rows at row index 2 (insertion starts at 3rd row)
sheet.getCells().insertRows(2, 10);

// Delete 5 rows now. (8th row - 12th row)
sheet.getCells().deleteRows(7, 5);

// Save the excel file.
workbook.save(path.join(dataDir, "out_book1.out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
