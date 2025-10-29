---
title: Gérer les données des fichiers Excel
linktitle: Données de cellules
type: docs
weight: 110
url: /fr/python-net/view-and-edit-excel-data/
description: Cet article décrit comment afficher et modifier les données des fichiers Excel avec la bibliothèque Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Python Excel, Aspose.Cells pour Python Gérer les données d un fichier Excel, Ajouter des données en Python à un fichier Excel, Récupérer des données d un fichier Excel en Python, Améliorer l efficacité de l ajout de données en Python, Gérer les données des cellules en Python, Mettre à jour les données des cellules en Python, Récupérer les données des cellules en Python, Insérer des données dans les cellules en Python.
---

{{% alert color="primary" %}}

Dans [Accéder aux cellules d'une feuille de calcul](/cells/fr/python-net/accessing-cells-of-a-worksheet/), nous avons discuté des approches de base pour accéder aux cellules d'une feuille de calcul. Cet article utilise l'une de ces approches pour ajouter différents types de données dans les cellules.

{{% /alert %}}

## **Comment ajouter des données aux cellules**

Aspose.Cells pour Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fournit une collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/). Chaque élément de la collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Aspose.Cells pour Python via .NET permet aux développeurs d'ajouter des données dans les cellules des feuilles de calcul en appelant la méthode [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool) de la classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell). Aspose.Cells pour Python via .NET fournit des versions surchargées de la méthode [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int) qui permettent aux développeurs d'ajouter différents types de données dans les cellules. En utilisant ces versions surchargées de la méthode [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int), il est possible d'ajouter des valeurs booléennes, des chaînes, des doubles, des entiers, des dates/heure, etc. dans la cellule.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AddingDataToCells-1.py" >}}

## **Comment améliorer l'efficacité**

Si vous utilisez la méthode [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int) pour mettre une grande quantité de données dans une feuille de calcul, vous devriez ajouter d'abord les valeurs aux cellules par lignes puis par colonnes. Cette approche améliore grandement l'efficacité de vos applications.

## **Comment récupérer des données à partir de cellules**

Aspose.Cells pour Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) qui permet d'accéder aux feuilles de calcul du fichier. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fournit une collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/). Chaque élément de la collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

La classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) fournit plusieurs propriétés qui permettent aux développeurs de récupérer des valeurs à partir des cellules selon leurs types de données. Ces propriétés incluent :

- [**string_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/string_value/): renvoie la valeur de chaîne de la cellule.
- [**double_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/double_value/): renvoie la valeur double de la cellule.
- [**bool_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/bool_value/): renvoie la valeur booléenne de la cellule.
- [**date_time_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/date_time_value/): renvoie la valeur date/heure de la cellule.
- [**float_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/float_value/): renvoie la valeur flottante de la cellule.
- [**int_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/int_value/): renvoie la valeur entière de la cellule.

Lorsqu'un champ n'est pas rempli, les cellules avec [**double_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/double_value/) ou [**float_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/float_value/) lèvent une exception.

Le type de données contenu dans une cellule peut également être vérifié en utilisant la propriété [**type**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/type/) de la classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell). En fait, la propriété [**type**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/type/) de la classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) est basée sur l'énumération [**CellValueType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellvaluetype) dont les valeurs prédéfinies sont répertoriées ci-dessous :

|**Types de valeur de cellule**|**Description**|
| :- | :- |
|IS_BOOL| Spécifie que la valeur de la cellule est booléenne.|
|IS_DATE_TIME| Spécifie que la valeur de la cellule est une date/heure.|
|IS_NULL| Représente une cellule vide.|
|IS_NUMERIC| Spécifie que la valeur de la cellule est numérique.|
|IS_STRING| Spécifie que la valeur de la cellule est une chaîne.|
|IS_ERROR| Spécifie que la valeur de la cellule est une valeur d'erreur.|
|IS_UNKNOWN| Spécifie que la valeur de la cellule est inconnue.|

Vous pouvez également utiliser les types de valeur de cellule prédéfinis ci-dessus pour comparer avec le Type de données présent dans chaque cellule.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-RetrievingDataFromCells-1.py" >}}

{{% alert color="primary" %}}

En travaillant sur des feuilles de calcul, les utilisateurs peuvent ajouter différents types de données dans les cellules. Ces types de données peuvent inclure des valeurs booléennes, entières, à virgule flottante, textuelles ou date/heure. Avec Aspose.Cells pour Python via .NET, vous pouvez obtenir les valeurs appropriées des cellules selon leurs types de données.

{{% /alert %}}

## **Sujets avancés**
- [Accès aux cellules d'une feuille de calcul](/cells/fr/python-net/accessing-cells-of-a-worksheet/)
- [Convertir des données numériques textuelles en nombre](/cells/fr/python-net/convert-text-numeric-data-to-number/)
- [Création de sous-totaux](/cells/fr/python-net/creating-subtotals/)
- [Filtrage des données](/cells/fr/python-net/data-filtering/)
- [Tri des données](/cells/fr/python-net/sort-data-of-excel/)
- [Validation des données](/cells/fr/python-net/data-validation/)
- [Obtenir la valeur de chaîne de cellule avec et sans mise en forme](/cells/fr/python-net/get-cell-string-value-with-format-strategy/)
- [Ajouter du texte enrichi HTML à l'intérieur de la cellule](/cells/fr/python-net/adding-html-rich-text-inside-the-cell/)
- [Trouver ou rechercher des données](/cells/fr/python-net/find-or-search-data/)
- [Insérer des hyperliens dans Excel ou OpenOffice](/cells/fr/python-net/insert-hyperlinks-to-excel/)
- [Mesurer la largeur et la hauteur de la valeur de la cellule en pixels](/cells/fr/python-net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Conversion entre le nom de cellule et l'indice de ligne/colonne](/cells/fr/python-net/names-and-indices/)
- [Peupler d'abord les données par ligne puis par colonne](/cells/fr/python-net/populate-data-first-by-row-then-by-column/)
- [Préserver le préfixe d'apostrophe unique de la valeur de la cellule ou de la plage](/cells/fr/python-net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Accéder et mettre à jour les parties du texte enrichi de la cellule](/cells/fr/python-net/access-and-update-the-portions-of-rich-text-of-cell/)
{{< app/cells/assistant language="python-net" >}}
