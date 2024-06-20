---
title: Noms et Indices
type: docs
weight: 10
url: /fr/cpp/names-and-indices/
---

## **Obtenir le nom de cellule à partir des indices de ligne et de colonne**
Il est possible de trouver le nom d'une cellule en donnant l'index de ligne et de colonne. Cet article explique comment faire.
Aspose.Cells fournit la méthode [CellsHelper::CellIndexToName](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellindextoname/) qui permet aux développeurs d'obtenir le nom d'une cellule s'ils fournissent l'indice de ligne et de colonne.

{{% alert color="primary" %}} 

Contrairement à Microsoft Excel, où les index de lignes et de colonnes commencent à 1, Aspose.Cells commence à compter les index de lignes et de colonnes à partir de 0.

{{% /alert %}} 

Le code d'exemple suivant illustre comment utiliser [CellsHelper::CellIndexToName](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellindextoname/) pour accéder au nom d'une cellule en connaissant son indice de ligne et de colonne. Le code génère la sortie suivante.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetCellNameFromRowAndColumn-new.cpp" >}}
## **Obtenir les indices de ligne et de colonne à partir du nom de la cellule**
Il est possible de trouver un indice de ligne et de colonne de la cellule à partir de son nom. Cet article explique comment.
Aspose.Cells fournit la méthode [CellsHelper.CellNameToIndex](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/) qui permet aux développeurs d'obtenir l'indice de ligne et de colonne à partir du nom de la cellule.

{{% alert color="primary" %}} 

Contrairement à Microsoft Excel, où les index de lignes et de colonnes commencent à 1, Aspose.Cells commence à compter les index de lignes et de colonnes à partir de 0.

{{% /alert %}} 

Le code d'exemple suivant illustre comment utiliser [CellsHelper::CellNameToIndex](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/) pour obtenir l'indice de ligne et de colonne à partir du nom de la cellule. Le code génère la sortie suivante.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetRowAndColumnFromCellName-new.cpp" >}}
