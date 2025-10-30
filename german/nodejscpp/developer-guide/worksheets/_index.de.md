---  
title: Verwalten von Arbeitsblättern von Microsoft Excel Dateien mit Node.js über C++  
linktitle: Arbeitsblätter  
type: docs  
weight: 90  
url: /de/nodejs-cpp/manage-worksheets/  
description: Hinzufügen, Entfernen und Aktivieren von Arbeitsblättern mit Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Entwickler können Arbeitsblätter in Microsoft Excel-Dateien mithilfe der flexiblen API von Aspose.Cells einfach programmgesteuert erstellen und verwalten. Dieses Thema beschreibt Ansätze zum Hinzufügen und Entfernen von Arbeitsblättern in Microsoft Excel-Dateien.  
{{% /alert %}}  

Aspose.Cells stellt eine Klasse bereit, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), die eine Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Klasse enthält eine [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.  

Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse repräsentiert. Die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung von Arbeitsblättern.  

## **Arbeitsblätter zu einer neuen Excel-Datei hinzufügen**  

Um programmgesteuert eine neue Excel-Datei zu erstellen:  

1. Erstellen Sie ein Objekt der [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Klasse.  
1. Rufen Sie die [**WorksheetCollection.add(SheetType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#add-sheettype-)-Methode der [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)-Klasse auf. Ein leeres Arbeitsblatt wird automatisch zur Excel-Datei hinzugefügt. Es kann referenziert werden, indem der Blattindex des neuen Arbeitsblatts an die [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-Sammlung übergeben wird.  
1. Holen Sie sich eine Arbeitsblatt-Referenz.  
1. Arbeiten Sie an den Arbeitsblättern.  
1. Speichern Sie die neue Excel-Datei mit den neuen Arbeitsblättern, indem Sie die [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)-Methode der [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Klasse aufrufen.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const i = workbook.getWorksheets().getCount();
workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Setting the name of the newly added worksheet
worksheet.setName("My Worksheet");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Arbeitsblätter zu einem Designer-Arbeitsblatt hinzufügen**  

Der Vorgang zum Hinzufügen von Arbeitsblättern zu einer Designer-Tabelle ist derselbe wie bei einem neuen Arbeitsblatt, außer dass die Excel-Datei bereits existiert und vor dem Hinzufügen von Arbeitsblättern geöffnet werden muss. Eine Designer-Tabelle kann durch die [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Klasse geöffnet werden.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(inputPath);

// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Adding a new worksheet to the Workbook object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Setting the name of the newly added worksheet
worksheet.setName("My Worksheet");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

## **Zugriff auf Arbeitsblätter mithilfe des Blattnamens**  

Greifen Sie auf jedes Arbeitsblatt zu, indem Sie dessen Namen oder Index angeben.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(inputPath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing a worksheet using its sheet name
const worksheet = workbook.getWorksheets().get("Sheet1");
const cell = worksheet.getCells().get("A1");
console.log(cell.getValue());
```  

## **Arbeitsblätter anhand des Blattnamens entfernen**  

Um Arbeitsblätter aus einer Datei zu entfernen, rufen Sie die [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-)-Methode der [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)-Klasse auf. Übergeben Sie den Blattnamen an die [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-)-Methode, um ein bestimmtes Arbeitsblatt zu entfernen.  

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

// Removing a worksheet using its sheet name
workbook.getWorksheets().removeAt("Sheet1");

// Save workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Arbeitsblätter anhand des Blattindex entfernen**  

Das Entfernen von Arbeitsblättern nach Namen funktioniert gut, wenn der Name des Arbeitsblatts bekannt ist. Wenn Sie den Namen des Arbeitsblatts nicht kennen, verwenden Sie eine überladene Version der [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-)-Methode, die den Blattindex anstelle des Blattnamens nimmt.  

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

// Removing a worksheet using its sheet index
workbook.getWorksheets().removeAt(0);

// Save workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Aktivierung von Tabellen und Markierung einer aktiven Zelle im Arbeitsblatt**  

Manchmal benötigen Sie ein bestimmtes Arbeitsblatt, das beim Öffnen einer Microsoft Excel-Datei aktiv und sichtbar ist. Ebenso möchten Sie vielleicht eine bestimmte Zelle aktivieren und die Bildlaufleisten so einstellen, dass die aktive Zelle angezeigt wird. Aspose.Cells ist in der Lage, all diese Aufgaben auszuführen.  

Ein **aktives Tabellenblatt** ist ein Blatt, an dem Sie arbeiten: Der Name des aktiven Blattes auf der Registerkarte ist standardmäßig fett gedruckt.  

Eine **aktive Zelle** ist eine ausgewählte Zelle, in die Daten eingegeben werden, wenn Sie mit der Eingabe beginnen. Es ist jeweils nur eine Zelle aktiv. Die aktive Zelle ist durch einen starken Rahmen hervorgehoben.  

### **Aktivierung von Tabellen und Markierung einer Zelle als aktiv**  

Aspose.Cells bietet spezielle API-Aufrufe zum Aktivieren eines Blatts und einer Zelle. Zum Beispiel ist die [**WorksheetCollection.getActiveSheetIndex()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getActiveSheetIndex--)-Eigenschaft nützlich, um das aktive Blatt in einer Arbeitsmappe festzulegen. Ebenso wird die [**Worksheet.getActiveCell()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getActiveCell--)-Eigenschaft verwendet, um eine aktive Zelle im Arbeitsblatt zu setzen und zu erhalten.  

Um sicherzustellen, dass die horizontalen oder vertikalen Bildlaufleisten bei den gewünschten Zeilen- und Spaltenindizes positioniert sind, verwenden Sie die Eigenschaften [**Worksheet.getFirstVisibleRow()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFirstVisibleRow--) und [**Worksheet.getFirstVisibleColumn()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFirstVisibleColumn--).  

Das folgende Beispiel zeigt, wie ein Arbeitsblatt aktiviert und eine aktive Zelle darin markiert wird. In der generierten Ausgabe werden die Bildlaufleisten gescrollt, um die 2. Zeile und 2. Spalte als erste sichtbare Zeile und Spalte zu zeigen.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Add a worksheet if collection is empty
const worksheets = workbook.getWorksheets();
if (worksheets.getCount() === 0) {
worksheets.add();
}

// Get the first worksheet in the workbook.
const worksheet1 = worksheets.get(0);

// Get the cells in the worksheet.
const cells = worksheet1.getCells();

// Input data into B2 cell.
cells.get(1, 1).putValue("Hello World!");

// Set the first sheet as an active sheet.
workbook.getWorksheets().setActiveSheetIndex(0);

// Set B2 cell as an active cell in the worksheet.
worksheet1.setActiveCell("B2");

// Set the B column as the first visible column in the worksheet.
worksheet1.setFirstVisibleColumn(1);

// Set the 2nd row as the first visible row in the worksheet.
worksheet1.setFirstVisibleRow(1);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```  

## **Erweiterte Themen**  
- [Arbeitsblätter kopieren und verschieben](/cells/de/nodejs-cpp/copying-and-moving-worksheets/)  
- [Anzahl der Zellen im Arbeitsblatt zählen](/cells/de/nodejs-cpp/count-number-of-cells-in-the-worksheet/)  
- [Erkennen von leeren Arbeitsblättern](/cells/de/nodejs-cpp/detecting-empty-worksheets/)  
- [Feststellen, ob das Arbeitsblatt ein Dialogblatt ist](/cells/de/nodejs-cpp/find-if-the-worksheet-is-dialog-sheet/)  
- [Arbeitsblatt eindeutige ID abrufen](/cells/de/nodejs-cpp/get-worksheet-unique-id/)  
- [Erstellen, Manipulieren oder Entfernen von Szenarien aus Arbeitsblättern](/cells/de/nodejs-cpp/create-manipulate-or-remove-scenarios-from-worksheets/)  
- [Seitenumbrüche verwalten](/cells/de/nodejs-cpp/managing-page-breaks/)  
- [Seiteneinrichtungsfunktionen](/cells/de/nodejs-cpp/page-setup-features/)   
- [Verwenden Sie die *Sheet.SheetId*-Eigenschaft von OpenXml mit Aspose.Cells](/cells/de/nodejs-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)  
- [Arbeitsblattansichten](/cells/de/nodejs-cpp/worksheet-views/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
