---
title: Spécification de la position absolue de l'élément pivot
type: docs
weight: 50
url: /fr/net/specifying-the-absolute-position-of-the-pivot-item/
---
{{% alert color="primary" %}}

Parfois, l'utilisateur doit spécifier la position absolue des éléments pivots, Aspose.Cells API a exposé quelques nouvelles propriétés et une méthode pour répondre aux besoins de l'utilisateur.

-  Ajoutée[**PivotItem.PositionPivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position) propriété qui peut être utilisée pour spécifier l'index de position dans tous les PivotItems quel que soit le nœud parent. Ajoutée[**PivotItem.PositionInSameParentNodePivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) propriété qui peut être utilisée pour spécifier l'index de position dans les PivotItems sous le même nœud parent.
-  Ajoutée[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move)afin de déplacer l'élément vers le haut ou vers le bas en fonction de la valeur count, où count est le nombre de positions pour déplacer le PivotItem vers le haut ou vers le bas. Si la valeur de comptage est inférieure à zéro, l'élément sera déplacé vers le haut où, comme si la valeur de comptage est supérieure à zéro, le PivotItem se déplacera vers le bas, le paramètre de type booléen isSameParent spécifie si l'opération de déplacement doit être effectuée dans le même nœud parent ou non.
-  Obsolète le*PivotItem.Move(int count)* méthode, il est donc suggéré d'utiliser la méthode nouvellement ajoutée[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) au lieu.

{{% /alert %}}

 L'exemple de code suivant crée un tableau croisé dynamique, puis il spécifie les positions des éléments de pivot dans le même nœud parent. Vous pouvez télécharger le[source Excel](5112632.xlsx) et[sortie Excel](5112619.xlsx) fichiers pour votre référence. Si vous ouvrez le fichier Excel de sortie, vous verrez que l'élément Pivot "4H12" est à la 0ème position dans le parent "K11" et "DIF400" est à la 3ème position. De même, CA32 est en position 1 et AAA3 est en position 2

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.cs" >}}

{{% alert color="primary" %}}

Veuillez noter qu'il est nécessaire d'appeler les méthodes PivotTable.RefreshData et PivotTable.CalculateData avant d'utiliser[**PivotItem.PositionPivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position), [**PivotItem.PositionInSameParentNodePivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) propriétés et[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) méthode.

{{% /alert %}}
