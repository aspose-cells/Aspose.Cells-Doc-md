---
title: Obtenir l index des cellules avec Golang via C++
linktitle: Obtenir l indice des cellules
type: docs
weight: 600
url: /fr/go-cpp/get-cells-index/
description: Apprenez comment obtenir l index de la ligne ou de la colonne par le nom de la ligne, de la colonne ou des cellules. Convertissez le nom de la cellule en index de ligne et de colonne zéro based en utilisant Aspose.Cells avec Golang via C++.
keywords: Obtenir l index de la ligne et de la colonne par le nom de la cellule, obtenir l index de la colonne par le nom de la colonne, obtenir l index de la ligne par le nom de la ligne, obtenir l index par le nom de la cellule.
---

{{% alert color="primary" %}}
La vue par défaut d’Excel utilise la référence A1, où chaque colonne est définie comme A, B, C...., et les cellules sont nommées A1, B2, C3... et ainsi de suite.
Vous souhaitez peut-être connaître la ligne et la colonne où se trouve cette cellule.

{{% /alert %}}

## **Scénarios d'utilisation possibles**

Lorsque vous devez uniquement manipuler des données spécifiques sur la feuille de calcul par l’index de ligne et de colonne, vous devez connaître ces indices.
Aspose.Cells permet cette fonctionnalité pour obtenir l’indice de ligne et de colonne par le nom de la ligne, de la colonne et de la cellule.
Aspose.Cells offre les propriétés et méthodes suivantes pour vous aider à atteindre vos objectifs :

- [**CellsHelper::CellNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/cellnametoindex/)
- [**CellsHelper::ColumnIndexToName**](https://reference.aspose.com/cells/go-cpp/cellshelper/columnindextoname/)
- [**CellsHelper::ColumnNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/columnnametoindex/)
- [**CellsHelper::RowIndexToName**](https://reference.aspose.com/cells/go-cpp/cellshelper/rowindextoname/)
- [**CellsHelper::RowNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/rownametoindex/)

Note : L’indice est basé sur zéro dans Aspose.Cells for C++, mais l’identifiant de la ligne est basé sur un dans MS Excel.

## **Obtenez les index des cellules en utilisant Aspose.Cells**

Cet exemple montre comment :

1. Créer un classeur et ajouter des données.
1. Trouver la cellule spécifique dans la première feuille de calcul.
1. Obtenir l'index de ligne et l'index de colonne par le nom de la cellule.
1. Obtenir l'index de colonne par le nom de la colonne.
1. Obtenir l'index de ligne par le nom de la ligne.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CellsIndex.go" >}}
