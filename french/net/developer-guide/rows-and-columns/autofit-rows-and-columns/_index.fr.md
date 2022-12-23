---
title: Ajustement automatique des lignes et des colonnes
type: docs
weight: 20
url: /fr/net/autofit-rows-and-columns/
---
{{% alert color="primary" %}}

Microsoft Excel permet aux utilisateurs de redimensionner automatiquement la largeur et la hauteur des cellules en fonction de leur contenu. Cette fonctionnalité est également disponible via Aspose.Cells afin que les développeurs puissent dimensionner automatiquement les dimensions d'une cellule lors de l'exécution.

{{% /alert %}}

## **Ajustement automatique**

Aspose.Cells fournit un[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe qui représente un fichier Excel Microsoft. Le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe contient un[**Feuilles de travail**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) La classe fournit un large éventail de propriétés et de méthodes pour gérer une feuille de calcul. Cet article examine l'utilisation de[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)classe pour ajuster automatiquement les lignes ou les colonnes.

### **Ligne d'ajustement automatique - Simple**

 L'approche la plus simple pour dimensionner automatiquement la largeur et la hauteur d'une ligne consiste à appeler le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) méthode. Le[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index)prend un index de ligne (de la ligne à redimensionner) comme paramètre.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

### **AutoFit Row dans une plage de Cells**

 Une ligne est composée de plusieurs colonnes. Aspose.Cells permet aux développeurs d'adapter automatiquement une ligne en fonction du contenu d'une plage de cellules de la ligne en appelant une version surchargée du[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)méthode. Il prend les paramètres suivants :

- **Indice de ligne**, l'index de la ligne sur le point d'être ajusté automatiquement.
- **Index de la première colonne**, l'index de la première colonne de la ligne.
- **Index de la dernière colonne**, l'index de la dernière colonne de la ligne.

 Le[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)La méthode vérifie le contenu de toutes les colonnes de la ligne, puis ajuste automatiquement la ligne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

### **Colonne d'ajustement automatique dans une plage de Cells**

 Une colonne est composée de plusieurs lignes. Il est possible d'adapter automatiquement une colonne en fonction du contenu d'une plage de cellules de la colonne en appelant une version surchargée de[**Ajustement automatique de la colonne**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)méthode qui prend les paramètres suivants :

- **Indice de colonne**l'index de la colonne sur le point d'être ajusté automatiquement.
- **Index de la première ligne**, l'index de la première ligne de la colonne.
- **Index de la dernière ligne**, l'index de la dernière ligne de la colonne.

 Le[**Ajustement automatique de la colonne**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)La méthode vérifie le contenu de toutes les lignes de la colonne, puis ajuste automatiquement la colonne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

### **Ajustement automatique des lignes pour fusionné Cells**

 Avec Aspose.Cells, il est possible d'ajuster automatiquement les lignes même pour les cellules qui ont été fusionnées à l'aide de la[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) API. [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)la classe fournit[**AutoFitMergedCellsTypeAutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) propriété qui peut être utilisée pour ajuster automatiquement les lignes des cellules fusionnées.[**AutoFitMergedCellsTypeAutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)accepte[**AutoFitMergedCellsTypeAutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype) énumérable qui a les membres suivants.

- Aucun : ignore les cellules fusionnées.
- FirstLine : étend uniquement la hauteur de la première ligne.
- LastLine : étend uniquement la hauteur de la dernière ligne.
- EachLine : étend uniquement la hauteur de chaque ligne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

 Vous pouvez également essayer d'utiliser les versions surchargées de[**AutoFitRows**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) & [**Ajustement automatique des colonnes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns) méthodes acceptant une plage de lignes/colonnes et une instance de[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) pour ajuster automatiquement les lignes/colonnes sélectionnées avec votre choix[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)en conséquence.

Les signatures des procédés précités sont les suivantes :

1.  AutoFitRows(int startRow, int endRow,[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)options)
1. AutoFitColumns(int firstColumn, int lastColumn,[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)options)

{{% /alert %}}

## **Important à savoir**

{{% alert color="primary" %}}

 Si une cellule est fusionnée, les méthodes AutoFit ne seront pas appliquées, ce qui correspond au même comportement que dans Microsoft Excel. Vous pouvez contourner ce problème en utilisant le filtre automatique API. De plus, si le texte d'une cellule est enveloppé, le[**Ajustement automatique de la colonne**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) méthode ne sera pas appliquée non plus. Une autre chose que vous devez savoir est que le*Ajustement automatique*les méthodes prennent du temps. Vous devez donc appeler ces méthodes aussi rarement que possible pour garantir l'efficacité de votre application.

{{% /alert %}}

## **Sujets avancés**
- [Ajustement automatique des lignes pour fusionné Cells](/cells/fr/net/autofit-rows-for-merged-cells/)
