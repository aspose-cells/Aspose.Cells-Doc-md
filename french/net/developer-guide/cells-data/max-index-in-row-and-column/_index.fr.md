---
title: Obtenir l indice de colonne maximal dans la ligne et l indice de ligne maximal dans la colonne
type: docs
weight: 600
url: /fr/net/get-max-index-in-row-and-column/
description: Apprenez comment obtenir l indice de colonne maximal dans la rangée et l indice de rangée maximal dans la colonne à travers l API Aspose.Cells for .NET.
keywords: Obtenir l indice de colonne maximal dans la rangée, obtenir l indice de rangée maximal dans la colonne, obtenir l indice de colonne de données maximal dans la rangée, obtenir l indice de rangée de données maximal dans la colonne. 
---

## **Scénarios d'utilisation possibles**
Lorsque vous avez seulement besoin de manipuler certaines données sur les rangées ou colonnes, vous avez besoin de connaître la plage de données des rangées et colonnes. Aspose.Cells offre cette fonctionnalité. Pour obtenir l'indice de colonne maximal sur une rangée, vous pouvez obtenir les propriétés [Row.LastCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/) et [Row.LastDataCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/), puis utiliser la propriété [Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) pour obtenir l'indice de colonne maximal et l'indice de colonne de données maximal. Mais pour obtenir l'indice de rangée maximal et l'indice de données de rangée maximal sur une colonne, vous devez créer une plage sur la colonne, puis parcourir la plage pour trouver la dernière cellule, et enfin obtenir l'attribut [Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) sur la cellule.

Aspose.Cells fournit les propriétés et méthodes suivantes pour vous aider à atteindre vos objectifs.
- [**Row.LastCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/)
- [**Row.LastDataCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/)
- [**Cell.Column**](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)
- [**Cell.Row**](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)

## **Obtenir l'indice de colonne maximal dans la rangée et l'indice de rangée maximal dans la colonne en utilisant Aspose.Cells**
Cet exemple montre comment :

1. Charger le [fichier d'exemple](sample.xlsx).
1. Obtenir la ligne qui a besoin d'obtenir l'indice de colonne maximal et l'indice de colonne de données maximal.
1. Obtenir l'attribut [Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) sur la cellule.
1. Créez une plage basée sur la colonne.
1. Obtenez l'itérateur et parcourez la plage.
1. Obtenir l'attribut [Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) sur la cellule.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-max-index-of-row-and-column.cs" >}}
