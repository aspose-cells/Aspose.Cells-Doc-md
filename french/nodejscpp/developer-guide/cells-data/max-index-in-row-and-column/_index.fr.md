---
title: Obtenir l indice de colonne maximal dans la ligne et l indice de ligne maximal dans la colonne
type: docs
weight: 600
url: /fr/nodejs-cpp/get-max-index-in-row-and-column/
description: Apprenez comment obtenir l’indice de la colonne maximale dans une ligne et l’indice de la ligne maximale dans une colonne via l’API Aspose.Cells for Node.js via C++.
keywords: Obtenir l indice de la colonne maximale dans une ligne via Node.js en C++, Obtenir l indice de la ligne maximale dans une colonne via Node.js en C++, Obtenir l’indice de la colonne de données maximale dans une ligne via Node.js en C++, Obtenir l’indice de la ligne de données maximale dans une colonne via Node.js en C++.
---

## **Scénarios d'utilisation possibles**
Lorsque vous avez seulement besoin de manipuler certaines données sur les lignes ou les colonnes, vous devez connaître la plage de données des lignes et des colonnes. Aspose.Cells for Node.js via C++ offre cette fonctionnalité. Pour obtenir l’indice de la colonne maximale d'une ligne, vous pouvez utiliser les méthodes [**Row.getLastCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastCell--) et [**Row.getLastDataCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastDataCell--), puis utiliser la méthode [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--) pour obtenir l’indice de la colonne maximale et l’indice de la colonne de données maximale. Mais pour obtenir l’indice de la ligne maximale et l’indice de la ligne de données maximale d'une colonne, vous devez créer une plage sur la colonne, puis parcourir la plage pour trouver la dernière cellule, et enfin appeler la méthode [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--) sur la cellule.

Aspose.Cells for Node.js via C++ fournit les propriétés et méthodes suivantes pour vous aider à atteindre vos objectifs.
- [**Row.getLastCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastCell--)
- [**Row.getLastDataCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastDataCell--)
- [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--)
- [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--)

## **Obtenir l’indice de la colonne maximale dans une ligne et l’indice de la ligne maximale dans une colonne**
Cet exemple montre comment :

1. Charger le [fichier d'exemple](sample.xlsx).
1. Obtenir la ligne qui a besoin d'obtenir l'indice de colonne maximal et l'indice de colonne de données maximal.
1. Appeler la méthode [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--) sur la cellule.
1. Créez une plage basée sur la colonne.
1. Obtenez l'itérateur et parcourez la plage.
1. Appeler la méthode [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--) sur la cellule.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-max-index-in-row-and-column.js" >}}

