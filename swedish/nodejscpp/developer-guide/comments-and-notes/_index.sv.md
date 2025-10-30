---
title: Hantera kommentarer och anteckningar med Node.js via C++
linktitle: Kommentarer och noteringar
type: docs
weight: 128
url: /sv/nodejs-cpp/comments-and-notes/
description: Infoga och hantera kommentarer eller anteckningar med Aspose.Cells for Node.js via C++.
keywords: infoga kommentarer, infoga anteckningar Node.js via C++
---

## **Introduktion**

Kommentarer används för att lägga till ytterligare information i celler. Aspose.Cells for Node.js via C++ erbjuder två metoder för att lägga till kommentarer i celler. Den första är att skapa kommentarer manuellt i en designer-fil. Dessa kommentarer importeras sedan med Aspose.Cells. Den andra är att lägga till kommentarer med Aspose.Cells API vid körning. Detta ämne diskuterar hur man lägger till kommentarer i celler med Aspose.Cells API. Formatering av kommentarer kommer också att förklaras.

## **Lägga till en kommentar**

Lägg till en kommentar i en cell genom att anropa [**Comments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection)-samlingen [**CommentCollection.add(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#add-number-number-)-metod (inkapslad i [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)). Den nya [**Comment**](https://reference.aspose.com/cells/nodejs-cpp/comment)-objektet kan nås från [**Comments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection)-samlingen genom att ange kommentaren index. Efter åtkomst till [**Comment**](https://reference.aspose.com/cells/nodejs-cpp/comment)-objektet, anpassa kommentarenotisen genom att använda [**getNote()**](https://reference.aspose.com/cells/nodejs-cpp/comment/#getNote--)-egenskapen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a comment to "F5" cell
const commentIndex = worksheet.getComments().add("F5");

// Accessing the newly added comment
const comment = worksheet.getComments().get(commentIndex);

// Setting the comment note
comment.setNote("Hello Aspose!");

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Kommentarformatering**

Det är också möjligt att formatera kommentarers utseende genom att konfigurera deras höjd, bredd och teckensnittsinställningar.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a comment to "F5" cell
const commentIndex = worksheet.getComments().add("F5");

// Accessing the newly added comment
const comment = worksheet.getComments().get(commentIndex);

// Setting the comment note
comment.setNote("Hello Aspose!");

// Setting the font size of a comment to 14
comment.getFont().setSize(14);

// Setting the font of a comment to bold
comment.getFont().setIsBold(true);

// Setting the height of the font to 10
comment.setHeightCM(10);

// Setting the width of the font to 2
comment.setWidthCM(2);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Lägg till en bild till en kommentar**

Med Microsoft Excel 2007 är det också möjligt att ha en bild som bakgrund till en cellkommentar. I Excel 2007 uppnås detta genom följande steg. (De förutsätter att du redan har lagt till en cellkommentar.)

1. Högerklicka på cellen som innehåller kommentaren.
1. Välj ** Visa/dölj kommentarer ** och ta bort all text från kommentaren.
1. Klicka på kommentarens kant för att markera den.
1. Välj ** Formatera **, sedan ** Kommentar **.
1. På fliken ** Färg och linjer **, expandera **Färg** listan.
1. Klicka på **Fyllnings effekter**.
1. På fliken **Bild**, klicka på **Välj bild**.
1. Hitta och välj bilden.
1. Klicka **OK** tills alla dialogrutor har stängts.

Aspose.Cells tillhandahåller också den här funktionen. Nedan finns ett kodexempel som skapar en XLSX-fil från grunden och lägger till en kommentar i cellen "A1" med en bild som bakgrund.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook
const workbook = new AsposeCells.Workbook();

// Get a reference of comments collection with the first sheet
const comments = workbook.getWorksheets().get(0).getComments();

// Add a comment to cell A1
const commentIndex = comments.add(0, 0);
const comment = comments.get(commentIndex);
comment.setNote("First note.");
comment.getFont().setName("Times New Roman");

// Load an image into stream
const bmpPath = path.join(dataDir, "logo.jpg");
const bmpData = fs.readFileSync(bmpPath);

// Set image data to the shape associated with the comment
comment.getCommentShape().getFill().setImageData(bmpData);

// Save the workbook
workbook.save(path.join(dataDir, "book1.out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **Fortsatta ämnen**
- [Ändra textriktning för kommentaren](/cells/sv/nodejs-cpp/change-text-direction-of-the-comment/)
- [Hur man ändrar färgen på kommentarsfönstret](/cells/sv/nodejs-cpp/how-to-change-the-comment-font-color/)
- [Hur man ställer in kommentarens bakgrund](/cells/sv/nodejs-cpp/how-to-set-comment-background/)
- [Trådade Kommentarer](/cells/sv/nodejs-cpp/threaded-comments/)

{{< app/cells/assistant language="nodejs-cpp" >}}
