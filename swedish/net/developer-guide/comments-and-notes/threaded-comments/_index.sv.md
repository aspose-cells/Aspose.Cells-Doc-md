---
title: Trådade kommentarer
type: docs
weight: 140
url: /sv/net/threaded-comments/
---
## **Trådade kommentarer**

MS Excel 365 har en funktion för att lägga till trådade kommentarer. Dessa kommentarer fungerar som konversationer och kan användas för diskussioner. Kommentarerna kommer nu med en svarsruta som tillåter trådade konversationer. De gamla kommentarerna heter Notes i Excel 365. Skärmdumpen nedan visar hur trådade kommentarer visas när de öppnas i Excel.

![todo:image_alt_text](threaded-comments_1.jpg)

Trådade kommentarer visas så här i äldre versioner av Excel. Följande bilder har tagits genom att öppna exempelfilen i Excel 2016.

![todo:image_alt_text](threaded-comments_2.jpg)

![todo:image_alt_text](threaded-comments_3.jpg)

Aspose.Cells tillhandahåller också funktionen för att hantera trådade kommentarer.

## **Lägg till trådade kommentarer**

### **Lägg till trådad kommentar med Excel**

För att lägga till trådade kommentarer i Excel 365, följ följande steg.

- Metod 1
 - Klicka på**Recension** Flik
 - Klicka på**Ny kommentar** knapp
 - Detta öppnar en dialog för att skriva kommentarer i den aktiva cellen.
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- Metod 2
 - Högerklicka på cellen där du vill infoga kommentaren.
 - Klicka på**Ny kommentar** alternativ.
 - Detta öppnar en dialog för att skriva kommentarer i den aktiva cellen.
  - ![todo:image_alt_text](threaded-comments_5)

### **Lägg till trådad kommentar med Aspose.Cells**

Aspose.Cells tillhandahåller[**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) metod för att lägga till trådade kommentarer[**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1)metoden accepterar följande tre parametrar.

- Cell Namn: Namnet på cellen där kommentaren kommer att infogas.
- Kommentarstext: Texten i kommentaren.
- [**Trådad kommentar Författare**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthor): Författaren till kommentaren

Följande kodexempel visar användningen av[**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1)metod för att lägga till trådad kommentar till cell A1. Vänligen se[utdata Excel-fil](89849859.xlsx) genereras av koden för referens.

#### **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-AddThreadedComments-1.cs" >}}

## **Läs trådade kommentarer**

### **Läs trådade kommentarer med Excel**

För att läsa trådade kommentarer i Excel, håll helt enkelt muspekaren över cellen som innehåller kommentarerna för att se kommentarerna. Kommentarsvyn kommer att se ut som vyn i följande bild.

![todo:image_alt_text](threaded-comments_1.jpg)

### **Läs trådade kommentarer med Aspose.Cells**

Aspose.Cells tillhandahåller[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)metod för att hämta trådade kommentarer för den angivna kolumnen.[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)metoden accepterar kolumnnamnet som en parameter och returnerar[**ThreadedComment Collection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). Du kan iterera över[**ThreadedComment Collection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection)för att se kommentarerna.

Följande exempel visar att du läser kommentarer från kolumn A1 genom att ladda[exempel på Excel-fil](89849861.xlsx). Se konsolutgången som genereras av koden för referens.

#### **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedComments-1.cs" >}}

#### **Konsolutgång**

Kommentar: Testtrådad kommentar

Författare: Aspose Test

### **Läs Skapade tid för trådade kommentarer**

Aspose.Cells tillhandahåller[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)metod för att hämta trådade kommentarer för den angivna kolumnen.[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)metoden accepterar kolumnnamnet som en parameter och returnerar[**ThreadedComment Collection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). Du kan iterera över[**ThreadedComment Collection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) och använda[**ThreadedComment.CreatedTime**](https://reference.aspose.com/cells/net/aspose.cells/threadedcomment/properties/createdtime) fast egendom.

Följande exempel visar att du läser den skapade tiden för trådade kommentarer genom att ladda[exempel på Excel-fil](89849861.xlsx). Se konsolutgången som genereras av koden för referens.

#### **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedCommentCreatedTime-1.cs" >}}

#### **Konsolutgång**

Kommentar: Testtrådad kommentar

Författare: Aspose Test

Skapat tid: 15/5/2019 12:46:23

## **Redigera trådade kommentarer**

### **Redigera trådad kommentar med Excel**

 För att redigera en trådad kommentar i Excel, klicka på**Redigera** länk på kommentaren som visas i följande bild.

![todo:image_alt_text](threaded-comments_7.jpg)

### **Redigera trådad kommentar med Aspose.Cells**

Aspose.Cells tillhandahåller[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) metod för att hämta trådade kommentarer för den angivna kolumnen.[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)metoden accepterar kolumnnamnet som en parameter och returnerar[**ThreadedComment Collection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). Du kan uppdatera den önskade kommentaren i[**ThreadedComment Collection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection)och spara arbetsboken.

Följande exempel visar redigering av den första trådade kommentaren i kolumn A1 genom att ladda[exempel på Excel-fil](89849861.xlsx). Vänligen se[utdata Excel-fil](89849862.xlsx)genereras av koden som visar den uppdaterade kommentaren som referens.

#### **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-EditThreadedComments-1.cs" >}}

## **Ta bort trådade kommentarer**

### **Ta bort trådade kommentarer med Excel**

 För att ta bort trådade kommentarer i Excel, högerklicka på cellen som innehåller kommentarerna och klicka på**Ta bort kommentar** alternativ som visas i följande bild.

![todo:image_alt_text](threaded-comments_8.jpg)

### **Ta bort trådade kommentarer med Aspose.Cells**

Aspose.Cells tillhandahåller[**Comments.RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index)metod för att ta bort kommentarer för den angivna kolumnen.[**Comments.RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index)metod accepterar kolumnnamnet som en parameter tar bort kommentarerna i den kolumnen.

Följande exempel visar hur du tar bort kommentarer i kolumn A1 genom att ladda[exempel på Excel-fil](89849861.xlsx). Vänligen se[utdata Excel-fil](89849864.xlsx)genereras av koden för referens.

#### **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-RemoveThreadedComments-1.cs" >}}

{{% alert color="primary" %}}

 Observera att genom att ta bort kommentar med Aspose.Cells tas författaren inte bort automatiskt. Om du också behöver ta bort författaren, använd metoden RemoveAt för[**ThreadedCommentAuthorCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthorcollection) klass som visas i exemplet ovan.

{{% /alert %}}
