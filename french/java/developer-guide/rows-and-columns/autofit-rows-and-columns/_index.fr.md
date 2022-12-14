---
title: Ajustement automatique des lignes et des colonnes
type: docs
weight: 20
url: /fr/java/autofit-rows-and-columns/
---
{{% alert color="primary" %}} 

Microsoft Excel fournit une bonne fonctionnalité pour dimensionner automatiquement la largeur et la hauteur d'une cellule en fonction de son contenu. Cette fonctionnalité est également disponible pour les utilisateurs de Aspose.Cells avec la possibilité de dimensionner automatiquement les dimensions d'une cellule lors de l'exécution.

{{% /alert %}} 
## **Ajustement automatique**
 Aspose.Cells fournit une classe,[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , qui représente un fichier Excel Microsoft. La[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe contient un[Des feuilles de calcul](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)collection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel.

 Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classer. La[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) La classe fournit un large éventail de propriétés et de méthodes pour gérer une feuille de calcul. Cet article examine l'utilisation de[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)classe pour ajuster automatiquement les lignes ou les colonnes.
### **Ligne d'ajustement automatique - Simple**
 L'approche la plus simple pour dimensionner automatiquement la largeur et la hauteur d'une ligne consiste à appeler le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classer'[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\) ) méthode. La[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)) prend un index de ligne (de la ligne à redimensionner) comme paramètre.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **AutoFit Row dans une plage de Cells**
 Une ligne est composée de plusieurs colonnes. Aspose.Cells permet aux développeurs d'adapter automatiquement une ligne en fonction du contenu d'une plage de cellules de la ligne en appelant une version surchargée du[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) méthode. Il prend les paramètres suivants :

- **Indice de ligne**, l'index de la ligne sur le point d'être ajusté automatiquement.
- **Index de la première colonne**, l'index de la première colonne de la ligne.
- **Index de la dernière colonne**, l'index de la dernière colonne de la ligne.

 La[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) vérifie le contenu de toutes les colonnes de la ligne, puis ajuste automatiquement la ligne.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **Colonne d'ajustement automatique - Simple**
 Le moyen le plus simple de redimensionner automatiquement la largeur et la hauteur d'une colonne est d'appeler le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classer'[AjusterAutoColonne](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\) ) méthode. La[AjusterAutoColonne](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)prend l'index de colonne (de la colonne sur le point d'être redimensionnée) comme paramètre.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Colonne d'ajustement automatique dans une plage de Cells**
 Une colonne est composée de plusieurs lignes. Il est possible d'adapter automatiquement une colonne en fonction du contenu d'une plage de cellules de la colonne en appelant une version surchargée de[AjusterAutoColonne](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) méthode qui prend les paramètres suivants :

- **Indice de colonne**, représente l'index de la colonne dont le contenu doit s'adapter automatiquement
- **Index de la première ligne**, représente l'indice de la première ligne de la colonne
- **Index de la dernière ligne**, représente l'indice de la dernière ligne de la colonne

 La[AjusterAutoColonne](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) vérifie le contenu de toutes les lignes de la colonne, puis ajuste automatiquement la colonne.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **Ajustement automatique des lignes pour fusionné Cells**
Avec Aspose.Cells, il est possible d'ajuster automatiquement les lignes même pour les cellules qui ont été fusionnées à l'aide de la[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) API. [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)la classe fournit[AutoFitMergedCellsTypeAutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType)propriété qui peut être utilisée pour ajuster automatiquement les lignes des cellules fusionnées.[AutoFitMergedCellsTypeAutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType)accepte[AutoFitMergedCellsTypeAutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType)énumérable qui a les membres suivants.

- [RIEN](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE): Ignorer les cellules fusionnées.
- [PREMIÈRE LIGNE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST_LINE): Agrandit uniquement la hauteur de la première ligne.
- [DERNIÈRE LIGNE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST_LINE): Agrandit uniquement la hauteur de la dernière ligne.
- [CHAQUE LIGNE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH_LINE): Agrandit uniquement la hauteur de chaque ligne.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

 Vous pouvez également utiliser les versions surchargées de[autoFitRowsautoFitRows](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows\(\)) & [AutoFitColumns](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns\(\) ) méthodes acceptant une plage de lignes/colonnes et une instance de[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) pour ajuster automatiquement les lignes/colonnes sélectionnées avec le[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)en conséquence.

Les signatures des procédés précités sont les suivantes :

1.  autoFitRows(int startRow, int endRow,[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)options)
1.  autoFitColumns(int firstColumn, int lastColumn,[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)options)
## **Important à savoir**
{{% alert color="primary" %}} 

 Si une cellule est fusionnée, le*Ajustement automatique* méthodes ne seront pas appliquées, ce qui correspond au même comportement que dans Microsoft Excel. De plus, si le texte d'une cellule est encapsulé, le[AjusterAutoColonne](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\) ) ne sera pas appliquée non plus. Une autre chose que vous devez savoir est que le*Ajustement automatique*les méthodes prennent du temps. Vous devez donc appeler ces méthodes aussi rarement que possible pour garantir l'efficacité de votre application.

{{% /alert %}}
