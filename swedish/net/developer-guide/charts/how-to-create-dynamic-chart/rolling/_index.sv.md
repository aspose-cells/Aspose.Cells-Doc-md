---
title: Hur man skapar dynamiskt rullande diagram
description: Lär dig hur man skapar ett dynamiskt rullande diagram med hjälp av Aspose.Cells for .NET. Vår guide kommer att visa hur man implementerar smidiga dataövergångar och rullande genomsnitt i ditt diagram för en kontinuerlig och uppdaterad display.
keywords: Aspose.Cells for .NET, dynamiskt rullande diagram, dataövergångar, smidiga genomsnitt, kontinuerlig display, uppdaterar visualisering.
type: docs
weight: 74
url: /sv/net/create-dynamic-rolling-chart/
---

## **Möjliga användningsscenario**
Ett dynamiskt rullande diagram syftar till en grafisk representation som visar data punkter som konstant förskjuts och uppdateras över tiden. Det är en typ av diagram som kontinuerligt uppdaterar sig själv och visar ett rullande fönster av de senaste datapunkterna samtidigt som äldre datapunkter kastas bort när nya kommer in.

Dynamiska rullande diagram används vanligen för att visualisera trender och mönster i realtid eller strömningsdata. De är särskilt användbara i scenarier där tidsmässiga aspekter och förändringar över tid är avgörande, såsom analys av aktiemarknaden, väderövervakning eller spårning av liveprestanda.

Dessa diagram använder vanligtvis animation eller automatisk rullning för att säkerställa att den mest aktuella informationen alltid presenteras. Längden på det rullande fönstret kan anpassas för att visa en specifik tidsperiod, såsom den senaste timmen, dagen eller veckan.

Sammanfattningsvis är ett dynamiskt rullande diagram en kontinuerligt uppdaterad grafisk representation som visar de senaste datapunkterna samtidigt som äldre kastas bort, vilket gör att användarna kan observera trender och mönster i realtid.

## **Använd Aspose Cells för att skapa dynamiskt rullande diagram**
I de följande styckena kommer vi att visa dig hur du skapar ett dynamiskt rullande diagram med hjälp av Aspose.Cells. Vi kommer att visa koden för exemplet, liksom Excel-filen skapad med denna kod.

## **Exempelkod**
Följande provkod kommer att generera [Dynamic Rolling Chart File](DynamicRollingChart.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-dynamic-rolling-chart.cs" >}}

## **Anteckningar**
I den genererade filen kan du fortsätta att lägga till data i kolumnerna A och B, samtidigt som diagrammet dynamiskt räknar de senaste 5 datamängderna. Detta görs med hjälp av "OFFSET"-formeln i provkoden:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Du kan prova att ändra numret "-5" till "-10" i formeln, och det dynamiska diagrammet kommer att räkna de senaste 10 datamängderna. Nu har vi skapat ett dynamiskt rullande diagram med hjälp av Aspose.Cells framgångsrikt.
