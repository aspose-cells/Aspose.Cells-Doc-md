---
title: Masquer et afficher des lignes et des colonnes
type: docs
weight: 60
url: /fr/net/hiding-and-showing-rows-and-columns/
---

{{% alert color="primary" %}}

Parfois, il est judicieux de masquer certaines lignes ou colonnes dans une feuille de calcul et de les afficher plus tard. Microsoft Excel fournit cette fonctionnalité et Aspose.Cells également.

{{% /alert %}}

## **Contrôler la visibilité des lignes et des colonnes**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une collection [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) qui permet aux développeurs d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) qui représente toutes les cellules de la feuille de calcul. La collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) fournit plusieurs méthodes pour gérer les lignes ou les colonnes dans une feuille de calcul. Certaines d'entre elles sont discutées ci-dessous.

### **Masquer les lignes et les colonnes**

Les développeurs peuvent masquer une ligne ou une colonne en appelant respectivement les méthodes [**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) et [**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Les deux méthodes prennent l'index de la ligne ou de la colonne comme paramètre pour masquer la ligne ou colonne spécifique.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Il est également possible de masquer une ligne ou une colonne en définissant respectivement la hauteur de la ligne ou la largeur de la colonne à 0.

{{% /alert %}}

### **Afficher des lignes et des colonnes**

Les développeurs peuvent afficher toute ligne ou colonne masquée en appelant respectivement les méthodes [**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) et [**UnhideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Les deux méthodes prennent deux paramètres :

- **Index de la ligne ou de la colonne** - l'index d'une ligne ou colonne utilisé pour afficher la ligne ou colonne spécifique.
- **Hauteur de la ligne ou largeur de la colonne** - la hauteur de la ligne ou la largeur de la colonne assignée à la ligne ou colonne après démasquage.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Lorsque vous rendez une colonne masquée visible, si vous avez besoin de la restaurer à la largeur précédemment assignée ou à sa largeur d'origine, veuillez démasquer la colonne avec une largeur négative. Par exemple : worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Masquer plusieurs lignes et colonnes**

Les développeurs peuvent masquer plusieurs lignes ou colonnes en une seule fois en appelant respectivement les méthodes [**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) et [**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Les deux méthodes prennent l'index de la ligne ou de la colonne de départ et le nombre de lignes ou de colonnes à masquer comme paramètres.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Il est également possible d'utiliser les méthodes [**UnhideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) et [**UnhideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns) de la classe [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) pour rendre plusieurs lignes et colonnes visibles.

{{% /alert %}}
