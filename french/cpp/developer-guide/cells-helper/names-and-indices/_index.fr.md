---
title: Noms et indices
type: docs
weight: 10
url: /fr/cpp/names-and-indices/
---
##  **Obtenez le nom Cell à partir des index de lignes et de colonnes**
Il est possible de trouver le nom d'une cellule à partir de l'index de la ligne et de la colonne. Cet article explique comment.
 Aspose.Cells fournit le[CellsHelper ::CellIndexToName](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellindextoname/) méthode qui permet aux développeurs d'obtenir le nom d'une cellule s'ils fournissent l'index des lignes et des colonnes.

{{% alert color="primary" %}} 

Contrairement à Microsoft Excel, où les indices de ligne et de colonne commencent à 1, Aspose.Cells commence à compter les indices de ligne et de colonne à partir de 0.

{{% /alert %}} 

 L'exemple de code suivant illustre comment utiliser[CellsHelper ::CellIndexToName](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellindextoname/) pour accéder au nom d'une cellule à partir d'un index de ligne et de colonne connu. Le code génère la sortie suivante.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetCellNameFromRowAndColumn-new.cpp" >}}
##  **Obtenir les indices de lignes et de colonnes à partir du nom Cell**
Il est possible de retrouver un index de ligne et de colonne de la cellule à partir de son nom. Cet article explique comment.
 Aspose.Cells fournit le[CellsHelper.CellNameToIndex](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/) méthode qui permet aux développeurs d'obtenir un index de ligne et de colonne à partir du nom de la cellule.

{{% alert color="primary" %}} 

Contrairement à Microsoft Excel, où les indices de ligne et de colonne commencent à 1, Aspose.Cells commence à compter les indices de ligne et de colonne à partir de 0.

{{% /alert %}} 

 L'exemple de code suivant illustre comment utiliser[CellsHelper ::CellNameToIndex](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/)pour obtenir l'index de ligne et de colonne à partir du nom de la cellule. Le code génère la sortie suivante.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetRowAndColumnFromCellName-new.cpp" >}}
