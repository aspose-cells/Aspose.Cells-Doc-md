---
title: Hur man ändrar bakgrund i kommentar i Excel med Node.js via C++
linktitle: Kommentarbakgrund
type: docs
weight: 190
url: /sv/nodejs-cpp/how-to-set-comment-background/
description: Hur man ändrar färg i kommentar och infogar bild eller bild i kommentar i Excel med Aspose.Cells for Node.js via C++.
keywords: lägg till infattad bild, färg, kommentarbakgrund Excel Node.js via C++
---

{{% alert color="primary" %}}
Kommentarer läggs till celler för att dokumentera kommentarer, allt från detaljer om hur en formel fungerar, var ett värde kommer ifrån eller frågor från granskare. Kommentarer spelar en extremt viktig roll när flera personer diskuterar eller granskar samma dokument vid olika tillfällen. Hur kan man skilja mellan olika personers kommentarer? Ja, vi kan ställa in en annan bakgrundsfärg för varje kommentar. Men när vi behöver bearbeta många dokument och många kommentarer, är att göra det manuellt en katastrof. Lyckligtvis tillhandahåller [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) ett API som låter dig göra detta i kod.
{{% /alert %}}

## **Hur man ändrar färg i kommentar i Excel**

När du inte behöver standardbakgrundsfärgen för kommentarer kan du vilja ersätta den med en färg du är intresserad av. Hur ändrar jag bakgrundsfärgen på kommentarrutan i Excel?

Följande kod kommer att guida dig hur du använder [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) för att lägga till din favoritbakgrundsfärg till kommentarer efter eget val.

Här har vi förberett en [exempel fil](exmaple.xlsx) för dig. Denna fil används för att initialisera Workbook-objektet i koden nedan.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Initialize a new workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "example.xlsx"));

// Accessing the newly added comment
const comment = workbook.getWorksheets().get(0).getComments().get(0);

// change background color
const shape = comment.getCommentShape();
shape.getFill().getSolidFill().setColor(AsposeCells.Color.Red);

// Save the Excel file
workbook.save(path.join(dataDir, "result.xlsx"));
```

Kör ovanstående kod så får du en [utdatafil](result.xlsx).

## **Hur man infogar bild eller bild i kommentar i Excel**

Microsoft Excel låter användare anpassa utseendet och känslan av kalkylblad i stor utsträckning. Det är till och med möjligt att lägga till bakgrundsbilder i kommentarer. Att lägga till en bakgrundsbild kan vara ett estetiskt val eller användas för att stärka varumärket.

Exempelkoden nedan skapar en XLSX-fil från början med [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) API, och lägger till en kommentar med bakgrundsbild i cell A1.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

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
const fs = require("fs");
const bmp = fs.readFileSync(path.join(dataDir, "image2.jpg"));
const ms = Buffer.from(bmp);

// Set image data to the shape associated with the comment
comment.getCommentShape().getFill().setImageData(ms);

// Save the workbook
const outputFilePath = path.join(dataDir, "commentwithpicture1.out.xlsx");
workbook.save(outputFilePath, AsposeCells.SaveFormat.Xlsx);
```

