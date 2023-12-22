---
title: Formater les lignes et les colonnes
linktitle: Lignes et colonnes
type: docs
weight: 100
url: /fr/net/adjusting-row-height-and-column-width/
description: Aspose.Cells for .NET peut prendre en charge la modification de la hauteur des lignes ou de la largeur des colonnes, ainsi que l'application du formatage sur les lignes ou les colonnes.
keywords: Set row height and column width, Adjust row height and column width, change the row height or column width, format rows and columns, how to set row height and column width.
---
{{% alert color="primary" %}}

Lorsque vous travaillez avec des feuilles de calcul et ajoutez des données à des lignes ou des colonnes, vous devrez peut-être modifier la hauteur des lignes ou la largeur des colonnes. Parfois, l'application d'un formatage sur des lignes ou des colonnes signifie que la hauteur ou la largeur actuelle doit être modifiée pour afficher les données. Normalement, les utilisateurs ajustent la hauteur des lignes et la largeur des colonnes dans un environnement WYSIWYG à l'aide d'Excel Microsoft. Mais, avec Aspose.Cells, les développeurs peuvent effectuer ces opérations au moment de l'exécution.

{{% /alert %}}

##  **Travailler avec des lignes**

###  **Comment ajuster la hauteur des rangées**

 Aspose.Cells propose un cours,[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , cela représente un fichier Excel Microsoft. Le[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contient un[**Collection de feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fournit un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection qui représente toutes les cellules de la feuille de calcul.

 Le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)La collection fournit plusieurs méthodes pour gérer les lignes ou les colonnes d’une feuille de calcul. Certains d’entre eux sont abordés ci-dessous plus en détail.

###  **Comment définir la hauteur d'une ligne**

 Il est possible de définir la hauteur d'une seule ligne en appelant la commande[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) la collection[**Définir la hauteur de la ligne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) méthode. Le[**Définir la hauteur de la ligne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight)La méthode prend les paramètres suivants comme suit :

- *Indice de ligne**, l'index de la ligne dont vous modifiez la hauteur.
- *Hauteur de ligne**, la hauteur de ligne à appliquer sur la ligne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightOfRow-1.cs" >}}

###  **Comment définir la hauteur de toutes les lignes d'une feuille de calcul**

 Si les développeurs doivent définir la même hauteur de ligne pour toutes les lignes de la feuille de calcul, ils peuvent le faire en utilisant l'option[**Hauteur standard**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardheight) propriété du[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection.

**Exemple:**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightAllRows-1.cs" >}}

##  **Travailler avec des colonnes**

###  **Comment définir la largeur d'une colonne**

 Définissez la largeur d'une colonne en appelant le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) la collection[**Définir la largeur de la colonne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) méthode. Le[**Définir la largeur de la colonne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth)La méthode prend les paramètres suivants :

- *Indice de colonne**, l'index de la colonne dont vous modifiez la largeur.
- *Largeur de colonne**, la largeur de colonne souhaitée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.cs" >}}

###  **Comment définir la largeur de colonne en pixels**

Définissez la largeur d'une colonne en appelant le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)la collection[**DéfinirColonneLargeurPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)méthode. Le[**DéfinirColonneLargeurPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)La méthode prend les paramètres suivants :

- *Indice de colonne**, l'index de la colonne dont vous modifiez la largeur.
- *Largeur de colonne**, la largeur de colonne souhaitée en pixels.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.cs" >}}

###  **Comment définir la largeur de toutes les colonnes d'une feuille de calcul**

 Pour définir la même largeur de colonne pour toutes les colonnes de la feuille de calcul, utilisez l'option[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) la collection[**Largeur standard**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardwidth)propriété.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.cs" >}}

##  **Sujets avancés**
- [Ajustement automatique des lignes et des colonnes](/cells/fr/net/autofit-rows-and-columns/)
- [Convertir du texte en colonnes à l'aide de Aspose.Cells](/cells/fr/net/convert-text-to-columns-using-aspose-cells/)
- [Copie de lignes et de colonnes](/cells/fr/net/copying-rows-and-columns/)
- [Supprimer des lignes et des colonnes vides dans une feuille de calcul](/cells/fr/net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Regroupement et dissociation de lignes et de colonnes](/cells/fr/net/grouping-and-ungrouping-rows-and-columns/)
- [Masquer et afficher des lignes et des colonnes](/cells/fr/net/hiding-and-showing-rows-and-columns/)
- [Insérer ou supprimer des lignes dans une feuille de calcul Excel](/cells/fr/net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Insertion et suppression de lignes et de colonnes d'un fichier Excel](/cells/fr/net/inserting-and-deleting-rows-and-columns/)
- [Supprimer les lignes en double dans une feuille de calcul](/cells/fr/net/remove-duplicate-rows-in-a-worksheet/)
- [Mettre à jour les références dans d'autres feuilles de calcul tout en supprimant les colonnes et les lignes vides d'une feuille de calcul](/cells/fr/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
