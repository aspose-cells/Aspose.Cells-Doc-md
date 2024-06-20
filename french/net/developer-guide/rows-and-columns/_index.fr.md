---
title: Format des lignes et des colonnes
linktitle: Lignes et colonnes
type: docs
weight: 100
url: /fr/net/adjusting-row-height-and-column-width/
description: Aspose.Cells for .NET peut prendre en charge le changement de hauteur de ligne ou de largeur de colonne, ainsi que l application de mise en forme sur les lignes ou les colonnes.
keywords: Définir la hauteur de ligne et la largeur de colonne, ajuster la hauteur de ligne et la largeur de colonne, changer la hauteur de ligne ou la largeur de colonne, formater les lignes et les colonnes, comment définir la hauteur de ligne et la largeur de colonne.
---


{{% alert color="primary" %}}

Lorsque vous travaillez avec des feuilles de calcul et que vous ajoutez des données aux lignes ou aux colonnes, vous pourriez avoir besoin de modifier la hauteur des lignes ou la largeur des colonnes. Parfois, l'application de formats sur les lignes ou les colonnes signifie que la hauteur ou la largeur actuelle doit changer pour afficher les données. Normalement, les utilisateurs ajustent les hauteurs de ligne et les largeurs de colonne dans un environnement WYSIWYG en utilisant Microsoft Excel. Mais, avec Aspose.Cells, les développeurs peuvent effectuer ces opérations à l'exécution.

{{% /alert %}}

## **Travailler avec des lignes**

### **Comment ajuster la hauteur de ligne**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient un [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) qui représente toutes les cellules de la feuille de calcul.

La collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) offre plusieurs méthodes pour gérer les lignes ou les colonnes dans une feuille de calcul. Certaines d'entre elles sont discutées ci-dessous en détail.

### **Comment définir la hauteur d'une ligne**

Il est possible de définir la hauteur d'une seule ligne en appelant la méthode [**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). La méthode [**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) prend les paramètres suivants comme suit:

- **Index de ligne**, l'index de la ligne pour laquelle vous modifiez la hauteur.
- **Hauteur de la ligne**, la hauteur de la ligne à appliquer sur la ligne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightOfRow-1.cs" >}}

### **Comment définir la hauteur de toutes les lignes dans une feuille de calcul**

Si les développeurs doivent définir la même hauteur de ligne pour toutes les lignes dans la feuille de calcul, ils peuvent le faire en utilisant la propriété [**StandardHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardheight) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells).

**Exemple :**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightAllRows-1.cs" >}}

## **Travailler avec les colonnes**

### **Comment définir la largeur d'une colonne**

Définissez la largeur d'une colonne en appelant la méthode [**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). La méthode [**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) prend les paramètres suivants :

- Index de la colonne, l'index de la colonne dont vous changez la largeur.
- Largeur de colonne, la largeur de colonne souhaitée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.cs" >}}

### **Comment définir la largeur de colonne en pixels**

Définissez la largeur d'une colonne en appelant la méthode [**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). La méthode [**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel) prend les paramètres suivants :

- Index de la colonne, l'index de la colonne dont vous changez la largeur.
- Largeur de colonne, la largeur de colonne souhaitée en pixels.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.cs" >}}

### **Comment définir la largeur de toutes les colonnes dans une feuille de calcul**

Pour définir la même largeur de colonne pour toutes les colonnes dans la feuille de calcul, utilisez la propriété [**StandardWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardwidth) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.cs" >}}

## **Sujets avancés**
- [Ajuster automatiquement les lignes et les colonnes](/cells/fr/net/autofit-rows-and-columns/)
- [Convertir du texte en colonnes à l'aide de Aspose.Cells](/cells/fr/net/convert-text-to-columns-using-aspose-cells/)
- [Copier des lignes et des colonnes](/cells/fr/net/copying-rows-and-columns/)
- [Supprimer les lignes et les colonnes vides dans une feuille de calcul](/cells/fr/net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Regrouper et dégrouper les lignes et les colonnes](/cells/fr/net/grouping-and-ungrouping-rows-and-columns/)
- [Masquer et afficher des lignes et des colonnes](/cells/fr/net/hiding-and-showing-rows-and-columns/)
- [Insérer ou supprimer des lignes dans une feuille de calcul Excel](/cells/fr/net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Insérer et supprimer des lignes et des colonnes d'un fichier Excel](/cells/fr/net/inserting-and-deleting-rows-and-columns/)
- [Supprimer les lignes en double dans une feuille de calcul](/cells/fr/net/remove-duplicate-rows-in-a-worksheet/)
- [Mettre à jour les références dans d'autres feuilles de calcul tout en supprimant les colonnes et les rangées vides dans une feuille de calcul](/cells/fr/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
