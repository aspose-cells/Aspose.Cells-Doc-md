---
title: Come applicare/impostare l allineamento del testo a una casella di testo con Node.js tramite C++
linktitle: Applicare/impostare l allineamento del testo alla casella di testo
type: docs
weight: 20
url: /it/nodejs-cpp/applying-text-alignment-to-partial-text-inside-the-textbox/
description: Come applicare/impostare l allineamento del testo a una casella di testo in Aspose.Cells for Node.js via C++.
keywords: applica/imposta l allineamento alla TextBox nel Foglio di lavoro Excel Aspose Node.js tramite C++
---

Le caselle di testo possono migliorare l'espressività dei nostri documenti e diagrammi, e applicare diversi allineamenti a diverse parti di una TextBox può aiutare a evidenziare punti di interesse per i lettori. Ma l'allineamento predefinito della TextBox non soddisfa tutte le esigenze. Per questo, potrebbe essere necessario regolare ogni TextBox per soddisfare le tue specifiche. Se non hai molti oggetti TextBox da modificare, sei fortunato. Se ci sono molte TextBox da regolare, credo che potresti avere dei problemi. Non preoccuparti ora, [Aspose.Cells](https://products.aspose.com/cells/) fornisce un'interfaccia API per aiutarti a fare proprio questo.

Il seguente codice di esempio applica l'allineamento del testo a una casella di testo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
const shapes = workbook.getWorksheets().get(0).getShapes();

// add a TextBox
const shape = shapes.addTextBox(2, 0, 2, 0, 50, 120);
shape.setText("This is a test.");

// set alignment
shape.setTextHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
shape.setTextVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Save the excel file.
workbook.save(path.join(dataDir, "result.xlsx"));
```

Puoi anche modificare l'allineamento del testo di alcune parti di una forma TextBox usando il testo HTML appropriato. Il seguente esempio di codice applica l'allineamento del testo a parte del testo all’interno della TextBox.

[file origine](SampleTextboxExcel2016.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "SampleTextboxExcel2016.xlsx");

// Initialize an object of the Workbook class to load the template file
const sourceWb = new AsposeCells.Workbook(sourceFilePath);

// Access the target textbox whose text is to be aligned
const sourceTextBox = sourceWb.getWorksheets().get(0).getShapes().get(0);

// Create an object of the target workbook
const destWb = new AsposeCells.Workbook();

// Access the first worksheet from the collection
const _sheet = destWb.getWorksheets().get(0);

// Create new textbox
const _textBox = _sheet.getShapes().addShape(AsposeCells.MsoDrawingType.TextBox, 1, 0, 1, 0, 200, 200);

// Alternatively text box can be added using the following line as well
// const _textBox = _sheet.getShapes().addTextBox(1, 0, 1, 0, 200, 200);

// Use Html string from a template file textbox
_textBox.setHtmlText(sourceTextBox.getHtmlText());

// Save the workbook on disk
destWb.save("Output.xlsx");
```
