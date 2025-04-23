---
title: Hur man lägger till ikonsatser för villkorsstyrd formatering
description: Hur man använder Aspose.Cells biblioteket i C# för att tillämpa villkorsstyrd formatering med ikonsatser. Genom att justera dessa kriterier får du mer kontroll över hur cellerna ser ut och framhävs.
keywords: Aspose.Cells, Ikonsatser Villkorsstyrd Formatering, C#, Villkor, Format
type: docs
weight: 70
url: /sv/net/how-to-add-icon-sets-conditional-formatting/
---

## **Möjliga användningsscenario**
Att använda ikonsatser för villkorsstyrd formatering i Excel är ett utmärkt sätt att visualisera datatrender eller kategorier vid en snabb blick med hjälp av symboler som pilar, trafikljus, stjärnor, flaggor och mer. Det ger ett extra lager av tydlighet till ditt kalkylblad utan att behöva diagram eller djupare analyser.

1. Omedelbara visuella insikter: Ikoner gör det superenkelt att se vilka värden som är höga, medel eller låga utan att läsa varje siffra. Perfekt för instrumentpaneler, KPI:er och prestationsspårning.
1. Enkel trendidentifiering: Pilar visar om värdena ökar, minskar eller förblir neutrala. Trafikljus eller former hjälper till att visa status eller brådska.
1. Professionellt utseende: Gör rapporter mer polerade och presentationsklara. Hjälper icke-tekniska att snabbt förstå data.
1. Dynamiskt och automatiskt: Uppdateras automatiskt när värdena ändras — inget behov av att manuellt omformattera.

## **Hur man lägger till ikonsatser för villkorsstyrd formatering med Excel**
För att lägga till ikonsatser för villkorsstyrd formatering i Excel, gör så här steg för steg:

1. Välj ditt område av numeriska data. Exempel: B2:B20 (kan vara försäljningssiffror, prestationspoäng, etc.).
1. Gå till fliken Start.
1. Klicka på Villkorsstyrd formatering i Stilar-gruppen.
1. Hovera över Ikonuppsättningar.
1. Välj en ikonstil: Pilar, Trafikljus, Stjärnor, etc.
1. Ikonerna visas automatiskt baserat på värdefördelningen: Grön ikon = topp 67%, Gul ikon = mellan 33–67%, Röd ikon = botten 33%.


## **Hur man lägger till ikonuppsättningar i villkorsstyrd formatering med Aspose.Cells for .NET**

Aspose.Cells stöder fullt ut den villkorsstyrda formatering som tillhandahålls av Microsoft Excel 2007 och senare versioner i XLSX-format på cells vid körning. Exemplet demonstrerar en övning för villkorsstyrd formatering med ikonuppsättningar med olika inställningar.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-IconSets.cs" >}}

{{< app/cells/assistant language="csharp" >}}
