---
title: Créer une zone de texte dans laquelle chaque ligne a un alignement horizontal différent avec Node.js via C++
linktitle: Créer une zone de texte dans laquelle chaque ligne a un alignement horizontal différent
type: docs
weight: 310
url: /fr/nodejs-cpp/create-textbox-in-which-each-line-is-having-different-horizontal-alignment/
description: Apprenez à créer une zone de texte dans laquelle chaque ligne peut avoir un alignement horizontal différent en utilisant Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}
Vous pouvez définir l'alignement horizontal de votre texte de paragraphe en utilisant la propriété [**TextParagraph.getAlignmentType()**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/#getAlignmentType--).
{{% /alert %}}

Le code d'exemple suivant crée trois lignes et définit l'alignement horizontal de chacune d'entre elles.

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
{{< app/cells/assistant language="nodejs-cpp" >}}
