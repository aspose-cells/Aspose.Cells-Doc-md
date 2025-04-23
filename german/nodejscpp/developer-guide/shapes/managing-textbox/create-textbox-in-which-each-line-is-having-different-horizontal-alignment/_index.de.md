---
title: Erstellen Sie eine TextBox, in der jede Zeile eine andere horizontale Ausrichtung hat, mit Node.js via C++
linktitle: Erstellen Sie ein Textfeld, in dem jede Zeile eine andere horizontale Ausrichtung hat
type: docs
weight: 310
url: /de/nodejs-cpp/create-textbox-in-which-each-line-is-having-different-horizontal-alignment/
description: Erfahren Sie, wie Sie mit Aspose.Cells for Node.js via C++ eine TextBox erstellen, in der jede Zeile eine andere horizontale Ausrichtung haben kann.
---

{{% alert color="primary" %}}
Sie können die horizontale Ausrichtung Ihres Absatztextes mit der Eigenschaft [**TextParagraph.getAlignmentType()**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/#getAlignmentType--) festlegen.
{{% /alert %}}

Der folgende Beispielcode erstellt drei Linien und legt die horizontale Ausrichtung jeder von ihnen fest.

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
