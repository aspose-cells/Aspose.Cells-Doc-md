---
title: Wie man die Textausrichtung auf Textfelder mit Node.js via C++ anwendet/einstellt
linktitle: Textausrichtung für Textfeld anwenden/einstellen
type: docs
weight: 20
url: /de/nodejs-cpp/applying-text-alignment-to-partial-text-inside-the-textbox/
description: Wie man die Textausrichtung auf Textfelder in Aspose.Cells for Node.js via C++ anwendet/einstellt.
keywords: Textausrichtung auf TextBox Arbeitsblatt Excel Aspose Node.js via C++ anwenden/einstellen
---

TextBoxen können die Ausdruckskraft unserer Dokumente und Diagramme verbessern, und das Anwenden verschiedener Ausrichtungen auf unterschiedliche Teile eines TextBox kann helfen, interessante Punkte für die Leser hervorzuheben. Aber die Standardausrichtung einer TextBox erfüllt nicht alle unsere Bedürfnisse. Für diesen Zweck müssen Sie jede TextBox an Ihre Zielanforderungen anpassen. Wenn Sie nicht viele TextBox-Objekte zum Anpassen haben, haben Sie Glück. Wenn es jedoch sehr viele TextBoxen gibt, denke ich, könnten Sie Probleme bekommen. Keine Sorge, [Aspose.Cells](https://products.aspose.com/cells/) bietet eine API-Schnittstelle, die Ihnen genau dabei hilft.

Der folgende Beispielcode wendet die Textausrichtung auf ein TextBox an.

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

Sie können auch die Textausrichtung einiger Texte innerhalb einer TextBox-Form anhand des entsprechenden HTML-Texts ändern. Das folgende Beispiel wendet die Textausrichtung auf den Teiltext innerhalb der TextBox an.

[Quelldatei](SampleTextboxExcel2016.xlsx)

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
{{< app/cells/assistant language="nodejs-cpp" >}}
