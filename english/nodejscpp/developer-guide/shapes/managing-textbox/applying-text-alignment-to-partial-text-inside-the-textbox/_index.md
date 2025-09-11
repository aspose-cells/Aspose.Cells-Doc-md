---
title: How to apply/set text alignment to textbox with Node.js via C++
linktitle: Apply/Set text alignment to textbox
type: docs
weight: 20
url: /nodejs-cpp/applying-text-alignment-to-partial-text-inside-the-textbox/
description: How to apply/set text alignment to textbox in Aspose.Cells for Node.js via C++.
keywords: apply/set alignment TextBox Worksheet Excel Aspose Node.js via C++
---

TextBoxes can improve the expressiveness of our documents and diagrams, and applying different alignments to different parts of a TextBox can help highlight points of interest to readers. But the default alignment of TextBox does not meet all our needs. For this, you may need to adjust each TextBox to meet your target requirements. If you don't have a lot of TextBox objects to tweak, you're in luck. If there are so many TextBoxes to adjust, I think you will be in trouble. Don't worry now, [Aspose.Cells](https://products.aspose.com/cells/) provides such an API interface to help you do just that.

The following sample code applies text alignment to a TextBox.

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

You can also change the text alignment of some text inside a TextBox shape with the appropriate HTML text. The following sample code applies the text alignment to partial text inside the TextBox.

[source file](SampleTextboxExcel2016.xlsx)

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