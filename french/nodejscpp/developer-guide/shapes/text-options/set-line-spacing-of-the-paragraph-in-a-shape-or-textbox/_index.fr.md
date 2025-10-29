---  
title: Définir l espacement des lignes du paragraphe dans une forme ou une zone de texte avec Node.js via C++  
linktitle: Définir l espacement des lignes du paragraphe dans une forme ou un TextBox  
type: docs  
weight: 290  
url: /fr/nodejs-cpp/set-line-spacing-of-the-paragraph-in-a-shape-or-textbox/  
description: Apprenez à définir l espacement des lignes des paragraphes dans les formes ou zones de texte en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Vous pouvez définir l'espacement des lignes du paragraphe, l'espace avant et l'espace après en utilisant les propriétés [**TextParagraph.getLineSpace()**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/#getLineSpace--), [**TextParagraph.getSpaceBefore()**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/#getSpaceBefore--), et [**TextParagraph.getSpaceAfter()**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/#getSpaceAfter--) de la classe [**TextParagraph**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/).  

{{% /alert %}}  

Le code d'échantillon suivant explique l'utilisation des propriétés mentionnées.  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
