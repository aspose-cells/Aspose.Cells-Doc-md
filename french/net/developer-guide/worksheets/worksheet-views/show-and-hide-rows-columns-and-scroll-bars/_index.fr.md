---
title: Afficher et masquer les lignes, colonnes et barres de défilement
type: docs
weight: 20
url: /fr/net/show-and-hide-rows-columns-and-scroll-bars/
description: Cet article montre comment afficher et masquer programmablement les lignes et colonnes de feuille de calcul Excel en utilisant le langage C# et l API ou la bibliothèque .NET. La visibilité des barres de défilement peut être ajustée et plusieurs lignes et colonnes peuvent être masquées.
---

{{% alert color="primary" %}}

Aspose.Cells offre des moyens de contrôler la visibilité des lignes, des colonnes et des barres de défilement d'une feuille de calcul.

{{% /alert %}}

## **Afficher et masquer les lignes et les colonnes**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) qui permet aux développeurs d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) qui représente toutes les cellules de la feuille de calcul. La collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) propose plusieurs méthodes pour gérer les lignes ou les colonnes dans une feuille de calcul. Quelques-unes de ces méthodes sont discutées ci-dessous.

### **Afficher les lignes et les colonnes**

Les développeurs peuvent afficher toute ligne ou colonne masquée en appelant respectivement les méthodes [**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) et [**UnhideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Les deux méthodes prennent deux paramètres :

- **Index de la ligne ou de la colonne** - l'index d'une ligne ou colonne utilisé pour afficher la ligne ou colonne spécifique.
- **Hauteur de la ligne ou largeur de la colonne** - la hauteur de la ligne ou la largeur de la colonne assignée à la ligne ou colonne après démasquage.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Lorsque vous rendez une colonne masquée visible, si vous avez besoin de la restaurer à la largeur précédemment assignée ou à sa largeur d'origine, veuillez démasquer la colonne avec une largeur négative. Par exemple : worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Masquer les lignes et les colonnes**

Les développeurs peuvent masquer une ligne ou une colonne en appelant respectivement les méthodes [**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) et [**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Les deux méthodes prennent l'index de la ligne ou de la colonne comme paramètre pour masquer la ligne ou colonne spécifique.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Il est également possible de masquer une ligne ou une colonne en définissant respectivement la hauteur de la ligne ou la largeur de la colonne à 0.

{{% /alert %}}

### **Masquer plusieurs lignes et colonnes**

Les développeurs peuvent masquer plusieurs lignes ou colonnes en une seule fois en appelant respectivement les méthodes [**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) et [**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Les deux méthodes prennent l'index de la ligne ou de la colonne de départ et le nombre de lignes ou de colonnes à masquer comme paramètres.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

## **Afficher et masquer les barres de défilement**

Les barres de défilement sont utilisées pour naviguer dans le contenu de n'importe quel fichier. Normalement, il existe deux types de barres de défilement :

- Barres de défilement verticales
- Barres de défilement horizontales

Microsoft Excel propose également des barres de défilement horizontales et verticales permettant aux utilisateurs de naviguer dans le contenu de la feuille de calcul. En utilisant Aspose.Cells, les développeurs peuvent contrôler la visibilité des deux types de barres de défilement dans les fichiers Excel.

### **Contrôler la visibilité des barres de défilement**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) offre une large gamme de propriétés et de méthodes pour gérer un fichier Excel. Pour contrôler la visibilité des barres de défilement, utilisez les propriétés [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) et [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) de la classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) et [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) sont des propriétés booléennes, ce qui signifie que ces propriétés ne peuvent stocker que des valeurs **true** ou **false**.

#### **Rendre les barres de défilement visibles**

Rendez les barres de défilement visibles en définissant les propriétés [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) ou [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) de la classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sur **true**.

#### **Masquer les barres de défilement**

Masquez les barres de défilement en définissant la [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) propriété de la classe sur **faux**.

**Code d'exemple**

Ci-dessous se trouve un code complet qui ouvre un fichier Excel, book1.xls, masque les deux barres de défilement, puis enregistre le fichier modifié sous le nom de output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideScrollBars-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
