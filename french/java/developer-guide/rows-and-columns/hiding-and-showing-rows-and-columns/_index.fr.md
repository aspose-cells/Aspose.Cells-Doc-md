---
title: Masquer et afficher des lignes et des colonnes
type: docs
weight: 50
url: /fr/java/hiding-and-showing-rows-and-columns/
---

## **Introduction**
Parfois, il peut également être nécessaire pour les utilisateurs de masquer certaines lignes ou colonnes de la feuille de calcul et de les afficher ultérieurement. Microsoft Excel fournit cette fonctionnalité et il en va de même pour Aspose.Cells.
## **Contrôler la visibilité des lignes et des colonnes**
Aspose.Cells fournit une classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contient une collection [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fournit une collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) qui représente toutes les cellules de la feuille de calcul. La collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) fournit plusieurs méthodes pour gérer les lignes ou colonnes dans une feuille de calcul. Certaines d'entre elles sont discutées ci-dessous.
### **Masquer des lignes ou des colonnes**
Les développeurs peuvent masquer une ligne ou une colonne en appelant respectivement les méthodes [HideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideRow\(int\)) et [HideColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideColumn\(int\)) de la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Les deux méthodes prennent l'index de la ligne/colonne à masquer en paramètre.

{{% alert color="primary" %}} 

Remarque : Il est également possible de masquer une ligne ou une colonne en définissant respectivement la hauteur de la ligne ou la largeur de la colonne à 0.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-HidingRowsandColumns-HidingRowsandColumns.java" >}}
### **Afficher des lignes et des colonnes**
Les développeurs peuvent afficher toute ligne ou colonne masquée en appelant respectivement les méthodes [UnhideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideRow\(int,%20double\)) et [UnhideColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideColumn\(int,%20double\)) de la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Les deux méthodes prennent deux paramètres :

- **Index de la ligne ou de la colonne** - l'index d'une ligne ou colonne utilisé pour afficher la ligne ou colonne spécifique.
- **Hauteur de la ligne ou largeur de la colonne** - la hauteur de la ligne ou la largeur de la colonne assignée à la ligne ou à la colonne après son affichage.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UnhidingRowsandColumns-UnhidingRowsandColumns.java" >}}

{{% alert color="primary" %}} 

Lorsque vous rendez une colonne/ligne masquée visible, si vous devez restaurer la largeur ou la hauteur précédemment assignée, ou sa largeur ou sa hauteur d'origine, veuillez démasquer la colonne ou la ligne avec une largeur ou une hauteur négative. Par exemple, worksheet.getCells().unhideColumn(5, -1)

{{% /alert %}}
