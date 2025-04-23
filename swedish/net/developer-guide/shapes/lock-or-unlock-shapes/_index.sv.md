---
title: Lås eller lås upp figurer
linktitle: Lås eller lås upp figurer
type: docs
weight: 200
url: /sv/net/lock-or-unlock-shapes/
description: Denna artikel visar kod som förklarar hur man låser eller låser upp figurer för att skydda dem med Aspose.Cells biblioteket.
keywords: C# Låsa figurer för att skydda dem, hur man låser eller låser upp figurer med C#, lås eller lås upp figurer i C#.
---

## **Möjliga användningsscenario**

Ibland behöver du skydda alla figurer i vissa arbetsblad för att förhindra att de förstörs av oönskade situationer. I så fall måste du låsa alla figurer i det angivna arbetsbladet. 

Att låsa figurer i ett kalkylblad eller dokument kan vara fördelaktigt av flera skäl:
1. Förhindra oavsiktliga ändringar: Att låsa figurer säkerställer att de inte oavsiktligt flyttas, resizeas eller tas bort av användare. Detta är särskilt viktigt i komplexa dokument där figurer kan användas för anteckningar, illustrationer eller som en del av dokumentets design.
1. Bibehåll layout och design: Figurer är ofta avgörande för ett dokuments layout och visuella design. Att låsa dem bevarar det avsedda utseendet, vilket säkerställer att dokumentet förblir professionellt och visuellt tilltalande.
1. Dataintegritet: I kalkylblad kan figurer användas för att markera viktiga datapunkter, lägga till kommentarer eller ge visuella förklaringar. Att låsa dessa figurer säkerställer att den kontextuella information de ger är korrekt och intakt.
1. Konsistens i delade dokument: När man samarbetar om dokument kan olika användare ha varierande nivåer av expertis. Att låsa figurer hjälper till att upprätthålla konsekvensen i hela dokumentet genom att förhindra oavsiktliga ändringar.
1. Säkerhet: I känsliga dokument kan låsta figurer vara en del av en bredare strategi för att skydda information. Till exempel kan låsta figurer användas för att skydda specifika anteckningar eller markeringar som ger kritisk kontext.

Ibland behöver du kunna modifiera vissa figurer i vissa skyddade arbetsblad, i så fall måste du låsa upp dessa figurer. Denna artikel kommer att introducera i detalj hur man låser och låser upp angivna figurer.

## **Hur man låser figurer för att skydda dem i Excel**

Så här låser du celler i Microsoft Excel:

1. Öppna din Excel-fil: Öppna Excel-filen som innehåller figurerna du vill låsa.

1. Välj figuren: Klicka på figuren du vill låsa. Du kan också välja flera figurer genom att hålla nere Ctrl-tangenten och klicka på varje figur.

1. Öppna Fomateringspanelen för figur: Högerklicka på den valda figuren eller figurerna och välj "Storlek och egenskaper." Alternativt kan du gå till "Formatera"-fliken på menyfliksområdet och i "Storlek"-gruppen klicka på dialogikonen för att öppna "Formatera figur"-panelen.
1. Lås figuren: I "Formatera figur"-panelen, gå till fliken "Storlek & Egenskaper" (ikonen ser ut som en kvadrat med pilar). Under avsnittet "Egenskaper", bocka i rutan för "Låst."
<br>
<img src="1.png" width=60% />
1. Skydda arket: Gå till "Granska"-fliken på menyfliksområdet. Klicka på "Skydda blad." Ange ett lösenord (valfritt) och välj de behörigheter du vill tillåta (t.ex. välja låsta celler, formatera celler etc.). Klicka på "OK."
<br>
<img src="2.png" width=60% />

## **Hur man låser alla figurer i ett specifikt ark**

För att skydda alla former i ett angivet arbetsblad, använd [Worksheet.Protect( ProtectionType.Objects)](https://reference.aspose.com/cells/net/aspose.cells/worksheet/protect/#protect) metoden, som visas i följande exempelkod.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-1.cs" >}}

## **Hur man låser upp angivna figurer i ett skyddat arbetsblad**

För att låsa upp en angiven form i ett skyddat arbetsblad, använd [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/), som visas i följande exempelkod.

Observera: [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/) är meningsfull endast när arbetsbladet är skyddat.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-2.cs" >}}

{{< app/cells/assistant language="csharp" >}}
