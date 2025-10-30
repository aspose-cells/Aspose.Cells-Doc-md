---
title: Hur man får objektets position i diagrammet
description: Lär dig hur du hämtar objektspositioner i Excel diagram med Aspose.Cells for .NET. 
keywords: Aspose.Cells for .NET, Excel diagram, Hämta objektpositioner.
type: docs
weight: 74
url: /sv/net/how-to-get-object-position-in-chart/
---

## Möjliga användningsfall
I vissa scenarier kan du behöva få positionen för objekten i en Excel-diagram. Du kan enkelt uppnå detta krav med Aspose.Cells.

## Exempel: Hämta objektets position i diagrammet

Följande kod laddar [exempelfilen](TestFile.xlsx) och genererar [utdatafilen](Output.xlsx).
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "get-object-position-in-chart.cs" >}}

Med den ovanstående koden kan du få positionen för diagrammets titel och diagrammets PlotArea. 
Med positionsinformationen kan former placeras i motsvarande position i diagrammet. 
Resultatet visas på följande bild, där en form placeras i det övre vänstra hörnet av PlotArea och en annan form placeras under diagrammets titel.
![todo:image_alt_text](OutputResult.png)

## Enhetsförklaring och konvertering

Det finns tre enheter för objektets position i diagrammet:

1. Enheter för förhållandet av diagramområdet.

2. Enheter av 1/4000 av diagramområdet. Detta är en enhet som används i äldre versioner av Excel-filer och rekommenderas inte.

3. Enheter i pixel.

Deras konverteringskod visas i följande kod: 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "object-position-unit-in-chart.cs" >}}

{{< app/cells/assistant language="csharp" >}}
