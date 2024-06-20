---
title: Masquer et afficher des lignes et des colonnes
type: docs
weight: 60
url: /fr/python-net/hiding-and-showing-rows-and-columns/
description: Cet article montre comment masquer et afficher des lignes et des colonnes avec l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Excel Python, Aspose.Cells Python Masquer et Afficher des Lignes, Python Masquer et Afficher des Colonnes, Python Masquer Lignes et Colonnes, Python Afficher Lignes et Colonnes.
---

{{% alert color="primary" %}}

Il est parfois judicieux de masquer certaines lignes ou colonnes dans une feuille de calcul et de les afficher plus tard. Microsoft Excel offre cette fonctionnalité et c'est également le cas d'Aspose.Cells pour Python via .NET.

{{% /alert %}}

## **Contrôler la visibilité des lignes et des colonnes**

Aspose.Cells pour Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), qui représente un classeur Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient un [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) qui permet aux développeurs d'accéder à chaque feuille de calcul du classeur Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fournit une collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) qui représente toutes les cellules de la feuille de calcul. La collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) propose plusieurs méthodes pour gérer les lignes ou colonnes dans une feuille de calcul. Certaines d'entre elles sont discutées ci-dessous.

## **Comment masquer des lignes et des colonnes**

Les développeurs peuvent masquer une ligne ou une colonne en appelant respectivement les méthodes [**hide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_row/) et [**hide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_column/) de la collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Les deux méthodes prennent l'index de la ligne ou de la colonne comme paramètre pour masquer la ligne ou colonne spécifique.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-HidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

Il est également possible de masquer une ligne ou une colonne en définissant respectivement la hauteur de la ligne ou la largeur de la colonne à 0.

{{% /alert %}}

## **Comment afficher des lignes et des colonnes**

Les développeurs peuvent afficher toute ligne ou colonne masquée en appelant respectivement les méthodes [**unhide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_row/) et [**unhide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_column/) de la collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Les deux méthodes prennent deux paramètres :

- **Index de la ligne ou de la colonne** - l'index d'une ligne ou colonne utilisé pour afficher la ligne ou colonne spécifique.
- **Hauteur de la ligne ou largeur de la colonne** - la hauteur de la ligne ou la largeur de la colonne assignée à la ligne ou colonne après démasquage.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-UnhidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

Lorsque vous rendez une colonne masquée visible, si vous avez besoin de la restaurer à la largeur précédemment assignée ou à sa largeur d'origine, veuillez démasquer la colonne avec une largeur négative. Par exemple : worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

## **Comment masquer plusieurs lignes et colonnes**

Les développeurs peuvent masquer plusieurs lignes ou colonnes en une seule fois en appelant respectivement les méthodes [**hide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_rows/) et [**hide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_columns/) de la collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Les deux méthodes prennent l'index de la ligne ou de la colonne de départ et le nombre de lignes ou de colonnes à masquer comme paramètres.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

Il est également possible d'utiliser les méthodes [**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows/) et [**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns/) de la classe [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) pour rendre plusieurs lignes et colonnes visibles.

{{% /alert %}}
