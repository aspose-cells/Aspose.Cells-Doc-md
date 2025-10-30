---  
title: Come cambiare il colore del carattere del commento con Node.js tramite C++  
linktitle: Come cambiare il colore del carattere del commento  
type: docs  
weight: 180  
url: /it/nodejs-cpp/how-to-change-the-comment-font-color/  
---  

{{% alert color="primary" %}}  
Microsoft Excel permette agli utenti di aggiungere commenti alle celle per includere informazioni aggiuntive e evidenziare i dati. Gli sviluppatori potrebbero aver bisogno di personalizzare il commento per specificare le impostazioni di allineamento, la direzione del testo, il colore del carattere, ecc. Aspose.Cells for Node.js via C++ fornisce API per completare il task.  
{{% /alert %}}  

Aspose.Cells for Node.js via C++ fornisce una proprietà [**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--) per impostare il colore del carattere del commento. Il seguente esempio di codice dimostra l’uso della proprietà [**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--) per impostare la direzione del testo di un commento.  

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

Il file di output (102662195.xlsx) generato dal codice sopra è allegato per il tuo riferimento.  
{{< app/cells/assistant language="nodejs-cpp" >}}
