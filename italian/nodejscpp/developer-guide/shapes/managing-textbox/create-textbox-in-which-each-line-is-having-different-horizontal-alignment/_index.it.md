---
title: Crea una TextBox in cui ogni riga ha un allineamento orizzontale diverso utilizzando Node.js tramite C++
linktitle: Crea TextBox in cui ogni riga ha un diverso Allineamento Orizzontale
type: docs
weight: 310
url: /it/nodejs-cpp/create-textbox-in-which-each-line-is-having-different-horizontal-alignment/
description: Impara come creare una TextBox in cui ogni riga può avere un allineamento orizzontale diverso usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}
È possibile impostare l'allineamento orizzontale del testo del paragrafo utilizzando la proprietà [**TextParagraph.getAlignmentType()**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/#getAlignmentType--).
{{% /alert %}}

Il seguente codice di esempio crea tre righe e imposta l'allineamento orizzontale di ciascuna di esse.

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
