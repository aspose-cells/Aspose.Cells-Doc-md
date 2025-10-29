---
title: Gérer les données des fichiers Excel avec Golang via C++
linktitle: Données de cellules
type: docs
weight: 110
url: /fr/go-cpp/view-and-edit-excel-data/
description: Cet article explique comment visualiser et modifier les données des fichiers Excel avec la bibliothèque Aspose.Cells en utilisant C++.
keywords: Aspose.Cells C++ Gérer les données du fichier Excel, ajouter des données au fichier Excel, récupérer des données du fichier Excel, comment améliorer l efficacité de l ajout de données, gérer les données des cellules, mettre à jour les données des cellules, obtenir les données des cellules, insérer des données dans les cellules
---

{{% alert color="primary" %}}

Dans [Accéder aux cellules d'une feuille de calcul](/cells/fr/cpp/accessing-cells-of-a-worksheet/), nous avons discuté des approches de base pour accéder aux cellules d'une feuille de calcul. Cet article utilise l'une de ces approches pour ajouter différents types de données aux cellules.

{{% /alert %}}

## **Comment ajouter des données aux cellules**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) contient une collection [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fournit une collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Chaque élément de la collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells permet aux développeurs d'ajouter des données aux cellules des feuilles de calcul en appelant la méthode [**PutValue**](https://reference.aspose.com/cells/go-cpp/cell/putvalue/) de la classe [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/). Aspose.Cells fournit des versions surchargées de la méthode [**PutValue**](https://reference.aspose.com/cells/go-cpp/cell/putvalue/) qui permettent aux développeurs d'ajouter différents types de données aux cellules. En utilisant ces versions surchargées de la méthode [**PutValue**](https://reference.aspose.com/cells/go-cpp/cell/putvalue/), il est possible d'ajouter des valeurs booléennes, des chaînes, des doubles, des entiers ou des valeurs de date/heure, etc. à la cellule.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CellsData.go" >}}
## **Comment améliorer l'efficacité**

Si vous utilisez la méthode [**PutValue**](https://reference.aspose.com/cells/go-cpp/cell/putvalue_bool/) pour mettre une grande quantité de données dans une feuille de calcul, vous devriez ajouter d'abord les valeurs aux cellules par lignes puis par colonnes. Cette approche améliore grandement l'efficacité de vos applications.

## **Comment récupérer des données à partir de cellules**

Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) contient une [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection qui permet d'accéder aux feuilles de calcul dans le fichier. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fournit une [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. Chaque élément de la [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

La classe [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) fournit plusieurs propriétés qui permettent aux développeurs de récupérer des valeurs à partir des cellules selon leurs types de données. Ces propriétés incluent :

- [**StringValue**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/): renvoie la valeur de chaîne de la cellule.
- [**DoubleValue**](https://reference.aspose.com/cells/go-cpp/cell/getdoublevalue/): renvoie la valeur double de la cellule.
- [**BoolValue**](https://reference.aspose.com/cells/go-cpp/cell/getboolvalue/): renvoie la valeur booléenne de la cellule.
- [**DateTimeValue**](https://reference.aspose.com/cells/go-cpp/cell/getdatetimevalue/): renvoie la valeur date/heure de la cellule.
- [**FloatValue**](https://reference.aspose.com/cells/go-cpp/cell/getfloatvalue/): renvoie la valeur flottante de la cellule.
- [**IntValue**](https://reference.aspose.com/cells/go-cpp/cell/getintvalue/): renvoie la valeur entière de la cellule.

Lorsqu'un champ n'est pas rempli, les cellules avec [**DoubleValue**](https://reference.aspose.com/cells/go-cpp/cell/getdoublevalue/) ou [**FloatValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/) lèvent une exception.

Le type de données contenu dans une cellule peut également être vérifié en utilisant la propriété [**Type**](https://reference.aspose.com/cells/go-cpp/cell/gettype/) de la classe [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/). En fait, la propriété [**Type**](https://reference.aspose.com/cells/go-cpp/cell/gettype/) de la classe [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) est basée sur l'énumération [**CellValueType**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/) dont les valeurs prédéfinies sont répertoriées ci-dessous :

|**Types de valeur de cellule**|**Description**|
| :- | :- |
|IsBool| Spécifie que la valeur de la cellule est un booléen.
|IsDateTime| Spécifie que la valeur de la cellule est une date/heure.
|IsNull| Représente une cellule vide.
|IsNumeric| Spécifie que la valeur de la cellule est numérique.
|IsString| Spécifie que la valeur de la cellule est une chaîne de caractères.
|IsUnknown| Spécifie que la valeur de la cellule est inconnue.

Vous pouvez également utiliser les types de valeur de cellule prédéfinis ci-dessus pour comparer avec le Type de données présent dans chaque cellule.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CellsData-1.go" >}}
{{% alert color="primary" %}}

En travaillant sur des feuilles de calcul, les utilisateurs peuvent ajouter différents types de données dans les cellules. Ces types de données peuvent inclure des valeurs booléennes, entières, à virgule flottante, du texte ou date/heure. Avec Aspose.Cells, vous pouvez obtenir les valeurs appropriées des cellules selon leurs types de données.

{{% /alert %}}

## **Sujets avancés**
- [Accès aux cellules d'une feuille de calcul](/cells/fr/cpp/accessing-cells-of-a-worksheet/)
- [Convertir des données numériques textuelles en nombre](/cells/fr/cpp/convert-text-numeric-data-to-number/)
- [Création de sous-totaux](/cells/fr/cpp/creating-subtotals/)
- [Filtrage des données](/cells/fr/cpp/data-filtering/)
- [Tri des données](/cells/fr/cpp/sort-data-of-excel/)
- [Validation des données](/cells/fr/cpp/data-validation/)
- [Trouver ou rechercher des données](/cells/fr/cpp/find-or-search-data/)
- [Obtenir la valeur de chaîne de cellule avec et sans mise en forme](/cells/fr/cpp/get-cell-string-value-with-and-without-formatting/)
- [Ajouter du texte enrichi HTML à l'intérieur de la cellule](/cells/fr/cpp/adding-html-rich-text-inside-the-cell/)
- [Insérer des hyperliens dans Excel ou OpenOffice](/cells/fr/cpp/insert-hyperlinks-to-excel/)
- [Comment et où utiliser des énumérateurs](/cells/fr/cpp/how-and-where-to-use-enumerators/)
- [Mesurer la largeur et la hauteur de la valeur de la cellule en pixels](/cells/fr/cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Lire les valeurs de cellule dans plusieurs threads simultanément](/cells/fr/cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Conversion entre le nom de cellule et l'indice de ligne/colonne](/cells/fr/cpp/names-and-indices/)
- [Peupler d'abord les données par ligne puis par colonne](/cells/fr/cpp/populate-data-first-by-row-then-by-column/)
- [Préserver le préfixe d'apostrophe unique de la valeur de la cellule ou de la plage](/cells/fr/cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Accéder et mettre à jour les parties du texte enrichi de la cellule](/cells/fr/cpp/access-and-update-the-portions-of-rich-text-of-cell/)
