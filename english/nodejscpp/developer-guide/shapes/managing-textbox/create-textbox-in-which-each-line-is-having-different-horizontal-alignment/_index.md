---
title: Create TextBox in which each line has a different Horizontal Alignment with Node.js via C++
linktitle: Create TextBox in which each line is having different Horizontal Alignment
type: docs
weight: 310
url: /nodejs-cpp/create-textbox-in-which-each-line-is-having-different-horizontal-alignment/
description: Learn how to create a TextBox in which each line can have a different horizontal alignment using Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}
You can set the horizontal alignment of your paragraph text using the [**TextParagraph.AlignmentType**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/#alignmentType) property.
{{% /alert %}}

The following sample code creates three lines and sets the horizontal alignment of each of them.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Add text box inside the sheet.
ws.getShapes().addTextBox(2, 0, 2, 0, 80, 400);

// Access first shape which is a text box and set its text.
const shape = ws.getShapes().get(0);
shape.setText("Sign up for your free phone number.\nCall and text online for free.\nCall your friends and family.");

// Access the first paragraph and set its horizontal alignment to left.
let p = shape.getTextBody().getTextParagraphs().get(0);
p.setAlignmentType(AsposeCells.TextAlignmentType.Left);

// Access the second paragraph and set its horizontal alignment to center.
p = shape.getTextBody().getTextParagraphs().get(1);
p.setAlignmentType(AsposeCells.TextAlignmentType.Center);

// Access the third paragraph and set its horizontal alignment to right.
p = shape.getTextBody().getTextParagraphs().get(2);
p.setAlignmentType(AsposeCells.TextAlignmentType.Right);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
