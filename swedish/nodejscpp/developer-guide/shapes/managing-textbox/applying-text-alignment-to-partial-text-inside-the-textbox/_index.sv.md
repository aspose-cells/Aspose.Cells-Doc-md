---
title: Hur man använder/inställer textjustering i textruta med Node.js via C++
linktitle: Tillämpa / ställa in textjustering för textrutan
type: docs
weight: 20
url: /sv/nodejs-cpp/applying-text-alignment-to-partial-text-inside-the-textbox/
description: Hur man använder/inställer textjustering i textruta i Aspose.Cells for Node.js via C++.
keywords: Använd/inställ utfall för TextBox arbetsblad Excel Aspose Node.js via C++
---

TextBoxar kan förbättra uttryckssättet i våra dokument och diagram, och att tillämpa olika justeringar på olika delar av en TextBox kan hjälpa till att lyfta fram intressanta punkter för läsare. Men standardjusteringen av TextBox möter inte alla våra behov. För detta kan du behöva justera varje TextBox för att möta dina målkrav. Om du inte har många TextBox-objekt att finjustera är du lyckligt lottad. Om det finns så många TextBoxar att justera, tror jag att du kommer att ha problem. Oroa dig inte nu, [Aspose.Cells](https://products.aspose.com/cells/) tillhandahåller ett API-gränssnitt för att hjälpa dig med just detta.

Följande kodexempel tillämpar textjustering på en TextBox.

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

Du kan också ändra textjusteringen för vissa delar av en TextBox-form med rätt HTML-text. Följande exempel kod tillämpar textjustering på del av texten i TextBoxen.

[källfil](SampleTextboxExcel2016.xlsx)

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
