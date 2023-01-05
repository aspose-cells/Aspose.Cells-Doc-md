---
title: Accéder au Cells d'une feuille de calcul
type: docs
weight: 10
url: /fr/java/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}} 

Nous savons que toutes les feuilles de calcul peuvent contenir des données qui sont essentiellement stockées dans des cellules (avec lesquelles une feuille de calcul est composée). Une cellule est une partie de base d'une feuille de calcul utilisée pour construire la feuille de calcul entière sous la forme d'une séquence de lignes et de colonnes. Avant d'essayer d'accéder aux données d'une feuille de calcul, nous aurions besoin d'accéder à ses cellules. Ainsi, dans cette rubrique, nous aborderons certaines approches de base pour accéder aux cellules de feuille de calcul lors de l'exécution à l'aide de Aspose.Cells.

{{% /alert %}} 
## **Accéder au Cells**
 Aspose.Cells fournit une classe,[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) qui représente un fichier Excel Microsoft. Le[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe contient un[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) collection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classe. Le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la classe offre une[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection qui représente toutes les cellules de la feuille de calcul.

 Nous pouvons utiliser le[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection pour accéder aux cellules d'une feuille de calcul. Aspose.Cells fournit différentes approches de base pour accéder aux cellules :

1. [Utilisation du nom de cellule](/cells/fr/java/accessing-cells-of-a-worksheet/).
1. [Utilisation de l'index de ligne et de colonne](/cells/fr/java/accessing-cells-of-a-worksheet/).
### **Utilisation du nom Cell**
 Les développeurs peuvent accéder à n'importe quelle cellule spécifique en transmettant son nom de cellule au[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collecte de la[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)classe.

 Si vous créez une feuille de calcul vierge au début, le nombre de[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)la collecte est nulle. Lorsque vous utilisez cette approche pour accéder à une cellule, il vérifie si cette cellule existe dans la collection ou non. Si oui, il renvoie l'objet cellule dans la collection sinon, il crée un nouveau[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) objet, ajoute l'objet au[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection, puis renvoie l'objet. Cette approche est le moyen le plus simple d'accéder à la cellule si vous connaissez Excel Microsoft, mais elle est plus lente que les autres approches.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingCellName-UsingCellName.java" >}}



### **Utilisation de l'index des lignes et des colonnes du Cell**
 Les développeurs peuvent accéder à n'importe quelle cellule spécifique en transmettant les indices de sa ligne et de sa colonne au[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collecte de la[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)classe.

Cette approche fonctionne de la même manière que celle de la première approche.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingRowAndColumnIndexOfCell-UsingRowAndColumnIndexOfCell.java" >}}
### **Articles Liés**
{{% alert color="primary" %}} 

- [Plages nommées](/cells/fr/java/named-ranges/)

{{% /alert %}} 
## **Accès à la plage d'affichage maximale de la feuille de calcul**
Aspose.Cells permet aux développeurs d'accéder à la plage d'affichage maximale d'une feuille de calcul. La plage d'affichage maximale - la plage de cellules entre la première et la dernière cellule avec du contenu - est utile lorsque vous devez copier, sélectionner ou afficher l'intégralité du contenu d'une feuille de calcul dans une image.

 Vous pouvez accéder à la plage d'affichage maximale d'une feuille de calcul à l'aide de[Feuille de calcul.getCells().getMaxDisplayRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange).

Dans la figure suivante, la plage d'affichage maximale de la feuille de calcul sélectionnée est A1:G15.

**Affichage de la plage d'affichage maximale de cette feuille de calcul** 

![tâche : image_autre_texte](accessing-cells-of-a-worksheet_1.png)

 L'exemple de code suivant montre comment accéder au[MaxDisplayRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange)la propriété. Le code génère la sortie suivante.

{{< highlight "java" >}}

 Maximum Display Range: =Sheet1!$A$1:$G$15

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessingMaximumDisplayRangeofWorksheet-AccessingMaximumDisplayRangeofWorksheet.java" >}}
