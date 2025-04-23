---
title: Afficher et masquer les quadrillages et les en têtes de ligne et de colonne
type: docs
weight: 30
url: /fr/python-net/show-and-hide-gridlines-and-row-column-headers/
description: Cet article fournit un code d exemple pour utiliser l API Aspose.Cells pour Python via .NET afin de masquer ou afficher de manière programmatique les lignes, colonnes, en têtes et lignes de la grille d une feuille de calcul Excel.
keywords: Bibliothèque Excel Python, Python afficher et masquer la grille, Python afficher et masquer les en têtes de lignes et de colonnes, Python afficher et masquer la grille et les en têtes.
---

{{% alert color="primary" %}}

Aspose.Cells pour Python via .NET supporte la gestion de l'affichage des lignes et colonnes de la grille par défaut. Il permet également de contrôler la visibilité des en-têtes de lignes et de colonnes.

{{% /alert %}}

## **Afficher et masquer les quadrillages**

Toutes les feuilles de calcul Excel ont des quadrillages par défaut. Ils facilitent la délimitation des cellules afin de faciliter la saisie de données dans des cellules particulières. Les quadrillages nous permettent de visualiser une feuille de calcul comme une collection de cellules, où chaque cellule est facilement identifiable.

### **Contrôler la visibilité des quadrillages**

Aspose.Cells pour Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) contient une collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) qui permet aux développeurs d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) offre une large gamme de propriétés et méthodes pour gérer une feuille de calcul. Pour contrôler la visibilité de la grille, utilisez la propriété de la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/). [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) est une propriété booléenne, ce qui signifie qu'elle ne peut stocker qu'une valeur **vraie** ou **fausse**.

#### **Rendre les quadrillages visibles**

Rendez les quadrillages visibles en définissant la propriété [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) de la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sur **true**.

#### **Masquer les quadrillages**

Masquez les quadrillages en définissant la propriété [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) de la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sur **false**.

Un exemple complet est donné ci-dessous qui démontre l'utilisation de la propriété [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) en ouvrant un fichier Excel (book1.xls), en masquant les quadrillages sur la première feuille de calcul et en enregistrant le fichier modifié sous le nom output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideGridlines-1.py" >}}

## **Afficher et masquer les entêtes de ligne des colonnes**

Toutes les feuilles de calcul d'un fichier Excel sont composées de cellules disposées en lignes et colonnes. Toutes les lignes et colonnes ont des valeurs uniques qui servent à les identifier ainsi que chaque cellule. Par exemple, les lignes sont numérotées – 1, 2, 3, 4, etc. – et les colonnes sont ordonnées alphabétiquement – A, B, C, D, etc. Les valeurs des lignes et colonnes sont affichées dans les en-têtes. En utilisant Aspose.Cells pour Python via .NET, les développeurs peuvent contrôler la visibilité de ces en-têtes de lignes et de colonnes.

### **Contrôler la visibilité des feuilles de calcul**

Aspose.Cells pour Python via .NET offre une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) contient une collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) qui permet aux développeurs d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) offre une large gamme de propriétés et méthodes pour gérer une feuille de calcul. Pour contrôler la visibilité des en-têtes de lignes et de colonnes, utilisez la propriété [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) de la classe [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/). [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) est une propriété booléenne, ce qui signifie qu'elle ne peut stocker qu'une valeur **vraie** ou **fausse**.

#### **Rendre les entêtes de ligne/colonne visibles**

Rendez les entêtes de ligne et de colonne visibles en définissant la propriété [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) de la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sur **true**.

#### **Masquer les entêtes de ligne/colonne**

Masquez les entêtes de ligne et de colonne en définissant la propriété [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) de la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sur **false**.

Un exemple complet est donné ci-dessous qui montre comment utiliser la propriété [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) en ouvrant un fichier Excel (book1.xls), en masquant les entêtes de ligne et de colonne sur la première feuille de calcul et en enregistrant le fichier modifié sous le nom output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideRowColumnHeaders-1.py" >}}

{{% alert color="primary" %}}

Il est également possible d'utiliser les méthodes [**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows) et [**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns) de la classe [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) pour rendre plusieurs lignes et colonnes visibles.

{{% /alert %}}
