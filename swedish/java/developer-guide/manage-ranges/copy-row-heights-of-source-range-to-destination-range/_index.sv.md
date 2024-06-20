---
title: Kopiera radhöjderna i källområdet till destinationsområdet
type: docs
weight: 250
url: /sv/java/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}} 

Ibland behöver användaren kopiera radhöjder från källområdet till destinationen. Aspose.Cells tillhandahåller [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS) enum för detta ändamål. När du anger [PasteOptions.setPasteType()](https://reference.aspose.com/cells/java/com.aspose.cells/pasteoptions#PasteType) egenskapen med [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS) enum, kommer höjderna på alla rader inuti källområdet att kopieras till destinationen.

{{% /alert %}} 
## **Kopiera radhöjder från källspann till destinationspann**
Följande kodsnutt förklarar hur man använder [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS) enum för att kopiera radhöjder från källområdet till destinationen. När du öppnar den genererade Excel-filen i Microsoft Excel kommer du att se att destinationens radhöjder är exakt desamma som källoradernas höjder.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRowHeights-CopyRowHeights.java" >}}
