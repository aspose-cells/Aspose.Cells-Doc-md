---
title: Spécification de la position absolue de l élément du tableau croisé dynamique
type: docs
weight: 50
url: /fr/net/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

Parfois, l'utilisateur doit spécifier la position absolue des éléments du tableau croisé dynamique. L'API Aspose.Cells a exposé quelques nouvelles propriétés et une méthode pour répondre aux besoins de l'utilisateur.

- Ajouté la propriété [**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position) qui peut être utilisée pour spécifier l'index de position dans tous les PivotItems indépendamment du nœud parent. Ajouté la propriété [**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) qui peut être utilisée pour spécifier l'index de position dans les PivotItems sous le même nœud parent.
- Ajout de la méthode [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) pour déplacer l'élément vers le haut ou vers le bas en fonction de la valeur du compteur, où le compteur est le nombre de positions pour déplacer l'élément du tableau croisé dynamique vers le haut ou vers le bas. Si la valeur du compteur est inférieure à zéro, l'élément sera déplacé vers le haut, alors que si la valeur du compteur est supérieure à zéro, l'élément du tableau croisé dynamique se déplacera vers le bas. Le paramètre de type booléen isSameParent spécifie si l'opération de déplacement doit être effectuée dans le même nœud parent ou non.
- Obsolète la méthode *PivotItem.Move(int count)*, il est donc conseillé d'utiliser la méthode nouvellement ajoutée [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) à la place.

{{% /alert %}}

Le code d'exemple suivant crée un tableau croisé dynamique et spécifie ensuite les positions des éléments du tableau croisé dynamique dans le même nœud parent. Vous pouvez télécharger les fichiers [Excel source](5112632.xlsx) et [Excel de sortie](5112619.xlsx) pour votre référence. Si vous ouvrez le fichier Excel de sortie, vous verrez l'élément du tableau croisé dynamique "4H12" est à la 0e position dans le parent "K11" et "DIF400" est à la 3e position. De même, CA32 est à la position 1 et AAA3 est à la position 2

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.cs" >}}

{{% alert color="primary" %}}

Veuillez noter qu'il est nécessaire d'appeler les méthodes PivotTable.RefreshData et PivotTable.CalculateData avant d'utiliser les propriétés [**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position), [**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) et la méthode [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move).

{{% /alert %}}
