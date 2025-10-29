---
title: Afficher et masquer les lignes, colonnes et barres de défilement
type: docs
weight: 20
url: /fr/python-net/show-and-hide-rows-columns-and-scroll-bars/
description: Cet article démontre comment afficher et masquer de manière programmatique les lignes et colonnes d une feuille de calcul Excel en utilisant l API Aspose.Cells pour Python via .NET. La visibilité des barres de défilement peut être ajustée, et plusieurs lignes et colonnes peuvent être cachées.
keywords: Bibliothèque Excel Python, Python afficher et masquer les lignes et colonnes, Python masquer les lignes et colonnes, Python afficher la barre de défilement verticale, Python afficher la barre de défilement horizontale, Python masquer la barre de défilement verticale, Python masquer la barre de défilement horizontale, Python afficher et masquer les lignes, colonnes et barres de défilement.
---

{{% alert color="primary" %}}

Aspose.Cells pour Python via .NET offre des moyens de contrôler la visibilité des lignes, colonnes et barres de défilement d'une feuille de calcul.

{{% /alert %}}

## **Afficher et masquer les lignes et les colonnes**

Aspose.Cells pour Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) qui permet aux développeurs d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) offre une collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) qui représente toutes les cellules de la feuille. La collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) fournit plusieurs méthodes pour gérer les lignes ou colonnes dans une feuille de calcul. Certaines de ces méthodes sont abordées ci-dessous.

### **Afficher les lignes et les colonnes**

Les développeurs peuvent afficher toute ligne ou colonne masquée en appelant respectivement les méthodes [**unhide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_row/) et [**unhide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_column/) de la collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/). Les deux méthodes prennent deux paramètres :

- **Index de la ligne ou de la colonne** - l'index d'une ligne ou colonne utilisé pour afficher la ligne ou colonne spécifique.
- **Hauteur de la ligne ou largeur de la colonne** - la hauteur de la ligne ou la largeur de la colonne assignée à la ligne ou colonne après démasquage.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-UnhidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

Lorsque vous rendez une colonne masquée visible, si vous avez besoin de la restaurer à la largeur précédemment assignée ou à sa largeur d'origine, veuillez démasquer la colonne avec une largeur négative. Par exemple : worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Masquer les lignes et les colonnes**

Les développeurs peuvent masquer une ligne ou une colonne en appelant respectivement les méthodes [**hide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_row/) et [**hide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_column/) de la collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Les deux méthodes prennent l'index de la ligne ou de la colonne comme paramètre pour masquer la ligne ou colonne spécifique.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-HidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

Il est également possible de masquer une ligne ou une colonne en définissant respectivement la hauteur de la ligne ou la largeur de la colonne à 0.

{{% /alert %}}

### **Masquer plusieurs lignes et colonnes**

Les développeurs peuvent masquer plusieurs lignes ou colonnes en une seule fois en appelant respectivement les méthodes [**hide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_rows/) et [**hide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_columns) de la collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Les deux méthodes prennent l'index de la ligne ou de la colonne de départ et le nombre de lignes ou de colonnes à masquer comme paramètres.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.py" >}}

## **Afficher et masquer les barres de défilement**

Les barres de défilement sont utilisées pour naviguer dans le contenu de n'importe quel fichier. Normalement, il existe deux types de barres de défilement :

- Barres de défilement verticales
- Barres de défilement horizontales

Microsoft Excel fournit également des barres de défilement horizontales et verticaux permettant aux utilisateurs de faire défiler le contenu de la feuille de calcul. Avec Aspose.Cells pour Python via .NET, les développeurs peuvent contrôler la visibilité des deux types de barres de défilement dans les fichiers Excel.

### **Contrôler la visibilité des barres de défilement**

Aspose.Cells pour Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) offre une large gamme de propriétés et méthodes pour gérer un fichier Excel. Pour contrôler la visibilité des barres de défilement, utilisez les propriétés [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) et [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) de la classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) et [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) sont des propriétés booléennes, ce qui signifie que ces propriétés ne peuvent stocker que des valeurs **vraies** ou **fausses**.

#### **Rendre les barres de défilement visibles**

Rendez les barres de défilement visibles en définissant les propriétés [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) ou [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) de la classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sur **true**.

#### **Masquer les barres de défilement**

Masquez les barres de défilement en définissant la [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) propriété de la classe sur **faux**.

**Code d'exemple**

Ci-dessous se trouve un code complet qui ouvre un fichier Excel, book1.xls, masque les deux barres de défilement, puis enregistre le fichier modifié sous le nom de output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Worksheets-Display-DisplayHideScrollBars-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
