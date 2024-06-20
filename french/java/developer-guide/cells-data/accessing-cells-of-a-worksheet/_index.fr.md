---
title: Accès aux cellules d une feuille de calcul
type: docs
weight: 10
url: /fr/java/accessing-cells-of-a-worksheet/
---

{{% alert color="primary" %}} 

Nous savons que toutes les feuilles de calcul peuvent contenir des données qui sont essentiellement stockées dans des cellules (avec lesquelles une feuille de calcul est constituée). Une cellule est une partie fondamentale d'une feuille de calcul qui est utilisée pour construire la feuille de calcul entière sous forme de séquence de lignes et de colonnes. Avant d'essayer d'accéder aux données d'une feuille de calcul, nous aurions besoin d'accéder à ses cellules. Ainsi, dans ce sujet, nous discuterons de quelques approches de base pour accéder aux cellules de la feuille de calcul lors de l'exécution en utilisant Aspose.Cells.

{{% /alert %}} 
## **Accéder aux cellules**
Aspose.Cells fournit une classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contient une collection [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fournit une collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) qui représente toutes les cellules de la feuille de calcul.

Nous pouvons utiliser la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) pour accéder aux cellules dans une feuille de calcul. Aspose.Cells fournit différentes approches de base pour accéder aux cellules:

1. [En utilisant le nom de la cellule](/cells/fr/java/acces-aux-cellules-d-une-feuille-de-calcul/).
1. [En utilisant l'index de la ligne et de la colonne](/cells/fr/java/acces-aux-cellules-d-une-feuille-de-calcul/).
### **Utilisation du nom de la cellule**
Les développeurs peuvent accéder à une cellule spécifique en passant son nom de cellule à la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) de la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet).

Si vous créez une feuille de calcul vide au début, le nombre de la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) est zéro. Lorsque vous utilisez cette approche pour accéder à une cellule, elle vérifiera si cette cellule existe dans la collection ou non. Si oui, elle renvoie l'objet cellule de la collection sinon, elle crée un nouvel objet [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell), ajoute l'objet à la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) et renvoie ensuite l'objet. Cette approche est la manière la plus simple d'accéder à la cellule si vous êtes familier avec Microsoft Excel mais c'est plus lent que d'autres approches.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingCellName-UsingCellName.java" >}}



### **Utilisation de l'index de la ligne et de la colonne de la cellule**
Les développeurs peuvent accéder à une cellule spécifique en passant les indices de sa ligne et de sa colonne à la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) de la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet).

Cette approche fonctionne de la même manière que la première approche.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingRowAndColumnIndexOfCell-UsingRowAndColumnIndexOfCell.java" >}}
### **Articles connexes**
{{% alert color="primary" %}} 

- [Plages nommées](/cells/fr/java/named-ranges/)

{{% /alert %}} 
## **Accéder à la plage d'affichage maximale d'une feuille de calcul**
Aspose.Cells permet aux développeurs d'accéder à la plage d'affichage maximale d'une feuille de calcul. La plage d'affichage maximale - la plage de cellules entre la première et la dernière cellule avec du contenu - est utile lorsque vous avez besoin de copier, sélectionner ou afficher l'intégralité du contenu d'une feuille de calcul dans une image.

Vous pouvez accéder à la plage d'affichage maximale d'une feuille de calcul en utilisant [Worksheet.getCells().getMaxDisplayRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange).

Dans la figure suivante, la plage d'affichage maximale de la feuille de calcul sélectionnée est A1:G15.

**Affichage de la plage d'affichage maximale de cette feuille de calcul** 

![todo:image_alt_text](accessing-cells-of-a-worksheet_1.png)

Le code suivant illustre comment accéder à la propriété [MaxDisplayRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange). Le code génère la sortie suivante.

{{< highlight java >}}

 Maximum Display Range: =Sheet1!$A$1:$G$15

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessingMaximumDisplayRangeofWorksheet-AccessingMaximumDisplayRangeofWorksheet.java" >}}
