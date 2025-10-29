---
title: Obtenir l indice de la colonne maximale dans une ligne et l indice de la ligne maximale dans une colonne avec Golang via C++
linktitle: Obtenir l indice de colonne maximal dans la ligne et l indice de ligne maximal dans la colonne
type: docs
weight: 600
url: /fr/go-cpp/get-max-index-in-row-and-column/
description: Découvrez comment obtenir l’indice de la colonne maximale dans une ligne et l’indice de la ligne maximale dans une colonne via l’API Aspose.Cells for C++.
keywords: Obtenir l indice de colonne maximal dans la rangée, obtenir l indice de rangée maximal dans la colonne, obtenir l indice de colonne de données maximal dans la rangée, obtenir l indice de rangée de données maximal dans la colonne.
---

## **Scénarios d'utilisation possibles**
 Lorsque vous avez seulement besoin de manipuler certaines données sur les lignes ou colonnes, vous devez connaître la plage de données des lignes et colonnes. Aspose.Cells offre cette fonctionnalité. Pour obtenir l'indice de colonne maximale sur une ligne, vous pouvez utiliser les propriétés [Row.GetLastCell()](https://reference.aspose.com/cells/go-cpp/row/getlastcell/) et [Row.GetLastDataCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/), puis utiliser la propriété [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) pour obtenir l'indice de colonne maximum et l'indice de la dernière colonne de données. Mais pour obtenir l'indice de ligne maximum et l'indice de la dernière ligne de données dans une colonne, vous devez créer une plage sur la colonne, puis parcourir cette plage pour trouver la dernière cellule, et finalement obtenir l'attribut [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) sur la cellule.

Aspose.Cells fournit les propriétés et méthodes suivantes pour vous aider à atteindre vos objectifs.
- [**Row.GetLastCell()**](https://reference.aspose.com/cells/go-cpp/row/getlastcell/)
- [**Row.GetLastDataCell()**](https://reference.aspose.com/cells/go-cpp/row/getlastdatacell/)
- [**Cell.GetColumn()**](https://reference.aspose.com/cells/go-cpp/cell/getcolumn/)
- [**Cell.GetRow()**](https://reference.aspose.com/cells/go-cpp/cell/getrow/)

## **Obtenir l'indice de colonne maximal dans la rangée et l'indice de rangée maximal dans la colonne en utilisant Aspose.Cells**
Cet exemple montre comment :

1. Charger le [fichier d'exemple](sample.xlsx).
1. Obtenir la ligne qui a besoin d'obtenir l'indice de colonne maximal et l'indice de colonne de données maximal.
1. Obtenir l'attribut [Cell.GetColumn()](https://reference.aspose.com/cells/go-cpp/cell/getcolumn/) sur la cellule.
1. Créez une plage basée sur la colonne.
1. Obtenez l'itérateur et parcourez la plage.
1. Obtenir l'attribut [Cell.GetRow()](https://reference.aspose.com/cells/go-cpp/cell/getrow/) sur la cellule.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MaxIndexInRowAndColumn.go" >}}
