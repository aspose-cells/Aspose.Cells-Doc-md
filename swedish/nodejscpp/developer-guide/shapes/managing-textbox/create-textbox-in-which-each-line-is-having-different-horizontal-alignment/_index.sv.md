---
title: Skapa TextBox där varje rad har en annan horisontell justering med Node.js via C++
linktitle: Skapa textfält där varje rad har olika horisontell justering
type: docs
weight: 310
url: /sv/nodejs-cpp/create-textbox-in-which-each-line-is-having-different-horizontal-alignment/
description: Lär dig att skapa en TextBox där varje rad kan ha en annan horisontell justering med Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}
Du kan ställa in den horisontella justeringen av din styckes text med hjälp av [**TextParagraph.getAlignmentType()**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/#getAlignmentType--) egenskapen.
{{% /alert %}}

Följande kodexempel skapar tre linjer och ställer in den horisontella justeringen för var och en av dem.

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
