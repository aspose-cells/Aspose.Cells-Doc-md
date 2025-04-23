---
title: Kopiera radhöjderna i källområdet till destinationsområdet
type: docs
weight: 590
url: /sv/net/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}}

Ibland behöver användaren kopiera radhöjderna i källområdet till destinationsområdet. Aspose.Cells tillhandahåller [**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype)-uppställning för detta ändamål. När du anger [**PasteOptions.PasteType**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions/properties/pastetype)-egenskapen med [**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype)-uppställning kopieras höjderna på alla rader inne i källområdet till destinationsområdet.

{{% /alert %}}

Följande kodexempel förklarar hur man använder [**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype)-enumet för att kopiera radhöjder från källområdet till destinationsområdet. När du öppnar den genererade utfil i Microsoft Excel kommer du att se att destinationsområdets radhöjder är exakt desamma som källområdets radhöjder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetRowHeights-GetRowHeightsOfSourceRangeToDestinationRange.cs" >}}
{{< app/cells/assistant language="csharp" >}}
