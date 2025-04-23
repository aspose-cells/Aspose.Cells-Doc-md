---
title: Hur man skalar ett kalkylblad
type: docs
weight: 130
url: /sv/net/how-to-scale-a-worksheet/
description: Denna artikel visar dig kod som förklarar hur man skalar ett arbetsblad med Aspose.Cells biblioteket.
keywords: C# skala ett arbetsblad, Hur man skalar ett arbetsblad med C#, Skala ett arbetsblad i C#.
---

## **Möjliga användningsscenario**
Att skala ett kalkylblad kan vara användbart av olika skäl, beroende på sammanhanget du arbetar i. Här är några vanliga skäl för att skala ett kalkylblad:
1. Passa på sida: För att säkerställa att allt innehåll får plats på en enda sida eller ett specifikt antal sidor vid utskrift, vilket gör det lättare att läsa och hantera utan att behöva bläddra igenom flera sidor.

1. Presentation: För att få arbetsbladet att se mer organiserat och professionellt ut, särskilt när du delar det med andra i möten eller rapporter.

1. Läslighet: För att justera storleken på texten och andra element för bättre läsbarhet, särskilt för personer som kan ha svårt att läsa mindre teckensnitt.

1. Platsförvaltning: För att optimera användningen av utrymmet på ett arbetsblad, säkerställa att det inte finns onödig tomrum och att all viktig information är synlig utan överdriven scrollning.

1. Data Visualisering: När det gäller diagram och grafer kan skala hjälpa till att göra dem mer förståeliga genom att justera storleken för att passa den tillgängliga platsen lämpligen.

1. Konsekvens: För att upprätthålla ett konsekvent utseende och känsla över flera arbetsblad eller dokument, vilket är särskilt viktigt i professionella och utbildningsinställningar.

## **Hur man skalar ett kalkylblad i Excel**
Att skala ett arbetsblad i Excel kan hjälpa dig att få ditt innehåll att passa på en enda sida eller ett specificerat antal sidor vid utskrift. Här är stegen för att skala ett arbetsblad:

1. Öppna ditt arbetsblad: Öppna Excel-arbetsbladet som du vill skala.

1. Gå till fliken Sidlayout: Klicka på fliken Sidlayout i bandet.

1. Skala för att passa grupp: I fliken Sidlayout, hitta gruppen Skala för att passa. Här har du alternativen för att justera skalan. Bredd: Detta alternativ tillåter dig att specificera hur många sidor bred det utskrivna arbetsbladet ska vara. Höjd: Detta alternativ tillåter dig att specificera hur många sidor högt det utskrivna arbetsbladet ska vara. Skala: Du kan också ange en anpassad procentandel för skalan här.
<br>
<img src="1.png" width=60% />

1. Justera Bredd och Höjd: Ställ in Bredd och Höjd till önskat antal sidor. Till exempel, ställ båda till 1 sida om du vill att arbetsbladet ska passa på en sida.

1. Justera skaleringsprocenten (om nödvändigt): Om du föredrar att ange en specifik skaleringsprocent, justera rutan Skala. Till exempel, att ställa in den till 50% gör att allt blir halvt så stort.


## **Hur man skalar ett arbetsblad med C#**
Aspose.Cells är ett kraftfullt bibliotek för att arbeta med Excel-filer programmatiskt. För att skala ett arbetsblad med Aspose.Cells, måste du följa dessa steg: ladda [exempel fil](sample.xlsx) och justera utskriftsinställningarna så att innehållet passar till det önskade antalet sidor eller en specifik procentuell storlek av originalet.

### **Exempel: Passa till sida**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-scale-a-worksheet-fit-to-page.cs" >}}
<br>
<img src="3.png" width=60% />

### **Exempel: Skala till procentandel**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-scale-a-worksheet-scale-to-percentage.cs" >}}
<br>
<img src="2.png" width=60% />
{{< app/cells/assistant language="csharp" >}}
