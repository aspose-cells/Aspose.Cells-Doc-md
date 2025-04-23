---
title: Noms et Indices
type: docs
weight: 10
url: /fr/go-cpp/names-and-indices/
---

## **Obtenir le nom de cellule à partir des indices de ligne et de colonne**

Il est possible de trouver le nom d'une cellule en donnant l'index de ligne et de colonne. Cet article explique comment faire.
Aspose.Cells fournit la méthode [CellsHelper_CellIndexToName](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellindextoname/), qui permet aux développeurs d'obtenir le nom d'une cellule en fournissant l'index de la ligne et de la colonne.

{{% alert color="primary" %}}

Contrairement à Microsoft Excel, où les index de lignes et de colonnes commencent à 1, Aspose.Cells commence à compter les index de lignes et de colonnes à partir de 0.

{{% /alert %}}

Le code d'exemple suivant illustre comment utiliser [CellsHelper_CellIndexToName](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellindextoname/) pour accéder au nom d'une cellule donné un index de ligne et de colonne connu. Le code génère la sortie suivante.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetCellNameFromRowAndColumn.go" >}}

## **Obtenir les indices de ligne et de colonne à partir du nom de la cellule**

Il est possible de trouver un indice de ligne et de colonne de la cellule à partir de son nom. Cet article explique comment.
Aspose.Cells fournit la méthode [CellsHelper_CellNameToIndex](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellnametoindex/), qui permet aux développeurs d'obtenir un index de ligne et de colonne à partir du nom d'une cellule.

{{% alert color="primary" %}}

Contrairement à Microsoft Excel, où les index de lignes et de colonnes commencent à 1, Aspose.Cells commence à compter les index de lignes et de colonnes à partir de 0.

{{% /alert %}}

Le code d'exemple suivant illustre comment utiliser [CellsHelper_CellNameToIndex](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellnametoindex/) pour obtenir l'index de ligne et de colonne à partir du nom d'une cellule. Le code génère la sortie suivante.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetRowAndColumnFromCellName.go" >}}
