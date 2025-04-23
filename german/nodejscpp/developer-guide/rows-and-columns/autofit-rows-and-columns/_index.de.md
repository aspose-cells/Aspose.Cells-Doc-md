---  
title: Zeilen und Spalten mit Node.js über C++ automatisch anpassen  
linktitle: Zeilen und Spalten automatisch anpassen  
type: docs  
weight: 20  
url: /de/nodejs-cpp/autofit-rows-and-columns/  
description: Dieser Artikel zeigt, wie man Zeilen, Spalten, Zeilen von zusammengeführten Zellen und Zeilen in einem Bereich von Zellen mit Aspose.Cells for Node.js via C++ automatisch anpasst.  
keywords: Automatisches Anpassen von Zeilen mit Node.js über C++, automatisches Anpassen von Spalten mit Node.js über C++, automatisches Anpassen von Zeile in einem Zellbereich mit Node.js über C++, automatisches Anpassen von Zeilen zusammengeführter Zellen mit Node.js über C++  
---  

{{% alert color="primary" %}}  
Microsoft Excel erlaubt es, die Breite und Höhe der Zellen entsprechend ihres Inhalts automatisch anzupassen. Dieses Feature ist auch über Aspose.Cells for Node.js via C++ verfügbar, sodass Entwickler die Abmessungen einer Zelle zur Laufzeit automatisch anpassen können.  
{{% /alert %}}  

## **Automatische Anpassung**  

Aspose.Cells stellt eine Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) bereit, die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) enthält eine Sammlung [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), die Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung eines Arbeitsblatts. Dieser Artikel beschäftigt sich mit der Verwendung der Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet), um Zeilen oder Spalten automatisch anzupassen.  

### **AutoFit Zeile - Einfach**  

Der einfachste Ansatz, um die Breite und Höhe einer Zeile automatisch anzupassen, besteht darin, die Methode [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) der [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-)-Klasse aufzurufen. Die [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-)-Methode nimmt einen Zeilenindex (der Zeile, die angepasst werden soll) als Parameter.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileBuffer = fs.readFileSync(inputPath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the 3rd row of the worksheet
worksheet.autoFitRow(1);

// Saving the modified Excel file
const outputPath = path.join(dataDir, "output.xlsx");
workbook.save(outputPath);
```  

### **Wie man eine Zeile in einem Zellenbereich automatisch anpasst**  

Eine Zeile besteht aus vielen Spalten. Aspose.Cells ermöglicht es Entwicklern, eine Zeile basierend auf den Inhalten innerhalb eines Zellbereichs in der Zeile automatisch anzupassen, indem eine überladene Version der Methode [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-number-number-) aufgerufen wird. Diese nimmt die folgenden Parameter entgegen:  

- **Zeilenindex**, der Index der zu automatisch anzupassenden Zeile.  
- **Erster Spaltenindex**, der Index der ersten Spalte der Zeile.  
- **Letzter Spaltenindex**, der Index der letzten Spalte der Zeile.  

Die [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-number-number-)-Methode überprüft den Inhalt aller Spalten in der Zeile und passt die Zeile entsprechend an.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileData = fs.readFileSync(inputPath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileData);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the 3rd row of the worksheet
worksheet.autoFitRow(1, 0, 5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

### **Wie man eine Spalte in einem Zellenbereich automatisch anpasst**  

Eine Spalte besteht aus vielen Zeilen. Es ist möglich, eine Spalte anhand des Inhalts in einem Bereich von Zellen durch Aufruf einer überladenen Version der Methode [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-) anzupassen, die die folgenden Parameter akzeptiert:  

- **Spaltenindex**, der Index der zu automatisch anzupassenden Spalte.  
- **Erster Zeilenindex**, der Index der ersten Zeile der Spalte.  
- **Letzter Zeilenindex**, der Index der letzten Zeile der Spalte.  

Die [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-)-Methode überprüft den Inhalt aller Zeilen in der Spalte und passt die Spalte entsprechend an.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const workbook = new AsposeCells.Workbook(fs.readFileSync(inputPath));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the Column of the worksheet
worksheet.autoFitColumn(4);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

### **Wie man Zeilen für zusammengeführte Zellen automatisch anpasst**  

Mit Aspose.Cells ist es möglich, Zeilen automatisch anzupassen, selbst bei Zellen, die zusammengeführt wurden, mithilfe der API [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions). Die Klasse [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) bietet die Eigenschaft [**AutoFitterOptions.getAutoFitMergedCellsType()**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getAutoFitMergedCellsType--), die verwendet werden kann, um Zeilen für zusammengeführte Zellen automatisch anzupassen. [**AutoFitterOptions.getAutoFitMergedCellsType()**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getAutoFitMergedCellsType--) akzeptiert eine [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/nodejs-cpp/autofitmergedcellstype) aufzählbare Sammlung, die die folgenden Mitglieder enthält.  

- Keine: Zusammengeführte Zellen ignorieren.  
- ErsteZeile: Erweitert nur die Höhe der ersten Zeile.  
- LetzteZeile: Erweitert nur die Höhe der letzten Zeile.  
- JedeZeile: Erweitert nur die Höhe jeder Zeile.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(dataDir, "output");

// Instantiate a new Workbook
const wb = new AsposeCells.Workbook();

// Get the first (default) worksheet
const worksheet = wb.getWorksheets().get(0);

// Create a range A1:B1
const range = worksheet.getCells().createRange(0, 0, 1, 2);

// Merge the cells
range.merge();

// Insert value to the merged cell A1
worksheet.getCells().get(0, 0).setValue("A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

// Create a style object
const style = worksheet.getCells().get(0, 0).getStyle();

// Set wrapping text on
style.setIsTextWrapped(true);

// Apply the style to the cell
worksheet.getCells().get(0, 0).setStyle(style);

// Create an object for AutoFitterOptions
const options = new AsposeCells.AutoFitterOptions();

// Set auto-fit for merged cells
options.setAutoFitMergedCellsType(AsposeCells.AutoFitMergedCellsType.EachLine);

// Autofit rows in the sheet (including the merged cells)
worksheet.autoFitRows(options);

// Save the Excel file
wb.save(path.join(outputDir, "AutofitRowsforMergedCells.xlsx"));
```  

{{% alert color="primary" %}}  
Sie können auch versuchen, die überladenen Versionen der [**autoFitRows**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRows-number-number-AutoFitterOptions-) & [**autoFitColumns**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumns-number-number-AutoFitterOptions-) Methoden zu verwenden, die eine Reihe von Zeilen/Spalten und eine Instanz von [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) akzeptieren, um die ausgewählten Zeilen/Spalten entsprechend Ihrer gewünschten [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) automatisch anzupassen.  

Die Signaturen der genannten Methoden sind wie folgt:  

1. autoFitZeilen(int startZeile, int endZeile, [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) Optionen)  
1. autoFitSpalten(int ersteSpalte, int letzteSpalte, [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) Optionen)  
{{% /alert %}}  

## **Wichtig zu wissen**  

{{% alert color="primary" %}}  
Wenn eine Zelle zusammengeführt ist, werden die autoFit-Methoden nicht angewendet, was dasselbe Verhalten wie in Microsoft Excel ist. Sie können dies umgehen, indem Sie die Autofilter-API verwenden. Außerdem wird die [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-) Methode nicht angewendet, wenn der Text in einer Zelle umbrochen ist. Ein weiterer Punkt ist, dass die *autoFit*-Methoden zeitaufwendig sind. Daher sollten Sie diese Methoden so selten wie möglich aufrufen, um die Effizienz Ihrer Anwendung zu gewährleisten.  
{{% /alert %}}  

## **Erweiterte Themen**  
- [Automatisches Anpassen von Zeilen für zusammengeführte Zellen](/cells/de/nodejs-cpp/autofit-rows-for-merged-cells/)  

