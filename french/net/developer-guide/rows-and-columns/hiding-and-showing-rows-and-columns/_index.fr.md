---
title: Masquer et afficher des lignes et des colonnes
type: docs
weight: 60
url: /fr/net/hiding-and-showing-rows-and-columns/
---
{{% alert color="primary" %}}

Parfois, il est judicieux de masquer certaines lignes ou colonnes dans une feuille de calcul et de les afficher ultérieurement. Microsoft Excel fournit cette fonctionnalité, tout comme Aspose.Cells.

{{% /alert %}}

## **Contrôle de la visibilité des lignes et des colonnes**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , qui représente un fichier Excel Microsoft. La[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) qui permet aux développeurs d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer. La[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe offre une[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection qui représente toutes les cellules de la feuille de calcul. La[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection propose plusieurs méthodes de gestion des lignes ou des colonnes dans une feuille de calcul. Quelques-uns d'entre eux sont discutés ci-dessous.

### **Masquer des lignes et des colonnes**

 Les développeurs peuvent masquer une ligne ou une colonne en appelant le[**Masquer la ligne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) et[**CacherColonne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) méthodes de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collecte respectivement. Les deux méthodes prennent l'index de ligne et de colonne comme paramètre pour masquer la ligne ou la colonne spécifique.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Il est également possible de masquer une ligne ou une colonne en définissant respectivement la hauteur de ligne ou la largeur de colonne sur 0.

{{% /alert %}}

### **Affichage des lignes et des colonnes**

 Les développeurs peuvent afficher n'importe quelle ligne ou colonne masquée en appelant le[**Afficher la ligne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) et[**Afficher la colonne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) méthodes de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collecte respectivement. Les deux méthodes prennent deux paramètres :

- **Index de ligne ou de colonne** - l'index d'une ligne ou d'une colonne qui est utilisé pour afficher la ligne ou la colonne spécifique.
- **Hauteur de ligne ou largeur de colonne** - la hauteur de ligne ou la largeur de colonne attribuée à la ligne ou à la colonne après l'affichage.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Lorsque vous rendez visible une colonne masquée, si vous devez la restaurer à la largeur précédemment attribuée ou à sa largeur d'origine, veuillez afficher la colonne avec une largeur négative. Par exemple : worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Masquer plusieurs lignes et colonnes**

 Les développeurs peuvent masquer plusieurs lignes ou colonnes à la fois en appelant le[**Masquer les lignes**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) et[**CacherColonnes**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) méthodes de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collecte respectivement. Les deux méthodes prennent l'index de la ligne ou de la colonne de départ et le nombre de lignes ou de colonnes qui doivent être masquées comme paramètres.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

 Il est également possible d'utiliser le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) classer'[**Afficher les lignes**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) et[**Afficher les colonnes**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns)méthodes pour rendre plusieurs lignes et colonnes visibles.

{{% /alert %}}
