---
title: Accéder au Cells d'une feuille de calcul
type: docs
weight: 10
url: /fr/cpp/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}} 

Nous savons que toutes les feuilles de calcul peuvent contenir des données qui sont essentiellement stockées dans des cellules (qui composent une feuille de calcul). Une cellule est un élément de base d'une feuille de calcul utilisée pour construire l'ensemble de la feuille de calcul sous la forme d'une séquence de lignes et de colonnes. Avant d'essayer d'accéder aux données d'une feuille de calcul, nous devons accéder à ses cellules. Ainsi, dans cette rubrique, nous aborderons quelques approches de base pour accéder aux cellules d'une feuille de calcul au moment de l'exécution à l'aide de Aspose.Cells.

{{% /alert %}} 
##  **Accès au Cells**
 Aspose.Cells propose un cours[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Excel. Le[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la classe contient un[Des feuilles de calcul](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)collection qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. Le[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) la classe fournit un[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)collection qui représente toutes les cellules de la feuille de calcul.

 On peut utiliser[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)collection pour accéder aux cellules d’une feuille de calcul. Aspose.Cells propose trois approches de base pour accéder aux cellules d'une feuille de calcul :

1. En utilisant le nom de la cellule.
1. Utilisation de l'index de ligne et de colonne d'une cellule.
1.  Utiliser un index de cellule dans le[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)collection

{{% alert color="primary" %}} 

Nous avons mentionné que la 3ème approche est la plus rapide et la 1ère approche est la plus lente. La différence de performances entre les approches est très faible, ne vous inquiétez donc pas de la dégradation des performances, quelle que soit l'approche que vous utilisez.

{{% /alert %}} 
###  **Utilisation du nom Cell**
 Les développeurs peuvent accéder à n'importe quelle cellule spécifique en transmettant son nom de cellule au[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collecte des[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)classe comme index.

 Si vous créez une feuille de calcul vierge au début, le nombre de[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)la collecte est nulle. Lorsque vous utilisez cette approche pour accéder à une cellule, il vérifiera si cette cellule existe ou non dans la collection. Si oui, il renvoie l'objet cellule dans la collection sinon, il crée un nouveau[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) objet, ajoute l'objet à l'objet[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)collection, puis renvoie cet objet. Cette approche est le moyen le plus simple d'accéder à la cellule si vous êtes familier avec Excel Microsoft, mais c'est la plus lente par rapport aux autres approches.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingCellName-new.cpp" >}}
###  **Utilisation de l'index de lignes et de colonnes du Cell**
 Les développeurs peuvent accéder à n'importe quelle cellule spécifique en transmettant les indices de sa ligne et de sa colonne au[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collecte des[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)classe. Cette approche fonctionne de la même manière que celle de la première approche.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingRowAndColumnIndexOfTheCell-new.cpp" >}}
##  **Accès à la plage d'affichage maximale de la feuille de calcul**
Aspose.Cells permet aux développeurs d'accéder à la plage d'affichage maximale d'une feuille de calcul. La plage d'affichage maximale - la plage de cellules entre la première et la dernière cellule contenant du contenu - est utile lorsque vous devez copier, sélectionner ou afficher l'intégralité du contenu d'une feuille de calcul dans une image.

Vous pouvez accéder à la plage d'affichage maximale d'une feuille de calcul en utilisant[MaxDisplayRange](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) méthode du[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)collection.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingMaximumDisplayRangeOfWorksheet-new.cpp" >}}
