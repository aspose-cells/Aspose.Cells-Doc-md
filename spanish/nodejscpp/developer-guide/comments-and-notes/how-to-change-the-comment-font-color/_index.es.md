---  
title: Cómo cambiar el color de la fuente del comentario con Node.js a través de C++  
linktitle: Cómo cambiar el color de fuente del comentario  
type: docs  
weight: 180  
url: /es/nodejs-cpp/how-to-change-the-comment-font-color/  
---  

{{% alert color="primary" %}}  
Microsoft Excel permite a los usuarios agregar comentarios a las celdas para agregar información adicional y resaltar datos. Los desarrolladores pueden necesitar personalizar el comentario para especificar configuraciones de alineación, dirección del texto, color de fuente, etc. Aspose.Cells for Node.js via C++ proporciona APIs para lograr esta tarea.  
{{% /alert %}}  

Aspose.Cells for Node.js via C++ proporciona una propiedad [**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--) para establecer el color de fuente del comentario. El siguiente código de ejemplo demuestra el uso de la propiedad [**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--) para configurar la dirección del texto en un comentario.  

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

El [archivo de salida](102662195.xlsx) generado por el código anterior se adjunta para su referencia.  
{{< app/cells/assistant language="nodejs-cpp" >}}
