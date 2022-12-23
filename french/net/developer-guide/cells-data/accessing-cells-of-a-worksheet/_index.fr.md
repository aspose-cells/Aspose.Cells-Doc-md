---
title: Accéder au Cells d'une feuille de calcul
type: docs
weight: 10
url: /fr/net/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}}

Nous savons que toutes les feuilles de calcul peuvent contenir des données qui sont essentiellement stockées dans des cellules (avec lesquelles une feuille de calcul est composée). Une cellule est une partie de base d'une feuille de calcul utilisée pour construire la feuille de calcul entière sous la forme d'une séquence de lignes et de colonnes. Avant d'essayer d'accéder aux données d'une feuille de calcul, nous aurions besoin d'accéder à ses cellules. Ainsi, dans cette rubrique, nous aborderons certaines approches de base pour accéder aux cellules de feuille de calcul lors de l'exécution à l'aide de Aspose.Cells.

{{% /alert %}}

## **Accéder au Cells**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Excel. Le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe contient un[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe offre une[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection qui représente toutes les cellules de la feuille de calcul.

 On peut utiliser[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection pour accéder aux cellules d'une feuille de calcul. Aspose.Cells propose trois approches de base pour accéder aux cellules d'une feuille de calcul :

1. Utilisation du nom de la cellule.
1. Utilisation de l'index de ligne et de colonne d'une cellule.
1.  L'utilisation d'un index de cellule dans le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)le recueil

**IMPORTANT:**Nous avons mentionné que la 3ème approche est la plus rapide et la 1ère approche est la plus lente. La différence de performances entre les approches est très faible, ne vous inquiétez donc pas de la dégradation des performances, quelle que soit l'approche que vous utilisez.

### **Utilisation du nom Cell**

 Les développeurs peuvent accéder à n'importe quelle cellule spécifique en transmettant son nom de cellule au[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collecte de la[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)classe comme index.

 Si vous créez une feuille de calcul vierge au début, le nombre de[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)la collecte est nulle. Lorsque vous utilisez cette approche pour accéder à une cellule, il vérifie si cette cellule existe dans la collection ou non. Si oui, il renvoie l'objet cellule dans la collection sinon, il crée un nouveau[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) objet, ajoute l'objet au[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection, puis renvoie l'objet. Cette approche est le moyen le plus simple d'accéder à la cellule si vous connaissez Excel Microsoft, mais c'est la plus lente par rapport aux autres approches.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellName-1.cs" >}}

### **Utilisation de l'index des lignes et des colonnes du Cell**

 Les développeurs peuvent accéder à n'importe quelle cellule spécifique en transmettant les indices de sa ligne et de sa colonne au[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collecte de la[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)classe.

Cette approche fonctionne de la même manière que celle de la première approche.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingRowAndColumnIndexOfCell-1.cs" >}}

### **Utilisation de l'index Cell dans la collection Cells**

 Une cellule est également accessible en transmettant l'index numérique de la cellule au[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)le recueil.

 Si vous utilisez cette approche pour accéder aux cellules, une exception peut être levée si l'index numérique de la cellule est hors plage. Cette approche est la plus rapide pour accéder aux cellules, mais une chose importante à savoir est que si vous utilisez cette approche pour accéder à un objet de cellule, l'index numérique peut changer après l'ajout de nouvelles cellules au[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) le recueil. Les objets de cellule dans le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection sont triés en interne par index de ligne et de colonne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellIndexInCellsCollection-1.cs" >}}

## **Accès à la plage d'affichage maximale de la feuille de calcul**

Aspose.Cells permet aux développeurs d'accéder à la plage d'affichage maximale d'une feuille de calcul. La plage d'affichage maximale - la plage de cellules entre la première et la dernière cellule avec du contenu - est utile lorsque vous devez copier, sélectionner ou afficher l'intégralité du contenu d'une feuille de calcul dans une image.

 Vous pouvez accéder à la plage d'affichage maximale d'une feuille de calcul à l'aide de[**Feuille de travail.Cells.MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) . L'exemple de code suivant montre comment accéder au[**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)la propriété.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.cs" >}}
