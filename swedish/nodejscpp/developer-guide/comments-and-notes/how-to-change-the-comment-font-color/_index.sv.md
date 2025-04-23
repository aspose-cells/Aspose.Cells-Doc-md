---  
title: Hur man ändrar kommentarens teckens färg med Node.js via C++  
linktitle: Hur man ändrar kommentarens teckensnittsfärg  
type: docs  
weight: 180  
url: /sv/nodejs-cpp/how-to-change-the-comment-font-color/  
---  

{{% alert color="primary" %}}  
Microsoft Excel tillåter användare att lägga till kommentarer till celler för att lägga till ytterligare information och belysa data. Utvecklare kan behöva anpassa kommentaren för att ange alignmentsinställningar, textinriktning, teckensfärg etc. Aspose.Cells for Node.js via C++ tillhandahåller API:er för att genomföra uppgiften.  
{{% /alert %}}  

Aspose.Cells for Node.js via C++ tillhandahåller en [**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--) egenskap för att ställa in teckensfärgen för kommentaren. Följande exempel visar användningen av [**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--)-egenskapen för att ställa in textinriktning för en kommentar.  

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

Den [utdatafil](102662195.xlsx) som genererats av ovanstående kod bifogas för din referens.  
