---
title: Ajustement automatique des lignes et des colonnes
type: docs
weight: 20
url: /fr/net/autofit-rows-and-columns/
description: Cet article montre comment ajuster automatiquement les lignes, les colonnes, les lignes de cellules fusionnées et les lignes d'une plage de cellules à l'aide du Aspose.Cells for .NET API.
keywords: Autofit rows, autofit columns, autofit row in a range of cells, autofit rows of merged cells
---
{{% alert color="primary" %}}

Microsoft Excel permet aux utilisateurs de dimensionner automatiquement la largeur et la hauteur des cellules en fonction de leur contenu. Cette fonctionnalité est également disponible via Aspose.Cells afin que les développeurs puissent dimensionner automatiquement les dimensions d'une cellule au moment de l'exécution.

{{% /alert %}}

##  **Montage automatique**

Aspose.Cells fournit un[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe qui représente un fichier Excel Microsoft. Le[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook)la classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) La classe fournit un large éventail de propriétés et de méthodes pour gérer une feuille de calcul. Cet article examine l'utilisation du[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)classe pour ajuster automatiquement les lignes ou les colonnes.

###  **Ligne d'ajustement automatique - Simple**

 L'approche la plus simple pour dimensionner automatiquement la largeur et la hauteur d'une ligne consiste à appeler le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe[**Ajustement automatique de la ligne**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) méthode. Le[**Ajustement automatique de la ligne**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index)La méthode prend un index de ligne (de la ligne à redimensionner) comme paramètre.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

###  **Comment ajuster automatiquement une ligne dans une plage de Cells**

 Une ligne est composée de plusieurs colonnes. Aspose.Cells permet aux développeurs d'ajuster automatiquement une ligne en fonction du contenu d'une plage de cellules dans la ligne en appelant une version surchargée du[**Ajustement automatique de la ligne**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)méthode. Il prend les paramètres suivants :

- *Indice de ligne**, l'index de la ligne sur le point d'être ajusté automatiquement.
- *Indice de la première colonne**, l'index de la première colonne de la ligne.
- *Indice de la dernière colonne**, l'index de la dernière colonne de la ligne.

 Le[**Ajustement automatique de la ligne**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)La méthode vérifie le contenu de toutes les colonnes de la ligne, puis ajuste automatiquement la ligne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

###  **Comment ajuster automatiquement une colonne dans une plage de Cells**

 Une colonne est composée de plusieurs lignes. Il est possible d'ajuster automatiquement une colonne en fonction du contenu d'une plage de cellules de la colonne en appelant une version surchargée de[**Colonne Ajustement automatique**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)méthode qui prend les paramètres suivants :

- *Indice de colonne**, l'index de la colonne sur le point d'être ajusté automatiquement.
- *Indice de la première ligne**, l'index de la première ligne de la colonne.
- *Indice de la dernière ligne**, l'index de la dernière ligne de la colonne.

 Le[**Colonne Ajustement automatique**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)La méthode vérifie le contenu de toutes les lignes de la colonne, puis ajuste automatiquement la colonne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

###  **Comment ajuster automatiquement les lignes pour Cells fusionné**

 Avec Aspose.Cells, il est possible d'ajuster automatiquement les lignes même pour les cellules qui ont été fusionnées à l'aide du[**Options d'ajustement automatique**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) API. [**Options d'ajustement automatique**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)la classe fournit[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) propriété qui peut être utilisée pour ajuster automatiquement les lignes pour les cellules fusionnées.[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)accepte[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype) énumérable qui a les membres suivants.

- Aucun : ignore les cellules fusionnées.
- FirstLine : augmente uniquement la hauteur de la première ligne.
- LastLine : augmente uniquement la hauteur de la dernière ligne.
- EachLine : augmente uniquement la hauteur de chaque ligne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

 Vous pouvez également essayer d'utiliser les versions surchargées de[**Ajustement automatique des lignes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) & [**Colonnes d'ajustement automatique**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns) méthodes acceptant une plage de lignes/colonnes et une instance de[**Options d'ajustement automatique**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) pour ajuster automatiquement les lignes/colonnes sélectionnées avec votre choix[**Options d'ajustement automatique**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)par conséquent.

Les signatures des méthodes précitées sont les suivantes :

1.  AutoFitRows(int startRow, int endRow,[**Options d'ajustement automatique**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)choix)
1.  AutoFitColumns(int premièreColonne, int dernièreColonne,[**Options d'ajustement automatique**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)choix)

{{% /alert %}}

##  **Important à savoir**

{{% alert color="primary" %}}

Si une cellule est fusionnée, les méthodes AutoFit ne seront pas appliquées, ce qui correspond au même comportement que dans Microsoft Excel. Vous pouvez contourner ce problème en utilisant le filtre automatique API. De plus, si le texte d'une cellule est renvoyé à la ligne, le[**Colonne Ajustement automatique**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) la méthode ne sera pas non plus appliquée. Une autre chose que vous devez savoir est que le*Ajustement automatique*les méthodes prennent du temps. Vous devez donc appeler ces méthodes aussi rarement que possible pour garantir l’efficacité de votre application.

{{% /alert %}}

##  **Sujets avancés**
- [Ajustement automatique des lignes pour Cells fusionné](/cells/fr/net/autofit-rows-for-merged-cells/)
