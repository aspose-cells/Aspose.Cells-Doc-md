---
title: Formatering av ett cellintervall
type: docs
weight: 60
url: /sv/net/aspose-cells-griddesktop/formatting-a-range-of-cells/
keywords: GridDesktop, format, stil, celler
description: Den här artikeln introducerar hur man tillämpar stilformat på celler i GridDesktop.
---

{{% alert color="primary" %}} 

Det här ämnet tillhör också serien ämnen som är relaterade till tillämpning av teckeninställningar och andra formateringsstilar på celler. Våra senaste ämnen har täckt väl om hantering av sådana funktioner. Till exempel kan du hänvisa till [Ändra teckensnitt & färg för en cell](/cells/sv/net/changing-the-font-and-color-of-a-cell/) och [Tillämpa stilar på celler](/cells/sv/net/applying-styles-on-cells/) för att lära dig om samma funktioner. Vad är då nytt i det här ämnet om vi redan har täckt dessa begrepp. Jo, den enda skillnaden med det här ämnet jämfört med de tidigare är att vi kommer att tillämpa formateringsinställningar (relaterade till teckensnitt och andra stilar) på ett cellintervall istället för bara en enskild cell. Vi hoppas att du fortfarande kommer att finna det här ämnet användbart för dig.

{{% /alert %}} 
## **Inställning av teckensnitt & stil i ett cellintervall**
Innan vi pratar om formateringsinställningar (som vi redan har pratat mycket om i våra tidigare ämnen), bör vi veta hur man skapar ett cellintervall. Tja, vi kan skapa ett cellintervall med hjälp av **CellRange**-klassen vars konstruktor tar några parametrar för att ange cellintervall. Vi kan ange cellintervallet med hjälp av **Namn** eller **Rad & Kolumnindex** för start- och slutceller.

När vi har skapat en **CellRange** objekt kan vi använda de överbelastade versionerna av **SetStyle**, **SetFont** & **SetFontColor** metoder av Worksheet som kan ta en **CellRange** objekt för att tillämpa formateringsinställningar på det angivna cellområdet.

Låt oss kolla på ett exempel för att förstå denna grundläggande koncept.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FormattingCellRange-1.cs" >}}
