---
title: Kopiera områden i Excel med Node.js via C++
linktitle: Kopiera områden
type: docs
weight: 105
url: /sv/nodejs-cpp/copy-ranges-of-Excel/
---

## **Introduktion**

I Excel kan du markera ett område, kopiera området och sedan klistra in det med specifika alternativ på samma arbetsblad, andra arbetsblad eller andra filer.

## **Kopiera områden med Aspose.Cells for Node.js via C++**

Aspose.Cells for Node.js via C++ tillhandahåller några överbelastningar av [Range.copy(Range, PasteOptions)](https://reference.aspose.com/cells/nodejs-cpp/range/#copy-range-pasteoptions-) metoder för att kopiera området. Och [Range.copyStyle(Range)](https://reference.aspose.com/cells/nodejs-cpp/range/#copyStyle-range-) kopierar endast formateringen av området; [Range.copyData(Range)](https://reference.aspose.com/cells/nodejs-cpp/range/#copyData-range-) kopierar endast värdena.

## **Kopiera område**

Skapa två områden: källområdet och målordet, och kopiera sedan källområdet till målordet med metoden `Range.copy`.

Se följande kod:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get all the worksheets in the book.
let worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
let worksheet = workbook.getWorksheets().get(0);

// Create a range of cells.
let sourceRange = worksheet.getCells().createRange("A1", "A2");

// Input some data with some formattings into A few cells in the range.
sourceRange.get(0, 0).setValue("Test");
sourceRange.get(1, 0).setValue(123);

// Create target range of cells.
let targetRange = worksheet.getCells().createRange("B1", "B2");

// Copy source range to target range in the same worksheet 
targetRange.copy(sourceRange);

// Create target range of cells.
workbook.getWorksheets().add();
worksheet = workbook.getWorksheets().get(1);

targetRange = worksheet.getCells().createRange("A1", "A2");
// Copy source range to target range in another worksheet 
targetRange.copy(sourceRange);

// Copy to another workbook
const anotherWorkbook = new AsposeCells.Workbook();

worksheet = workbook.getWorksheets().get(0);

targetRange = worksheet.getCells().createRange("A1", "A2");
// Copy source range to target range in another workbook 
targetRange.copy(sourceRange);
```

## **Klistra in område med alternativ**

Aspose.Cells for Node.js via C++ stöder att klistra in området med specifika typer.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
const worksheet = workbook.getWorksheets().get(0);

// Create a range of cells.
const sourceRange = worksheet.getCells().createRange("A1", "A2");

// Input some data with some formattings into
// A few cells in the range.
sourceRange.get(0, 0).setValue("Test");
sourceRange.get(1, 0).setValue(123);

// Create target range of cells.
const targetRange = worksheet.getCells().createRange("B1", "B2");

// Init paste options.
const options = new AsposeCells.PasteOptions();
// Set paste type.
options.setPasteType(AsposeCells.PasteType.ValuesAndFormats);
options.setSkipBlanks(true);
// Copy source range to target range
targetRange.copy(sourceRange, options);
```

## **Endast kopiera data för området**

Dessutom kan du kopiera data med metoden `Range.copyData` som visas i följande kod:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
const worksheet = worksheets.get(0);

// Create a range of cells.
const sourceRange = worksheet.getCells().createRange("A1", "A2");

// Input some data with some formattings into
// A few cells in the range.
sourceRange.get(0, 0).setValue("Test");
sourceRange.get(1, 0).setValue(123);

// Create target range of cells.
const targetRange = worksheet.getCells().createRange("B1", "B2");

// Copy the data of source range to target range
targetRange.copyData(sourceRange);
```

## **Fortsatta ämnen**
- [Kopiera radhöjder från källspann till destinationspann](/cells/sv/nodejs-cpp/copy-row-heights-of-source-range-to-destination-range/)

{{< app/cells/assistant language="nodejs-cpp" >}}
