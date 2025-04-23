---
title: Gérer les données des fichiers Excel
linktitle: Données de cellules
type: docs
weight: 110
url: /fr/net/view-and-edit-excel-data/
description: Cet article décrit comment afficher et modifier les données des fichiers Excel avec la bibliothèque Aspose.Cells.
keywords: Aspose.Cells C# Gérer les données du fichier Excel, ajouter des données au fichier Excel, obtenir des données du fichier Excel, Comment améliorer l efficacité de l ajout de données, gérer les données des cellules, mettre à jour les données des cellules, obtenir les données des cellules, insérer les données des cellules
---

{{% alert color="primary" %}}

Dans [Accéder aux cellules d'une feuille de calcul](/cells/fr/net/accessing-cells-of-a-worksheet/), nous avons discuté des approches de base pour accéder aux cellules dans une feuille de calcul. Cet article utilise l'une de ces approches pour ajouter différents types de données aux cellules.

{{% /alert %}}

## **Comment ajouter des données aux cellules**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Chaque élément de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Aspose.Cells permet aux développeurs d'ajouter des données aux cellules des feuilles de calcul en appelant la méthode [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) de la classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). Aspose.Cells fournit des versions surchargées de la méthode [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) qui permettent aux développeurs d'ajouter différents types de données aux cellules. En utilisant ces versions surchargées de la méthode [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index), il est possible d'ajouter des valeurs booléennes, des chaînes, des doubles, des entiers ou des valeurs de date/heure, etc. à la cellule.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}

## **Comment améliorer l'efficacité**

Si vous utilisez la méthode [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) pour mettre une grande quantité de données dans une feuille de calcul, vous devriez ajouter d'abord les valeurs aux cellules par lignes puis par colonnes. Cette approche améliore grandement l'efficacité de vos applications.

## **Comment récupérer des données à partir de cellules**

Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection qui permet d'accéder aux feuilles de calcul dans le fichier. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit une [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection. Chaque élément de la [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

La classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) fournit plusieurs propriétés qui permettent aux développeurs de récupérer des valeurs à partir des cellules selon leurs types de données. Ces propriétés incluent :

- [**StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue): renvoie la valeur de chaîne de la cellule.
- [**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue): renvoie la valeur double de la cellule.
- [**BoolValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/boolvalue): renvoie la valeur booléenne de la cellule.
- [**DateTimeValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/datetimevalue): renvoie la valeur date/heure de la cellule.
- [**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue): renvoie la valeur flottante de la cellule.
- [**IntValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/intvalue): renvoie la valeur entière de la cellule.

Lorsqu'un champ n'est pas rempli, les cellules avec [**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue) ou [**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue) lèvent une exception.

Le type de données contenu dans une cellule peut également être vérifié en utilisant la propriété [**Type**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) de la classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). En fait, la propriété [**Type**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) de la classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) est basée sur l'énumération [**CellValueType**](https://reference.aspose.com/cells/net/aspose.cells/cellvaluetype) dont les valeurs prédéfinies sont répertoriées ci-dessous :

|**Types de valeur de cellule**|**Description**|
| :- | :- |
|IsBool| Spécifie que la valeur de la cellule est un booléen.
|IsDateTime| Spécifie que la valeur de la cellule est une date/heure.
|IsNull| Représente une cellule vide.
|IsNumeric| Spécifie que la valeur de la cellule est numérique.
|IsString| Spécifie que la valeur de la cellule est une chaîne de caractères.
|IsUnknown| Spécifie que la valeur de la cellule est inconnue.

Vous pouvez également utiliser les types de valeur de cellule prédéfinis ci-dessus pour comparer avec le Type de données présent dans chaque cellule.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}}

En travaillant sur des feuilles de calcul, les utilisateurs peuvent ajouter différents types de données dans les cellules. Ces types de données peuvent inclure des valeurs booléennes, entières, à virgule flottante, du texte ou date/heure. Avec Aspose.Cells, vous pouvez obtenir les valeurs appropriées des cellules selon leurs types de données.

{{% /alert %}}

## **Sujets avancés**
- [Accès aux cellules d'une feuille de calcul](/cells/fr/net/accessing-cells-of-a-worksheet/)
- [Convertir des données numériques textuelles en nombre](/cells/fr/net/convert-text-numeric-data-to-number/)
- [Création de sous-totaux](/cells/fr/net/creating-subtotals/)
- [Filtrage des données](/cells/fr/net/data-filtering/)
- [Tri des données](/cells/fr/net/sort-data-of-excel/)
- [Validation des données](/cells/fr/net/data-validation/)
- [Exporter des données depuis une feuille de calcul](/cells/fr/net/export-data-from-worksheet/)
- [Trouver ou rechercher des données](/cells/fr/net/find-or-search-data/)
- [Obtenir la valeur de chaîne de cellule avec et sans mise en forme](/cells/fr/net/get-cell-string-value-with-and-without-formatting/)
- [Ajouter du texte enrichi HTML à l'intérieur de la cellule](/cells/fr/net/adding-html-rich-text-inside-the-cell/)
- [Insérer des hyperliens dans Excel ou OpenOffice](/cells/fr/net/insert-hyperlinks-to-excel/)
- [Importer des données dans une feuille de calcul](/cells/fr/net/import-data-into-worksheet/)
- [Comment et où utiliser des énumérateurs](/cells/fr/net/how-and-where-to-use-enumerators/)
- [Mesurer la largeur et la hauteur de la valeur de la cellule en pixels](/cells/fr/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Lire les valeurs de cellule dans plusieurs threads simultanément](/cells/fr/net/reading-cell-values-in-multiple-threads-simultaneously/)
- [Conversion entre le nom de cellule et l'indice de ligne/colonne](/cells/fr/net/names-and-indices/)
- [Peupler d'abord les données par ligne puis par colonne](/cells/fr/net/populate-data-first-by-row-then-by-column/)
- [Préserver le préfixe d'apostrophe unique de la valeur de la cellule ou de la plage](/cells/fr/net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Accéder et mettre à jour les parties du texte enrichi de la cellule](/cells/fr/net/access-and-update-the-portions-of-rich-text-of-cell/)



{{< app/cells/assistant language="csharp" >}}
