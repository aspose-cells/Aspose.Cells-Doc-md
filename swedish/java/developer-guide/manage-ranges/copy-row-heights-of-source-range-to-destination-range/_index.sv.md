---
title: Kopiera radhöjder för källintervall till destinationsintervall
type: docs
weight: 250
url: /sv/java/copy-row-heights-of-source-range-to-destination-range/
---
{{% alert color="primary" %}} 

 Ibland måste användaren kopiera radhöjder för källintervall till destinationsintervall. Aspose.Cells tillhandahåller[PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS) uppräkning för detta ändamål. När du ska ställa in[PasteOptions.setPasteType()](https://reference.aspose.com/cells/java/com.aspose.cells/pasteoptions#PasteType) fastighet med[PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS) Enum så kommer höjderna på alla rader inom källområdet att kopieras till destinationsområdet.

{{% /alert %}} 
## **Kopiera radhöjder för källintervall till destinationsintervall**
 Följande exempelkod förklarar hur du använder[PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS)enum för att kopiera radhöjder för källintervall till destinationsintervall. När du öppnar excel-filen som genereras av den här koden i Microsoft Excel, kommer du att se att destinationsintervallets radhöjder är exakt samma som källintervallets radhöjder.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRowHeights-CopyRowHeights.java" >}}
