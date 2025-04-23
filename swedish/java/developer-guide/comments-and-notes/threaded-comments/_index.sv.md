---
title: Trådade kommentarer
type: docs
weight: 140
url: /sv/java/threaded-comments/
---

# **Trådade Kommentarer**
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
  - Klicka på **Ny kommentar** alternativet.
  - Detta kommer att öppna en dialogruta för att ange kommentarer i den aktiva cellen.
  - ![todo:image_alt_text](threaded-comments_5)
### **Lägg till trådad kommentar med hjälp av Aspose.Cells**
Aspose.Cells tillhandahåller [Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment-java.lang.String-java.lang.String-com.aspose.cells.ThreadedCommentAuthor-) metod för att lägga till trådade kommentarer. [Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment-java.lang.String-java.lang.String-com.aspose.cells.ThreadedCommentAuthor-) accepterar följande tre parametrar.

- Cell namn: Namnet på cellen där kommentaren ska infogas.
- Kommentartext: Kommentarens innehåll.
- [ThreadedCommentAuthor](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentAuthor): Författaren till kommentaren

Följande kodexempel visar användningen av [Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment-java.lang.String-java.lang.String-com.aspose.cells.ThreadedCommentAuthor-) för att lägga till en trådad kommentar i cell A1. Se den [utdata Excel-filen](AddThreadedComments_out.xlsx) som genererats av koden för referens.
#### **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddThreadedComments-1.java" >}}
## **Läs trådade kommentarer**
### **Läs trådade kommentarer med Excel**
För att läsa trådade kommentarer i Excel, svep helt enkelt musen över cellen som innehåller kommentarerna för att visa kommentarerna. Kommentarerna kommer att se ut som i följande bild.

![todo:image_alt_text](threaded-comments_1.jpg)
### **Läs trådade kommentarer med Aspose.Cells**
Aspose.Cells tillhandahåller [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) metod för att hämta trådade kommentarer för den angivna kolumnen. [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) tar emot kolumnnamnet som parameter och returnerar [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Du kan iterera över [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection) för att se kommentarerna.

Följande exempel demonstrerar läsning av kommentarer från kolumn A1 genom att ladda den [prov Excel-fil](ThreadedCommentsSample.xlsx). Vänligen se konsolens utdata genererad av koden för referens.
#### **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedComments-1.java" >}}
#### **Konsoloutput**

{{< highlight java >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Läs skapad tid för trådade kommentarer**
Aspose.Cells tillhandahåller [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) metod för att hämta trådade kommentarer för den angivna kolumnen. [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) tar emot kolumnnamnet som parameter och returnerar [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Du kan iterera över [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection) och använda egenskapen [ThreadedComment.CreatedTime](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcomment#CreatedTime).

Följande exempel demonstrerar läsning av skapad tid för trådade kommentarer genom att ladda den [prov Excel-fil](ThreadedCommentsSample.xlsx). Vänligen se konsolens utdata genererad av koden för referens.
#### **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedCommentCreatedTime-1.java" >}}
#### **Konsoloutput**

{{< highlight java >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 2019-05-15T12:46:23

{{< /highlight >}}

## **Redigera trådade kommentarer**
### **Redigera trådad kommentar med Excel**
För att redigera en trådad kommentar i Excel, klicka på **Redigera** länken på kommentaren enligt följande bild.

![todo:image_alt_text](threaded-comments_7.jpg)
### **Redigera trådad kommentar med hjälp av Aspose.Cells**
Aspose.Cells tillhandahåller [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) metod för att hämta trådade kommentarer för den angivna kolumnen. [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) tar emot kolumnnamnet som parameter och returnerar [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Du kan uppdatera den nödvändiga kommentaren i [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection) och spara arbetsboken.

Följande exempel demonstrerar redigering av den första trådade kommentaren i kolumn A1 genom att ladda den [prov Excel-fil](ThreadedCommentsSample.xlsx). Vänligen se den [utdata Excel-fil](EditThreadedComments.xlsx) genererad av koden som visar den uppdaterade kommentaren för referens.
#### **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "EditThreadedComments-1.java" >}}
## **Ta bort trådade kommentarer**
### **Ta bort trådade kommentarer med Excel**
För att ta bort trådade kommentarer i Excel, högerklicka på cellen som innehåller kommentarerna och klicka på **Radera kommentar** alternativet enligt följande bild.

![todo:image_alt_text](threaded-comments_8.jpg)
### **Ta bort trådade kommentarer med hjälp av Aspose.Cells**
Aspose.Cells tillhandahåller [Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt-int-) metod för att ta bort kommentarer för den angivna kolumnen. [Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt-int-) tar emot kolumnnamnet som parameter och tar bort kommentarerna i den kolumnen. 

Följande exempel demonstrerar borttagning av kommentarer i kolumn A1 genom att ladda den [prov Excel-fil](ThreadedCommentsSample.xlsx). Vänligen se den [utdata Excel-fil](ThreadedCommentsSample_Out.xlsx) genererad av koden för referens.
#### **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "RemoveThreadedComments-1.java" >}}

{{% alert color="primary" %}} 

Observera att genom att ta bort en kommentar med Aspose.Cells, tas inte författaren bort automatiskt. Om du behöver ta bort författaren också, använd då [ThreadedCommentAuthorCollection.removeAt](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcommentauthorcollection#removeAt-int-) metod som visas i exemplet ovan.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
