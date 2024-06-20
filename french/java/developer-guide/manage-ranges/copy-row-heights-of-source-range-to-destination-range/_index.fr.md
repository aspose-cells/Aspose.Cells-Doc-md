---
title: Copier la hauteur des lignes de la plage source vers la plage de destination
type: docs
weight: 250
url: /fr/java/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}} 

Parfois, l'utilisateur a besoin de copier la hauteur des lignes de la plage source vers la plage de destination. Aspose.Cells fournit l'énumération [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS) à cet effet. Lorsque vous définirez la propriété [PasteOptions.setPasteType()](https://reference.aspose.com/cells/java/com.aspose.cells/pasteoptions#PasteType) avec l'énumération [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS), les hauteurs de toutes les lignes à l'intérieur de la plage source seront copiées vers la plage de destination.

{{% /alert %}} 
## **Copier les hauteurs de ligne de la plage source vers la plage de destination**
Le code d'exemple suivant explique comment utiliser l'énumération [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS) pour copier les hauteurs de lignes de la plage source dans la plage de destination. Une fois que vous ouvrirez le fichier Excel de sortie généré par ce code dans Microsoft Excel, vous verrez que les hauteurs de lignes de la plage de destination sont exactement les mêmes que celles de la plage source.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRowHeights-CopyRowHeights.java" >}}
