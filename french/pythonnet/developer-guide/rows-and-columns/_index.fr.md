---
title: Format des lignes et des colonnes
linktitle: Lignes et colonnes
type: docs
weight: 100
url: /fr/python-net/adjusting-row-height-and-column-width/
description: Aspose.Cells pour Python via .NET peut prendre en charge le changement de hauteur de ligne ou de largeur de colonne, ainsi que l application de mise en forme sur les lignes ou les colonnes.
keywords: Bibliothèque Python Excel, Définir la hauteur de ligne et la largeur de colonne en python, Ajuster la hauteur de ligne et la largeur de colonne en python, Changer la hauteur de ligne ou la largeur de colonne en python, Formater les lignes et les colonnes en python, Comment définir la hauteur de ligne et la largeur de colonne en python.
---


{{% alert color="primary" %}}

Lorsqu'on travaille avec des feuilles de calcul et l'ajout de données dans des lignes ou des colonnes, il peut être nécessaire de modifier la hauteur des lignes ou la largeur des colonnes. Parfois, l'application de mise en forme sur des lignes ou des colonnes signifie que la hauteur ou la largeur actuelle doit changer pour afficher les données. Normalement, les utilisateurs ajustent les hauteurs de lignes et les largeurs de colonnes dans un environnement WYSIWYG en utilisant Microsoft Excel. Mais, avec Aspose.Cells pour Python via .NET, les développeurs peuvent effectuer ces opérations pendant l'exécution.

{{% /alert %}}

## **Travailler avec des lignes**

### **Comment ajuster la hauteur de ligne**

Aspose.Cells pour Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient une [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) qui représente toutes les cellules de la feuille de calcul.

La collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) offre plusieurs méthodes pour gérer les lignes ou les colonnes dans une feuille de calcul. Certaines d'entre elles sont discutées ci-dessous en détail.

### **Comment définir la hauteur d'une ligne**

Il est possible de définir la hauteur d'une seule ligne en appelant la méthode [**set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) de la collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). La méthode [**set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) prend les paramètres suivants comme suit:

- **row**, l'index de la ligne dont vous modifiez la hauteur.
- **height**, la hauteur de ligne à appliquer sur la ligne.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingHeightOfRow-1.py" >}}

### **Comment définir la hauteur de toutes les lignes dans une feuille de calcul**

Si les développeurs doivent définir la même hauteur de ligne pour toutes les lignes dans la feuille de calcul, ils peuvent le faire en utilisant la propriété [**standard_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/standard_height) de la collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells).

**Exemple :**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingHeightAllRows-1.py" >}}

## **Travailler avec les colonnes**

### **Comment définir la largeur d'une colonne**

Définissez la largeur d'une colonne en appelant la méthode [**set_column_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width/#int-float) de la collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). La méthode [**set_column_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width/#int-float) prend les paramètres suivants :

- **colonne**, l'index de la colonne dont vous modifiez la largeur.
- **largeur**, largeur de colonne souhaitée.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.py" >}}

### **Comment définir la largeur de colonne en pixels**

Définissez la largeur d'une colonne en appelant la méthode [**set_column_width_pixel**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width_pixel/#int-int) de la collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). La méthode [**set_column_width_pixel**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width_pixel/#int-int) prend les paramètres suivants :

- **colonne**, l'index de la colonne dont vous modifiez la largeur.
- **pixels**, la largeur de colonne souhaitée en pixels.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.py" >}}

### **Comment définir la largeur de toutes les colonnes dans une feuille de calcul**

Pour définir la même largeur de colonne pour toutes les colonnes dans la feuille de calcul, utilisez la propriété [**standard_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/standard_width) de la collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.py" >}}

## **Sujets avancés**
- [Ajuster automatiquement les lignes et les colonnes](/cells/fr/python-net/autofit-rows-and-columns/)
- [Convertir du texte en colonnes à l'aide de Aspose.Cells](/cells/fr/python-net/convert-text-to-columns-using-aspose-cells/)
- [Copier des lignes et des colonnes](/cells/fr/python-net/copying-rows-and-columns/)
- [Supprimer les lignes et les colonnes vides dans une feuille de calcul](/cells/fr/python-net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Regrouper et dégrouper les lignes et les colonnes](/cells/fr/python-net/grouping-and-ungrouping-rows-and-columns/)
- [Masquer et afficher des lignes et des colonnes](/cells/fr/python-net/hiding-and-showing-rows-and-columns/)
- [Insérer ou supprimer des lignes dans une feuille de calcul Excel](/cells/fr/python-net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Insérer et supprimer des lignes et des colonnes d'un fichier Excel](/cells/fr/python-net/inserting-and-deleting-rows-and-columns/)
- [Supprimer les lignes en double dans une feuille de calcul](/cells/fr/python-net/remove-duplicate-rows-in-a-worksheet/)
- [Mettre à jour les références dans d'autres feuilles de calcul tout en supprimant les colonnes et les rangées vides dans une feuille de calcul](/cells/fr/python-net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
