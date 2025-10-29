---
title: Obtenir l indice des cellules
type: docs
weight: 600
url: /fr/nodejs-cpp/get-cells-index/
description: Apprenez comment obtenir la ligne ou la colonne par le nom de la ligne, de la colonne ou des cellules. Convertissez le nom de la cellule en index de ligne et de colonne à base zéro.
keywords: Obtenir l index de la ligne et de la colonne par le nom de la cellule, obtenir l index de la colonne par le nom de la colonne, obtenir l index de la ligne par le nom de la ligne, obtenir l index par le nom de la cellule. 
---

{{% alert color="primary" %}}
La vue par défaut d'Excel est la référence de style A1, chaque colonne est définie comme A, B, C.... , et les cellules sont nommées A1, B2, C3... et ainsi de suite.
Vous pouvez vouloir savoir quelle est la ligne et la colonne de cette cellule.

{{% /alert %}}


## **Scénarios d'utilisation possibles**
Lorsque vous avez seulement besoin de manipuler des données spécifiques sur la feuille de calcul par index de ligne et de colonne, vous devez connaître les index de la colonne et de la ligne de cette cellule spécifique. 
Aspose.Cells for Node.js via C++ offre cette fonctionnalité pour obtenir l'index de ligne et de colonne par le nom de la ligne, de la colonne et de la cellule. 
Aspose.Cells for Node.js via C++ fournit les propriétés et méthodes suivantes pour vous aider à atteindre vos objectifs.
- [**CellsHelper.cellNameToIndex(string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#cellNameToIndex-string-)
- [**CellsHelper.columnIndexToName**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#columnIndexToName-number-)
- [**CellsHelper.columnNameToIndex**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#columnNameToIndex-string-)
- [**CellsHelper.rowIndexToName**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#rowIndexToName-number-)
- [**CellsHelper.rowNameToIndex**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#rowNameToIndex-string-)

Note : L'indexation est basée sur zéro dans Aspose.Cells for Node.js via C++, mais l'identifiant de la ligne est basé sur un dans MS Excel.

## **Obtenir les index des cellules en utilisant Aspose.Cells for Node.js via C++**
Cet exemple montre comment :

1. Créer un classeur et ajouter des données.
1. Trouver la cellule spécifique dans la première feuille de calcul.
1. Obtenir l'index de ligne et l'index de colonne par le nom de la cellule.
1. Obtenir l'index de colonne par le nom de la colonne.
1. Obtenir l'index de ligne par le nom de la ligne.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-get-index.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
