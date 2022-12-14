---
title: Obtenir la valeur de chaîne Cell avec et sans formatage
type: docs
weight: 230
url: /fr/java/get-cell-string-value-with-and-without-formatting/
---
{{% alert color="primary" %}} 

 Aspose.Cells fournit une méthode[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\) qui peut être utilisé pour obtenir la valeur de chaîne de la cellule avec ou sans formatage. Supposons que vous ayez une cellule avec la valeur 0,012345 et que vous l'ayez formatée pour n'afficher que deux décimales. Il s'affichera alors sous la forme 0,01 dans Excel. Vous pouvez récupérer des valeurs de chaîne à la fois 0,01 et 0,012345 à l'aide de la[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\) ) méthode. Ça prend[CellValueFormatStrategy](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy)enum comme paramètre qui a les valeurs suivantes

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL_STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY_STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **Obtenir la valeur de chaîne Cell avec et sans formatage**
 L'exemple de code suivant explique l'utilisation de[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)) méthode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **Sortie console**
Vous trouverez ci-dessous la sortie de la console de l'exemple de code ci-dessus.

{{< highlight "java" >}}

 0.01

0.012345

{{< /highlight >}}
