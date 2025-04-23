---
title: Trådade kommentarer
type: docs
weight: 140
url: /sv/net/threaded-comments/
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

Aspose.Cells tillhandahåller metoden [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) för att lägga till trådad kommentar. Metoden [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) accepterar följande tre parametrar.

- Cell namn: Namnet på cellen där kommentaren ska infogas.
- Kommentartext: Kommentarens innehåll.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthor): Kommentarens författare

Följande kodexempel visar användningen av [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1)-metoden för att lägga till trådad kommentar till cell A1. Se den [utdata Excel-filen](89849859.xlsx) som genererats av koden för referens.

#### **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-AddThreadedComments-1.cs" >}}

## **Läs trådade kommentarer**

### **Läs trådade kommentarer med Excel**

För att läsa trådade kommentarer i Excel, svep helt enkelt musen över cellen som innehåller kommentarerna för att visa kommentarerna. Kommentarerna kommer att se ut som i följande bild.

![todo:image_alt_text](threaded-comments_1.jpg)

### **Läs trådade kommentarer med Aspose.Cells**

Aspose.Cells tillhandahåller metoden [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) för att hämta trådade kommentarer för den angivna kolumnen. Metoden [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) tar kolumnnamnet som en parameter och returnerar [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). Du kan iterera över [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) för att visa kommentarerna.

Följande exempel visar hur man läser kommentarer från kolumn A1 genom att läsa in [provexemplet Excel-filen](89849861.xlsx). Se konsolens utdata som genererats av koden för referens.

#### **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedComments-1.cs" >}}

#### **Konsoloutput**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Läs skapad tid för trådade kommentarer**

Aspose.Cells tillhandahåller metoden [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) för att hämta trådad kommentar för den angivna kolumnen. Metoden [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) tar kolumnnamnet som en parameter och returnerar [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). Du kan iterera över [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) och använda egenskapen [**ThreadedComment.CreatedTime**](https://reference.aspose.com/cells/net/aspose.cells/threadedcomment/properties/createdtime).

Följande exempel visar hur man läser skapad tid för trådade kommentarer genom att läsa in [provexemplet Excel-filen](89849861.xlsx). Se konsolens utdata som genererats av koden för referens.

#### **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedCommentCreatedTime-1.cs" >}}

#### **Konsoloutput**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 5/15/2019 12:46:23 PM

{{< /highlight >}}

## **Redigera trådade kommentarer**

### **Redigera trådad kommentar med Excel**

För att redigera en trådad kommentar i Excel, klicka på länken **Redigera** i kommentaren enligt bilden nedan.

![todo:image_alt_text](threaded-comments_7.jpg)

### **Redigera trådad kommentar med hjälp av Aspose.Cells**

Aspose.Cells tillhandahåller [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) metod för att hämta trådade kommentarer för den angivna kolumnen. [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) metoden accepterar kolumnnamnet som en parameter och returnerar [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). Du kan uppdatera den kommentar du behöver i [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) och spara arbetsboken.

Följande exempel visar redigering av den första trådade kommentaren i kolumn A1 genom att ladda den [Exempel på Excel-fil](89849861.xlsx). Se också den [utdata av Excel-filen](89849862.xlsx) som genererats av koden och visar den uppdaterade kommentaren för referens.

#### **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-EditThreadedComments-1.cs" >}}

## **Ta bort trådade kommentarer**

### **Ta bort trådade kommentarer med Excel**

För att ta bort trådade kommentarer i Excel, högerklicka på cellen som innehåller kommentarerna och välj alternativet **Radera kommentar** enligt bilden nedan.

![todo:image_alt_text](threaded-comments_8.jpg)

### **Ta bort trådade kommentarer med hjälp av Aspose.Cells**

Aspose.Cells tillhandahåller [**Comments.RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index) metod för att ta bort kommentarer för den angivna kolumnen. [**Comments.RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index) metoden accepterar kolumnnamnet som en parameter och tar bort kommentarerna i den kolumnen.

Följande exempel visar borttagning av kommentarer i kolumn A1 genom att ladda den [Exempel på Excel-fil](89849861.xlsx). Se också den [utdata av Excel-filen](89849864.xlsx) som genererats av koden för referens.

#### **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-RemoveThreadedComments-1.cs" >}}

{{% alert color="primary" %}}

Observera att genom att ta bort kommentaren med Aspose.Cells tas inte författaren bort automatiskt. Om du behöver ta bort författaren också, använd RemoveAt-metoden i [**ThreadedCommentAuthorCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthorcollection) -klassen enligt exemplet ovan.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
