---
title: Accès aux cellules d une feuille de calcul
type: docs
weight: 10
url: /fr/cpp/accessing-cells-of-a-worksheet/
---

{{% alert color="primary" %}} 

Nous savons que toutes les feuilles de calcul peuvent contenir des données qui sont essentiellement stockées dans des cellules (avec lesquelles une feuille de calcul est constituée). Une cellule est une partie fondamentale d'une feuille de calcul qui est utilisée pour construire la feuille de calcul entière sous forme de séquence de lignes et de colonnes. Avant d'essayer d'accéder aux données d'une feuille de calcul, nous aurions besoin d'accéder à ses cellules. Ainsi, dans ce sujet, nous discuterons de quelques approches de base pour accéder aux cellules de la feuille de calcul lors de l'exécution en utilisant Aspose.Cells.

{{% /alert %}} 
## **Accéder aux cellules**
Aspose.Cells fournit une classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection de [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fournit une collection de [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) qui représente toutes les cellules de la feuille de calcul.

Nous pouvons utiliser la collection de [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) pour accéder aux cellules d'une feuille de calcul. Aspose.Cells fournit trois approches de base pour accéder aux cellules d'une feuille de calcul :

1. En utilisant le nom de la cellule.
2. Utiliser l'index de la ligne et de la colonne de la cellule.
1. En utilisant l'indice d'une cellule dans la collection de [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)

{{% alert color="primary" %}} 

Nous avons mentionné que la 3ème approche est la plus rapide et que la 1ère approche est la plus lente. La différence de performances entre les approches est très faible, alors ne vous inquiétez pas de la dégradation des performances, quelle que soit l'approche que vous utilisez.

{{% /alert %}} 
### **Utilisation du nom de la cellule**
Les développeurs peuvent accéder à une cellule spécifique en passant son nom de cellule à la collection [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) de la classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) en tant qu'index.

Si vous créez une feuille de calcul vide au début, le nombre d'éléments de la collection [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) est zéro. Lorsque vous utilisez cette approche pour accéder à une cellule, elle vérifie si cette cellule existe dans la collection ou non. Si oui, elle renvoie l'objet de la cellule de la collection, sinon, elle crée un nouvel objet [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/), ajoute l'objet à la collection [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) et renvoie cet objet. Cette approche est la façon la plus simple d'accéder à la cellule si vous êtes familier avec Microsoft Excel mais c'est la plus lente par rapport aux autres approches.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingCellName-new.cpp" >}}
### **Utilisation de l'index de la ligne et de la colonne de la cellule**
Les développeurs peuvent accéder à une cellule spécifique en passant les indices de sa ligne et de sa colonne à la collection [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) de la classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Cette approche fonctionne de la même manière que la première approche.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingRowAndColumnIndexOfTheCell-new.cpp" >}}
## **Accéder à la plage d'affichage maximale d'une feuille de calcul**
Aspose.Cells permet aux développeurs d'accéder à la plage d'affichage maximale d'une feuille de calcul. La plage d'affichage maximale - la plage de cellules entre la première et la dernière cellule contenant du contenu - est utile lorsque vous devez copier, sélectionner ou afficher l'ensemble du contenu d'une feuille de calcul dans une image.

Vous pouvez accéder à la plage d'affichage maximale d'une feuille de calcul en utilisant la méthode [MaxDisplayRange](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) de la collection [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingMaximumDisplayRangeOfWorksheet-new.cpp" >}}
