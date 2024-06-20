---
title: Kopiera rader och kolumner
type: docs
weight: 20
url: /sv/cpp/copying-rows-and-columns/
---

## **Introduktion**
Ibland behöver du kopiera rader och kolumner i ett arbetsblad utan att kopiera hela arbetsbladet. Med Aspose.Cells är det möjligt att kopiera rader och kolumner inom eller mellan arbetsböcker.
När en rad (eller kolumn) kopieras kopieras data som finns i den, inklusive formler - med uppdaterade referenser - och värden, kommentarer, formatering, dolda celler, bilder och andra ritobjekt också.
## **Kopiera rader och kolumner med Microsoft Excel**
1. Markera raden eller kolumnen som du vill kopiera.
1. För att kopiera rader eller kolumner, klicka på **Kopiera** på **Standard** verktygsfältet, eller tryck på **CTRL**+**C**.
1. Välj en rad eller en kolumn nedanför eller till höger om där du vill kopiera ditt val.
1. När du kopierar rader eller kolumner, klicka på **Kopierade celler** på menyn **Infoga**.

{{% alert color="primary" %}} 

Om du klickar på **Klistra in** på verktygsfältet **Standard** eller trycker på **CTRL**+**V** istället för att klicka på en kommando i menyn **Infoga**, ersätts eventuellt innehållet i destinationscellerna.

{{% /alert %}} 
## **Använda Aspose.Cells**
### **Kopiera rader**
Aspose.Cells tillhandahåller CopyRow-metoden i Aspose::Cells::ICells-klassen. Denna metod kopierar alla typer av data inklusive formler, värden, kommentarer, cellformat, dolda celler, bilder och andra ritobjekt från källraden till destinationsraden.

CopyRow-metoden tar följande parametrar:

- källans Cells-objekt,
- källradens index, och
- destinationsradens index.

Använd denna metod för att kopiera en rad inom ett blad eller till ett annat blad. CopyRow-metoden fungerar på ett liknande sätt som Microsoft Excel. Så, till exempel, behöver du inte ställa in höjden på destinationsraden explicit, det värdet kopieras också.

Exemplet nedan visar hur du kopierar en rad i en arbetsbok. Det använder en mall för Microsoft Excel-fil och kopierar den andra raden (komplett med data, formatering, kommentarer, bilder och så vidare) och klistrar in den i den 12: e raden i samma arbetsbok.

Du kan hoppa över steget som hämtar källradshöjden med hjälp av **GetRowHeigh**-metoden och sedan ställer in destinationsradens höjd med hjälp av **SetRowHeight**-metoden eftersom **CopyRow**-metoden automatiskt tar hand om radhöjden.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingRows-new.cpp" >}}

{{% alert color="primary" %}} 

När du kopierar rader är det viktigt att notera relaterade bilder, diagram eller andra ritobjekt eftersom det är detsamma som med Microsoft Excel:

1. Om källradindexet är 5 kopieras bilden, diagrammet osv., om det ingår i de tre raderna (det startande radindexet är 4 och det slutliga radindexet är 6).
1. De befintliga bilderna, diagrammen osv. i destinationsraden kommer inte att tas bort.

{{% /alert %}} 
### **Kopiera kolumner**
Aspose.Cells tillhandahåller CopyColumn-metoden i Aspose::Cells::ICells-klassen, denna metod kopierar alla typer av data, inklusive formler - med uppdaterade referenser - och värden, kommentarer, cellformat, dolda celler, bilder och andra ritobjekt från källkolumnen till destinationskolumnen.

Metoden CopyColumn tar följande parametrar:

- källans Cells-objekt,
- källkolumnens index och
- destinationskolumnens index.

Använd CopyColumn-metoden för att kopiera en kolumn inom ett blad eller till ett annat blad.

Detta exempel kopierar en kolumn från ett blad och klistrar in den i ett blad i en annan arbetsbok.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingColumns-new.cpp" >}}
