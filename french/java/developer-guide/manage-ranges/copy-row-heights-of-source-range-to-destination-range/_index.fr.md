---
title: Copier la hauteur des lignes de la plage source vers la plage de destination
type: docs
weight: 250
url: /fr/java/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}} 

Parfois, l'utilisateur doit copier la hauteur des lignes de la plage source vers la plage de destination. Aspose.Cells offre la valeur de l'énumération [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW-HEIGHTS) à cet effet. En définissant la propriété [PasteOptions.setPasteType()](https://reference.aspose.com/cells/java/com.aspose.cells/pasteoptions#PasteType) avec l'énumération [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW-HEIGHTS), les hauteurs de toutes les lignes de la plage source seront copiées vers la plage de destination.

{{% /alert %}} 
## **Copier les hauteurs de ligne de la plage source vers la plage de destination**
Le code exemple suivant explique comment utiliser l'énumération [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW-HEIGHTS) pour copier la hauteur des lignes de la plage source vers la plage de destination. Une fois le fichier excel généré par ce code ouvert dans Microsoft Excel, vous verrez que les hauteurs des lignes de la plage de destination sont exactement les mêmes que celles de la plage source.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRowHeights-CopyRowHeights.java" >}}
{{< app/cells/assistant language="java" >}}
