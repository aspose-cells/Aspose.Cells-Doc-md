---
title: Ajuster automatiquement les lignes et les colonnes
type: docs
weight: 20
url: /fr/python-net/autofit-rows-and-columns/
description: Cet article montre comment ajuster automatiquement les lignes, les colonnes, les lignes de cellules fusionnées et les lignes dans une plage de cellules avec l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Python Excel, Ajuster automatiquement les lignes en Python, Ajuster automatiquement les colonnes en Python, Ajuster automatiquement la ligne dans une plage de cellules en Python, Ajuster automatiquement les lignes des cellules fusionnées en Python.
---

{{% alert color="primary" %}}

Microsoft Excel permet aux utilisateurs de ajuster automatiquement la largeur et la hauteur des cellules en fonction de son contenu. Cette fonctionnalité est également disponible via Aspose.Cells pour Python via .NET afin que les développeurs puissent ajuster automatiquement les dimensions d'une cellule à l'exécution.

{{% /alert %}}

## **Ajustement automatique**

Aspose.Cells for Python via .NET fournit une classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fournit une grande variété de propriétés et de méthodes pour gérer une feuille de calcul. Cet article examine l'utilisation de la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) pour ajuster automatiquement les lignes ou les colonnes.

### **Ajuster automatiquement la ligne - Simple**

L'approche la plus directe pour redimensionner automatiquement la largeur et la hauteur d'une ligne consiste à appeler la méthode [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int) de la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La méthode [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int) prend en paramètre un indice de ligne (de la ligne à redimensionner).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsandColumns-1.py" >}}

### **Comment ajuster automatiquement une ligne dans une plage de cellules**

Une ligne est composée de nombreuses colonnes. Aspose.Cells for Python via .NET permet aux développeurs d'ajuster automatiquement une ligne en fonction du contenu dans une plage de cellules à l'intérieur de la ligne en appelant une version surchargée de la méthode [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int-int-int). Elle prend les paramètres suivants :

- **Index de la ligne**, l'index de la ligne à ajuster automatiquement.
- **Index de la première colonne**, l'index de la première colonne de la ligne.
- **Index de la dernière colonne**, l'index de la dernière colonne de la ligne.

La méthode [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int-int-int) vérifie le contenu de toutes les colonnes de la ligne, puis ajuste automatiquement la ligne.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowinSpecificRange-1.py" >}}

### **Comment ajuster automatiquement une colonne dans une plage de cellules**

Une colonne est composée de nombreuses lignes. Il est possible d'ajuster automatiquement une colonne en fonction du contenu dans une plage de cellules dans la colonne en appelant une version surchargée de la méthode [**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) qui prend les paramètres suivants :

- **Index de la colonne**, l'index de la colonne à ajuster automatiquement.
- **Index de la première ligne**, l'index de la première ligne de la colonne.
- **Index de la dernière ligne**, l'index de la dernière ligne de la colonne.

La méthode [**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) vérifie le contenu de toutes les lignes de la colonne, puis ajuste automatiquement la colonne.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitColumninSpecificRange-1.py" >}}

### **Comment ajuster automatiquement les lignes pour les cellules fusionnées**

Avec Aspose.Cells for Python via .NET, il est possible d'ajuster automatiquement les lignes même pour les cellules qui ont été fusionnées en utilisant l'API [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions). La classe [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) fournit la propriété [**auto_fit_merged_cells_type**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/auto_fit_merged_cells_type/) qui peut être utilisée pour ajuster automatiquement les lignes pour les cellules fusionnées. [**auto_fit_merged_cells_type**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/auto_fit_merged_cells_type/) accepte un [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitmergedcellstype) énumérable qui comporte les membres suivants.

- AUCUN : Ignorer les cellules fusionnées.
- PREMIÈRE_LIGNE : Étendre uniquement la hauteur de la première ligne.
- DERNIÈRE_LIGNE: Ne modifie que la hauteur de la dernière ligne.
- CHAQUE_LIGNE: Ne modifie que la hauteur de chaque ligne.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsforMergedCells-1.py" >}}

{{% alert color="primary" %}}

Vous pouvez également essayer d'utiliser les versions surchargées des méthodes [**auto_fit_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_rows/#int-int-aspose.cells.AutoFitterOptions) et [**auto_fit_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_columns/#int-int-aspose.cells.AutoFitterOptions) acceptant une plage de lignes/colonnes et une instance de [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) pour ajuster automatiquement les lignes/colonnes sélectionnées avec votre [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) désiré en conséquence.

Les signatures des méthodes susmentionnées sont les suivantes:

1. auto_fit_rows(début_ligne, fin_ligne, [**options**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) options)
1. auto_fit_columns(first_column, last_column, [**options**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions))

{{% /alert %}}

## **Important à savoir**

{{% alert color="primary" %}}

Si une cellule est fusionnée, les méthodes AutoFit ne seront pas appliquées, ce qui est le même comportement que dans Microsoft Excel. Vous pouvez contourner cela en utilisant l'API de filtre automatique. De plus, si le texte dans une cellule est enveloppé, la méthode [**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) ne sera pas appliquée non plus. Une autre chose que vous devez savoir est que les méthodes *AutoFit* sont consommatrices de temps. Par conséquent, vous devez appeler ces méthodes aussi rarement que possible pour garantir l'efficacité de votre application.

{{% /alert %}}

## **Sujets avancés**
- [Ajustement automatique des lignes pour les cellules fusionnées](/cells/fr/python-net/autofit-rows-for-merged-cells/)
{{< app/cells/assistant language="python-net" >}}
