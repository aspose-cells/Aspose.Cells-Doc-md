---
title: Ajuster la hauteur de la ligne et la largeur de la colonne
type: docs
weight: 10
url: /fr/java/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}} 

Lorsque vous travaillez avec des feuilles de calcul et que vous ajoutez des données à des lignes ou des colonnes, vous pourriez avoir besoin de modifier la hauteur des lignes ou la largeur des colonnes. Parfois, appliquer une mise en forme aux lignes ou aux colonnes signifie que la hauteur ou la largeur actuelle doit changer pour afficher les données. Normalement, les utilisateurs ajustent les hauteurs de lignes et les largeurs de colonnes dans un environnement WYSIWYG en utilisant Microsoft Excel. Mais, avec Aspose.Cells, les développeurs peuvent effectuer ces opérations à l'exécution. Les indices des lignes et des colonnes commenceront à partir de 0.

{{% /alert %}} 
## **Travailler avec des lignes**
### **Ajuster la hauteur de la ligne**
Aspose.Cells fournit une classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contient une [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fournit une collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) qui représente toutes les cellules de la feuille de calcul.

La collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) fournit plusieurs méthodes pour gérer les lignes ou les colonnes dans une feuille de calcul. Certaines d'entre elles sont discutées ci-dessous plus en détail.
### **Définir la hauteur de la ligne**
Il est possible de définir la hauteur d'une seule ligne en appelant la méthode [setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\)) de la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). La méthode [setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\)) prend les paramètres suivants :

- **Index de ligne**, l'index de la ligne pour laquelle vous modifiez la hauteur.
- **Hauteur de la ligne**, la hauteur de la ligne à appliquer sur la ligne.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightOfRow-SettingHeightOfRow.java" >}}
### **Définir la hauteur de toutes les lignes**
Pour définir la même hauteur de ligne pour toutes les lignes dans une feuille de calcul, utilisez la méthode [setStandardHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardHeight) de la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightAllRows-SettingHeightAllRows.java" >}}
## **Travailler avec les colonnes**
### **Définir la largeur d'une colonne**
Définissez la largeur d'une colonne en appelant la méthode [setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\)) de la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). La méthode [setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\)) prend les paramètres suivants :

- Index de la colonne, l'index de la colonne dont vous changez la largeur.
- Largeur de colonne, la largeur de colonne souhaitée.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfColumn-SettingWidthOfColumn.java" >}}
### **Définir la largeur de toutes les colonnes**
Pour définir la même largeur de colonne pour toutes les colonnes dans une feuille de calcul, utilisez la méthode [setStandardWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardWidth) de la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfAllColumns-SettingWidthOfAllColumns.java" >}}
