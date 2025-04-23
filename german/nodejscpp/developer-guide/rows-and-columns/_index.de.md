---  
title: Formatieren von Zeilen und Spalten mit Node.js über C++  
linktitle: Zeilen und Spalten  
type: docs  
weight: 100  
url: /de/nodejs-cpp/adjusting-row-height-and-column-width/  
description: Aspose.Cells for Node.js via C++ kann die Zeilenhöhe oder Spaltenbreite unterstützen sowie die Formatierung von Zeilen oder Spalten anwenden.  
keywords: Zeilenhöhe und Spaltenbreite einstellen, Zeilenhöhe und Spaltenbreite anpassen, die Zeilenhöhe oder Spaltenbreite ändern, Zeilen und Spalten formatieren, wie man die Zeilenhöhe und Spaltenbreite einstellt  
---  

{{% alert color="primary" %}}  
Beim Arbeiten mit Tabellenkalkulationen und beim Hinzufügen von Daten zu Zeilen oder Spalten müssen Sie gelegentlich die Höhe der Zeilen oder die Breite der Spalten ändern. Manchmal erfordert die Formatierung auf Zeilen oder Spalten, dass die aktuelle Höhe oder Breite angepasst wird, um die Daten anzuzeigen. Normalerweise passen Benutzer Zeilenhöhen und Spaltenbreiten in einer WYSIWYG-Umgebung mit Microsoft Excel an. Mit Aspose.Cells können Entwickler diese Operationen jedoch zur Laufzeit ausführen.  
{{% /alert %}}  

## **Arbeiten mit Zeilen**  

### **Wie man die Zeilenhöhe anpasst**  

Aspose.Cells stellt eine Klasse, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), bereit, die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) enthält eine [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection), die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) bietet eine [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung, die alle Zellen im Arbeitsblatt repräsentiert.  

Die Sammlung [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) bietet mehrere Methoden zur Verwaltung von Zeilen oder Spalten in einem Arbeitsblatt. Einige davon werden im Folgenden ausführlicher erläutert.  

### **Wie man die Höhe einer Zeile festlegt**  

Es ist möglich, die Höhe einer einzelnen Zeile festzulegen, indem die [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlungsmethode [**setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-) aufgerufen wird. Die [**setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-)-Methode übernimmt folgende Parameter:

- **Zeilenindex**, der Index der Zeile, deren Höhe geändert wird.  
- **Zeilenhöhe**, die auf die Zeile anzuwendende Zeilenhöhe.

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Creating a file stream containing the Excel file to be opened
const fstream = fs.createReadStream(filePath);

// Reading the file stream into a buffer
const chunks = [];
fstream.on('data', chunk => chunks.push(chunk));
fstream.on('end', () => {
const buffer = Buffer.concat(chunks);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(buffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the height of the second row to 13
worksheet.getCells().setRowHeight(1, 13);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream.close();
```  

### **Wie man die Höhe aller Zeilen in einem Arbeitsblatt festlegt**  

Wenn Entwickler die gleiche Zeilenhöhe für alle Zeilen im Arbeitsblatt festlegen müssen, können sie dies durch Verwendung der [**getStandardHeight()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getStandardHeight--)-Eigenschaft der [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlung tun.  

**Beispiel:**  

```javascript
const fs = require("fs");
const path = require("path");
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

// Setting the height of all rows in the worksheet to 15
worksheet.getCells().setStandardHeight(15);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
// (Note: Closing the file stream is unnecessary in this context as it's a 
// synchronous read performed using fs.readFileSync, which does not require
// explicit closure, but if using fs.createReadStream, you would handle it accordingly)
```  

## **Arbeiten mit Spalten**  

### **Wie man die Breite einer Spalte festlegt**  

Setzen Sie die Breite einer Spalte, indem Sie die [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlungsmethode [**setColumnWidth(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidth-number-number-) aufrufen. Die [**setColumnWidth(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidth-number-number-)-Methode erfordert folgende Parameter:  

- **Spaltenindex**, der Index der Spalte, deren Breite geändert wird.  
- **Spaltenbreite**, die gewünschte Spaltenbreite.  

```javascript
const fs = require("fs");
const path = require("path");
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

// Setting the width of the second column to 17.5
worksheet.getCells().setColumnWidth(1, 17.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream; // Note: No explicit close needed for fs.readFileSync
```  

### **Wie man die Spaltenbreite in Pixeln festlegt**  

Setzen Sie die Breite einer Spalte, indem Sie die [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlungsmethode [**setColumnWidthPixel(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidthPixel-number-number-) aufrufen. Die [**setColumnWidthPixel(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidthPixel-number-number-)-Methode erfordert folgende Parameter:  

- **Spaltenindex**, der Index der Spalte, deren Breite geändert wird.  
- **Spaltenbreite**, die gewünschte Spaltenbreite in Pixel.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const outDir = path.join(__dirname, "output");

// Load source Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set the width of the column in pixels
worksheet.getCells().setColumnWidthPixel(7, 200);

workbook.save(path.join(outDir, "SetColumnWidthInPixels_Out.xlsx"));
```  

### **Wie man die Breite aller Spalten in einem Arbeitsblatt festlegt**  

Um die gleiche Spaltenbreite für alle Spalten im Arbeitsblatt festzulegen, verwenden Sie die [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-Sammlungseigenschaft [**getStandardWidth()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getStandardWidth--).  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
// Opening the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the width of all columns in the worksheet to 20.5
worksheet.getCells().setStandardWidth(20.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
// No explicit close needed in Node.js
```  

## **Erweiterte Themen**  
- [Automatische Anpassung von Zeilen und Spalten](/cells/de/nodejs-cpp/autofit-rows-and-columns/)  
- [Text in Spalten konvertieren mit Aspose.Cells](/cells/de/nodejs-cpp/convert-text-to-columns-using-aspose-cells/)  
- [Kopieren von Zeilen und Spalten](/cells/de/nodejs-cpp/copying-rows-and-columns/)  
- [Leere Zeilen und Spalten in einem Arbeitsblatt löschen](/cells/de/nodejs-cpp/delete-blank-rows-and-columns-in-a-worksheet/)  
- [Gruppieren und Aufheben der Gruppierung von Zeilen und Spalten](/cells/de/nodejs-cpp/grouping-and-ungrouping-rows-and-columns/)  
- [Zeilen und Spalten ausblenden und anzeigen](/cells/de/nodejs-cpp/hiding-and-showing-rows-and-columns/)  
- [Zeilen in einem Excel-Arbeitsblatt einfügen oder löschen](/cells/de/nodejs-cpp/insert-or-delete-rows-in-an-excel-worksheet/)  
- [Einfügen und Löschen von Zeilen und Spalten einer Excel-Datei](/cells/de/nodejs-cpp/inserting-and-deleting-rows-and-columns/)  
- [Duplikate Zeilen in einem Arbeitsblatt entfernen](/cells/de/nodejs-cpp/remove-duplicate-rows-in-a-worksheet/)  
- [Aktualisieren Sie Verweise in anderen Arbeitsblättern, während Sie leere Spalten und Zeilen in einem Arbeitsblatt löschen](/cells/de/nodejs-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)  

