---
title: Hur man skapar dynamisk rullande diagram med Golang via C++
linktitle: Hur man skapar dynamiskt rullande diagram
description: Lär dig att skapa ett dynamiskt rullande diagram med Aspose.Cells for C++. Vår guide visar hur du implementerar smidiga dataövergångar och glidande medelvärden i ditt diagram för kontinuerlig och uppdaterad visning.
keywords: Aspose.Cells for C++, Dynamiskt rullande diagram, Dataövergångar, Smidiga medelvärden, Kontinuerlig visning, Uppdaterad visualisering.
type: docs
weight: 74
url: /sv/go-cpp/create-dynamic-rolling-chart/
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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Rolling.go" >}}
## **Anteckningar**
I den genererade filen kan du fortsätta att lägga till data i kolumnerna A och B, samtidigt som diagrammet dynamiskt räknar de senaste 5 datamängderna. Detta görs med hjälp av "OFFSET"-formeln i provkoden:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Rolling-1.go" >}}
Du kan prova att ändra numret "-5" till "-10" i formeln, och det dynamiska diagrammet kommer att räkna de senaste 10 datamängderna. Nu har vi skapat ett dynamiskt rullande diagram med hjälp av Aspose.Cells framgångsrikt.
