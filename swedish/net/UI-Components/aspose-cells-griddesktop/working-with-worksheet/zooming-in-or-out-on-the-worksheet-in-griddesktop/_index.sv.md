---
title: Zooma in eller ut på arbetsbladet i GridDesktop
type: docs
weight: 160
url: /sv/net/zooming-in-or-out-on-the-worksheet-in-griddesktop/
---
{{% alert color="primary" %}} 

Ibland, när du arbetar med dina data, kanske du vill förstora innehållet på skärmen utan att faktiskt ändra teckenstorleken. Du kan till exempel ha formaterat din text så att den använder ett litet teckensnitt. (Detta är ofta nödvändigt för att få all din information på en utskrift.) När du arbetar i kalkylbladet är teckensnittet dock svårt att läsa eftersom det är så litet.

Microsoft Excel finns ett zoomreglage tillgängligt för att snabbt och enkelt zooma in och ut ur dokument. Zoomreglaget är vanligtvis i det nedre högra hörnet av mjukvarufönstret.

Aspose.Cells tillåter också utvecklare att ställa in kalkylbladets zoomfaktor, så innehållet ska visas enligt önskat procentvärde.

{{% /alert %}} 
## **Zooma in eller ut med Aspose.Cells.GridDesktop**
Aspose.Cells tillhandahåller Aspose.Cells.GridDesktop.Worksheet-klassen som har ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att ställa in ett kalkylblads zoomfaktor, använd kalkylbladsklassens Zoom-egenskap. Zoomfaktorn ställs in genom att tilldelas ett numeriskt (heltal) värde till egenskapen Zoom.

Vi bygger en MS Excel-liknande zoomreglage med TrackBar (.NET) kontroll. I ett WinForm-projekt placerar vi Aspose.Cells.GridDesktop-kontrollen från Toolbox till formuläret och anger några egenskaper för att ställa in dess namn, storlek eller andra aspekter därefter. Nu placerar vi TrackBar-kontrollen @ nedre högra hörnet under GridDesktop-kontrollen, vi lägger också en Label-kontroll som skulle visa procentvärdet du anger via TrackBar-kontrollens handtag. Vi lägger till relativa kodrader i TrackBars Scroll-händelse, så när du bläddrar i Trackbar-kontrollen bör GridDesktop zooma in eller ut för att visa data/innehåll i den.

Ett komplett exempel ges nedan som visar hur man använder egenskapen Zoom för att ställa in zoomfaktorn för det aktiva kalkylbladet i GridDesktop. Vi importerar först en mall Excel-fil till GridDesktop.

Skriv nedanstående kod i formulärets Load-händelse för att ställa in mallens Excel-fil i GridDesktop och trackbar-värdet.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-LoadEvent.cs" >}}


Kopiera nu nedanstående kod inuti spårrullningshändelsen och kör applikationen. Du kommer att märka att rörlig spårstapel ändrar kalkylbladets zoomegenskap.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-ZoomInOut.cs" >}}
