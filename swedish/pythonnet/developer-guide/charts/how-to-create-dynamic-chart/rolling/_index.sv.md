---
title: Hur man skapar dynamiskt rullande diagram
description: Lär dig hur man skapar ett dynamiskt rullande diagram med Aspose.Cells för Python via .NET. Vår guide visar hur man implementerar smidiga dataövergångar och glidande medelvärden i ditt diagram för en kontinuerlig och uppdaterad visning.
keywords: Aspose.Cells för Python via .NET, Dynamiskt Rullande Diagram, Dataövergångar, Smidiga Medelvärden, Kontinuerlig Visning, Uppdaterad visualisering.
type: docs
weight: 74
url: /sv/python-net/create-dynamic-rolling-chart/
---

## **Möjliga användningsscenario**
Ett dynamiskt rullande diagram syftar till en grafisk representation som visar data punkter som konstant förskjuts och uppdateras över tiden. Det är en typ av diagram som kontinuerligt uppdaterar sig själv och visar ett rullande fönster av de senaste datapunkterna samtidigt som äldre datapunkter kastas bort när nya kommer in.

Dynamiska rullande diagram används vanligen för att visualisera trender och mönster i realtid eller strömningsdata. De är särskilt användbara i scenarier där tidsmässiga aspekter och förändringar över tid är avgörande, såsom analys av aktiemarknaden, väderövervakning eller spårning av liveprestanda.

Dessa diagram använder vanligtvis animation eller automatisk rullning för att säkerställa att den mest aktuella informationen alltid presenteras. Längden på det rullande fönstret kan anpassas för att visa en specifik tidsperiod, såsom den senaste timmen, dagen eller veckan.

Sammanfattningsvis är ett dynamiskt rullande diagram en kontinuerligt uppdaterad grafisk representation som visar de senaste datapunkterna samtidigt som äldre kastas bort, vilket gör att användarna kan observera trender och mönster i realtid.

## **Använd Aspose.Cells för Python via .NET för att skapa ett dynamiskt rullande diagram**
I de följande styckena visar vi hur du skapar ett dynamiskt rullande diagram med Aspose.Cells för Python via .NET. Vi visar exempel på koden samt den Excel-fil som skapats med denna kod.

## **Exempelkod**
Följande provkod kommer att generera [Dynamic Rolling Chart File](DynamicRollingChart.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-create-dynamic-rolling-chart.py" >}}

## **Anteckningar**
I den genererade filen kan du fortsätta att lägga till data i kolumnerna A och B, samtidigt som diagrammet dynamiskt räknar de senaste 5 datamängderna. Detta görs med hjälp av "OFFSET"-formeln i provkoden:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Du kan prova att ändra talet "-5" till "-10" i formeln, och det dynamiska diagrammet kommer att räkna de senaste 10 datamängderna. Vi har nu framgångsrikt skapat ett dynamiskt rullande diagram med Aspose.Cells för Python via .NET.
