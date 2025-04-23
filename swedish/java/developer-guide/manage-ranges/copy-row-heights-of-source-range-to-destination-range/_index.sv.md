---
title: Kopiera radhöjderna i källområdet till destinationsområdet
type: docs
weight: 250
url: /sv/java/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}} 

Ibland behöver användaren kopiera radhöjder för ett källdatum till destinationsområdet. Aspose.Cells tillhandahåller enumen [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW-HEIGHTS) för detta syfte. När du sätter egenskapen [PasteOptions.setPasteType()](https://reference.aspose.com/cells/java/com.aspose.cells/pasteoptions#PasteType) till enumen [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW-HEIGHTS) kommer höjderna för alla rader i källdatum att kopieras till destinationsområdet.

{{% /alert %}} 
## **Kopiera radhöjder från källspann till destinationspann**
Följande exempel visar hur du använder enumen [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW-HEIGHTS) för att kopiera radhöjder från källdatum till destinationsområde. När du öppnar utdata Excel-filen som genererats av denna kod i Microsoft Excel, kommer du att se att radhöjderna i destinationsområdet är exakt desamma som i källdatumet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRowHeights-CopyRowHeights.java" >}}
{{< app/cells/assistant language="java" >}}
