---
title: Kopiera rader och kolumner
type: docs
weight: 30
url: /sv/java/copying-rows-and-columns/
---
## **Introduktion**
Ibland måste du kopiera rader och kolumner i ett kalkylblad utan att kopiera hela kalkylbladet. Med Aspose.Cells är det möjligt att kopiera rader och kolumner inom eller mellan arbetsböcker.

När en rad (eller kolumn) kopieras, kopieras även data som finns i den, inklusive formler - med uppdaterade referenser - och värden, kommentarer, formatering, dolda celler, bilder och andra ritobjekt.
## **Kopiera rader och kolumner med Microsoft Excel**
1. Välj den rad eller kolumn som du vill kopiera.
1.  För att kopiera rader eller kolumner, klicka**Kopiera** på**Standard** verktygsfältet eller tryck på**CTRL**+**C**.
1. Välj en rad eller kolumn nedan eller till höger om var du vill kopiera ditt val.
1.  Klicka på när du kopierar rader eller kolumner**Kopierat Cells** på**Föra in** meny.

{{% alert color="primary" %}} 

 Om du klickar**Klistra** på**Standard** verktygsfältet eller tryck**CTRL**+** V** istället för att klicka på ett kommando på**Insert**-menyn, allt innehåll i destinationscellerna ersätts.

{{% /alert %}} 

## **Kopiera en rad**

 Aspose.Cells tillhandahåller[copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\) ) metod för[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)klass. Denna metod kopierar alla typer av data inklusive formler, värden, kommentarer, cellformat, dolda celler, bilder och andra ritobjekt från källraden till målraden.

 De[copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) metod tar följande parametrar:

-  källan[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)objekt,
- källradens index, och
- destinationsradindex.

 Använd den här metoden för att kopiera en rad i ett ark eller till ett annat ark. De[copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\))-metoden fungerar på liknande sätt som Microsoft Excel. Så, till exempel, behöver du inte ställa in höjden på destinationsraden explicit, det värdet kopieras också.

Följande exempel visar hur man kopierar en rad i ett kalkylblad. Den använder en mall Microsoft Excel-fil och kopierar den andra raden (komplett med data, formatering, kommentarer, bilder och så vidare) och klistra in den på den 12:e raden i samma kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingRows-CopyingRows.java" >}}



Följande utdata genereras när koden nedan exekveras.

**Raden kopieras med högsta grad av precision och noggrannhet** 

![todo:image_alt_text](copying-rows-and-columns_1.png)

{{% alert color="primary" %}} 

När du kopierar rader är det viktigt att notera relaterade bilder, diagram eller andra ritobjekt eftersom detta är samma sak med Microsoft Excel:

1. Om källradens index är 5, kopieras bilden, diagrammet etc. om det finns i de tre raderna (startradindex är 4 och slutradens index är 6).
1. De befintliga bilderna, sjökorten etc. på destinationsraden kommer inte att tas bort.

{{% /alert %}} 

## **Kopiera flera rader**

 Du kan också kopiera flera rader till en ny destination medan du använder[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int)) metod som tar en extra parameter av typen heltal för att specificera antalet källrader som ska kopieras.

Nedan är en ögonblicksbild av kalkylarket som innehåller 3 rader med data, medan kodavsnittet nedan kopierar alla 3 raderna till en ny plats från 7:e raden.

![todo:image_alt_text](copy-rows-and-columns_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleRows-CopyingMultipleRows.java" >}}

Här är den resulterande kalkylbladsvyn efter exekvering av ovanstående kodavsnitt.

![todo:image_alt_text](copy-rows-and-columns_4.png)

## **Kopiera en kolumn**

 Aspose.Cells tillhandahåller[copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\) ) metod för[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)klass, kopierar denna metod alla typer av data, inklusive formler - med uppdaterade referenser - och värden, kommentarer, cellformat, dolda celler, bilder och andra ritobjekt från källkolumnen till målkolumnen.

 De[copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) metod tar följande parametrar:

-  källan[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)objekt,
- källkolumnindex och
- målkolumnindex.

 Använd[copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) metod för att kopiera en kolumn inom ett ark eller till ett annat ark.

Det här exemplet kopierar en kolumn från ett kalkylblad och klistrar in den i ett kalkylblad i en annan arbetsbok.

**En kolumn kopieras från en arbetsbok till en annan** 

![todo:image_alt_text](copying-rows-and-columns_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingColumns-CopyingColumns.java" >}}

## **Kopiera flera kolumner**

 Liknande[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int) )-metoden tillhandahåller API:erna Aspose.Cells också[**Cells.copyColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns(com.aspose.cells.Cells,%20int,%20int,%20int)) för att kopiera flera källkolumner till en ny plats.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleColumns-CopyingMultipleColumns.java" >}}

Så här ser källblad och kalkylblad ut i Excel.

![todo:image_alt_text](copy-rows-and-columns_7.png)

![todo:image_alt_text](copy-rows-and-columns_8.png)


## **Klistra in rader/kolumner med inklistringsalternativ**
 Aspose.Cells ger nu[Klistra in Alternativ](https://reference.aspose.com/cells/java/com.aspose.cells/PasteOptions) när du använder funktioner[CopyRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRows\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.CopyOptions,%20com.aspose.cells.PasteOptions\) ) och[CopyColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.PasteOptions\)). Det gör det möjligt att ställa in lämpliga inklistringsalternativ liknande Excel.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-PastingDataWithPasteOptions.java" >}}

