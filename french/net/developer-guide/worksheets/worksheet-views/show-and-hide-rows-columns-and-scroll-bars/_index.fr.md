---
title: Afficher et masquer les lignes, les colonnes et les barres de défilement
type: docs
weight: 20
url: /fr/net/show-and-hide-rows-columns-and-scroll-bars/
description: Cet article explique comment afficher et masquer par programmation des lignes et des colonnes de feuille de calcul Excel à l'aide de la langue C# et de la bibliothèque .NET API. La visibilité des barres de défilement peut être ajustée et plusieurs lignes et colonnes peuvent être masquées.
---
{{% alert color="primary" %}}

Aspose.Cells fournit des moyens de contrôler la visibilité des lignes, des colonnes et des barres de défilement d'une feuille de calcul.

{{% /alert %}}

## **Afficher et masquer les lignes et les colonnes**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , qui représente un fichier Excel Microsoft. Le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**Feuilles de travail**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection qui permet aux développeurs d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe offre une[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection qui représente toutes les cellules de la feuille de calcul. Le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection propose plusieurs méthodes de gestion des lignes ou des colonnes dans une feuille de calcul. Quelques-uns d'entre eux sont discutés ci-dessous.

### **Afficher les lignes et les colonnes**

 Les développeurs peuvent afficher n'importe quelle ligne ou colonne masquée en appelant le[**Afficher la ligne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) et[**Afficher la colonne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) méthodes de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collecte respectivement. Les deux méthodes prennent deux paramètres :

- **Index de ligne ou de colonne** - l'index d'une ligne ou d'une colonne qui est utilisé pour afficher la ligne ou la colonne spécifique.
- **Hauteur de ligne ou largeur de colonne** - la hauteur de ligne ou la largeur de colonne attribuée à la ligne ou à la colonne après l'affichage.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Lorsque vous rendez visible une colonne masquée, si vous devez la restaurer à la largeur précédemment attribuée ou à sa largeur d'origine, veuillez afficher la colonne avec une largeur négative. Par exemple : worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Masquer les lignes et les colonnes**

 Les développeurs peuvent masquer une ligne ou une colonne en appelant le[**Masquer la ligne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) et[**CacherColonne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) méthodes de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collecte respectivement. Les deux méthodes prennent l'index de ligne et de colonne comme paramètre pour masquer la ligne ou la colonne spécifique.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Il est également possible de masquer une ligne ou une colonne en définissant respectivement la hauteur de ligne ou la largeur de colonne sur 0.

{{% /alert %}}

### **Masquer plusieurs lignes et colonnes**

 Les développeurs peuvent masquer plusieurs lignes ou colonnes à la fois en appelant le[**Masquer les lignes**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) et[**CacherColonnes**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) méthodes de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collecte respectivement. Les deux méthodes prennent l'index de la ligne ou de la colonne de départ et le nombre de lignes ou de colonnes qui doivent être masquées comme paramètres.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

## **Afficher et masquer les barres de défilement**

Les barres de défilement sont utilisées pour naviguer dans le contenu de n'importe quel fichier. Normalement, il existe deux types de barres de défilement :

- Barres de défilement verticales
- Barres de défilement horizontales

Microsoft Excel fournit également des barres de défilement horizontales et verticales permettant aux utilisateurs de faire défiler le contenu des feuilles de calcul. En utilisant Aspose.Cells, les développeurs peuvent contrôler la visibilité des deux types de barres de défilement dans les fichiers Excel.

### **Contrôle de la visibilité des barres de défilement**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook)qui représente un fichier Excel. Le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) fournit un large éventail de propriétés et de méthodes pour gérer un fichier Excel. Pour contrôler la visibilité des barres de défilement, utilisez le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) et[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) Propriétés.[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) et[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) sont des propriétés booléennes, ce qui signifie que ces propriétés ne peuvent stocker**vrai** ou alors**faux** valeurs.

#### **Rendre les barres de défilement visibles**

 Rendez les barres de défilement visibles en définissant le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) ou alors[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) propriété à**vrai**.

#### **Masquer les barres de défilement**

 Masquez les barres de défilement en définissant le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) ou alors[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) propriété à**faux**.

**Exemple de code**

Vous trouverez ci-dessous un code complet qui ouvre un fichier Excel, book1.xls, masque les deux barres de défilement, puis enregistre le fichier modifié sous output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideScrollBars-1.cs" >}}
