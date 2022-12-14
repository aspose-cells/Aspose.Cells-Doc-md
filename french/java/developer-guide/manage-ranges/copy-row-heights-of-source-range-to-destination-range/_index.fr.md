---
title: Copier les hauteurs de ligne de la plage source dans la plage de destination
type: docs
weight: 250
url: /fr/java/copy-row-heights-of-source-range-to-destination-range/
---
{{% alert color="primary" %}} 

 Parfois, l'utilisateur doit copier les hauteurs de ligne de la plage source dans la plage de destination. Aspose.Cells fournit[Type de collage.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS) énumération à cet effet. Quand vous fixerez[PasteOptions.setPasteType()](https://reference.aspose.com/cells/java/com.aspose.cells/pasteoptions#PasteType) propriété avec[Type de collage.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS) enum alors les hauteurs de toutes les lignes à l'intérieur de la plage source seront copiées dans la plage de destination.

{{% /alert %}} 
## **Copier les hauteurs de ligne de la plage source dans la plage de destination**
 L'exemple de code suivant explique comment utiliser[Type de collage.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS)enum pour copier les hauteurs de ligne de la plage source dans la plage de destination. Une fois que vous aurez ouvert le fichier Excel de sortie généré par ce code dans Microsoft Excel, vous verrez que les hauteurs de ligne de la plage de destination sont exactement les mêmes que les hauteurs de ligne de la plage source.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRowHeights-CopyRowHeights.java" >}}
