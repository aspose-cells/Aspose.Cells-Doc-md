---
title: Afficher et masquer les quadrillages et les en têtes de ligne et de colonne
type: docs
weight: 30
url: /fr/python-net/show-and-hide-gridlines-and-row-column-headers/
description: Cet article fournit un code d exemple pour utiliser l API Aspose.Cells pour Python via .NET afin de masquer ou afficher de manière programmatique les lignes de grille, les en têtes de lignes et de colonnes d une feuille de calcul Excel.
keywords: Bibliothèque Excel Python, Afficher et masquer les lignes de grille Python, Comment afficher et masquer les en têtes de lignes de colonnes en Python, Comment afficher et masquer les lignes de grille et les en têtes de lignes de colonnes en Python.
---

{{% alert color="primary" %}}

Aspose.Cells pour Python via .NET prend en charge le masquage et l'affichage des lignes de la feuille de calcul qui sont visibles par défaut. Il permet également de contrôler la visibilité des en-têtes de lignes et de colonnes de la feuille de calcul.

{{% /alert %}}

## **Afficher et masquer les quadrillages**

Toutes les feuilles de calcul Excel ont des quadrillages par défaut. Ils facilitent la délimitation des cellules afin de faciliter la saisie de données dans des cellules particulières. Les quadrillages nous permettent de visualiser une feuille de calcul comme une collection de cellules, où chaque cellule est facilement identifiable.

### **Contrôler la visibilité des quadrillages**

Aspose.Cells pour Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) contient une collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) permettant aux développeurs d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-et/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) fournit un large éventail de propriétés et méthodes pour gérer une feuille de calcul. Pour contrôler la visibilité des lignes de grille, utilisez la propriété de classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/). [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) est une propriété booléenne, ce qui signifie qu'elle ne peut stocker qu'une valeur **true** ou **false**.

#### **Rendre les quadrillages visibles**

Rendez les quadrillages visibles en définissant la propriété [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) de la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sur **true**.

#### **Masquer les quadrillages**

Masquez les quadrillages en définissant la propriété [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) de la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sur **false**.

Un exemple complet est donné ci-dessous qui démontre l'utilisation de la propriété [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) en ouvrant un fichier Excel (book1.xls), en masquant les quadrillages sur la première feuille de calcul et en enregistrant le fichier modifié sous le nom output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideGridlines-1.py" >}}

## **Afficher et masquer les entêtes de ligne des colonnes**

Toutes les feuilles de calcul d'un fichier Excel sont composées de cellules disposées en lignes et colonnes. Toutes les lignes et colonnes ont des valeurs uniques qui sont utilisées pour les identifier et pour identifier les cellules individuelles. Par exemple, les lignes sont numérotées - 1, 2, 3, 4, etc. - et les colonnes sont ordonnées alphabétiquement - A, B, C, D, etc. Les valeurs de ligne et de colonne sont affichées dans les en-têtes. En utilisant Aspose.Cells pour Python via .NET, les développeurs peuvent contrôler la visibilité de ces en-têtes de lignes et de colonnes.

### **Contrôler la visibilité des feuilles de calcul**

Aspose.Cells pour Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/pytho-net/aspose.cells/workbook/) contient une collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) permettant aux développeurs d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) fournit un large éventail de propriétés et méthodes pour gérer une feuille de calcul. Pour contrôler la visibilité des en-têtes de lignes et de colonnes, utilisez la propriété de classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/). [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) est une propriété booléenne, ce qui signifie qu'elle ne peut stocker qu'une valeur **true** ou **false**.

#### **Rendre les entêtes de ligne/colonne visibles**

Rendez les entêtes de ligne et de colonne visibles en définissant la propriété [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) de la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sur **true**.

#### **Masquer les entêtes de ligne/colonne**

Masquez les entêtes de ligne et de colonne en définissant la propriété [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) de la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sur **false**.

Un exemple complet est donné ci-dessous qui montre comment utiliser la propriété [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) en ouvrant un fichier Excel (book1.xls), en masquant les entêtes de ligne et de colonne sur la première feuille de calcul et en enregistrant le fichier modifié sous le nom output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideRowColumnHeaders-1.py" >}}

{{% alert color="primary" %}}

Il est également possible d'utiliser les méthodes [**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows) et [**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns) de la classe [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) pour rendre plusieurs lignes et colonnes visibles.

{{% /alert %}}
