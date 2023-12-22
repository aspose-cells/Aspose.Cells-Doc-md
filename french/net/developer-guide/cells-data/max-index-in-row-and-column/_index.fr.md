---
title: Obtenir l'index de colonne maximum dans la ligne et l'index de ligne maximum dans la colonne
type: docs
weight: 600
url: /fr/net/get-max-index-in-row-and-column/
description: Découvrez comment obtenir l'index de colonne maximum dans la ligne et l'index de ligne maximum dans la colonne via le Aspose.Cells for .NET API.
keywords: Get Max Column Index in Row, Get Max Row Index in Column, Get Max Data Column Index in Row, Get Max Data Row Index in Column. 
---
##  **Scénarios d'utilisation possibles**
Lorsque vous avez uniquement besoin de manipuler certaines données sur les lignes ou les colonnes, vous devez connaître la plage de données des lignes et des colonnes. Aspose.Cells offre cette fonctionnalité. Pour obtenir l'index de colonne maximum sur une ligne, vous pouvez obtenir le[Ligne.LastCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/) et[Ligne.LastDataCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/) propriétés, puis utilisez le[Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) propriété pour obtenir l’index de colonne maximum et l’index de colonne de données maximum. Mais pour obtenir l'index de ligne maximum et l'index de données de ligne maximum sur une colonne, vous devez créer une plage sur la colonne, puis parcourir la plage pour trouver la dernière cellule, et enfin obtenir le[Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) attribut sur la cellule.

Aspose.Cells fournit les propriétés et méthodes suivantes pour vous aider à atteindre vos objectifs.
- [**Ligne.LastCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/)
- [**Ligne.LastDataCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/)
- [**Cell.Column**](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)
- [**Cell.Row**](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)

##  **Obtenez l'index de colonne maximum dans la ligne et l'index de ligne maximum dans la colonne en utilisant Aspose.Cells**
Cet exemple montre comment :

1.  Chargez le[exemple de fichier](sample.xlsx).
1. Obtenez la ligne qui doit obtenir l’index de colonne maximum et l’index de colonne de données maximum.
1.  Obtenir[Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) attribut sur la cellule.
1. Créez une plage basée sur la colonne.
1. Obtenez l’itérateur et la plage de parcours.
1.  Obtenir[Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) attribut sur la cellule.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-max-index-of-row-and-column.cs" >}}