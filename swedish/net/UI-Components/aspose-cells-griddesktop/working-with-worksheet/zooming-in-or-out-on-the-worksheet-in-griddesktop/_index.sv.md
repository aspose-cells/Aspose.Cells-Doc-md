---
title: Zooma in eller ut på arbetsbladet i GridDesktop
type: docs
weight: 160
url: /sv/net/aspose-cells-griddesktop/zoom-in-or-out-on-the-worksheet-in-griddesktop/
keywords: GridDesktop, zoom, zooma in, zooma ut
description: Den här artikeln introducerar hur man zoomar in eller ut i GridDesktop.
---

{{% alert color="primary" %}} 

Ibland, när du arbetar med dina data, kan du vilja förstora innehållet på skärmen utan att faktiskt ändra teckensnittsstorleken. Till exempel kan du ha formaterat din text så att den använder en liten teckensnittsstorlek. (Detta är ofta nödvändigt för att få all din information på en utskrift.) När du arbetar i arbetsbladet är dock teckensnittet svårt att läsa eftersom det är så litet.

I Microsoft Excel finns en zoomskjutreglage för snabb och enkel zoomning in och ut ur dokumenten. Zoomskjutreglaget är vanligtvis i det nedre högra hörnet av programvarufönstret.

Aspose.Cells tillåter också utvecklare att ställa in arbetsbladets zoomfaktor, så innehållet bör visas enligt önskad procentsats.

{{% /alert %}} 
## **Zooma in eller ut med hjälp av Aspose.Cells.GridDesktop**
Aspose.Cells tillhandahåller klassen Aspose.Cells.GridDesktop.Worksheet som har ett brett utbud av egenskaper och metoder för hantering av arbetsblad. För att ställa in en arbetsblads zoomfaktor, använd egenskapen Zoom i Worksheet-klassen. Zoomfaktorn ställs in genom att tilldela ett numeriskt (heltal) värde till Zoom-egenskapen.

Vi bygger en MS Excel-liknande zoomskjutreglage med hjälp av TrackBar (.NET)-kontrollen. I en WinForm-projekt placerar vi Aspose.Cells.GridDesktop-kontrollen från verktygsfältet på formuläret och specificerar vissa egenskaper för att ange dess namn, storlek eller andra aspekter. Nu placerar vi TrackBar-kontrollen @ det nedre högra hörnet under Aspose.Cells.GridDesktop-kontrollen, vi lägger också till en Label-kontroll som skulle visa procentvärdet du specificerar via TrackBar-kontrollens handtag. Vi lägger till relativa kodrader i TrackBars Scroll-händelse, så när du skrollar på TrackBar-kontrollen bör GridDesktop zooma in eller ut för att visa data/innehåll i den.

Ett komplett exempel visas nedan som visar hur man använder Zoom-egenskapen för att ställa in zoomfaktorn för det aktiva arbetsbladet i GridDesktop. Vi importerar först en mall för Excel-fil till GridDesktop.

Skriv nedan kod i formulärets Laddningshändelse för att ställa in mallen för Excel-filen i GridDesktop och spårbandets värde.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-LoadEvent.cs" >}}


Kopiera nu nedan kod inne i spårkontrollens rullhändelse och kör applikationen. Du kommer att märka att när du flyttar spårkontrollen kommer zoom-egenskapen för arbetsbladet att ändras.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-ZoomInOut.cs" >}}
