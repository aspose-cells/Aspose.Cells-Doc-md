---
title: Hur man lägger till tidsperioders villkorsstyrd formatering
description: Hur man använder Aspose.Cells biblioteket i C# för att tillämpa villkorsstyrd formatering för tidsperioder. Genom att justera dessa kriterier kan du ha mer kontroll över hur celler ser ut och visas.
keywords: Aspose.Cells, villkorsstyrd formatering för tidsperioder, C#, Villkorsstyrd, Formatering
type: docs
weight: 70
url: /sv/net/how-to-add-time-periods-conditional-formatting/
---

## **Möjliga användningsscenario**
Att använda villkorsstyrd formatering för tidsperioder i Excel är mycket användbart när du arbetar med datum – det hjälper dig att visuellt spåra och hantera tidsbaserad data snabbt.
1. Omedelbara insikter om tidsbaserad data: Markera snabbt saker som dagens uppgifter, förra månadens försäljning, kommande deadlines, nästa veckas möten.
1. Bättre tidshantering: Hjälper dig att hålla koll på förfallodagar, händelser eller utgångna objekt. Bra för projektplaner, fakturor eller scheman.
1. Automatiska uppdateringar: Den uppdateras dynamiskt. Om dagens datum ändras, kommer Excel att uppdatera formateringen utan att du gör något.

1. Visuell tydlighet: Gör tidskänslig information framträdande med färger eller fet stil — så att den inte missas.

## **Hur man lägger till villkorsstyrd formatering för tidsperioder med Excel**
Så här kan du lägga till villkorsstyrd formatering för tidsperioder i Excel — mycket användbart för att markera datum som idag, förra veckan, nästa månad, etc.

Steg för att lägga till villkorsstyrd formatering för tidsperioder:
1. Markera det område av datumceller du vill formatera. Exempel: A2:A50.
1. Gå till fliken Hem i menyfliksområdet.
1. Klicka på Villkorsstyrd formatering i Stilar-gruppen.
1. Håll muspekaren över Markera cellregler.
1. Klicka på En datum som inträffar...
1. I dialogrutan som visas: Använd rullgardinsmenyn för att välja en tidsperiod (Idag, Igår, Imorgon, Senaste 7 dagar, Förra veckan, Nästa månad osv.).
1. Välj format (standard är ljusröd fyllning med mörkröd text, eller klicka på Anpassad formatering för att välja egna stilar).
1. Klicka på OK.


## **Hur man lägger till villkorsstyrd formatering för tidsperioder med Aspose.Cells for .NET**

Aspose.Cells stöder fullt ut den villkorsstyrda formateringen som Microsoft Excel 2007 och senare versioner tillhandahåller i XLSX-format på celler vid körning. Det här exemplet visar ett övningsexempel för villkorsstyrd formatering för tidsperioder med olika attributsets.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-TimePeriod.cs" >}}

{{< app/cells/assistant language="csharp" >}}
