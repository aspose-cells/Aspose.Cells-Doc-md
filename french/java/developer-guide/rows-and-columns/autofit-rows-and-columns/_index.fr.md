---
title: Ajuster automatiquement les lignes et les colonnes
type: docs
weight: 20
url: /fr/java/autofit-rows-and-columns/
---

{{% alert color="primary" %}} 

Microsoft Excel offre une bonne fonctionnalité pour ajuster automatiquement la largeur et la hauteur d'une cellule en fonction de son contenu. Cette fonctionnalité est également disponible pour les utilisateurs d'Aspose.Cells avec la possibilité de redimensionner automatiquement les dimensions d'une cellule à l'exécution.

{{% /alert %}} 
## **Ajustement automatique**
Aspose.Cells fournit une classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contient une collection [Worksheets](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel.

Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) propose un large éventail de propriétés et de méthodes pour gérer une feuille de calcul. Cet article explique comment utiliser la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) pour ajuster automatiquement les lignes ou les colonnes.
### **Ajuster automatiquement la ligne - Simple**
L'approche la plus simple pour ajuster automatiquement la largeur et la hauteur d'une ligne consiste à appeler la méthode [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-) de la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La méthode [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-) prend en paramètre un indice de ligne (de la ligne à redimensionner).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Ajuster automatiquement la ligne dans une plage de cellules**
Une ligne est composée de plusieurs colonnes. Aspose.Cells permet aux développeurs d'ajuster automatiquement une ligne en fonction du contenu dans une plage de cellules de la ligne en appelant une version surchargée de la méthode [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-int-int-). Elle prend les paramètres suivants :

- **Index de la ligne**, l'index de la ligne à ajuster automatiquement.
- **Index de la première colonne**, l'index de la première colonne de la ligne.
- **Index de la dernière colonne**, l'index de la dernière colonne de la ligne.

La méthode [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow-int-int-int-) vérifie le contenu de toutes les colonnes de la ligne puis ajuste automatiquement la hauteur de la ligne.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **Ajuster automatiquement la colonne - Simple**
La façon la plus simple d'ajuster automatiquement la largeur et la hauteur d'une colonne consiste à appeler la méthode [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-). La méthode [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-) prend en paramètre l'indice de la colonne (de la colonne à redimensionner).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Ajuster automatiquement la colonne dans une plage de cellules**
Une colonne est composée de plusieurs lignes. Il est possible d'ajuster automatiquement une colonne en fonction du contenu dans une plage de cellules de la colonne en appelant une version surchargée de la méthode [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-int-int-), qui prend les paramètres suivants :

- **Index de colonne**, représente l'index de la colonne dont le contenu doit être ajusté automatiquement
- **Index de la première ligne**, représente l'index de la première ligne de la colonne
- **Dernier index de ligne**, représente l'index de la dernière ligne de la colonne

La méthode [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-int-int-) vérifie le contenu de toutes les lignes de la colonne puis ajuste automatiquement la largeur de la colonne.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **Ajustement automatique des lignes pour les cellules fusionnées**
Avec Aspose.Cells, il est possible de redimensionner automatiquement les lignes même pour les cellules qui ont été fusionnées à l'aide de l'API [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions). La classe [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) fournit la propriété [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) qui peut être utilisée pour ajuster automatiquement les lignes pour les cellules fusionnées. [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) accepte l'énumération [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType) qui contient les membres suivants.

- [AUCUN](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE) : Ignorer les cellules fusionnées.
- [FIRST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST-LINE) : Se limite à étendre la hauteur de la première ligne.
- [LAST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST-LINE) : Se limite à étendre la hauteur de la dernière ligne.
- [EACH_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH-LINE) : Se limite à étendre la hauteur de chaque ligne.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

Vous pouvez également utiliser les versions surchargées des méthodes [autoFitRows](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows--) et [autoFitColumns](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns--) acceptant une plage de lignes/colonnes et une instance de [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) pour ajuster automatiquement les lignes/colonnes sélectionnées avec les [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) souhaités. 

Les signatures des méthodes susmentionnées sont les suivantes :

1. autoFitRows(int startRow, int endRow, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
1. autoFitColumns(int firstColumn, int lastColumn, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
## **Important à savoir**
{{% alert color="primary" %}} 

Si une cellule est fusionnée, alors les méthodes *AutoFit* ne seront pas appliquées, ce qui est le même comportement que dans Microsoft Excel. De plus, si le texte dans une cellule est enroulé, la méthode [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn-int-) ne sera pas non plus appliquée. Il faut savoir que les méthodes *AutoFit* sont gourmandes en temps. Par conséquent, vous devriez appeler ces méthodes aussi rarement que possible afin d’assurer l’efficacité de votre application.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
