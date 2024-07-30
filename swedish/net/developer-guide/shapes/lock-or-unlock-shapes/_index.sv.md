---
title: Lås eller lås upp figurer
linktitle: Lås eller lås upp figurer
type: docs
weight: 200
url: /sv/net/lock-or-unlock-shapes/
description: Den här artikeln visar kod som förklarar hur man låser eller låser upp former för att skydda dem med hjälp av Aspose.Cells biblioteket.
keywords: C# Lås former för att skydda dem, Hur man låser eller låser upp former med C#, Lås eller lås upp former för att skydda dem i C#.
---

## **Möjliga användningsscenario**

Ibland behöver du skydda alla figurer i vissa arbetsblad för att förhindra att de förstörs av oönskade situationer. I så fall måste du låsa alla figurer i det angivna arbetsbladet. 

Att låsa former i ett kalkylblad eller dokument kan vara fördelaktigt av flera skäl:
1. Förhindra oavsiktliga ändringar: Att låsa former säkerställer att de inte råkar flyttas, ändras i storlek eller tas bort av användare. Detta är särskilt viktigt i komplexa dokument där former kan användas för anteckningar, illustrationer eller som en del av dokumentets design.
1. Behåll layout och design: Former spelar ofta en avgörande roll i layout och visuell design av ett dokument. Genom att låsa dem bevarar man det avsedda utseendet, vilket säkerställer att dokumentet förblir professionellt och visuellt tilltalande.
1. Dataintegritet: I kalkylblad kan former användas för att markera viktiga datapunkter, lägga till kommentarer eller ge visuella förklaringar. Genom att låsa dessa former säkerställs att den kontextuella information de ger förblir korrekt och intakt.
1. Konsistens i delade dokument: När man samarbetar kring dokument kan olika användare ha varierande kunskapsnivå. Att låsa former hjälper till att bibehålla konsistens i dokumentet genom att förhindra oavsiktliga ändringar.
1. Säkerhet: I känsliga dokument kan låsning av former vara en del av en bredare strategi för att skydda information. Till exempel kan låsta former användas för att skydda specifika anteckningar eller markeringar som ger viktig kontext i finansiella rapporter eller juridiska dokument.

Ibland behöver du kunna ändra vissa former i vissa skyddade kalkylblad, i så fall behöver du låsa upp dessa former. Den här artikeln kommer att introducera i detalj hur man låser och låser upp specificerade former.

## **Hur man låser former för att skydda dem i Excel**

Här är hur du kan låsa celler i Microsoft Excel:

1. Öppna din Excel-fil: Öppna Excel-filen som innehåller de former du vill låsa.

1. Välj formen: Klicka på formen som du vill låsa. Du kan också välja flera former genom att hålla ner Ctrl-tangenten och klicka på varje form.

1. Öppna Format Shape-rutan: Högerklicka på den valda formen(formerna) och välj "Storlek och egenskaper." Alternativt kan du gå till fliken "Format" på menyn och i gruppen "Storlek" klicka på dialogrutan (en liten pil) för att öppna "Format Shape" rutan.
1. Lås formen: I "Format Shape" rutan, gå till fliken "Storlek och egenskaper" (ikonen ser ut som en fyrkant med pilar). Under avsnittet "Egenskaper", markera rutan för "Låst".
<br>
<img src="1.png" width=60% />
1. Skydda arbetsbladet: Gå till fliken "Granska" på menyn. Klicka på "Skydda ark." Ange ett lösenord (valfritt) och välj de behörigheter du vill tillåta (t.ex. att välja låsta celler, formatera celler osv.). Klicka på "OK."
<br>
<img src="2.png" width=60% />

## **Hur man låser alla former i ett angivet kalkylblad**

För att skydda alla former i ett angivet arbetsblad, använd [Worksheet.Protect( ProtectionType.Objects)](https://reference.aspose.com/cells/net/aspose.cells/worksheet/protect/#protect) metoden, som visas i följande exempelkod.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-1.cs" >}}

## **Hoe man låser upp specificerade former i ett skyddat kalkylblad**

För att låsa upp en angiven form i ett skyddat arbetsblad, använd [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/), som visas i följande exempelkod.

Observera: [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/) är meningsfull endast när arbetsbladet är skyddat.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-2.cs" >}}

