---
title: Kopiera rader och kolumner
type: docs
weight: 30
url: /sv/java/copying-rows-and-columns/
---

## **Introduktion**
Ibland behöver du kopiera rader och kolumner i en arbetsbok utan att kopiera hela arbetsboken. Med Aspose.Cells är det möjligt att kopiera rader och kolumner inom eller mellan arbetsböcker.

När en rad (eller kolumn) kopieras, kopieras också den data som finns i den, inklusive formler - med uppdaterade referenser - och värden, kommentarer, formatering, dolda celler, bilder och andra ritobjekt.
## **Kopiera rader och kolumner med Microsoft Excel**
1. Markera raden eller kolumnen som du vill kopiera.
1. För att kopiera rader eller kolumner, klicka på **Kopiera** på **Standard** verktygsfältet, eller tryck på **CTRL**+**C**.
1. Välj en rad eller en kolumn nedanför eller till höger om där du vill kopiera ditt val.
1. När du kopierar rader eller kolumner, klicka på **Kopierade celler** på menyn **Infoga**.

{{% alert color="primary" %}} 

Om du klickar på **Klistra in** på **Standard** verktygsfältet eller trycker på **CTRL**+**V** istället för att klicka på en kommando i **Infoga** menyn, ersätts eventuella innehåll i destinationens celler.

{{% /alert %}} 

## **Kopiera enstaka rad**

Aspose.Cells tillhandahåller [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) metoden från [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) klassen. Denna metod kopierar alla typer av data inklusive formler, värden, kommentarer, cellformat, dolda celler, bilder och andra ritobjekt från källraden till destinationsraden.

Metoden [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) tar följande parametrar:

- käll [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) objekt,
- källradens index, och
- destinationsradens index.

Använd denna metod för att kopiera en rad inom ett blad, eller till ett annat blad. [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) metoden fungerar på ett liknande sätt som Microsoft Excel. Så, till exempel, behöver du inte sätta höjden på destinationsraden explcit, det värdet kopieras också.

Följande exempel visar hur man kopierar en rad i en arbetsbok. Det använder en mall Microsoft Excel-fil och kopierar den andra raden (komplett med data, formatering, kommentarer, bilder och så vidare) och klistrar in den i den 12:e raden i samma arbetsbok.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingRows-CopyingRows.java" >}}



Följande utdata genereras när koden nedan körs.

**Raderna kopieras med högsta möjliga precision och noggrannhet** 

![todo:image_alt_text](copying-rows-and-columns_1.png)

{{% alert color="primary" %}} 

Vid kopiering av rader är det viktigt att notera relaterade bilder, diagram eller andra ritobjekt eftersom detta är detsamma med Microsoft Excel:

1. Om källradens index är 5, kopieras bilden, diagrammet osv. om den finns i de tre raderna (startindexet är 4 och slutindexet är 6).
1. De befintliga bilderna, diagrammen osv. i destinationsraden kommer inte att tas bort.

{{% /alert %}} 

## **Kopiera flera rader**

Du kan också kopiera flera rader till en ny destination samtidigt som du använder [**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int))-metoden som tar en ytterligare parameter av typ integer för att ange antalet källrader som ska kopieras.

Här är en ögonblicksbild av den inmatade kalkylarket som innehåller 3 rader med data medan kodsnutten nedan kopierar alla 3 rader till en ny plats som startar från den 7: e raden.

![todo:image_alt_text](copy-rows-and-columns_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleRows-CopyingMultipleRows.java" >}}

Här är den resulterande kalkylarksvisningen efter att ha kört kodsnutten ovan.

![todo:image_alt_text](copy-rows-and-columns_4.png)

## **Kopiera enstaka kolumn**

Aspose.Cells tillhandahåller [copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) metoden i [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) klassen, denna metod kopierar alla typer av data, inklusive formler - med uppdaterade referenser - och värden, kommentarer, cellformat, dolda celler, bilder och andra ritobjekt från källkolumnen till destinationskolumnen.

[copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) metoden tar följande parametrar:

- käll [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) objekt,
- källkolumnens index och
- destinationskolumnens index.

Använd [copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) metoden för att kopiera en kolumn i en kalkylblad eller till ett annat kalkylblad.

Detta exempel kopierar en kolumn från ett blad och klistrar in den i ett blad i en annan arbetsbok.

**En kolumn kopieras från en arbetsbok till en annan** 

![todo:image_alt_text](copying-rows-and-columns_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingColumns-CopyingColumns.java" >}}

## **Kopiera flera kolumner**

På liknande sätt som [**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int))-metoden tillhandahåller också Aspose.Cells API:er metoden [**Cells.copyColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns(com.aspose.cells.Cells,%20int,%20int,%20int)) för att kopiera flera källkolumner till en ny plats.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleColumns-CopyingMultipleColumns.java" >}}

Så här ser käll- och resulterande kalkylarken ut i Excel.

![todo:image_alt_text](copy-rows-and-columns_7.png)

![todo:image_alt_text](copy-rows-and-columns_8.png)


## **Klistra in rader/kolumner med klistralternativ**
Aspose.Cells tillhandahåller nu [PasteOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PasteOptions) när du använder funktioner [CopyRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRows\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.CopyOptions,%20com.aspose.cells.PasteOptions\)) och [CopyColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.PasteOptions\)). Det tillåter att ställa in lämpliga klistralternativ liknande Excel.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-PastingDataWithPasteOptions.java" >}}

