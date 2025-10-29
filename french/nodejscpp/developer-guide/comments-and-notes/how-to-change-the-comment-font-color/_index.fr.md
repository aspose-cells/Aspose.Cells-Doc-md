---  
title: Comment changer la couleur de la police du commentaire avec Node.js via C++  
linktitle: Comment changer la couleur de la police du commentaire  
type: docs  
weight: 180  
url: /fr/nodejs-cpp/how-to-change-the-comment-font-color/  
---  

{{% alert color="primary" %}}  
Microsoft Excel permet aux utilisateurs d'ajouter des commentaires aux cellules pour fournir des informations supplémentaires et mettre en évidence des données. Les développeurs peuvent avoir besoin de personnaliser le commentaire pour spécifier les paramètres d'alignement, la direction du texte, la couleur de la police, etc. Aspose.Cells for Node.js via C++ fournit des API pour accomplir cette tâche.  
{{% /alert %}}  

Aspose.Cells for Node.js via C++ offre une propriété [**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--) pour définir la couleur de la police du commentaire. Le code d'exemple ci-dessous montre comment utiliser cette propriété [**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--) pour définir la direction du texte d'un commentaire.  

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

Le [fichier de sortie](102662195.xlsx) généré par le code ci-dessus est joint à titre de référence.  
{{< app/cells/assistant language="nodejs-cpp" >}}
