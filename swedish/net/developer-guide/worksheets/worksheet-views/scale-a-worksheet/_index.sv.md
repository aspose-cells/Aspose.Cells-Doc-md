---
title: Hur man skalar en arbetsbok
type: docs
weight: 130
url: /sv/net/how-to-scale-a-worksheet/
description: Den här artikeln visar dig kod som förklarar hur man skalar en arbetsbok med hjälp av Aspose.Cells biblioteket.
keywords: C# skala en arbetsbok, Hur man skalar en arbetsbok med C#, Skala en arbetsbok i C#.
---

## **Möjliga användningsscenario**
Att skala en arbetsbok kan vara användbart av olika anledningar, beroende på sammanhanget där du arbetar. Här är några vanliga skäl till att skala en arbetsbok:
1. Anpassa till sida: För att säkerställa att allt innehåll ryms på en enda sida eller ett specifikt antal sidor vid utskrift, vilket gör det lättare att läsa och hantera utan att behöva bläddra genom flera sidor.

1. Presentation: För att göra arbetsboken mer organiserad och professionell, särskilt när den delas med andra under möten eller i rapporter.

1. Läsbarhet: För att justera storleken på texten och andra element för bättre läsbarhet, särskilt för personer som kan ha svårt att läsa mindre teckensnitt.

1. Plats hantering: För att optimera användningen av utrymme på en arbetsbok, och se till att det inte finns onödigt vitt utrymme och att all viktig information är synlig utan överdriven scrollning.

1. Data visualisering: I fallet med diagram och grafer kan skalan hjälpa till att göra dem mer begripliga genom att justera storleken för att passa det tillgängliga utrymmet på lämpligt sätt.

1. Konsistens: För att behålla en konsekvent utseende och känsla över flera arbetsböcker eller dokument, vilket är särskilt viktigt inom professionella och utbildningsmässiga miljöer.

## **Hur man skalar en arbetsbok i Excel**
Att skala en arbetsbok i Excel kan hjälpa dig att få ditt innehåll att rymmas på en enda sida eller ett angivet antal sidor vid utskrift. Här är stegen för att skala en arbetsbok:

1. Öppna din arbetsbok: Öppna den Excel arbetsbok som du vill skala.

1. Gå till fliken Sidlayout: Klicka på fliken Sidlayout i menyfliken.

1. Skala för att passa grupp: På fliken Sidlayout, hitta Skala för att passa gruppen. Här har du alternativ att justera skalan. Bredd: Det här alternativet låter dig specificera hur många sidor bred den tryckta arbetsboken kommer att vara. Höjd: Det här alternativet låter dig specificera hur många sidor hög den tryckta arbetsboken kommer att vara. Skala: Du kan också ange en anpassad skalningsprocent här.
<br>
<img src="1.png" width=60% />

1. Justera bredd och höjd: Ange bredd och höjd till ditt önskade antal sidor. Till exempel, sätt båda till 1 sida om du vill att arbetsboken ska rymmas på en sida.

1. Justera Skalningsprocent (om det behövs): Om du föredrar att ange en specifik skalningsprocent, justera Skala-rutan. Till exempel, att sätta den till 50% kommer göra allt hälften så stort.


## **Hur man skalar en arbetsblad med C#**
Aspose.Cells är ett kraftfullt bibliotek för att arbeta med Excel-filer programmatiskt. För att skala ett arbetsblad med Aspose.Cells, behöver du följa dessa steg: ladda [provfil](sample.xlsx) och justera utskriftsinställningarna så att innehållet passar på önskat antal sidor eller en specifik procentandel av originalstorleken.

### **Exempel: Anpassa till sida**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-scale-a-worksheet-fit-to-page.cs" >}}
<br>
<img src="3.png" width=60% />

### **Exempel: Skala till procent**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-scale-a-worksheet-scale-to-percentage.cs" >}}
<br>
<img src="2.png" width=60% />
