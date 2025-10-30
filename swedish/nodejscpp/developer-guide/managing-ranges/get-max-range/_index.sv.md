---  
title: Hämta maxområde i ett kalkylblad med Node.js via C++  
linktitle: Få maxintervall i ett arbetsblad  
type: docs  
weight: 360  
url: /sv/nodejs-cpp/get-max-range-in-a-worksheet/  
description: Denna artikel beskriver hur man får det maximala området, maximala dataintervallet och maximala visningsområdet för Excel filer med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

När vi läser data från arket behöver vi känna till det maximala området.  

När vi kopierar all data från ett ark behöver vi känna till det maximala området.  

När du exporterar ett specificerat område till HTML och PDF behöver vi känna till det maximala området.  

Aspose.Cells for Node.js via C++ innehåller olika metoder för att hitta det maximala området i ett kalkylblad.  

{{% /alert %}}  

## **Får maximalt intervall**  
I Aspose.Cells, om objekten [**row**](https://reference.aspose.com/cells/nodejs-cpp/row/) och [**column**](https://reference.aspose.com/cells/nodejs-cpp/column/) är initialiserade, kommer dessa rader och kolumner att räknas till det maximala området, även om det inte finns någon data i tomma rader eller kolumner.  

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

## **Får maximalt datointervall**  
I de flesta fall behöver vi bara få alla intervall som innehåller all data, även om de tomma cellerna utanför intervallet är formaterade.  
Och inställningarna för former, tabeller och pivottabeller kommer att ignoreras.  

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

## **Får maximalt visningsintervall**  
När vi exporterar all data från arket till HTML, PDF eller bilder behöver vi få ett område som innehåller alla synliga objekt, inklusive data, stilar, grafik, tabeller och pivottabeller.  
Följande kodexempel visar hur man renderar det maximala visningsområdet till HTML:  

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

Här är [källa excel-fil](Book1.xlsx).  

{{< app/cells/assistant language="nodejs-cpp" >}}
