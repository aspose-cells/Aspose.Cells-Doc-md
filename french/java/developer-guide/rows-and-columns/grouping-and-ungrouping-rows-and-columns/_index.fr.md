---
title: Regroupement et dégroupement des lignes et des colonnes
type: docs
weight: 40
url: /fr/java/grouping-and-ungrouping-rows-and-columns/
---

## **Introduction**
Dans un fichier Microsoft Excel, vous pouvez créer un plan pour les données afin de vous permettre d'afficher et de masquer les niveaux de détail d'un simple clic de souris.

Cliquez sur les **symboles de plan**, 1,2,3, + et - pour afficher rapidement uniquement les lignes ou colonnes fournissant des résumés ou des en-têtes de sections dans une feuille de calcul, ou vous pouvez utiliser les symboles pour voir les détails sous un résumé ou une en-tête individuelle comme le montre la figure ci-dessous:

Regroupement de lignes et de colonnes 

![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)
## **Gestion des groupes de lignes et de colonnes**
Aspose.Cells fournit une classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contient une collection [Worksheets](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fournit une collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) qui représente toutes les cellules de la feuille de calcul.

La collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) fournit plusieurs méthodes pour gérer les lignes ou colonnes dans une feuille de calcul, dont quelques-unes sont discutées plus en détail ci-dessous.
### **Regroupement des lignes et des colonnes**
Il est possible de regrouper des lignes ou des colonnes en appelant les méthodes [groupRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupRows\(int,%20int,%20boolean\)) et [groupColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupColumns\(int,%20int,%20boolean\)) de la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Les deux méthodes prennent les paramètres suivants :

- Indice de la première ligne/colonne, la première ligne ou colonne du groupe.
- Indice de la dernière ligne/colonne, la dernière ligne ou colonne du groupe.
- Est caché, un paramètre booléen qui spécifie s'il faut masquer ou non les lignes/colonnes après le regroupement.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-GroupingRowsandColumns-1.java" >}}
## **Paramètres de regroupement**
Microsoft Excel permet également de configurer les paramètres de regroupement pour l'affichage :

- Lignes de récapitulatif en dessous des détails.
- Colonnes récapitulatives à droite du détail.

**Paramètres de regroupement** 

![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_2.png)

Il est possible de configurer ces paramètres de regroupement en utilisant la propriété Outline de la classe Worksheet.
### **Lignes récapitulatives sous le détail**
Les développeurs peuvent contrôler l'affichage des lignes récapitulatives sous le détail en utilisant la méthode [SummaryRowBelow](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow) de la classe [Outline](https://reference.aspose.com/cells/java/com.aspose.cells/Outline).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowBelow-1.java" >}}
### **Colonnes récapitulatives à droite du détail**
Il est possible de contrôler si les colonnes récapitulatives sont affichées à droite des détails avec la méthode [SummaryColumnRight](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryColumnRight) de la classe [Outline](https://reference.aspose.com/cells/java/com.aspose.cells/Outline).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowRight-1.java" >}}
### **Dégroupement des lignes & des colonnes**
Dégrouper les lignes ou colonnes regroupées en appelant les méthodes [UngroupRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupRows\(int,%20int\)) et [UngroupColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupColumns\(int,%20int\)) de la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Les deux méthodes prennent les mêmes paramètres :

- Indice de la première ligne ou colonne, la première ligne/colonne à dissocier.
- Indice de la dernière ligne ou colonne, la dernière ligne/colonne à dissocier.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UngroupingRowsandColumns-UngroupingRowsandColumns.java" >}}
