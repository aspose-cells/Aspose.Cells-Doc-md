---
title: Obtenir l indice des cellules
type: docs
weight: 600
url: /fr/python-net/get-cells-index/
description: Apprenez comment obtenir la ligne ou la colonne par le nom de la ligne à travers l API Aspose.Cells pour Python via .NET, la colonne ou les cellules. Convertissez le nom de la cellule en index de ligne et de colonne à base zéro à travers l API Aspose.Cells pour Python via .NET.
keywords: Python Excel, Obtenez l index de la ligne et de la colonne par le nom de la cellule en utilisant Python, Obtenez l index de la colonne par le nom de la colonne en utilisant Python, Obtenez l index de la ligne par le nom de la ligne en utilisant Python, Obtenez l index par le nom de la cellule en utilisant Python. 
---

{{% alert color="primary" %}}
La vue par défaut d'Excel est la référence de style A1, chaque colonne est définie comme A, B, C.... , et les cellules sont nommées A1, B2, C3... et ainsi de suite.
Vous pouvez vouloir savoir quelle est la ligne et la colonne de cette cellule.

{{% /alert %}}


## **Scénarios d'utilisation possibles**
Lorsque vous avez seulement besoin de manipuler des données spécifiques sur la feuille de calcul par index de ligne et de colonne, vous devez connaître les index de la colonne et de la ligne de cette cellule spécifique. 
Aspose.Cells for Python via .NET offre cette fonctionnalité pour obtenir l'index de la ligne et de la colonne par le nom de la ligne, de la colonne et de la cellule. 
Aspose.Cells pour Python via .NET propose les propriétés et méthodes suivantes pour vous aider à atteindre vos objectifs.
- [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any)
- [**CellsHelper.column_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/column_index_to_name/#int)
- [**CellsHelper.column_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/column_name_to_index/#str)
- [**CellsHelper.row_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/row_index_to_name/#int)
- [**CellsHelper.row_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/row_name_to_index/#str)

Remarque: L'indexation est basée sur zéro dans Aspose.Cells pour Python via .NET, mais l'identifiant de la ligne est basé sur un dans MS Excel.

## **Obtenez les index des cellules en utilisant la bibliothèque Excel Aspose.Cells for Python**
Cet exemple montre comment :

1. Créer un classeur et ajouter des données.
1. Trouver la cellule spécifique dans la première feuille de calcul.
1. Obtenir l'index de ligne et l'index de colonne par le nom de la cellule.
1. Obtenir l'index de colonne par le nom de la colonne.
1. Obtenir l'index de ligne par le nom de la ligne.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-get-index.py" >}}
