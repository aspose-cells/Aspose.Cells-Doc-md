---
title: Spécification de la position absolue de l élément du tableau croisé dynamique
type: docs
weight: 50
url: /fr/nodejs-cpp/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

Parfois, l’utilisateur doit spécifier la position absolue des éléments de pivot, l’API Aspose.Cells for Node.js via C++ a exposé quelques nouvelles propriétés et une méthode pour répondre à cette exigence.

- Ajouté la propriété [**PivotItem.setPosition**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPosition-number-) qui peut être utilisée pour spécifier l'index de position dans tous les PivotItems indépendamment du nœud parent. Ajouté la propriété [**PivotItem.setPositionInSameParentNode**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPositionInSameParentNode-number-) qui peut être utilisée pour spécifier l'index de position dans les PivotItems sous le même nœud parent.
- Ajout de la méthode [**PivotItem.move**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-) pour déplacer l'élément vers le haut ou vers le bas en fonction de la valeur du compteur, où le compteur est le nombre de positions pour déplacer l'élément du tableau croisé dynamique vers le haut ou vers le bas. Si la valeur du compteur est inférieure à zéro, l'élément sera déplacé vers le haut, alors que si la valeur du compteur est supérieure à zéro, l'élément du tableau croisé dynamique se déplacera vers le bas. Le paramètre de type booléen isSameParent spécifie si l'opération de déplacement doit être effectuée dans le même nœud parent ou non.
- La méthode *PivotItem.move(int count)* étant obsolète, il est recommandé d’utiliser la nouvelle méthode [**PivotItem.move(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-).

{{% /alert %}}

Le code d'exemple suivant crée un tableau croisé dynamique et spécifie ensuite les positions des éléments du tableau croisé dynamique dans le même nœud parent. Vous pouvez télécharger les fichiers [Excel source](5112632.xlsx) et [Excel de sortie](5112619.xlsx) pour votre référence. Si vous ouvrez le fichier Excel de sortie, vous verrez l'élément du tableau croisé dynamique "4H12" est à la 0e position dans le parent "K11" et "DIF400" est à la 3e position. De même, CA32 est à la position 1 et AAA3 est à la position 2

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SpecifyAbsolutePositionOfPivotItem.js" >}}

{{% alert color="primary" %}}

Veuillez noter qu'il est nécessaire d'appeler les méthodes PivotTable.RefreshData et PivotTable.CalculateData avant d'utiliser les propriétés [**PivotItem.setPosition**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPosition-number-), [**PivotItem.setPositionInSameParentNode**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPositionInSameParentNode-number-) et la méthode [**PivotItem.move**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-).

{{% /alert %}}

