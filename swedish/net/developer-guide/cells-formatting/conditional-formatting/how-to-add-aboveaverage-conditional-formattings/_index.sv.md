---
title: Hur man lägger till Villkorlig formatering för över medelvärde
description: Hur man använder Aspose.Cells biblioteket i C# för att tillämpa Villkorlig formatering för över medelvärde. Genom att justera dessa kriterier får du mer kontroll över hur cellerna ser ut och uttrycker sig.
keywords: Aspose.Cells, Villkorlig formatering för över medelvärde, C#, Villkorlig, Formatering
type: docs
weight: 70
url: /sv/net/how-to-add-above-average-conditional-formatting/
---

## **Möjliga användningsscenario**
Att använda Villkorlig formatering för över medelvärde i verktyg som Microsoft Excel eller Google Sheets är ett snabbt och visuellt sätt att markera utstickande data—specifikt värden som är högre än medelvärdet i ett område. Här är varför du kanske vill använda det:
1. Snabbt upptäcka trender: Det hjälper dig att omedelbart identifiera högpresterande värden utan att manuellt beräkna medelvärden eller skanna igenom siffror.
1. Förenkla dataanalysen: Du behöver inte beräkna eller mata in några formler—det är ett automatisk sätt att tillämpa logikbaserad formatering, vilket sparar tid.
1. Förbättra visuell tilltalande: Färgkodning hjälper till att göra ditt kalkylblad lättare att läsa och mer visuellt engagerande, särskilt under presentationer.
1. Understödja beslutsfattande: Att snabbt identifiera värden över medelvärdet kan driva åtgärder, som att belöna högpresterare eller undersöka varför vissa produkter presterar bättre än andra.

## **Hur man lägger till Villkorlig formatering för över medelvärde i Excel**
För att lägga till Villkorlig formatering för över medelvärde i Excel, gör så här steg för steg:

1. Markera det cellområde du vill tillämpa formateringen på. Till exempel: A1:A20.
1. Gå till fliken Hem i menyfliksområdet.
1. Klicka på Villkorsstyrd formatering i Stilar-gruppen.
1. Hovra över Top/Bottom Rules.
1. Klicka på Över medelvärde...
1. I dialogrutan som visas: Den upptäcker automatiskt "Format a celler som är OVAN medelvärdet." Du kan ändra formateringsstilen genom att klicka på rullgardinsmenyn bredvid (t.ex. välja en färgfyllning eller anpassad formatering).
1. Klicka på OK. Alla celler i ditt valda område som är över medelvärdet för det området kommer att markeras.


## **Hur man lägger till Villkorlig formatering för över medelvärde med Aspose.Cells for .NET**

Aspose.Cells stöder fullt ut den villkorliga formateringen som tillhandahålls av Microsoft Excel 2007 och senare versioner i XLSX-format på celler vid körning. Detta exempel visar en övning för Villkorlig formatering för över medelvärde med olika uppsättningar av attribut.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-AboveAverage.cs" >}}

{{< app/cells/assistant language="csharp" >}}
