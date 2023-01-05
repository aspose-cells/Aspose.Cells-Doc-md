---
title: Formatera ett intervall på Cells
type: docs
weight: 60
url: /sv/net/formatting-a-range-of-cells/
---
{{% alert color="primary" %}} 

Det här ämnet tillhör också serien av ämnen som är relaterade till tillämpningen av teckensnittsinställningar och andra formateringsstilar på celler. Våra senaste ämnen har täckt väl om hantering av sådana funktioner. Du kan till exempel hänvisa till[Ändra teckensnitt och färg för en Cell](/cells/sv/net/changing-the-font-and-color-of-a-cell/) och[Applicera stilar på Cells](/cells/sv/net/applying-styles-on-cells/) ämnen för att lära dig om samma funktioner. Vad är då nytt i detta ämne om vi redan har täckt dessa begrepp. Tja, den enda skillnaden mellan detta ämne och de tidigare är att vi kommer att tillämpa formateringsinställningar (relaterade till teckensnitt och andra stilar) på ett antal celler istället för bara en enda cell. Vi hoppas att du fortfarande kommer att finna detta ämne användbart för dig.

{{% /alert %}} 
## **Ställa in teckensnitt och stil för ett intervall på Cells**
 Innan vi pratar om formateringsinställningar (som vi redan har pratat mycket om i våra tidigare ämnen), bör vi veta om hur man skapar en rad celler. Tja, vi kan skapa en rad celler med hjälp av**CellRange** klass vars konstruktor tar några parametrar för att specificera cellintervallet. Vi kan specificera cellintervallet med hjälp av**Namn** eller**Rad- och kolumnindex** av start- och slutceller.

 När vi har skapat en**CellRange** objekt så kan vi använda de överbelastade versionerna av**SetStyle**, **SetFont** & **SetFontColor** metoder för arbetsblad som kan ta en**CellRange** objekt för att tillämpa formateringsinställningar på det angivna cellintervallet.

Låt oss kolla in ett exempel för att förstå detta grundläggande koncept.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FormattingCellRange-1.cs" >}}
