---
title: Accès aux cellules d une feuille de calcul
type: docs
weight: 10
url: /fr/python-net/accessing-cells-of-a-worksheet/
description: Cet article montre comment obtenir la plage d affichage maximale de la feuille de calcul et accéder aux cellules à travers l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Excel Python, objet Cell, Accès aux cellules, Comment obtenir l objet Cell par index de ligne et de colonne de la cellule, Comment obtenir l objet Cell par index de cellule dans la collection de cellules, Comment obtenir l objet Cell par index de ligne et de colonne de la cellule, Obtenir la plage d affichage maximale de la feuille de calcul. 
---

{{% alert color="primary" %}}

Nous savons que toutes les feuilles de calcul peuvent contenir des données qui sont essentiellement stockées dans des cellules (avec lesquelles une feuille de calcul est constituée). Une cellule est une partie de base d'une feuille de calcul qui est utilisée pour construire toute la feuille de calcul comme une séquence de lignes et de colonnes. Avant d'essayer d'accéder aux données d'une feuille de calcul, nous devrions accéder à ses cellules. Ainsi, dans ce sujet, nous discuterons de quelques approches de base pour accéder aux cellules de la feuille de calcul en cours d'exécution à l'aide d'Aspose.Cells pour Python via .NET.

{{% /alert %}}

## **Comment accéder aux cellules**

Aspose.Cells pour Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient un [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) qui représente toutes les cellules de la feuille de calcul.

Nous pouvons utiliser la collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) pour accéder aux cellules dans une feuille de calcul. Aspose.Cells for Python via .NET propose trois approches de base pour accéder aux cellules dans une feuille de calcul :

1. Utiliser le nom de la cellule.
2. Utiliser l'index de la ligne et de la colonne de la cellule.
3. Utiliser un index de cellule dans la collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells).

**IMPORTANT :** Nous avons mentionné que la 3ème approche est la plus rapide et la 1ère approche est la plus lente. La différence de performance entre les approches est très faible, donc ne vous inquiétez pas de la dégradation des performances, quelle que soit l'approche que vous utilisez.

### **Comment obtenir l'objet de cellule par le nom de la cellule**

Les développeurs peuvent accéder à n'importe quelle cellule spécifique en passant son nom de cellule à la collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) de la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) en tant qu'index.

Si vous créez une feuille de calcul vide au départ, le nombre de la collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) est zéro. Lorsque vous utilisez cette approche pour accéder à une cellule, elle vérifie si cette cellule existe dans la collection ou non. Si oui, elle renvoie l'objet de cellule dans la collection, sinon elle crée un nouvel objet [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell), ajoute l'objet à la collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells), puis renvoie l'objet. Cette approche est la manière la plus simple d'accéder à la cellule si vous êtes familiarisé avec Microsoft Excel, mais c'est la plus lente par rapport aux autres approches.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingCellName-1.py" >}}

### **Comment obtenir l'objet de cellule par l'index de la ligne et de la colonne de la cellule**

Les développeurs peuvent accéder à n'importe quelle cellule spécifique en passant les indices de sa ligne et de sa colonne à la collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) de la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

Cette approche fonctionne de la même manière que la première approche.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingRowAndColumnIndexOfCell-1.py" >}}

### **Comment obtenir l'objet de cellule par l'index de la cellule dans la collection de cellules**

Une cellule peut également être accédée en passant l'index numérique de la cellule à la collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells).

Si vous utilisez cette approche pour accéder aux cellules, une exception peut être levée si l'index numérique de la cellule est hors de portée. Cette approche est la plus rapide pour accéder aux cellules, mais une chose importante à savoir est que si vous utilisez cette approche pour accéder à un objet de cellule, l'index numérique peut changer après l'ajout de nouvelles cellules à la collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Les objets de cellules dans la collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) sont triés en interne par les indices de ligne et de colonne.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingCellIndexInCellsCollection-1.py" >}}

## **Comment obtenir la plage d'affichage maximale de la feuille de calcul**

Aspose.Cells pour Python via .NET permet aux développeurs d'accéder à la plage d'affichage maximale d'une feuille de calcul. La plage d'affichage maximale - la plage de cellules entre la première et la dernière cellule contenant du contenu - est utile lorsque vous devez copier, sélectionner ou afficher l'ensemble du contenu d'une feuille de calcul dans une image.

Vous pouvez accéder à la plage d'affichage maximale d'une feuille de calcul en utilisant [**Worksheet.cells.max_display_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_display_range/). Le code d'exemple suivant illustre comment accéder à la propriété [**MaxDisplayRange**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_display_range/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
