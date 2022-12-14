---
title: Kopiera radhöjder för källintervall till destinationsintervall
type: docs
weight: 590
url: /sv/net/copy-row-heights-of-source-range-to-destination-range/
---
{{% alert color="primary" %}}

 Ibland måste användaren kopiera radhöjder för källintervall till destinationsintervall. Aspose.Cells tillhandahåller[**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype) uppräkning för detta ändamål. När du ska ställa in[**PasteOptions.PasteType**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions/properties/pastetype) fastighet med[**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype) Enum så kommer höjderna på alla rader inom källområdet att kopieras till destinationsområdet.

{{% /alert %}}

 Följande exempelkod förklarar hur du använder[**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype)enum för att kopiera radhöjder för källintervall till destinationsintervall. När du väl har öppnat excel-filen som genereras av den här koden i Microsoft Excel, kommer du att se att destinationsintervallets radhöjder är exakt samma som källintervallets radhöjder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetRowHeights-GetRowHeightsOfSourceRangeToDestinationRange.cs" >}}
