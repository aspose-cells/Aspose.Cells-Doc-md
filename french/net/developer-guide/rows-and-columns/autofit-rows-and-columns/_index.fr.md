---
title: Ajuster automatiquement les lignes et les colonnes
type: docs
weight: 20
url: /fr/net/autofit-rows-and-columns/
description: Cet article montre comment ajuster automatiquement les lignes, colonnes, les lignes de cellules fusionnées et les lignes dans une plage de cellules par l API Aspose.Cells for .NET.
keywords: Ajuster automatiquement les lignes, les colonnes, les lignes de cellules fusionnées et les lignes dans une plage de cellules.
---

{{% alert color="primary" %}}

Microsoft Excel permet aux utilisateurs de redimensionner automatiquement la largeur et la hauteur des cellules en fonction de leur contenu. Cette fonctionnalité est également disponible via Aspose.Cells afin que les développeurs puissent redimensionner automatiquement les dimensions d'une cellule à l'exécution.

{{% /alert %}}

## **Ajustement automatique**

Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient une collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit un large éventail de propriétés et de méthodes pour gérer une feuille de calcul. Cet article examine l'utilisation de la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) pour ajuster automatiquement les lignes ou les colonnes.

### **Ajuster automatiquement la ligne - Simple**

L'approche la plus directe pour redimensionner automatiquement la largeur et la hauteur d'une ligne consiste à appeler la méthode [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) de la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La méthode [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) prend en paramètre un indice de ligne (de la ligne à redimensionner).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

### **Comment ajuster automatiquement une ligne dans une plage de cellules**

Une ligne est composée de plusieurs colonnes. Aspose.Cells permet aux développeurs d'ajuster automatiquement une ligne en fonction du contenu dans une plage de cellules de la ligne en appelant une version surchargée de la méthode [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1). Elle prend les paramètres suivants :

- **Index de la ligne**, l'index de la ligne à ajuster automatiquement.
- **Index de la première colonne**, l'index de la première colonne de la ligne.
- **Index de la dernière colonne**, l'index de la dernière colonne de la ligne.

La méthode [**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1) vérifie le contenu de toutes les colonnes de la ligne, puis ajuste automatiquement la ligne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

### **Comment ajuster automatiquement une colonne dans une plage de cellules**

Une colonne est composée de nombreuses lignes. Il est possible d'ajuster automatiquement une colonne en fonction du contenu dans une plage de cellules dans la colonne en appelant une version surchargée de la méthode [**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) qui prend les paramètres suivants :

- **Index de la colonne**, l'index de la colonne à ajuster automatiquement.
- **Index de la première ligne**, l'index de la première ligne de la colonne.
- **Index de la dernière ligne**, l'index de la dernière ligne de la colonne.

La méthode [**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) vérifie le contenu de toutes les lignes de la colonne, puis ajuste automatiquement la colonne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

### **Comment ajuster automatiquement les lignes pour les cellules fusionnées**

Avec Aspose.Cells, il est possible de redimensionner automatiquement des lignes même pour les cellules fusionnées en utilisant l'API [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions). La classe [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) fournit la propriété [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) qui peut être utilisée pour redimensionner automatiquement les lignes pour les cellules fusionnées. [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) accepte [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype) énumérable qui contient les membres suivants.

- Aucun : Ignorer les cellules fusionnées.
- Première ligne : Étendre uniquement la hauteur de la première ligne.
- Dernière ligne : Étendre uniquement la hauteur de la dernière ligne.
- Chaque ligne : Étendre uniquement la hauteur de chaque ligne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

Vous pouvez également essayer d'utiliser les versions surchargées des méthodes [**AutoFitRows**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) et [**AutoFitColumns**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns) acceptant une plage de lignes/colonnes et une instance de [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) pour ajuster automatiquement les lignes/colonnes sélectionnées avec votre [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) désiré en conséquence.

Les signatures des méthodes susmentionnées sont les suivantes:

1. AutoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) options)
1. AutoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) options)

{{% /alert %}}

## **Important à savoir**

{{% alert color="primary" %}}

Si une cellule est fusionnée, les méthodes AutoFit ne seront pas appliquées, ce qui est le même comportement que dans Microsoft Excel. Vous pouvez contourner cela en utilisant l'API de filtre automatique. De plus, si le texte dans une cellule est enveloppé, la méthode [**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) ne sera pas appliquée non plus. Une autre chose que vous devez savoir est que les méthodes *AutoFit* sont consommatrices de temps. Par conséquent, vous devez appeler ces méthodes aussi rarement que possible pour garantir l'efficacité de votre application.

{{% /alert %}}

## **Sujets avancés**
- [Ajustement automatique des lignes pour les cellules fusionnées](/cells/fr/net/autofit-rows-for-merged-cells/)
{{< app/cells/assistant language="csharp" >}}
