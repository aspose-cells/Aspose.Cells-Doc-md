---
title: Hur man skapar ett dynamiskt rullande diagram
description: Lär dig hur du skapar ett dynamiskt rullande diagram med Aspose.Cells for .NET. Vår guide kommer att visa hur du implementerar smidiga dataövergångar och rullande medelvärden i ditt diagram för en kontinuerlig och uppdaterad visning.
keywords: Aspose.Cells for .NET, Dynamic Rolling Chart, Data Transitions, Smooth Averages, Continuous Display, Updating Visualization.
type: docs
weight: 74
url: /sv/net/create-dynamic-rolling-chart/
---
##  **Möjliga användningsscenarier**
Ett dynamiskt rullande diagram hänvisar till en grafisk representation som visar datapunkter som ständigt skiftar och uppdateras över tiden. Det är en typ av diagram som kontinuerligt uppdaterar sig själv och visar ett rullande fönster med de senaste datapunkterna samtidigt som äldre datapunkter kasseras när nya kommer in.

Dynamiska rullande diagram används vanligtvis för att visualisera trender och mönster i realtid eller strömmande data. De är särskilt användbara i scenarier där tidsmässiga aspekter och förändringar över tid är kritiska, såsom aktiemarknadsanalys, väderövervakning eller spårning av liveprestanda.

Dessa diagram använder vanligtvis animering eller automatisk rullning för att säkerställa att den mest uppdaterade informationen alltid presenteras. Längden på det rullande fönstret kan anpassas för att visa en specifik tidsperiod, såsom den senaste timmen, dagen eller veckan.

Sammanfattningsvis är ett dynamiskt rullande diagram en kontinuerligt uppdaterad grafisk representation som visar de senaste datapunkterna samtidigt som äldre kasseras, vilket gör att användare kan observera trender och mönster i realtid.

##  **Använd Aspose Cells för att skapa dynamiska rullande diagram**
I nästa stycke kommer vi att visa dig hur du skapar dynamiskt rullande diagram med Aspose.Cells. Vi visar dig koden för exemplet, samt Excel-filen som skapats med denna kod.

##  **Exempelkod**
 Följande exempelkod kommer att generera[Dynamisk rullande diagramfil](DynamicRollingChart.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-dynamic-rolling-chart.cs" >}}

##  **Anteckningar**
I den genererade filen kan du fortsätta att lägga till data i kolumnerna A och B, medan diagrammet dynamiskt räknar de senaste 5 datauppsättningarna. Detta görs med hjälp av formeln "OFFSET" i exempelkoden:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Du kan prova att ändra siffran "-5" till "-10" i formeln, så kommer det dynamiska diagrammet att räkna de senaste 10 uppsättningarna data. Nu har vi skapat ett dynamiskt rullande diagram med Aspose.Cells framgångsrikt.
