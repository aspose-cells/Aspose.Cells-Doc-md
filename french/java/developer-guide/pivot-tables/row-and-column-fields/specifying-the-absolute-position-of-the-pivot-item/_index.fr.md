---
title: Spécification de la position absolue de l élément de tableau croisé dynamique
type: docs
weight: 40
url: /fr/java/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

Parfois, l'utilisateur doit spécifier la position absolue des éléments du tableau croisé dynamique. L'API Aspose.Cells a exposé quelques nouvelles propriétés et une méthode pour répondre à cette exigence de l'utilisateur.

- Ajouté la propriété [**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position) qui peut être utilisée pour spécifier l'index de position dans tous les PivotItems indépendamment du nœud parent. Ajouté la propriété [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) qui peut être utilisée pour spécifier l'index de position dans les PivotItems sous le même nœud parent.
- Ajout de la méthode [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move-int-boolean-) afin de déplacer l'élément vers le haut ou vers le bas en fonction de la valeur de décompte, où le décompte est le nombre de positions à déplacer l'élément du tableau croisé dynamique vers le haut ou vers le bas. Si la valeur de décompte est inférieure à zéro, l'élément sera déplacé vers le haut, tandis que si la valeur de décompte est supérieure à zéro, l'élément du tableau croisé dynamique se déplacera vers le bas, le paramètre de type booléen isSameParent spécifiant si l'opération de déplacement doit être effectuée dans le même nœud parent ou non.
- Obsolète la méthode *PivotItem.move(int count)*, il est donc recommandé d'utiliser la méthode nouvellement ajoutée [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move-int-boolean-) à la place.

Veuillez noter qu'il est nécessaire d'appeler les méthodes [**PivotTable.refreshData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData--) et [**PivotTable.calculateData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData--) avant d'utiliser les propriétés [**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position), [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) et la méthode [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move-int-boolean-).

{{% /alert %}}

## Code d'exemple

Le code d'exemple suivant crée un tableau croisé dynamique, puis spécifie les positions des éléments du tableau croisé dynamique dans le même nœud parent.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.java" >}}
{{< app/cells/assistant language="java" >}}
