---
title: Obtenir l indice de colonne maximal dans la ligne et l indice de ligne maximal dans la colonne
type: docs
weight: 600
url: /fr/python-net/get-max-index-in-row-and-column/
description: Découvrez comment obtenir l indice de colonne maximal dans la ligne et l indice de ligne maximal dans la colonne grâce à l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Python Excel, obtenir l indice de colonne maximal dans la ligne en Python, obtenir l indice de ligne maximal dans la colonne en Python, obtenir l indice de colonne de données maximal dans la ligne en Python, obtenir l indice de ligne de données maximal dans la colonne en Python. 
---

## **Scénarios d'utilisation possibles**
Lorsque vous avez seulement besoin de manipuler certaines données sur les lignes ou les colonnes, vous devez connaître la plage de données des lignes et des colonnes. Aspose.Cells pour Python via .NET offre cette fonctionnalité. Pour obtenir l'indice de colonne maximal sur une ligne, vous pouvez obtenir les propriétés [Row.last_cell](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_cell/) et [Row.last_data_cell](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_data_cell/), puis utiliser la propriété [Cell.column](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/) pour obtenir l'indice de colonne maximal et l'indice de colonne de données maximal. Mais pour obtenir l'indice de ligne maximal et l'indice de données de la ligne maximal sur une colonne, vous devez créer une plage sur la colonne, puis parcourir la plage pour trouver la dernière cellule, et enfin obtenir l'attribut [Cell.row](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/) sur la cellule.

Aspose.Cells pour Python via .NET propose les propriétés et méthodes suivantes pour vous aider à atteindre vos objectifs.
- [**Row.last_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_cell/)
- [**Row.last_data_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_data_cell/)
- [**Cell.column**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/)
- [**Cell.row**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/)

## **Obtenir l'indice de colonne maximal dans la ligne et l'indice de ligne maximal dans la colonne à l'aide de la bibliothèque Excel Aspose.Cells pour Python**
Cet exemple montre comment :

1. Charger le [fichier d'exemple](sample.xlsx).
1. Obtenir la ligne qui a besoin d'obtenir l'indice de colonne maximal et l'indice de colonne de données maximal.
1. Obtenez l'attribut [Cell.column](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/) sur la cellule.
1. Créez une plage basée sur la colonne.
1. Obtenez l'itérateur et parcourez la plage.
1. Obtenez l'attribut [Cell.row](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/) sur la cellule.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Cells-max-index-of-row-and-column.py" >}}
