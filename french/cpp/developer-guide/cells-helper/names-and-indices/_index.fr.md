---
title: Noms et indices
type: docs
weight: 10
url: /fr/cpp/names-and-indices/
---
## **Obtenir le nom Cell à partir des indices de ligne et de colonne**
Il est possible de trouver le nom d'une cellule à partir de l'index de ligne et de colonne. Cet article explique comment.
Aspose.Cells fournit la méthode ICellsHelper.CellIndexToName_i qui permet aux développeurs d'obtenir le nom d'une cellule s'ils fournissent l'index de ligne et de colonne.

{{% alert color="primary" %}} 

Contrairement à Microsoft Excel, où les indices de ligne et de colonne commencent à 1, Aspose.Cells commence à compter les indices de ligne et de colonne à partir de 0.

{{% /alert %}} 

L'exemple de code suivant illustre comment utiliser ICellsHelper.CellIndexToName_i pour accéder au nom d'une cellule à partir d'un index de ligne et de colonne connu. Le code génère la sortie suivante.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetCellNameFromRowAndColumn.cpp" >}}
## **Obtenir les indices de ligne et de colonne à partir du nom Cell**
Il est possible de trouver un index de ligne et de colonne de la cellule à partir de son nom. Cet article explique comment.
Aspose.Cells fournit la méthode ICellsHelper.CellNameToIndex_i qui permet aux développeurs d'obtenir un index de ligne et de colonne à partir du nom de la cellule.

{{% alert color="primary" %}} 

Contrairement à Microsoft Excel, où les indices de ligne et de colonne commencent à 1, Aspose.Cells commence à compter les indices de ligne et de colonne à partir de 0.

{{% /alert %}} 

L'exemple de code suivant montre comment utiliser CellsHelper.CellNameToIndex pour obtenir l'index de ligne et de colonne à partir du nom de la cellule. Le code génère la sortie suivante.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetRowAndColumnFromCellName.cpp" >}}
