---  
title: Set Line Spacing of the Paragraph in a Shape or Textbox with Node.js via C++  
linktitle: Set Line Spacing of the Paragraph in a Shape or Textbox  
type: docs  
weight: 290  
url: /nodejs-cpp/set-line-spacing-of-the-paragraph-in-a-shape-or-textbox/  
description: Learn how to set the line spacing of paragraphs in shapes or textboxes using Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  

You can set the line spacing of the paragraph, its space before and after using the [**TextParagraph.getLineSpace()**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/#getLineSpace--), [**TextParagraph.getSpaceBefore()**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/#getSpaceBefore--), and [**TextParagraph.getSpaceAfter()**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/#getSpaceAfter--) properties of the [**TextParagraph**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/) class.  

{{% /alert %}}  

The following sample code explains the usage of the mentioned properties.  

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

// Set the line spacing
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

{{< app/cells/assistant language="nodejs-cpp" >}}
