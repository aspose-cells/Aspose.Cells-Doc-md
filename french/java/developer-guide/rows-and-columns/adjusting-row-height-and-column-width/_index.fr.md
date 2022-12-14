---
title: Ajustement de la hauteur des lignes et de la largeur des colonnes
type: docs
weight: 10
url: /fr/java/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

Lorsque vous travaillez avec des feuilles de calcul et que vous ajoutez des données à des lignes ou des colonnes, vous devrez peut-être modifier la hauteur des lignes ou la largeur des colonnes. Parfois, l'application d'une mise en forme aux lignes ou aux colonnes signifie que la hauteur ou la largeur actuelle doit changer pour afficher les données. Normalement, les utilisateurs ajustent la hauteur des lignes et la largeur des colonnes dans un environnement WYSIWYG à l'aide de Microsoft Excel. Mais, avec Aspose.Cells, les développeurs peuvent effectuer ces opérations lors de l'exécution. Les index des lignes et des colonnes commenceront à partir de 0.

{{% /alert %}} 
## **Travailler avec des lignes**
### **Réglage de la hauteur de rangée**
 Aspose.Cells fournit une classe,[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , qui représente un fichier Excel Microsoft. La[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe contient un[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classer. La[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la classe offre une[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection qui représente toutes les cellules de la feuille de calcul.

 La[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection fournit plusieurs méthodes pour gérer les lignes ou les colonnes dans une feuille de calcul. Certains d'entre eux sont discutés ci-dessous plus en détail.
### **Définition de la hauteur de ligne**
 Il est possible de définir la hauteur d'une seule ligne en appelant le[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) de la collection[setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\) ) méthode. La[setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\)) prend les paramètres suivants :

- **Indice de ligne**, l'index de la ligne dont vous modifiez la hauteur.
- **Hauteur de ligne**, la hauteur de ligne à appliquer sur la ligne.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightOfRow-SettingHeightOfRow.java" >}}
### **Définition de la hauteur de toutes les lignes**
 Pour définir la même hauteur de ligne pour toutes les lignes d'une feuille de calcul, utilisez la[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) de la collection[setStandardHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardHeight)méthode.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightAllRows-SettingHeightAllRows.java" >}}
## **Travailler avec des colonnes**
### **Définition de la largeur d'une colonne**
 Définissez la largeur d'une colonne en appelant la[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) de la collection[setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\) ) méthode. La[setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\)) prend les paramètres suivants :

- **Indice de colonne**, l'index de la colonne dont vous modifiez la largeur.
- **Largeur de colonne**, la largeur de colonne souhaitée.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfColumn-SettingWidthOfColumn.java" >}}
### **Définition de la largeur de toutes les colonnes**
 Pour définir la même largeur de colonne pour toutes les colonnes d'une feuille de calcul, utilisez la[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) de la collection[définirLargeurStandard](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardWidth)méthode.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfAllColumns-SettingWidthOfAllColumns.java" >}}
