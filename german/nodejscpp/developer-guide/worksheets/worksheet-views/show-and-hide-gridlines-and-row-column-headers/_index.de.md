---  
title: Gitternetzlinien und Zeilen und Spaltenüberschriften mit Node.js über C++ anzeigen und ausblenden  
linktitle: Rastlinien und Zeilen / Spaltenüberschriften ein und ausblenden  
type: docs  
weight: 30  
url: /de/nodejs-cpp/show-and-hide-gridlines-and-row-column-headers/  
description: Dieser Artikel enthält Beispielcode für die Verwendung der Node.js API über C++, um programmgesteuert Gitternetzlinien, Zeilen und Spaltenüberschriften eines Excel Arbeitsblatts auszublenden oder anzuzeigen.  
---  

{{% alert color="primary" %}}  
Aspose.Cells unterstützt das Ausblenden und Anzeigen von Rasterlinien des Arbeitsblatts, die standardmäßig sichtbar sind. Es ermöglicht auch die Kontrolle der Sichtbarkeit von Zeilen- und Spaltenüberschriften des Arbeitsblatts.  
{{% /alert %}}  

## **Rasterlinien anzeigen und ausblenden**  

Alle Excel-Arbeitsblätter haben standardmäßig Rasterlinien. Sie helfen dabei, Zellen abzugrenzen, sodass es einfach ist, Daten in bestimmte Zellen einzugeben. Rasterlinien ermöglichen es uns, ein Arbeitsblatt als eine Sammlung von Zellen zu betrachten, bei der jede Zelle leicht identifizierbar ist.  

### **Steuerung der Sichtbarkeit der Rastlinien**  

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), die eine Microsoft Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) enthält eine [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-Sammlung, die es Entwicklern ermöglicht, auf jedes Arbeitsblatt in der Excel-Datei zuzugreifen. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung eines Arbeitsblatts. Um die Sichtbarkeit der Gitternetzlinien zu steuern, verwenden Sie die Eigenschaft [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--). [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) ist eine Boolesche Eigenschaft, die nur einen **wahren** oder **falschen** Wert speichern kann.  

#### **Anzeigen von Rasterlinien**  

Machen Sie die Gitternetzlinien sichtbar, indem Sie die Eigenschaft [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) auf **true** setzen.  

#### **Rasterspalten ausblenden**  

Blenden Sie die Gitternetzlinien aus, indem Sie die Eigenschaft [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) auf **false** setzen.  

Ein vollständiges Beispiel wird unten gezeigt, das die Verwendung der Eigenschaft [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) demonstriert, indem eine Excel-Datei (book1.xls) geöffnet, die Gitternetzlinien auf dem ersten Arbeitsblatt ausgeblendet und die modifizierte Datei als output.xls gespeichert wird.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fileData = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file data
const workbook = new AsposeCells.Workbook(fileData);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the grid lines of the first worksheet of the Excel file
worksheet.setIsGridlinesVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

## **Zeigen und Ausblenden der Zeilen- und Spaltenüberschriften**  

Alle Arbeitsblätter in einer Excel-Datei bestehen aus Zellen, die in Zeilen und Spalten angeordnet sind. Alle Zeilen und Spalten haben eindeutige Werte, die zur Identifizierung und zum Identifizieren einzelner Zellen verwendet werden. Beispielsweise sind Zeilen nummeriert – 1, 2, 3, 4 usw. – und Spalten sind alphabetisch geordnet – A, B, C, D usw. Die Zeilen- und Spaltenwerte werden in den Überschriften angezeigt. Mit Aspose.Cells können Entwickler die Sichtbarkeit dieser Zeilen- und Spaltenüberschriften steuern.  

### **Steuerung der Sichtbarkeit der Arbeitsblätter**  

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), die eine Microsoft Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) enthält eine [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-Sammlung, die es Entwicklern ermöglicht, auf jedes Arbeitsblatt in der Excel-Datei zuzugreifen. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung eines Arbeitsblatts. Um die Sichtbarkeit von Zeilen- und Spaltenüberschriften zu steuern, verwenden Sie die Eigenschaft [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--). [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) ist eine Boolesche Eigenschaft, die nur einen **wahren** oder **falschen** Wert speichern kann.  

#### **Anzeigen von Zeilen-/Spaltenüberschriften**  

Machen Sie Zeilen- und Spaltenüberschriften sichtbar, indem Sie die Eigenschaft [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) auf **true** setzen.  

#### **Zeilen-/Spaltenheader ausblenden**  

Blenden Sie Zeilen- und Spaltenüberschriften aus, indem Sie die Eigenschaft [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) auf **false** setzen.  

Ein vollständiges Beispiel wird unten gezeigt, das die Verwendung der Eigenschaft [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) demonstriert, indem eine Excel-Datei (book1.xls) geöffnet, die Zeilen- und Spaltenüberschriften auf dem ersten Arbeitsblatt ausgeblendet und die modifizierte Datei als output.xls gespeichert wird.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object with file path
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the headers of rows and columns
worksheet.setIsRowColumnHeadersVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  
Es ist auch möglich, die Methoden [**Cells.unhideRows(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRows-number-number-number-) und [**Cells.unhideColumns(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumns-number-number-number-) der [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) Klasse zu verwenden, um mehrere Zeilen und Spalten sichtbar zu machen.  
{{% /alert %}}  

