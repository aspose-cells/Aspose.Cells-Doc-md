---
title: Masquer et afficher des lignes et des colonnes
type: docs
weight: 50
url: /fr/java/hiding-and-showing-rows-and-columns/
---
## **Introduction**
Parfois, les utilisateurs peuvent également demander de masquer certaines lignes ou colonnes de la feuille de calcul, puis de les afficher ultérieurement. Microsoft Excel fournit cette fonctionnalité ainsi que Aspose.Cells.
## **Contrôle de la visibilité des lignes et des colonnes**
 Aspose.Cells fournit une classe,[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , qui représente un fichier Excel Microsoft. La[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe contient un[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classer. La[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la classe offre une[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection qui représente toutes les cellules de la feuille de calcul. La[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)[](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection propose plusieurs méthodes de gestion des lignes ou des colonnes dans une feuille de calcul. Certains d'entre eux sont discutés ci-dessous.
### **Masquer des lignes ou des colonnes**
 Les développeurs peuvent masquer une ligne ou une colonne en appelant le[Masquer la ligne](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideRow\(int\) ) et[CacherColonne](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideColumn\(int\) ) les méthodes de[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collecte respectivement. Les deux méthodes prennent l'index de ligne/colonne comme paramètre pour masquer la ligne ou la colonne spécifique.

{{% alert color="primary" %}} 

Remarque : Il est également possible de masquer une ligne ou une colonne si nous définissons respectivement la hauteur de la ligne ou la largeur de la colonne sur 0.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-HidingRowsandColumns-HidingRowsandColumns.java" >}}
### **Affichage des lignes et des colonnes**
 Les développeurs peuvent afficher n'importe quelle ligne ou colonne masquée en appelant le[Afficher la ligne](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideRow\(int,%20double\) ) et[Afficher la colonne](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideColumn\(int,%20double\) ) les méthodes de[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collecte respectivement. Les deux méthodes prennent deux paramètres :

- **Index de ligne ou de colonne** - l'index d'une ligne ou d'une colonne qui est utilisé pour afficher la ligne ou la colonne spécifique.
- **Hauteur de ligne ou largeur de colonne** - la hauteur de ligne ou la largeur de colonne attribuée à la ligne ou à la colonne après son affichage.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UnhidingRowsandColumns-UnhidingRowsandColumns.java" >}}

{{% alert color="primary" %}} 

Lorsque vous rendez visible une colonne/ligne masquée, si vous devez la restaurer à la largeur ou à la hauteur précédemment attribuée, ou à sa largeur ou hauteur d'origine, veuillez afficher la colonne ou la ligne avec une largeur ou une hauteur négative. Par exemple, worksheet.getCells().unhideColumn(5, -1)

{{% /alert %}}
