---
title: Hur man lägger till villkorsstyrd formattering med datastavar
description: Hur man använder Aspose.Cells biblioteket i C# för att tillämpa villkorsstyrd formattering med datastavar. Genom att justera dessa kriterier får du mer kontroll över hur cellerna ser ut och framhävs.
keywords: Aspose.Cells, Villkorsstyrd formatering med datastavar, C#, Villkor, Format
type: docs
weight: 70
url: /sv/net/how-to-add-databars-conditional-formatting/
---

## **Möjliga användningsscenario**
Att använda datastavar i villkorsstyrd formatering är ett kraftfullt (och visuellt!) sätt att snabbt förstå dina data.

1. Visuell jämförelse av värden: Datastavar förvandlar siffror till horisontella staplar, vilket gör det extremt enkelt att jämföra värden sida vid sida — som ett mini-stapeldiagram inuti cellerna!
1. Omedelbar mönsterigenkänning: Du kan direkt se toppar, dalar och avvikelser utan att sortera eller skanna siffror.
1. Bättre läsbarhet: Särskilt användbart i långa tabeller — det minskar den kognitiva belastningen och hjälper dig att snabbt förstå nyckeltrender.
1. Dynamiskt och i realtid: När värdena ändras uppdateras staplarna automatiskt — perfekt för att spåra live-mått, framsteg eller KPI:er.
1. Professionella instrumentpaneler: Ger en ren, modern och polerad look till rapporter eller instrumentpaneler.

## **Hur man lägger till villkorsstyrd formatering med datastavar med Excel**
För att lägga till villkorsstyrd formatering med datastavar i Excel, gör så här steg för steg:

1. Välj ditt dataområde, till exempel: C2:C20 — detta kan vara försäljningssiffror, poäng eller framstegs värden.
1. Gå till fliken Hem i menyfliksområdet.
1. Klicka på Villkorsstyrd formatering i gruppen Stilar.
1. Håll muspekaren över Datastavar.
1. Välj en stil: Gradientfyllning (staplar tonar från vänster till höger) och Solid Fill (staplar har en solid färg).
1. Klicka på den stil du gillar — och du är klar!

## **Hur man lägger till villkorsstyrd formatering med datastavar med Aspose.Cells for .NET**

Aspose.Cells stöder fullt ut villkorsstyrd formatering som tillhandahålls av Microsoft Excel 2007 och senare versioner i XLSX-format på celler vid körning. Detta exempel demonstrerar en övning för villkorsstyrd formatering med datastavar med olika attribut.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-DataBar.cs" >}}

{{< app/cells/assistant language="csharp" >}}
