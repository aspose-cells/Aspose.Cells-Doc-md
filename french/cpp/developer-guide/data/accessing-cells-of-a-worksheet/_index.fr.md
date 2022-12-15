---
title: Accéder au Cells d'une feuille de calcul
type: docs
weight: 10
url: /fr/cpp/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}} 

Nous savons que toutes les feuilles de calcul peuvent contenir des données qui sont essentiellement stockées dans des cellules (avec lesquelles une feuille de calcul est composée). Une cellule est une partie de base d'une feuille de calcul utilisée pour construire la feuille de calcul entière sous la forme d'une séquence de lignes et de colonnes. Avant d'essayer d'accéder aux données d'une feuille de calcul, nous aurions besoin d'accéder à ses cellules. Ainsi, dans cette rubrique, nous aborderons certaines approches de base pour accéder aux cellules de feuille de calcul lors de l'exécution à l'aide de Aspose.Cells.

{{% /alert %}} 
## **Accéder au Cells**
 Aspose.Cells fournit une classe[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) qui représente un fichier Excel. La[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) classe contient un[Des feuilles de calcul](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)collection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[Feuille de calcul](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classer. La[Feuille de calcul](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) la classe offre une[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collection qui représente toutes les cellules de la feuille de calcul.

 On peut utiliser[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collection pour accéder aux cellules d'une feuille de calcul. Aspose.Cells propose trois approches de base pour accéder aux cellules d'une feuille de calcul :

1. Utilisation du nom de cellule.
1. Utilisation de l'index de ligne et de colonne d'une cellule.
1.  L'utilisation d'un index de cellule dans le[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)le recueil

{{% alert color="primary" %}} 

Nous avons mentionné que la 3ème approche est la plus rapide et la 1ère approche est la plus lente. La différence de performances entre les approches est très faible, ne vous inquiétez donc pas de la dégradation des performances, quelle que soit l'approche que vous utilisez.

{{% /alert %}} 
### **Utilisation du nom Cell**
 Les développeurs peuvent accéder à n'importe quelle cellule spécifique en transmettant son nom de cellule au[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) collecte de la[Feuille de calcul](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)classe comme index.

 Si vous créez une feuille de calcul vierge au début, le nombre de[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)la collecte est nulle. Lorsque vous utilisez cette approche pour accéder à une cellule, il vérifie si cette cellule existe dans la collection ou non. Si oui, il renvoie l'objet cellule dans la collection sinon, il crée un nouveau[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) objet, ajoute l'objet au[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collection, puis renvoie cet objet. Cette approche est le moyen le plus simple d'accéder à la cellule si vous connaissez Excel Microsoft, mais c'est la plus lente par rapport aux autres approches.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingCellName.cpp" >}}
### **Utilisation de l'index des lignes et des colonnes du Cell**
 Les développeurs peuvent accéder à n'importe quelle cellule spécifique en transmettant les indices de sa ligne et de sa colonne au[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) collecte de la[Feuille de calcul](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)classer. Cette approche fonctionne de la même manière que celle de la première approche.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingRowAndColumnIndexOfTheCell.cpp" >}}
## **Accès à la plage d'affichage maximale de la feuille de calcul**
Aspose.Cells permet aux développeurs d'accéder à la plage d'affichage maximale d'une feuille de calcul. La plage d'affichage maximale - la plage de cellules entre la première et la dernière cellule avec du contenu - est utile lorsque vous devez copier, sélectionner ou afficher tout le contenu d'une feuille de calcul dans une image.

 Vous pouvez accéder à la plage d'affichage maximale d'une feuille de calcul à l'aide de[MaxDisplayIRange](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad351277ccaa0a4e1e8cd0693a1e2e988) méthode de la[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)le recueil.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingMaximumDisplayRangeOfWorksheet.cpp" >}}
