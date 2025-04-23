---  
title: Trådade kommentarer med Node.js via C++  
linktitle: Trådade kommentarer  
type: docs  
weight: 140  
url: /sv/nodejs-cpp/threaded-comments/  
description: Hantera trådade kommentarer i Excel dokument med Aspose.Cells for Node.js via C++. Lär dig att lägga till, läsa, redigera och ta bort trådade kommentarer.  
---  

## **Trådade Kommentarer**  

MS Excel 365 ger en funktion för att lägga till trådade kommentarer. Dessa kommentarer fungerar som konversationer och kan användas för diskussioner. Kommentarerna levereras nu med en svarsruta som möjliggör trådade konversationer. De gamla kommentarerna kallas anteckningar i Excel 365. Skärmavbildningen nedan visar hur trådade kommentarer visas när de öppnas i Excel.  

![todo:image_alt_text](threaded-comments_1.jpg)  

Trådade kommentarer visas så här i äldre versioner av Excel. Följande bilder har tagits genom att öppna provfilen i Excel 2016.  

![todo:image_alt_text](threaded-comments_2.jpg)  

![todo:image_alt_text](threaded-comments_3.jpg)  

Aspose.Cells tillhandahåller också funktionen att hantera trådade kommentarer.  

## **Lägg till trådade kommentarer**  

### **Lägg till trådad kommentar med Excel**  

För att lägga till trådade kommentarer i Excel 365 följer du följande steg.  

- Metod 1  
  - Klicka på fliken **Granska**  
  - Klicka på knappen **Ny kommentar**  
  - Detta kommer att öppna en dialogruta för att ange kommentarer i den aktiva cellen.  
  - ![todo:image_alt_text](threaded-comments_4.jpg)  
- Metod 2  
  - Högerklicka på den cell där du vill infoga kommentaren.  
  - Klicka på alternativet **Ny kommentar**  
  - Detta kommer att öppna en dialogruta för att ange kommentarer i den aktiva cellen.  
  - ![todo:image_alt_text](threaded-comments_5)  

### **Lägg till trådad kommentar med hjälp av Aspose.Cells**  

Aspose.Cells tillhandahåller metoden [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) för att lägga till trådade kommentarer. Metoden [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) accepterar följande tre parametrar.  

- Cell namn: Namnet på cellen där kommentaren ska infogas.  
- Kommentartext: Kommentarens innehåll.  
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentauthor): Kommentarens författare  

Följande kodexempel demonstrerar användningen av [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-)-metoden för att lägga till en trådad kommentar till cell A1. Se den genererade [Excel-fil](89849859.xlsx) för referens.  

#### **Exempelkod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const outDir = path.join(__dirname, "output");

const workbook = new AsposeCells.Workbook();

// Add Author
const authorIndex = workbook.getWorksheets().getThreadedCommentAuthors().add("Aspose Test", "", "");
const author = workbook.getWorksheets().getThreadedCommentAuthors().get(authorIndex);

// Add Threaded Comment
workbook.getWorksheets().get(0).getComments().addThreadedComment("A1", "Test Threaded Comment", author);

workbook.save(outDir + "AddThreadedComments_out.xlsx");
```  

## **Läs trådade kommentarer**  

### **Läs trådade kommentarer med Excel**  

För att läsa trådade kommentarer i Excel, svep helt enkelt musen över cellen som innehåller kommentarerna för att visa kommentarerna. Kommentarerna kommer att se ut som i följande bild.  

![todo:image_alt_text](threaded-comments_1.jpg)  

### **Läs trådade kommentarer med Aspose.Cells**  

Aspose.Cells tillhandahåller metoden [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) för att hämta trådade kommentarer för den angivna kolumnen. Metoden [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) tar kolumnnamnet som en parameter och returnerar [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection). Du kan iterera över [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) för att visa kommentarerna.  

Följande exempel visar hur man läser kommentarer från kolumn A1 genom att läsa in [provexemplet Excel-filen](89849861.xlsx). Se konsolens utdata som genererats av koden för referens.  

#### **Exempelkod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data"); // Adjust as necessary

const filePath = path.join(sourceDir, "ThreadedCommentsSample.xlsx");

// Loads the workbook which contains threaded comments
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get Threaded Comments
const threadedComments = worksheet.getComments().getThreadedComments("A1");

const count = threadedComments.getCount();
for (let i = 0; i < count; i++) {
const comment = threadedComments.get(i);
console.log("Comment: " + comment.getNotes());
console.log("Author: " + comment.getAuthor().getName());
}
```  

#### **Konsoloutput**  

{{< highlight javascript >}}  

Comment: Test Threaded Comment  

Author: Aspose Test  

{{< /highlight >}}  

### **Läs skapad tid för trådade kommentarer**  

Aspose.Cells tillhandahåller [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-)-metoden för att hämta trådade kommentarer för angiven kolumn. [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-)-metoden accepterar kolumnnamn som parameter och returnerar [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection). Du kan iterera över [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) och använda [**ThreadedComment.getCreatedTime()**](https://reference.aspose.com/cells/nodejs-cpp/threadedcomment/#getCreatedTime--)-egenskapen.  

Följande exempel visar hur man läser skapad tid för trådade kommentarer genom att läsa in [provexemplet Excel-filen](89849861.xlsx). Se konsolens utdata som genererats av koden för referens.  

#### **Exempelkod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const filePath = path.join(sourceDir, "ThreadedCommentsSample.xlsx");

// Loads the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get Threaded Comments
const threadedComments = worksheet.getComments().getThreadedComments("A1");

const count = threadedComments.getCount();

for (let i = 0; i < count; i++) {
const comment = threadedComments.get(i);
console.log("Comment: " + comment.getNotes());
console.log("Author: " + comment.getAuthor().getName());
console.log("Created Time: " + comment.getCreatedTime());
}
```  

#### **Konsoloutput**  

{{< highlight javascript >}}  

Comment: Test Threaded Comment  

Author: Aspose Test  

Created Time: 5/15/2019 12:46:23 PM  

{{< /highlight >}}  

## **Redigera trådade kommentarer**  

### **Redigera trådad kommentar med Excel**  

För att redigera en trådad kommentar i Excel, klicka på länken **Redigera** i kommentaren enligt bilden nedan.  

![todo:image_alt_text](threaded-comments_7.jpg)  

### **Redigera trådad kommentar med hjälp av Aspose.Cells**  

Aspose.Cells tillhandahåller [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-)-metoden för att hämta trådade kommentarer för angiven kolumn. [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-)-metoden accepterar kolumnnamn som parameter och returnerar [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection). Du kan uppdatera den nödvändiga kommentaren i [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) och spara arbetsboken.  

Följande exempel visar redigering av den första trådade kommentaren i kolumn A1 genom att ladda den [Exempel på Excel-fil](89849861.xlsx). Se också den [utdata av Excel-filen](89849862.xlsx) som genererats av koden och visar den uppdaterade kommentaren för referens.  

#### **Exempelkod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source and output directories
const sourceDir = path.join(__dirname, "data");
const outDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "ThreadedCommentsSample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get Threaded Comment
const comment = worksheet.getComments().getThreadedComments("A1").get(0);
comment.setNotes("Updated Comment");

workbook.save(outDir + "EditThreadedComments.xlsx");
```  

## **Ta bort trådade kommentarer**  

### **Ta bort trådade kommentarer med Excel**  

För att ta bort trådade kommentarer i Excel, högerklicka på cellen som innehåller kommentarerna och välj alternativet **Radera kommentar** enligt bilden nedan.  

![todo:image_alt_text](threaded-comments_8.jpg)   


