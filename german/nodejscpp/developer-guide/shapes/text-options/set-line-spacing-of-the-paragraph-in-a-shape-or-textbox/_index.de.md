---  
title: Zeilenabstand des Absatzes in einer Form oder Textbox mit Node.js über C++ festlegen  
linktitle: Abstand zwischen Zeilen des Absatzes in einer Form oder Textfeld festlegen  
type: docs  
weight: 290  
url: /de/nodejs-cpp/set-line-spacing-of-the-paragraph-in-a-shape-or-textbox/  
description: Lernen Sie, wie der Zeilenabstand von Absätzen in Formen oder Textboxen mit Aspose.Cells for Node.js via C++ eingestellt wird.  
---  

{{% alert color="primary" %}}  

Sie können den Zeilenabstand des Absatzes, den Abstand davor und danach mit den Eigenschaften [**TextParagraph.getLineSpace()**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/#getLineSpace--), [**TextParagraph.getSpaceBefore()**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/#getSpaceBefore--) und [**TextParagraph.getSpaceAfter()**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/#getSpaceAfter--) der Klasse [**TextParagraph**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/) festlegen.  

{{% /alert %}}  

Der folgende Beispielcode erläutert die Verwendung der genannten Eigenschaften.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create a workbook
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Add text box inside the sheet
ws.getShapes().addTextBox(2, 0, 2, 0, 100, 200);

// Access first shape which is a text box and set its text
const shape = ws.getShapes().get(0);
shape.setText("Sign up for your free phone number.\nCall and text online for free.");

// Access the first paragraph
const p = shape.getTextBody().getTextParagraphs().get(1);

// Set the line space
p.setLineSpaceSizeType(AsposeCells.LineSpaceSizeType.Points);
p.setLineSpace(20);

// Set the space after
p.setSpaceAfterSizeType(AsposeCells.LineSpaceSizeType.Points);
p.setSpaceAfter(10);

// Set the space before
p.setSpaceBeforeSizeType(AsposeCells.LineSpaceSizeType.Points);
p.setSpaceBefore(10);

// Save the workbook in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

