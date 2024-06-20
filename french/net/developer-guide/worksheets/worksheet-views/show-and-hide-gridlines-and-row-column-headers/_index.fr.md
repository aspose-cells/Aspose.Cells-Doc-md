---
title: Afficher et masquer les quadrillages et les en têtes de ligne et de colonne
type: docs
weight: 30
url: /fr/net/show-and-hide-gridlines-and-row-column-headers/
description: Cet article fournit un code d exemple pour utiliser l API C# ou la bibliothèque .NET pour masquer ou afficher de manière programmée les quadrillages, les en têtes de lignes et de colonnes d une feuille de calcul Excel.
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge le masquage et l'affichage des quadrillages de la feuille de calcul qui sont visibles par défaut. Il permet également de contrôler la visibilité des en-têtes de lignes et de colonnes de la feuille de calcul.

{{% /alert %}}

## **Afficher et masquer les quadrillages**

Toutes les feuilles de calcul Excel ont des quadrillages par défaut. Ils facilitent la délimitation des cellules afin de faciliter la saisie de données dans des cellules particulières. Les quadrillages nous permettent de visualiser une feuille de calcul comme une collection de cellules, où chaque cellule est facilement identifiable.

### **Contrôler la visibilité des quadrillages**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) qui permet aux développeurs d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) offre une large gamme de propriétés et de méthodes pour gérer une feuille de calcul. Pour contrôler la visibilité des quadrillages, utilisez la propriété [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) de la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) est une propriété de type booléen, ce qui signifie qu'elle ne peut stocker qu'une valeur **true** ou **false**.

#### **Rendre les quadrillages visibles**

Rendez les quadrillages visibles en définissant la propriété [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) de la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sur **true**.

#### **Masquer les quadrillages**

Masquez les quadrillages en définissant la propriété [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) de la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sur **false**.

Un exemple complet est donné ci-dessous qui démontre l'utilisation de la propriété [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) en ouvrant un fichier Excel (book1.xls), en masquant les quadrillages sur la première feuille de calcul et en enregistrant le fichier modifié sous le nom output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideGridlines-1.cs" >}}

## **Afficher et masquer les entêtes de ligne des colonnes**

Toutes les feuilles de calcul d'un fichier Excel sont composées de cellules disposées en lignes et en colonnes. Toutes les lignes et colonnes ont des valeurs uniques qui sont utilisées pour les identifier et pour identifier les cellules individuelles. Par exemple, les lignes sont numérotées – 1, 2, 3, 4, etc. – et les colonnes sont ordonnées alphabétiquement – A, B, C, D, etc. Les valeurs de ligne et de colonne sont affichées dans les entêtes. En utilisant Aspose.Cells, les développeurs peuvent contrôler la visibilité de ces entêtes de ligne et de colonne.

### **Contrôler la visibilité des feuilles de calcul**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) qui permet aux développeurs d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) offre une large gamme de propriétés et de méthodes pour gérer une feuille de calcul. Pour contrôler la visibilité des entêtes de ligne et de colonne, utilisez la propriété [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) de la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) est une propriété de type booléen, ce qui signifie qu'elle ne peut stocker qu'une valeur **true** ou **false**.

#### **Rendre les entêtes de ligne/colonne visibles**

Rendez les entêtes de ligne et de colonne visibles en définissant la propriété [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) de la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sur **true**.

#### **Masquer les entêtes de ligne/colonne**

Masquez les entêtes de ligne et de colonne en définissant la propriété [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) de la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sur **false**.

Un exemple complet est donné ci-dessous qui montre comment utiliser la propriété [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) en ouvrant un fichier Excel (book1.xls), en masquant les entêtes de ligne et de colonne sur la première feuille de calcul et en enregistrant le fichier modifié sous le nom output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideRowColumnHeaders-1.cs" >}}

{{% alert color="primary" %}}

Il est également possible d'utiliser les méthodes [**UnhideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) et [**UnhideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns) de la classe [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) pour rendre plusieurs lignes et colonnes visibles.

{{% /alert %}}
