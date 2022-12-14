---
title: Copier les hauteurs de ligne de la plage source dans la plage de destination
type: docs
weight: 590
url: /fr/net/copy-row-heights-of-source-range-to-destination-range/
---
{{% alert color="primary" %}}

 Parfois, l'utilisateur doit copier les hauteurs de ligne de la plage source dans la plage de destination. Aspose.Cells fournit[**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype) énumération à cet effet. Quand vous fixerez[**PasteOptions.PasteType**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions/properties/pastetype) propriété avec[**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype) enum alors les hauteurs de toutes les lignes à l'intérieur de la plage source seront copiées dans la plage de destination.

{{% /alert %}}

 L'exemple de code suivant explique comment utiliser[**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype)enum pour copier les hauteurs de ligne de la plage source dans la plage de destination. Une fois que vous aurez ouvert le fichier Excel de sortie généré par ce code dans Microsoft Excel, vous verrez que les hauteurs de ligne de la plage de destination sont exactement les mêmes que les hauteurs de ligne de la plage source.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetRowHeights-GetRowHeightsOfSourceRangeToDestinationRange.cs" >}}
