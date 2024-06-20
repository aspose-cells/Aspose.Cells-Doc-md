---
title: Obtenir la valeur de la chaîne de la cellule avec et sans mise en forme
type: docs
weight: 230
url: /fr/java/get-cell-string-value-with-and-without-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells fournit une méthode [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)), qui peut être utilisée pour obtenir la valeur de chaîne de la cellule avec ou sans mise en forme. Supposons que vous ayez une cellule avec la valeur 0,012345 et que vous l'ayez formatée pour afficher uniquement deux décimales. Elle s'affichera alors comme 0,01 dans Excel. Vous pouvez récupérer les valeurs de chaîne à la fois comme 0,01 et comme 0,012345 en utilisant la méthode [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)). Elle prend en paramètre l'énumération [CellValueFormatStrategy](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy) avec les valeurs suivantes

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL_STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY_STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **Obtenir la valeur de chaîne de cellule avec et sans mise en forme**
Le code d'exemple suivant explique l'utilisation de la méthode [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **Sortie console**
Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

 0.01

0.012345

{{< /highlight >}}
