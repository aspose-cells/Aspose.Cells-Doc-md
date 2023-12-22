---
title: Obtenir l'indice Cells
type: docs
weight: 600
url: /fr/net/get-cells-index/
description: Découvrez comment obtenir une ligne ou une colonne par le nom de la ligne, de la colonne ou des cellules. Convertissez le nom de la cellule en index de ligne et de colonne de base zéro.
keywords: Get Row index and Column index by the name of the cell, Get Column index by the name of the column, Get Row index by the name of the row, Get the index by the name of cell. 
---
{{% alert color="primary" %}}
La vue par défaut d'Excel est la référence de style A1, chaque colonne est définie comme A, B, C.... et les cellules sont nommées comme A1, B2, C3... et ainsi de suite.
Vous voudrez peut-être savoir dans quelle ligne et dans quelle colonne se trouve cette cellule.

{{% /alert %}}


##  **Scénarios d'utilisation possibles**
 Lorsque vous avez uniquement besoin de manipuler des données spécifiques sur la feuille de calcul par index de ligne et de colonne, vous devez connaître les index de colonne et de colonne de cette cellule spécifique.
 Aspose.Cells offre cette fonctionnalité pour obtenir l'index des lignes et des colonnes par le nom de la ligne, de la colonne et de la cellule.
Aspose.Cells fournit les propriétés et méthodes suivantes pour vous aider à atteindre vos objectifs.
- [**CellsHelper.CellNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/cellnametoindex)
- [**CellsHelper.ColumnIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnindextoname)
- [**CellsHelper.ColumnNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnnametoindex)
- [**CellsHelper.RowIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rowindextoname)
- [**CellsHelper.RowNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rownametoindex)

Remarque : L'indexation est basée sur zéro dans Aspose.Cells pour .Net, mais l'identifiant de Row est basé sur un dans MS Excel.

##  **Obtenez les index Cells en utilisant Aspose.Cells**
Cet exemple montre comment :

1. Créez un classeur et ajoutez des données.
1. Recherchez la cellule spécifique dans la première feuille de calcul.
1. Obtenez l'index de ligne et l'index de colonne par le nom de la cellule.
1. Obtenez l'index de colonne par le nom de la colonne.
1. Obtenez l'index de ligne par le nom de la ligne.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-get-index.cs" >}}