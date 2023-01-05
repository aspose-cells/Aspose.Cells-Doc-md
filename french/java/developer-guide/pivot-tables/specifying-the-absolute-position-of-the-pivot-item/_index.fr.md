---
title: Spécification de la position absolue de l'élément pivot
type: docs
weight: 40
url: /fr/java/specifying-the-absolute-position-of-the-pivot-item/
---
{{% alert color="primary" %}}

Parfois, l'utilisateur a besoin de spécifier la position absolue des éléments de pivot, Aspose.Cells API a exposé quelques nouvelles propriétés et une méthode pour répondre à cette exigence de l'utilisateur.

-  Ajoutée[**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position) propriété qui peut être utilisée pour spécifier l'index de position dans tous les PivotItems quel que soit le nœud parent. Ajoutée[**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) propriété qui peut être utilisée pour spécifier l'index de position dans les PivotItems sous le même nœud parent.
-  Ajoutée[**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)afin de déplacer l'élément vers le haut ou vers le bas en fonction de la valeur du nombre, où le nombre est le nombre de positions pour déplacer le PivotItem vers le haut ou vers le bas. Si la valeur de comptage est inférieure à zéro, l'élément sera déplacé vers le haut alors que si la valeur de comptage est supérieure à zéro, le PivotItem se déplacera vers le bas, paramètre de type booléen isSameParent spécifiant si l'opération de déplacement doit être effectuée dans le même nœud parent ou ne pas.
-  Obsolète le*PivotItem.move(int count)* méthode, par conséquent, il est suggéré d'utiliser la méthode nouvellement ajoutée[**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)) au lieu.

 Attention, il faut téléphoner au[**PivotTable.refreshDataPivotTable.refreshData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData() ) et[**Tableau croisé dynamique.calculateData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData() ) méthodes avant d'utiliser[**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position), [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) propriétés et[**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)) méthode.

{{% /alert %}}

## Exemple de code

L'exemple de code suivant crée un tableau croisé dynamique, puis il spécifie les positions des éléments de pivot dans le même nœud parent.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.java" >}}
