---
title: Afficher et masquer le quadrillage et les en-têtes de colonne de ligne
type: docs
weight: 30
url: /fr/net/show-and-hide-gridlines-and-row-column-headers/
description: Cet article fournit un exemple de code permettant d'utiliser la bibliothèque C# API ou .NET pour masquer ou afficher par programme le quadrillage, les en-têtes de ligne et de colonne d'une feuille de calcul Excel.
---
{{% alert color="primary" %}}

Aspose.Cells prend en charge le masquage et l'affichage des quadrillages de la feuille de calcul qui sont visibles par défaut. Il permet également de contrôler la visibilité des en-têtes de colonne de ligne de la feuille de calcul.

{{% /alert %}}

## **Afficher et masquer le quadrillage**

Toutes les feuilles de calcul Excel ont un quadrillage par défaut. Ils aident à délimiter les cellules afin qu'il soit facile d'entrer des données dans des cellules particulières. Le quadrillage nous permet de visualiser une feuille de calcul comme une collection de cellules, où chaque cellule est facilement identifiable.

### **Contrôle de la visibilité du quadrillage**

Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook), qui représente un fichier Excel Microsoft. Le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe contient un[**Feuilles de travail**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)collection qui permet aux développeurs d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) La classe fournit un large éventail de propriétés et de méthodes pour gérer une feuille de calcul. Pour contrôler la visibilité des lignes de grille, utilisez la[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) la propriété.[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) est une propriété booléenne, ce qui signifie qu'elle ne peut stocker qu'un**vrai** ou alors**faux** évaluer.

#### **Rendre le quadrillage visible**

 Rendez le quadrillage visible en définissant le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) propriété à**vrai**.

#### **Masquer le quadrillage**

 Masquez le quadrillage en définissant le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) propriété à**faux**.

 Un exemple complet est donné ci-dessous qui démontre l'utilisation de la[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)propriété en ouvrant un fichier Excel (book1.xls), en masquant le quadrillage sur la première feuille de calcul et en enregistrant le fichier modifié sous output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideGridlines-1.cs" >}}

## **Afficher et masquer les en-têtes de colonne de ligne**

Toutes les feuilles de calcul d'un fichier Excel sont composées de cellules disposées en lignes et en colonnes. Toutes les lignes et colonnes ont des valeurs uniques qui sont utilisées pour les identifier et pour identifier des cellules individuelles. Par exemple, les lignes sont numérotées – 1, 2, 3, 4, etc. – et les colonnes sont classées par ordre alphabétique – A, B, C, D, etc. Les valeurs des lignes et des colonnes sont affichées dans les en-têtes. À l'aide de Aspose.Cells, les développeurs peuvent contrôler la visibilité de ces en-têtes de ligne et de colonne.

### **Contrôle de la visibilité des feuilles de calcul**

Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook), qui représente un fichier Excel Microsoft. Le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe contient un[**Feuilles de travail**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)collection qui permet aux développeurs d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) La classe fournit un large éventail de propriétés et de méthodes pour gérer une feuille de calcul. Pour contrôler la visibilité des en-têtes de ligne et de colonne, utilisez la[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe[**EstRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) la propriété.[**EstRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) est une propriété booléenne, ce qui signifie qu'elle ne peut stocker qu'un**vrai** ou alors**faux**évaluer.

#### **Rendre les en-têtes de ligne/colonne visibles**

 Rendez les en-têtes de ligne et de colonne visibles en définissant le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe[**EstRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) propriété à**vrai**.

#### **Masquer les en-têtes de ligne/colonne**

 Masquez les en-têtes de ligne et de colonne en définissant le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe[**EstRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) propriété à**faux**.

Un exemple complet est donné ci-dessous qui montre comment utiliser le[**EstRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)propriété en ouvrant un fichier Excel (book1.xls), en masquant les en-têtes de ligne et de colonne sur la première feuille de calcul et en enregistrant le fichier modifié sous output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideRowColumnHeaders-1.cs" >}}

{{% alert color="primary" %}}

 Il est également possible d'utiliser le[**Afficher les lignes**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) et[**Afficher les colonnes**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns) méthodes de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) classe pour rendre plusieurs lignes et colonnes visibles.

{{% /alert %}}
