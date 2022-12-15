---
title: Kopiera rader och kolumner
type: docs
weight: 40
url: /sv/net/copying-rows-and-columns/
---
## **Introduktion**

Ibland måste du kopiera rader och kolumner i ett kalkylblad utan att kopiera hela kalkylbladet. Med Aspose.Cells är det möjligt att kopiera rader och kolumner inom eller mellan arbetsböcker.
När en rad (eller kolumn) kopieras, kopieras även data som finns i den, inklusive formler - med uppdaterade referenser - och värden, kommentarer, formatering, dolda celler, bilder och andra ritobjekt.

## **Kopiera rader och kolumner med Microsoft Excel**

1. Välj den rad eller kolumn som du vill kopiera.
1.  Klicka på för att kopiera rader eller kolumner**Kopiera** på**Standard** verktygsfältet eller tryck på**CTRL**+**C**.
1. Välj en rad eller kolumn nedan eller till höger om var du vill kopiera ditt val.
1.  Klicka på när du kopierar rader eller kolumner**Kopierat Cells** på**Föra in** meny.

{{% alert color="primary" %}}

 Om du klickar**Klistra** på**Standard** verktygsfältet eller tryck**CTRL**+** V** istället för att klicka på ett kommando på**Insert**-menyn, allt innehåll i destinationscellerna ersätts.

{{% /alert %}}

## **Klistra in rader och kolumner med inklistringsalternativ med Microsoft Excel**

1. Markera cellerna som innehåller data eller andra attribut som du vill kopiera.
1.  Klicka på fliken Hem**Kopiera**.
1.  Klicka på den första cellen i området där du vill**klistra** vad du kopierade.
1.  Klicka på pilen bredvid på fliken Hem**Klistra** , och välj sedan**Klistra** Särskild.
1.  Välj**alternativ** du vill.

## **Använder Aspose.Cells**

## **Kopiera enstaka rader**

 Aspose.Cells tillhandahåller[**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) metod för[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)klass. Denna metod kopierar alla typer av data inklusive formler, värden, kommentarer, cellformat, dolda celler, bilder och andra ritobjekt från källraden till målraden.

 De[**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)metoden tar följande parametrar:

-  källan[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)objekt,
- källradens index, och
- destinationsradindex.

 Använd den här metoden för att kopiera en rad i ett ark eller till ett annat ark. De[**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)Metoden fungerar på liknande sätt som Microsoft Excel. Så, till exempel, behöver du inte ställa in höjden på destinationsraden explicit, det värdet kopieras också.

Följande exempel visar hur man kopierar en rad i ett kalkylblad. Den använder en mall Microsoft Excel-fil och kopierar den andra raden (komplett med data, formatering, kommentarer, bilder och så vidare) och klistra in den på den 12:e raden i samma kalkylblad.

 Du kan hoppa över steget som får källradens höjd med hjälp av[**Cells.GetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getrowheight) metod och ställer sedan in destinationsradens höjd med hjälp av[**Cells.SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) metod som[**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)metod tar automatiskt hand om radhöjden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingRows-1.cs" >}}

{{% alert color="primary" %}}

När du kopierar rader är det viktigt att notera relaterade bilder, diagram eller andra ritobjekt eftersom detta är samma sak med Microsoft Excel:

1. Om källradens index är 5, kopieras bilden, diagrammet etc. om det finns i de tre raderna (startradindex är 4 och slutradens index är 6).
1. De befintliga bilderna, sjökorten etc. på destinationsraden kommer inte att tas bort.

{{% /alert %}}

## **Kopiera flera rader**

Du kan också kopiera flera rader till en ny destination medan du använder[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)metod som tar en extra parameter av typen heltal för att specificera antalet källrader som ska kopieras.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}


## **Kopiera kolumner**

 Aspose.Cells tillhandahåller[**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) metod för[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)klass, kopierar denna metod alla typer av data, inklusive formler - med uppdaterade referenser - och värden, kommentarer, cellformat, dolda celler, bilder och andra ritobjekt från källkolumnen till målkolumnen.

 De[**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)metoden tar följande parametrar:

-  källan[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)objekt,
- källkolumnindex och
- målkolumnindex.

 Använd[**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)metod för att kopiera en kolumn inom ett ark eller till ett annat ark.

Det här exemplet kopierar en kolumn från ett kalkylblad och klistrar in den i ett kalkylblad i en annan arbetsbok.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingColumns-1.cs" >}}

## **Kopiera flera kolumner**

 Liknande[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) Aspose.Cells API:er tillhandahåller också[**Cells.CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index)metod för att kopiera flera källkolumner till en ny plats.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}


## **Klistra in rader/kolumner med inklistringsalternativ**

 Aspose.Cells ger nu[**Klistra in Alternativ**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions) när du använder funktioner[**CopyRows**](https://reference.aspose.com/cells/net/aspose.cells.cells/copyrows/methods/2) och[**CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells.cells/copycolumns/methods/1). Det gör det möjligt att ställa in lämpligt inklistringsalternativ som liknar Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.cs" >}}

