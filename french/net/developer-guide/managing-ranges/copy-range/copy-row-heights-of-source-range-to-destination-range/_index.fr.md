---
title: Copier la hauteur des lignes de la plage source vers la plage de destination
type: docs
weight: 590
url: /fr/net/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}}

Parfois, l'utilisateur a besoin de copier les hauteurs de ligne de la plage source vers la plage de destination. Aspose.Cells fournit l'énumération [**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype) à cet effet. Lorsque vous définirez la propriété [**PasteOptions.PasteType**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions/properties/pastetype) avec l'énumération [**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype), les hauteurs de toutes les lignes à l'intérieur de la plage source seront copiées vers la plage de destination.

{{% /alert %}}

Le code d'exemple suivant explique comment utiliser l'énumération [**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype) pour copier les hauteurs de ligne de la plage source dans la plage de destination. Une fois que vous ouvrirez le fichier Excel de sortie généré par ce code dans Microsoft Excel, vous verrez que les hauteurs de ligne de la plage de destination sont exactement les mêmes que celles de la plage source.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetRowHeights-GetRowHeightsOfSourceRangeToDestinationRange.cs" >}}
