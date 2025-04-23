---  
title: Wie man die Schriftfarbe eines Kommentars mit Node.js über C++ ändert  
linktitle: Wie ändere ich die Kommentarschriftfarbe  
type: docs  
weight: 180  
url: /de/nodejs-cpp/how-to-change-the-comment-font-color/  
---  

{{% alert color="primary" %}}  
Microsoft Excel erlaubt es Benutzern, Kommentare zu Zellen hinzuzufügen, um zusätzliche Informationen bereitzustellen und Daten hervorzuheben. Entwickler müssen möglicherweise die Kommentare anpassen, um Ausrichtungseinstellungen, Textrichtung, Schriftfarbe usw. festzulegen. Aspose.Cells for Node.js via C++ bietet die APIs für diese Aufgabe.  
{{% /alert %}}  

Aspose.Cells for Node.js via C++ stellt die [**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--)-Eigenschaft bereit, um die Schriftfarbe des Kommentars festzulegen. Der folgende Beispielcode zeigt die Verwendung der [**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--)-Eigenschaft, um die Textausrichtung eines Kommentars festzulegen.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add some text in cell A1
worksheet.getCells().get("A1").putValue("Here");

// Add a comment to A1 cell
const commentIndex = worksheet.getComments().add("A1");
const comment = worksheet.getComments().get(commentIndex);

// Set its vertical alignment setting            
comment.getCommentShape().setTextVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Set the Comment note
comment.setNote("This is my Comment Text. This is Test.");

const shape = worksheet.getComments().get("A1").getCommentShape();

shape.getFill().getSolidFill().setColor(AsposeCells.Color.Black);
const font = shape.getFont();
font.setColor(AsposeCells.Color.White);
const styleFlag = new AsposeCells.StyleFlag();
styleFlag.setFontColor(true);
shape.getTextBody().format(0, shape.getText().length, font, styleFlag);

// Save the Excel file
workbook.save(path.join(outputDir, "outputChangeCommentFontColor.xlsx"));
```  

Die [Ausgabedatei](102662195.xlsx), die vom obigen Code generiert wurde, ist als Referenz angehängt.  
