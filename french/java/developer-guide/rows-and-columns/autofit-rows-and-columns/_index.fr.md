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
L'approche la plus simple pour ajuster automatiquement la largeur et la hauteur d'une ligne est d'appeler la méthode [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)) de la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La méthode [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)) prend un index de ligne (de la ligne à redimensionner) en paramètre.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Ajuster automatiquement la ligne dans une plage de cellules**
Une ligne est composée de nombreuses colonnes. Aspose.Cells permet aux développeurs d'ajuster automatiquement une ligne en fonction du contenu dans une plage de cellules dans la ligne en appelant une version surchargée de la méthode [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)). Elle prend les paramètres suivants :

- **Index de la ligne**, l'index de la ligne à ajuster automatiquement.
- **Index de la première colonne**, l'index de la première colonne de la ligne.
- **Index de la dernière colonne**, l'index de la dernière colonne de la ligne.

La méthode [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) vérifie le contenu de toutes les colonnes de la ligne puis ajuste automatiquement la ligne.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **Ajuster automatiquement la colonne - Simple**
La manière la plus simple de redimensionner automatiquement la largeur et la hauteur d'une colonne est d'appeler la méthode [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)) de la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La méthode [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)) prend l'index de la colonne (de la colonne à redimensionner) comme paramètre.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Ajuster automatiquement la colonne dans une plage de cellules**
Une colonne est composée de nombreuses lignes. Il est possible de redimensionner automatiquement une colonne en fonction du contenu dans une plage de cellules de la colonne en appelant une version surchargée de la méthode [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) qui prend les paramètres suivants :

- **Index de colonne**, représente l'index de la colonne dont le contenu doit être ajusté automatiquement
- **Index de la première ligne**, représente l'index de la première ligne de la colonne
- **Dernier index de ligne**, représente l'index de la dernière ligne de la colonne

La méthode [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) vérifie le contenu de toutes les lignes de la colonne, puis ajuste automatiquement la largeur de la colonne.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **Ajustement automatique des lignes pour les cellules fusionnées**
Avec Aspose.Cells, il est possible de redimensionner automatiquement les lignes même pour les cellules qui ont été fusionnées à l'aide de l'API [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions). La classe [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) fournit la propriété [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) qui peut être utilisée pour ajuster automatiquement les lignes pour les cellules fusionnées. [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) accepte l'énumération [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType) qui contient les membres suivants.

- [AUCUN](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE) : Ignorer les cellules fusionnées.
- [PREMIÈRE_LIGNE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST_LINE) : Augmente uniquement la hauteur de la première ligne.
- [DERNIÈRE_LIGNE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST_LINE) : Augmente uniquement la hauteur de la dernière ligne.
- [CHAQUE_LIGNE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH_LINE) : Augmente uniquement la hauteur de chaque ligne.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

Vous pouvez également utiliser les versions surchargées des méthodes [autoFitRows](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows\(\)) & [autoFitColumns](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns\(\)) qui acceptent une plage de lignes/colonnes et une instance [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) pour adapter automatiquement les lignes/colonnes sélectionnées avec les [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) souhaités en conséquence.

Les signatures des méthodes susmentionnées sont les suivantes :

1. autoFitRows(int startRow, int endRow, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
1. autoFitColumns(int firstColumn, int lastColumn, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
## **Important à savoir**
{{% alert color="primary" %}} 

Si une cellule est fusionnée, les méthodes *AutoFit* ne seront pas appliquées, ce qui est le même comportement que dans Microsoft Excel. De plus, si le texte dans une cellule est enroulé, la méthode [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)) ne sera pas appliquée non plus. Une autre chose que vous devez savoir est que les méthodes *AutoFit* sont longues à exécuter. Vous devriez donc appeler ces méthodes aussi rarement que possible pour assurer l'efficacité de votre application.

{{% /alert %}}
