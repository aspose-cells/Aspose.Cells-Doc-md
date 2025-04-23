---
title: Accès aux cellules d une feuille de calcul
type: docs
weight: 10
url: /fr/nodejs-cpp/accessing-cells-of-a-worksheet/
description: Cet article explique comment obtenir la plage de visualisation maximale d une feuille de calcul et accéder aux cellules via l API de Aspose.Cells for Node.js via C++.
keywords: Obtenir un objet de cellule, Accéder aux cellules, Obtenir la plage d affichage maximale de la feuille de calcul. 
---

{{% alert color="primary" %}}

Nous savons que toutes les feuilles de calcul peuvent contenir des données essentiellement stockées dans des cellules (dont une feuille est composée). Une cellule est une partie fondamentale d'une feuille de calcul utilisée pour construire toute la feuille sous forme de lignes et de colonnes. Avant de tenter d'accéder aux données d'une feuille, nous devons y accéder. Dans ce sujet, nous discuterons de quelques méthodes de base pour accéder aux cellules d'une feuille au runtime en utilisant Aspose.Cells for Node.js via C++.

{{% /alert %}}

## **Comment accéder aux cellules**

Aspose.Cells for Node.js via C++ fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient un [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) qui permet d'accéder à chaque feuille dans le fichier Excel. Une feuille est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) qui représente toutes les cellules de la feuille.

Nous pouvons utiliser la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) pour accéder aux cellules dans une feuille. Aspose.Cells for Node.js via C++ offre trois approches de base pour accéder aux cellules dans une feuille :

1. Utiliser le nom de la cellule.
2. Utiliser l'index de la ligne et de la colonne de la cellule.
3. Utiliser un index de cellule dans la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells).

**IMPORTANT :** Nous avons mentionné que la 3ème approche est la plus rapide et la 1ère approche est la plus lente. La différence de performance entre les approches est très faible, donc ne vous inquiétez pas de la dégradation des performances, quelle que soit l'approche que vous utilisez.

### **Comment obtenir l'objet de cellule par le nom de la cellule**

Les développeurs peuvent accéder à n'importe quelle cellule spécifique en passant son nom de cellule à la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) de la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) en tant qu'index.

Si vous créez une feuille de calcul vide au départ, le nombre de la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) est zéro. Lorsque vous utilisez cette approche pour accéder à une cellule, elle vérifie si cette cellule existe dans la collection ou non. Si oui, elle renvoie l'objet de cellule dans la collection, sinon elle crée un nouvel objet [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell), ajoute l'objet à la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells), puis renvoie l'objet. Cette approche est la manière la plus simple d'accéder à la cellule si vous êtes familiarisé avec Microsoft Excel, mais c'est la plus lente par rapport aux autres approches.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingCellName-1.js" >}}

### **Comment obtenir l'objet de cellule par l'index de la ligne et de la colonne de la cellule**

Les développeurs peuvent accéder à n'importe quelle cellule spécifique en passant les indices de sa ligne et de sa colonne à la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) de la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

Cette approche fonctionne de la même manière que la première approche.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingRowAndColumnIndexOfCell-1.js" >}}

### **Comment obtenir l'objet de cellule par l'index de la cellule dans la collection de cellules**

Une cellule peut également être accédée en passant l'index numérique de la cellule à la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells).

Si vous utilisez cette approche pour accéder aux cellules, une exception peut être levée si l'index numérique de la cellule est hors de portée. Cette approche est la plus rapide pour accéder aux cellules, mais une chose importante à savoir est que si vous utilisez cette approche pour accéder à un objet de cellule, l'index numérique peut changer après l'ajout de nouvelles cellules à la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Les objets de cellules dans la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) sont triés en interne par les indices de ligne et de colonne.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingCellIndexInCellsCollection-1.js" >}}

## **Comment obtenir la plage d'affichage maximale de la feuille de calcul**

Aspose.Cells for Node.js via C++ pour Node.js via C++ permet aux développeurs d'accéder à la plage d'affichage maximale d'une feuille. La plage d'affichage maximale — la plage de cellules entre la première et la dernière cellule contenant du contenu — est utile lorsque vous souhaitez copier, sélectionner ou afficher tout le contenu d'une feuille dans une image.

Vous pouvez accéder à la plage d'affichage maximale d'une feuille de calcul en utilisant [**Cells.getMaxDisplayRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--). Le code d'exemple suivant illustre comment accéder à la propriété [**getMaxDisplayRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.js" >}}

