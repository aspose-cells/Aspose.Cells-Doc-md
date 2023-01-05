---
title: Trådade kommentarer
type: docs
weight: 140
url: /sv/java/threaded-comments/
---
# **Trådade kommentarer**
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
 - Klicka på**Recension**Flik
 - Klicka på**Ny kommentar**knapp
 - Detta öppnar en dialog för att skriva kommentarer i den aktiva cellen.
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- Metod 2
 - Högerklicka på cellen där du vill infoga kommentaren.
 - Klicka på**Ny kommentar**alternativ.
 - Detta öppnar en dialog för att skriva kommentarer i den aktiva cellen.
  - ![todo:image_alt_text](threaded-comments_5)
### **Lägg till trådad kommentar med Aspose.Cells**
Aspose.Cells tillhandahåller[Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) metod för att lägga till trådade kommentarer[Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) metod accepterar följande tre parametrar.

- Cell Namn: Namnet på cellen där kommentaren kommer att infogas.
- Kommentarstext: Texten i kommentaren.
- [Trådad kommentar Författare](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentAuthor): Författaren till kommentaren

Följande kodexempel visar användningen av[Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) metod för att lägga till trådad kommentar till cell A1. Vänligen se[utdata Excel-fil](AddThreadedComments_out.xlsx)genereras av koden för referens.
#### **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddThreadedComments-1.java" >}}
## **Läs trådade kommentarer**
### **Läs trådade kommentarer med Excel**
För att läsa trådade kommentarer i Excel, håll helt enkelt muspekaren över cellen som innehåller kommentarerna för att se kommentarerna. Kommentarsvyn kommer att se ut som vyn i följande bild.

![todo:image_alt_text](threaded-comments_1.jpg)
### **Läs trådade kommentarer med Aspose.Cells**
Aspose.Cells tillhandahåller[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) metod för att hämta trådade kommentarer för den angivna kolumnen.[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\))-metoden accepterar kolumnnamnet som en parameter och returnerar[ThreadedComment Collection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Du kan iterera över[ThreadedComment Collection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)för att se kommentarerna.

Följande exempel visar att du läser kommentarer från kolumn A1 genom att ladda[exempel på Excel-fil](ThreadedCommentsSample.xlsx). Se konsolutgången som genereras av koden för referens.
#### **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedComments-1.java" >}}
#### **Konsolutgång**
Kommentar: Testtrådad kommentar

Författare: Aspose Test
### **Läs Skapade tid för trådade kommentarer**
Aspose.Cells tillhandahåller[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) metod för att hämta trådade kommentarer för den angivna kolumnen.[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\))-metoden accepterar kolumnnamnet som en parameter och returnerar[ThreadedComment Collection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Du kan iterera över[ThreadedComment Collection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)och använda[ThreadedComment.CreatedTime](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcomment#CreatedTime)fast egendom.

Följande exempel visar att du läser den skapade tiden för trådade kommentarer genom att ladda[exempel på Excel-fil](ThreadedCommentsSample.xlsx). Se konsolutgången som genereras av koden för referens.
#### **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedCommentCreatedTime-1.java" >}}
#### **Konsolutgång**
Kommentar: Testtrådad kommentar

Författare: Aspose Test

Skapat tid: 2019-05-15T12:46:23
## **Redigera trådade kommentarer**
### **Redigera trådad kommentar med Excel**
För att redigera en trådad kommentar i Excel, klicka på**Redigera**länk på kommentaren som visas i följande bild.

![todo:image_alt_text](threaded-comments_7.jpg)
### **Redigera trådad kommentar med Aspose.Cells**
Aspose.Cells tillhandahåller[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) metod för att hämta trådade kommentarer för den angivna kolumnen.[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\))-metoden accepterar kolumnnamnet som en parameter och returnerar[ThreadedComment Collection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Du kan uppdatera den önskade kommentaren i[ThreadedComment Collection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)och spara arbetsboken.

Följande exempel visar redigering av den första trådade kommentaren i kolumn A1 genom att ladda[exempel på Excel-fil](ThreadedCommentsSample.xlsx). Vänligen se[utdata Excel-fil](EditThreadedComments.xlsx)genereras av koden som visar den uppdaterade kommentaren som referens.
#### **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "EditThreadedComments-1.java" >}}
## **Ta bort trådade kommentarer**
### **Ta bort trådade kommentarer med Excel**
För att ta bort trådade kommentarer i Excel, högerklicka på cellen som innehåller kommentarerna och klicka på**Ta bort kommentar**alternativ som visas i följande bild.

![todo:image_alt_text](threaded-comments_8.jpg)
### **Ta bort trådade kommentarer med Aspose.Cells**
Aspose.Cells tillhandahåller[Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt\(int\)) metod för att ta bort kommentarer för den angivna kolumnen.[Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt\(int\)) metod accepterar kolumnnamnet eftersom en parameter tar bort kommentarerna i den kolumnen.

Följande exempel visar hur du tar bort kommentarer i kolumn A1 genom att ladda[exempel på Excel-fil](ThreadedCommentsSample.xlsx). Vänligen se[utdata Excel-fil](ThreadedCommentsSample_Out.xlsx)genereras av koden för referens.
#### **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "RemoveThreadedComments-1.java" >}}

{{% alert color="primary" %}} 

 Observera att genom att ta bort kommentar med Aspose.Cells tas författaren inte bort automatiskt. Om du också behöver ta bort författaren, använd[ThreadedCommentAuthorCollection.removeAt](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcommentauthorcollection#removeAt\(int\)metod som visas i exemplet ovan.

{{% /alert %}}
