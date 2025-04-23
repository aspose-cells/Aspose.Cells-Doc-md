---
title: Trådade kommentarer
type: docs
weight: 140
url: /sv/python-net/threaded-comments/
---

## **Trådade Kommentarer**

MS Excel 365 ger en funktion för att lägga till trådade kommentarer. Dessa kommentarer fungerar som konversationer och kan användas för diskussioner. Kommentarerna levereras nu med en svarsruta som möjliggör trådade konversationer. De gamla kommentarerna kallas anteckningar i Excel 365. Skärmavbildningen nedan visar hur trådade kommentarer visas när de öppnas i Excel.

![todo:image_alt_text](threaded-comments_1.jpg)

Trådade kommentarer visas så här i äldre versioner av Excel. Följande bilder har tagits genom att öppna provfilen i Excel 2016.

![todo:image_alt_text](threaded-comments_2.jpg)

![todo:image_alt_text](threaded-comments_3.jpg)

Aspose.Cells för Python via .NET erbjuder också funktionen att hantera trådade kommentarer.

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

### **Lägg till trådad kommentar med Aspose.Cells för Python via .NET**

Aspose.Cells för Python via .NET tillhandahåller [**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment/)-metoden för att lägga till trådade kommentarer. [**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment)-metoden accepterar följande tre parametrar.

- Cell namn: Namnet på cellen där kommentaren ska infogas.
- Kommentartext: Kommentarens innehåll.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentauthor): Kommentarens författare

Följande kodexempel visar användningen av [**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment)-metoden för att lägga till trådad kommentar till cell A1. Se den [utdata Excel-filen](89849859.xlsx) som genererats av koden för referens.

#### **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-AddThreadedComments-1.py" >}}

## **Läs trådade kommentarer**

### **Läs trådade kommentarer med Excel**

För att läsa trådade kommentarer i Excel, svep helt enkelt musen över cellen som innehåller kommentarerna för att visa kommentarerna. Kommentarerna kommer att se ut som i följande bild.

![todo:image_alt_text](threaded-comments_1.jpg)

### **Läs trådade kommentarer med Aspose.Cells för Python via .NET**

Aspose.Cells för Python via .NET tillhandahåller [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments)-metoden för att hämta trådade kommentarer för den angivna kolumnen. [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments)-metoden accepterar kolumnnamnet som parameter och returnerar [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection). Du kan iterera över [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) för att se kommentarerna.

Följande exempel visar hur man läser kommentarer från kolumn A1 genom att läsa in [provexemplet Excel-filen](89849861.xlsx). Se konsolens utdata som genererats av koden för referens.

#### **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-ReadThreadedComments-1.py" >}}

#### **Konsoloutput**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Läs skapad tid för trådade kommentarer**

Aspose.Cells för Python via .NET tillhandahåller [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments)-metoden för att hämta trådade kommentarer för den angivna kolumnen. [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments)-metoden accepterar kolumnnamnet som parameter och returnerar [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection). Du kan iterera över [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) och använda [**ThreadedComment.created_time**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcomment/created_time)-egenskapen.

Följande exempel visar hur man läser skapad tid för trådade kommentarer genom att läsa in [provexemplet Excel-filen](89849861.xlsx). Se konsolens utdata som genererats av koden för referens.

#### **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-ReadThreadedCommentCreatedTime-1.py" >}}

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

### **Redigera trådad kommentar med Aspose.Cells för Python via .NET**

Aspose.Cells för Python via .NET tillhandahåller [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments)-metoden för att hämta trådade kommentarer för den angivna kolumnen. [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments)-metoden accepterar kolumnnamnet som parameter och returnerar [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection). Du kan uppdatera den önskade kommentaren i [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) och spara arbetsboken.

Följande exempel visar redigering av den första trådade kommentaren i kolumn A1 genom att ladda den [Exempel på Excel-fil](89849861.xlsx). Se också den [utdata av Excel-filen](89849862.xlsx) som genererats av koden och visar den uppdaterade kommentaren för referens.

#### **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-EditThreadedComments-1.py" >}}

