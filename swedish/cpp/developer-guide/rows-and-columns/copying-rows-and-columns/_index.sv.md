---
title: Kopiera rader och kolumner
type: docs
weight: 20
url: /sv/cpp/copying-rows-and-columns/
---
## **Introduktion**
Ibland behöver du kopiera rader och kolumner i ett kalkylblad utan att kopiera hela kalkylbladet. Med Aspose.Cells är det möjligt att kopiera rader och kolumner inom eller mellan arbetsböcker.
När en rad (eller kolumn) kopieras, kopieras även data som finns i den, inklusive formler - med uppdaterade referenser - och värden, kommentarer, formatering, dolda celler, bilder och andra ritobjekt.
## **Kopiera rader och kolumner med Microsoft Excel**
1. Välj den rad eller kolumn som du vill kopiera.
1.  Klicka på för att kopiera rader eller kolumner**Kopiera** på**Standard** verktygsfältet eller tryck på**CTRL**+**C**.
1. Välj en rad eller kolumn nedan eller till höger om var du vill kopiera ditt val.
1.  Klicka på när du kopierar rader eller kolumner**Kopierat Cells** på**Föra in** meny.

{{% alert color="primary" %}} 

 Om du klickar**Klistra** på**Standard** verktygsfältet eller tryck**CTRL**+** V** istället för att klicka på ett kommando på**Insert**-menyn, allt innehåll i destinationscellerna ersätts.

{{% /alert %}} 
## **Använder Aspose.Cells**
### **Kopiera rader**
Aspose.Cells tillhandahåller CopyRow-metoden för klassen Aspose::Cells::ICells. Denna metod kopierar alla typer av data inklusive formler, värden, kommentarer, cellformat, dolda celler, bilder och andra ritobjekt från källraden till målraden.

CopyRow-metoden tar följande parametrar:

- källan Cells objekt,
- källradens index, och
- destinationsradindex.

Använd den här metoden för att kopiera en rad i ett ark eller till ett annat ark. CopyRow-metoden fungerar på liknande sätt som Microsoft Excel. Så, till exempel, behöver du inte ställa in höjden på destinationsraden explicit, det värdet kopieras också.

Följande exempel visar hur man kopierar en rad i ett kalkylblad. Den använder en mall Microsoft Excel-fil och kopierar den andra raden (komplett med data, formatering, kommentarer, bilder och så vidare) och klistra in den på 12:e raden i samma kalkylblad.

 Du kan hoppa över steget som får källradens höjd med hjälp av**Get RowHeigh** metod och ställer sedan in destinationsradens höjd med hjälp av**SetRowHeight** metod som**CopyRow** metod tar automatiskt hand om radhöjden.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingRows.cpp" >}}

{{% alert color="primary" %}} 

När du kopierar rader är det viktigt att notera relaterade bilder, diagram eller andra ritobjekt eftersom detta är samma sak med Microsoft Excel:

1. Om källradens index är 5, kopieras bilden, diagrammet etc. om det finns i de tre raderna (startradindex är 4 och slutradens index är 6).
1. De befintliga bilderna, sjökorten etc. i destinationsraden kommer inte att tas bort.

{{% /alert %}} 
### **Kopiera kolumner**
Aspose.Cells tillhandahåller CopyColumn-metoden för klassen Aspose::Cells::ICells, denna metod kopierar alla typer av data, inklusive formler - med uppdaterade referenser - och värden, kommentarer, cellformat, dolda celler, bilder och andra ritobjekt från källan kolumnen till destinationskolumnen.

Metoden CopyColumn använder följande parametrar:

- källan Cells objekt,
- källkolumnindex och
- målkolumnindex.

Använd metoden CopyColumn för att kopiera en kolumn inom ett ark eller till ett annat ark.

Det här exemplet kopierar en kolumn från ett kalkylblad och klistrar in den i ett kalkylblad i en annan arbetsbok.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingColumns.cpp" >}}
