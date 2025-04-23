---  
title: Zeilen und Spalten mit Node.js via C++ kopieren  
linktitle: Kopieren von Zeilen und Spalten  
type: docs  
weight: 40  
url: /de/nodejs-cpp/copying-rows-and-columns/  
description: Dieser Artikel zeigt, wie man Zeilen und Spalten durch die Aspose.Cells for Node.js via C++ API kopiert.  
keywords: Node.js via C++, Wie man Zeilen und Spalten kopiert, Zeilen in Node.js kopieren, Spalten mit Node.js kopieren, Wie man Zeilen und Spalten mit Aspose.Cells for Node.js via C++ einfügt, Mehrere Zeilen und Spalten einfügen, Einzeilige Zeile oder Spalte kopieren und einfügen.  
---  

## **Einführung**  

Manchmal müssen Sie Zeilen und Spalten in einem Arbeitsblatt kopieren, ohne das gesamte Arbeitsblatt zu kopieren. Mit Aspose.Cells ist es möglich, Zeilen und Spalten innerhalb oder zwischen Arbeitsmappen zu kopieren.  
Wenn eine Zeile (oder Spalte) kopiert wird, werden auch die darin enthaltenen Daten, einschließlich Formeln - mit aktualisierten Verweisen - und Werten, Kommentare, Formatierungen, versteckte Zellen, Bilder und andere Zeichenobjekte ebenfalls kopiert.  

## **Wie man Zeilen und Spalten mit Microsoft Excel kopiert**  

1. Wählen Sie die zu kopierende Zeile oder Spalte aus.  
1. Zum Kopieren von Zeilen oder Spalten klicken Sie auf **Kopieren** in der **Standard**-Symbolleiste oder drücken Sie **STRG**+**C**.  
1. Wählen Sie eine Zeile oder Spalte unterhalb oder rechts von der Position aus, an der Sie Ihre Auswahl kopieren möchten.  
1. Beim Kopieren von Zeilen oder Spalten klicken Sie auf **Kopierte Zellen** im **Einfügen**-Menü.  

{{% alert color="primary" %}}  
Wenn Sie auf **Einfügen** in der **Standard**-Symbolleiste klicken oder **STRG**+**V** drücken, anstatt ein Befehl im **Einfügen**-Menü zu klicken, werden die Inhalte der Zielzellen ersetzt.  
{{% /alert %}}  

## **Wie man Zeilen und Spalten mit Paste-Optionen mit Microsoft Excel einfügt**  

1. Wählen Sie die Zellen aus, die die Daten oder andere Attribute enthalten, die Sie kopieren möchten.  
1. Klicken Sie auf der Registerkarte Start auf **Kopieren**.  
1. Klicken Sie auf die erste Zelle im Bereich, in dem Sie das, was Sie kopiert haben, **einfügen** möchten.  
1. Klicken Sie auf der Registerkarte Start auf den Pfeil neben **Einfügen**, und wählen Sie dann **Inhalt einfügen** aus.  
1. Wählen Sie die **Optionen**, die Sie möchten.  

## **So kopieren Sie Zeilen und Spalten mit Aspose.Cells for Node.js via C++**  

## **Wie man einzelne Zeilen kopiert**  

Aspose.Cells bietet die [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) Methode der [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) Klasse an. Diese Methode kopiert alle Datentypen einschließlich Formeln, Werte, Kommentare, Zellformate, versteckte Zellen, Bilder und andere Zeichenobjekte vom Quell- in den Zielbereich.  

Die [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) Methode akzeptiert folgende Parameter:  

- das Quell-[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) Objekt,  
- den Index der Quellzeile, und  
- den Index der Zielzeile.  

Verwenden Sie diese Methode, um eine Zeile innerhalb eines Blatts oder zu einem anderen Blatt zu kopieren. Die [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) Methode funktioniert ähnlich wie Microsoft Excel. Sie müssen beispielsweise die Höhe der Zielzeile nicht explizit einstellen, dieser Wert wird ebenfalls kopiert.  

Das folgende Beispiel zeigt, wie eine Zeile in einem Arbeitsblatt kopiert wird. Es verwendet eine Vorlage im Microsoft Excel Format und kopiert die zweite Zeile (einschließlich Daten, Formatierung, Kommentare, Bilder usw.) und fügt sie in die 12. Zeile desselben Arbeitsblatts ein.  

Sie können den Schritt überspringen, bei dem die Höhe der Quellzeile mit der [**Cells.getRowHeight(number, boolean, CellsUnitType)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRowHeight-number-boolean-cellsunittype-) Methode abgerufen wird, und dann die Höhe der Zielzeile mit der [**Cells.setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-) Methode einstellen, da die [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) Methode automatisch die Zeilenhöhe übernimmt.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing excel file.
const excelWorkbook1 = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Get the first worksheet in the workbook.
const wsTemplate = excelWorkbook1.getWorksheets().get(0);

// Copy the second row with data, formattings, images and drawing objects
// To the 16th row in the worksheet.
wsTemplate.getCells().copyRow(wsTemplate.getCells(), 1, 15);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  
Beim Kopieren von Zeilen ist es wichtig, darauf hinzuweisen, dass damit verbundene Bilder, Diagramme oder andere Zeichenobjekte genauso wie bei Microsoft Excel behandelt werden:  

1. Wenn der Quellzeilenindex 5 beträgt, wird das Bild, Diagramm usw. kopiert, wenn es in den drei Zeilen enthalten ist (der Startzeilenindex ist 4 und der Endzeilenindex ist 6).  
1. Die vorhandenen Bilder, Diagramme usw. in der Zielzeile werden nicht entfernt.  
{{% /alert %}}  

## **Wie man Mehrere Zeilen kopiert**  

Sie können auch mehrere Zeilen auf ein neues Ziel kopieren, während Sie die [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-) Methode verwenden, die einen zusätzlichen Parameter vom Typ Integer akzeptiert, um die Anzahl der zu kopierenden Quellzeilen anzugeben.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "aspose-sample.xlsx");

// Create an instance of Workbook class by loading the existing spreadsheet
const workbook = new AsposeCells.Workbook(filePath);

// Get the cells collection of first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Copy the first 3 rows to 7th row
cells.copyRows(cells, 0, 6, 3);

// Save the result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

## **Wie man Spalten kopiert**  

Aspose.Cells bietet die [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) Methode der [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) Klasse an, diese Methode kopiert alle Datentypen einschließlich Formeln—mit aktualisierten Verweisen—Werte, Kommentare, Zellformate, versteckte Zellen, Bilder und andere Zeichenobjekte vom Quell- in den Zielbereich.  

Die [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) Methode akzeptiert folgende Parameter:  

- das Quell-[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) Objekt,  
- Quellspaltenindex, und  
- der Zielspaltenindex.  

Verwenden Sie die [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) Methode, um eine Spalte innerhalb eines Blatts oder zu einem anderen Blatt zu kopieren.  

Dieses Beispiel kopiert eine Spalte aus einem Arbeitsblatt und fügt sie in ein Arbeitsblatt in einer anderen Arbeitsmappe ein.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook(filePath);

// Get the first worksheet in the book.
const ws1 = excelWorkbook1.getWorksheets().get(0);

// Copy the first column from the first worksheet of the first workbook into
// The first worksheet of the second workbook.
ws1.getCells().copyColumn(ws1.getCells(), ws1.getCells().getColumns().get(0).getIndex(), ws1.getCells().getColumns().get(2).getIndex());

// Autofit the column.
ws1.autoFitColumn(2);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "output.xls"));
```  

## **Wie man mehrere Spalten kopiert**  

Ähnlich wie die [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-) Methode bieten die APIs von Aspose.Cells auch die [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-) Methode an, um mehrere Quellspalten an eine neue Position zu kopieren.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an instance of Workbook class by loading the existing spreadsheet
const workbook = new AsposeCells.Workbook(path.join(dataDir, "aspose-sample.xlsx"));

// Get the first worksheet's cells collection
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

// Copy the first 3 columns to the 7th column
cells.copyColumns(cells, 0, 6, 3);

// Save the result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

## **Wie man Zeilen und Spalten mit Einfügeoptionen einfügt**  

Aspose.Cells bietet jetzt [**PasteOptions**](https://reference.aspose.com/cells/nodejs-cpp/pasteoptions/) bei Verwendung der Funktionen [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-) und [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-). Es ermöglicht, ähnlich wie in Excel, die geeignete Einfügeoption festzulegen.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleChangeChartDataSource.xlsx"));

// Access the first sheet which contains chart
const source = workbook.getWorksheets().get(0);

// Add another sheet named DestSheet
const destination = workbook.getWorksheets().add("DestSheet");

// Set CopyOptions.ReferToDestinationSheet to true
const options = new AsposeCells.CopyOptions();
options.setReferToDestinationSheet(true);

// Set PasteOptions
const pasteOptions = new AsposeCells.PasteOptions();
pasteOptions.setPasteType(AsposeCells.PasteType.Values);
pasteOptions.setOnlyVisibleCells(true);

// Copy all the rows of source worksheet to destination worksheet which includes chart as well
// The chart data source will now refer to DestSheet
destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options, pasteOptions);

// Save workbook in xlsx format
workbook.save(path.join(outputDir, "outputChangeChartDataSource.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  


