---
title: Hur man lägger till Top10 villkorsstyrd formatering
description: Hur man använder Aspose.Cells biblioteket i C# för att tillämpa Top10 villkorsstyrd formatering. Genom att justera dessa kriterier får du mer kontroll över hur cellerna ser ut och framträder.
keywords: Aspose.Cells, Top10 villkorsstyrd formatering, C#, Villkor, Formatering
type: docs
weight: 70
url: /sv/net/how-to-add-top10-conditional-formatting/
---

## **Möjliga användningsscenario**
Att använda Top 10 villkorsstyrd formatering i Excel hjälper dig att snabbt markera de värden som presterar bäst i en datamängd — inte bara de bokstavligen tio bästa, utan ofta de topp N värden eller topp N% (du kan välja!).

1. Upptäck trender och avvikare: Identifiera direkt de bästa prestaterna (t.ex. topp 10 säljare, bästa betyg, månader med högst intäkter). Gör det enkelt att analysera utan att sortera data.
1. Datavisualisering: Lägger till färgmarkeringar som gör viktiga datapunkter visuellt framhävda. Hjälper tittare av kalkylbladet att förstå nyckelvärdena i ett ögonblick.
1. Snabb jämförelse: Användbart i dashboards och rapporter där du vill lyfta fram excellens eller toppar.
1. Dynamiska uppdateringar: Om dina data ändras uppdateras den villkorsstyrda formateringen automatiskt för att återspegla de nya toppvärdena.

## **Hur man lägger till Top10 villkorsstyrd formatering med Excel**
Så här kan du steg för steg lägga till Top10 villkorsstyrd formatering i Excel:

1. Välj det cellområde du vill analysera. Till exempel: Välj B2:B100, om du arbetar med poäng eller försäljningssiffror.
1. Gå till fliken Hem i Excel-menyn.
1. Klicka på Villkorsstyrd formatering i Stilar-gruppen.
1. Håll muspekaren över Top/bottom-regler i rullgardinsmenyn.
1. Klicka på Top 10-objekt...
1. En dialogruta öppnas: Den säger: Formatera celler som rankas bland de 10 främsta. Du kan ändra numret (t.ex. Top 5, Top 3 osv.). Välj ett format (som en ljus röd fyllning, fet stil eller klicka på Anpassad formatering för fler alternativ).
1. Klicka på OK


## **Hur man lägger till Top10 villkorsstyrd formatering med Aspose.Cells for .NET**

Aspose.Cells stöder fullt ut den villkorsstyrda formatering som erbjuds av Microsoft Excel 2007 och senare i XLSX-format vid körning. Detta exempel visar en övning för Top 10 villkorsstyrd formatering med olika uppsättningar av attribut.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Top10.cs" >}}

{{< app/cells/assistant language="csharp" >}}
