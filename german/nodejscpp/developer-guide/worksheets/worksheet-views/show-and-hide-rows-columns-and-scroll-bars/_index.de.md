---  
title: Zeilen, Spalten und Scrollleisten mit Node.js über C++ anzeigen und ausblenden  
linktitle: Zeilen, Spalten und Bildlaufleisten anzeigen und ausblenden  
type: docs  
weight: 20  
url: /de/nodejs-cpp/show-and-hide-rows-columns-and-scroll-bars/  
description: Dieser Artikel zeigt, wie man programmgesteuert Excel Arbeitsblattzeilen und spalten mit Node.js über C++ anzeigt und ausblendet. Steuern Sie die Sichtbarkeit von Scrollleisten und blenden Sie mehrere Zeilen und Spalten effizient aus.  
---  

{{% alert color="primary" %}}  
Aspose.Cells bietet Möglichkeiten, die Sichtbarkeit von Zeilen, Spalten und Bildlaufleisten eines Arbeitsblatts zu steuern.  
{{% /alert %}}  

## **Zeilen und Spalten anzeigen und ausblenden**  

Aspose.Cells stellt eine Klasse, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), bereit, die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) Klasse enthält eine [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) Sammlung, die Entwicklern ermöglicht, auf jedes Arbeitsblatt in der Excel-Datei zuzugreifen. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) Klasse repräsentiert. Die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) Klasse bietet eine [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) Sammlung, die alle Zellen im Arbeitsblatt darstellt. Die [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) Sammlung bietet mehrere Methoden zur Verwaltung von Zeilen oder Spalten in einem Arbeitsblatt. Einige dieser Methoden werden nachstehend erläutert.  

### **Zeilen und Spalten anzeigen**  

Entwickler können jede ausgeblendete Zeile oder Spalte anzeigen, indem sie die Methoden [**unhideRow(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRow-number-number-) und [**unhideColumn(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumn-number-number-) der [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) Sammlung jeweils aufrufen. Beide Methoden nehmen zwei Parameter:  

- **Zeilen- oder Spaltenindex** - der Index einer Zeile oder Spalte, der verwendet wird, um die spezifische Zeile oder Spalte anzuzeigen.  
- **Zeilenhöhe oder Spaltenbreite** - die Zeilenhöhe oder Spaltenbreite, die der Zeile oder Spalte nach dem Ausblenden zugewiesen wird.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
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
Beim Wiederherstellen einer ausgeblendeten Spalte, falls Sie sie auf die zuvor zugewiesene Breite oder auf die ursprüngliche Breite zurücksetzen möchten, heben Sie die Ausblendung der Spalte mit einer negativen Breite auf. Zum Beispiel: worksheet.Cells.unhideColumn(5, -1)  
{{% /alert %}}  

### **Zeilen und Spalten ausblenden**  

Entwickler können eine Zeile oder Spalte ausblenden, indem sie die Methoden [**hideRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRow-number-) und [**hideColumn(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumn-number-) der [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) Sammlung aufrufen. Beide Methoden nehmen den Zeilen- und Spaltenindex als Parameter, um die spezifische Zeile oder Spalte auszublenden.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

const fileBuffer = fs.readFileSync(filePath);

const workbook = new AsposeCells.Workbook(fileBuffer);

const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().hideRow(2);

worksheet.getCells().hideColumn(1);

workbook.save(path.join(dataDir, "output.out.xls"));
```  

{{% alert color="primary" %}}  
Es ist auch möglich, eine Zeile oder Spalte auszublenden, indem die Zeilenhöhe oder Spaltenbreite auf 0 gesetzt wird.  
{{% /alert %}}  

### **Mehrere Zeilen und Spalten ausblenden**  

Entwickler können mehrere Zeilen oder Spalten gleichzeitig ausblenden, indem sie die Methoden [**hideRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRows-number-number-) und [**hideColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumns-number-number-) der [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) Sammlung aufrufen. Beide Methoden nehmen den Startindex der Zeile oder Spalte und die Anzahl der Zeilen oder Spalten, die ausgeblendet werden sollen, als Parameter.  

```javascript
const fs = require('fs');
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

// Hiding 3, 4 and 5 rows in the worksheet
worksheet.getCells().hideRows(2, 3);

// Hiding 2 and 3 columns in the worksheet
worksheet.getCells().hideColumns(1, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "outputxls"));

// No explicit close needed for file stream as we're working with in-memory data
```  

## **Bildlaufleisten einblenden und ausblenden**  

Bildlaufleisten werden verwendet, um den Inhalt einer Datei zu durchsuchen. Normalerweise gibt es zwei Arten von Bildlaufleisten:  

- Vertikale Scrollleisten  
- Horizontale Scrollleisten  

Microsoft Excel bietet auch horizontale und vertikale Scrollleisten an, damit Benutzer durch die Inhalte des Arbeitsblatts scrollen können. Mit Aspose.Cells können Entwickler die Sichtbarkeit beider Arten von Scrollleisten in Excel-Dateien steuern.  

### **Steuerung der Sichtbarkeit von Bildlaufleisten**  

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), die eine Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung einer Excel-Datei. Um die Sichtbarkeit von Scrollleisten zu steuern, verwenden Sie die Eigenschaften [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) und [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--). [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) und [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--) sind Boolesche Eigenschaften, was bedeutet, dass diese Eigenschaften nur **true** oder **false** speichern können.  

#### **Sichtbarkeit von Bildlaufleisten herstellen**  

Setzen Sie die [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) Klasse, [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) oder [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--) Eigenschaft auf **true**, um die Bildlaufleisten sichtbar zu machen.  

#### **Verbergen von Bildlaufleisten**  

Setzen Sie die [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) Klasse, [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) oder [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--) Eigenschaft auf **false**, um die Bildlaufleisten auszublenden.  

**Beispielcode**  

Im Folgenden finden Sie einen vollständigen Code, der eine Excel-Datei, book1.xls, öffnet, beide Bildlaufleisten ausblendet und dann die modifizierte Datei als output.xls speichert.  

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

// Hiding the vertical scroll bar of the Excel file
workbook.getSettings().setIsVScrollBarVisible(false);

// Hiding the horizontal scroll bar of the Excel file
workbook.getSettings().setIsHScrollBarVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

