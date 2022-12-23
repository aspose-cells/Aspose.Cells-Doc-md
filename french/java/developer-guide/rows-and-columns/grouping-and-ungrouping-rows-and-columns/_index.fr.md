---
title: Grouper et dissocier des lignes et des colonnes
type: docs
weight: 40
url: /fr/java/grouping-and-ungrouping-rows-and-columns/
---
## **Introduction**
Dans un fichier Excel Microsoft, vous pouvez créer un plan pour les données afin de vous permettre d'afficher et de masquer les niveaux de détail d'un simple clic de souris.

 Clique le**Symboles de contour**, 1,2,3, + et - pour afficher rapidement uniquement les lignes ou les colonnes qui fournissent des résumés ou des en-têtes pour les sections d'une feuille de calcul, ou vous pouvez utiliser les symboles pour voir les détails sous un résumé ou un en-tête individuel, comme indiqué ci-dessous dans la figure :

 Regroupement de lignes et de colonnes

![tâche : image_autre_texte](grouping-and-ungrouping-rows-and-columns_1.png)
## **Gestion de groupe de lignes et de colonnes**
 Aspose.Cells fournit une classe,[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) qui représente un fichier Excel Microsoft. Le[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe contient un[Feuilles de travail](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) collection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classe. Le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la classe offre une[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection qui représente toutes les cellules de la feuille de calcul.

 Le[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection fournit plusieurs méthodes pour gérer les lignes ou les colonnes dans une feuille de calcul, quelques-unes d'entre elles sont décrites ci-dessous plus en détail.
### **Regroupement de lignes et de colonnes**
 Il est possible de grouper des lignes ou des colonnes en appelant le[groupeRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupRows\(int,%20int,%20boolean\) ) et[groupeColonnes](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupColumns\(int,%20int,%20boolean\) ) les méthodes de[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)le recueil. Les deux méthodes prennent les paramètres suivants :

- Index de la première ligne/colonne, la première ligne ou colonne du groupe.
- Index de la dernière ligne/colonne, la dernière ligne ou colonne du groupe.
- Est masqué, un paramètre booléen qui spécifie s'il faut masquer ou non les lignes/colonnes après le regroupement.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-GroupingRowsandColumns-1.java" >}}
## **Paramètres de groupe**
Microsoft Excel permet également de configurer les paramètres de groupe pour afficher :

- Lignes récapitulatives sous les détails.
- Colonnes récapitulatives à droite du détail.

**Paramètres de groupe** 

![tâche : image_autre_texte](grouping-and-ungrouping-rows-and-columns_2.png)

Il est possible de configurer ces paramètres de groupe à l'aide de la propriété Outline de la classe Worksheet.
### **Lignes récapitulatives sous les détails**
 Les développeurs peuvent contrôler l'affichage des lignes récapitulatives sous les détails à l'aide de l'outil[Contour](https://reference.aspose.com/cells/java/com.aspose.cells/Outline) classe'[SummaryRowBelow](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow) méthode.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowBelow-1.java" >}}
### **Colonnes récapitulatives à droite du détail**
Il est possible de contrôler si les colonnes récapitulatives sont affichées à droite des détails avec la[Contour](https://reference.aspose.com/cells/java/com.aspose.cells/Outline) classe'[RésuméColonneDroite](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryColumnRight)méthode.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowRight-1.java" >}}
### **Dégrouper des lignes et des colonnes**
 Dissociez les lignes ou les colonnes groupées en appelant le[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) de la collection[Dissocier les lignes](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupRows\(int,%20int\) ) et[Dissocier les colonnes](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupColumns\(int,%20int\)) méthodes. Les deux méthodes prennent les mêmes paramètres :

- Premier index de ligne ou de colonne, la première ligne/colonne à dissocier.
- Index de la dernière ligne ou colonne, la dernière ligne/colonne à dissocier.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UngroupingRowsandColumns-UngroupingRowsandColumns.java" >}}
