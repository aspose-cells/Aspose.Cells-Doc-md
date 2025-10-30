---  
title: Maximalbereich in einem Arbeitsblatt mit Node.js über C++ abrufen  
linktitle: Holen Sie den maximalen Bereich in einem Arbeitsblatt ab  
type: docs  
weight: 360  
url: /de/nodejs-cpp/get-max-range-in-a-worksheet/  
description: Dieser Artikel beschreibt, wie man den Maximalbereich, den maximalen Datenbereich und den maximalen Anzeigebereich von Excel Dateien mit Aspose.Cells for Node.js via C++ erhält.  
---  

{{% alert color="primary" %}}  

Beim Lesen von Daten aus dem Arbeitsblatt müssen wir den maximalen Bereich kennen.  

Beim Kopieren aller Daten aus einem Arbeitsblatt müssen wir den maximalen Bereich kennen.  

Beim Exportieren eines bestimmten Bereichs nach HTML und PDF müssen wir den maximalen Bereich kennen.  

Aspose.Cells for Node.js via C++ bietet verschiedene Möglichkeiten, den maximalen Bereich in einem Arbeitsblatt zu finden.  

{{% /alert %}}  

## **Den Maximalbereich abrufen**  
In Aspose.Cells werden, wenn die Objekte [**row**](https://reference.aspose.com/cells/nodejs-cpp/row/) und [**column**](https://reference.aspose.com/cells/nodejs-cpp/column/) initialisiert sind, diese Zeilen und Spalten zum maximalen Bereich gezählt, selbst wenn in leeren Zeilen oder Spalten keine Daten vorhanden sind.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");

// Loads the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();
const sheet = worksheets.get(0);

// Gets the max data range.
let maxRow = sheet.getCells().getMaxRow();
let maxColumn = sheet.getCells().getMaxColumn();
// The range is A1:B3.
let range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);

sheet.getCells().get("A10").putValue(null);

maxRow = sheet.getCells().getMaxRow();
maxColumn = sheet.getCells().getMaxColumn();
// The range is updated to A1:B10.
range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);
```  

## **Maximalen Datenbereich abrufen**  
In den meisten Fällen müssen wir nur alle Bereiche erhalten, die alle Daten enthalten, auch wenn die leeren Zellen außerhalb des Bereichs formatiert sind.  
Und die Einstellungen zu Formen, Tabellen und Pivot-Tabellen werden ignoriert.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();
const sheet = worksheets.get(0);

// Gets the max data range.
let maxRow = sheet.getCells().getMaxDataRow();
let maxColumn = sheet.getCells().getMaxDataColumn();
// The range is A1:B3.
let range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);

sheet.getCells().get("A10").putValue(null);

maxRow = sheet.getCells().getMaxDataRow();
maxColumn = sheet.getCells().getMaxDataColumn();
// The range is still A1:B3.
range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);
```  

## **Maximale Anzeigebereich erhalten**  
Wenn wir alle Daten aus dem Arbeitsblatt in HTML, PDF oder Bildern exportieren, müssen wir einen Bereich erhalten, der alle sichtbaren Objekte enthält, einschließlich Daten, Styles, Grafiken, Tabellen und Pivot-Tabellen.  
Die folgenden Codes zeigen, wie der maximale Anzeigebereich in HTML gerendert wird:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Gets the max display range.
const range = worksheets.get(0).getCells().getMaxDisplayRange();

// Save the range to html
const saveOptions = new AsposeCells.HtmlSaveOptions();
saveOptions.setExportActiveWorksheetOnly(true);
saveOptions.setExportArea(AsposeCells.CellArea.createCellArea(range.getFirstRow(), range.getFirstColumn(), range.getFirstRow() + range.getRowCount() - 1, range.getFirstColumn() + range.getColumnCount() - 1));

// Save the range.
workbook.save("html.html", saveOptions);
```  

Hier ist die [Quelldatei Excel](Book1.xlsx).  

{{< app/cells/assistant language="nodejs-cpp" >}}
