---
title: Gérer les données des fichiers Excel
linktitle: Données de cellules
type: docs
weight: 110
url: /fr/nodejs-cpp/view-and-edit-excel-data/
description: Cet article décrit comment visualiser et modifier les données des fichiers Excel avec la bibliothèque Aspose.Cells pour Node.js via C++.
keywords: Aspose.Cells Node.js via C++, Gérer les données du fichier Excel, ajouter des données au fichier Excel, obtenir des données du fichier Excel, comment améliorer l efficacité de l ajout de données, gérer les données des cellules, mettre à jour les données des cellules, obtenir les données des cellules, insérer des données dans les cellules
---

{{% alert color="primary" %}}

Dans [Accéder aux cellules d'une feuille de calcul](/cells/fr/nodejs-cpp/accessing-cells-of-a-worksheet/), nous avons discuté des approches de base pour accéder aux cellules d'une feuille de calcul. Cet article utilise l'une de ces approches pour ajouter différents types de données aux cellules.

{{% /alert %}}

## **Comment ajouter des données aux cellules**

Aspose.Cells for Node.js via C++ fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) qui permet l'accès à chaque feuille dans le fichier Excel. Une feuille est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Chaque élément de la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

Aspose.Cells permet aux développeurs d'ajouter des données dans les cellules des feuilles de calcul en appelant la méthode [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) de la classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). Aspose.Cells propose des versions surchargeables de la méthode [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) qui permettent aux développeurs d'ajouter différents types de données dans les cellules. En utilisant ces versions surchargeables de la méthode [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-), il est possible d’ajouter des valeurs de type Boolean, chaîne, double, entier, ou date/heure, etc. dans la cellule.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AddDataToCells.js" >}}


## **Comment améliorer l'efficacité**

Si vous utilisez la méthode [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) pour insérer une grande quantité de données dans une feuille de calcul, vous devriez d'abord ajouter des valeurs aux cellules, ligne par ligne puis colonnes par colonnes. Cette approche améliore considérablement l'efficacité de vos applications.

## **Comment récupérer des données à partir de cellules**

Aspose.Cells for Node.js via C++ fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) qui permet l'accès aux feuilles dans le fichier. Une feuille est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Chaque élément de la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

La classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) fournit plusieurs propriétés permettant aux développeurs de récupérer les valeurs des cellules selon leurs types de données. Ces propriétés incluent :

- [**getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--) : renvoie la valeur chaîne de la cellule.
- [**getDoubleValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDoubleValue--) : renvoie la valeur double de la cellule.
- [**getBoolValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getBoolValue--) : renvoie la valeur booléenne de la cellule.
- [**getDateTimeValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDateTimeValue--) : renvoie la valeur date/heure de la cellule.
- [**getFloatValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFloatValue--) : renvoie la valeur float de la cellule.
- [**getIntValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getIntValue--) : renvoie la valeur entière de la cellule.

Lorsqu'un champ n'est pas rempli, les cellules avec [**getDoubleValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDoubleValue--) ou [**getFloatValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFloatValue--) génèrent une exception.

Le type de données contenu dans une cellule peut également être vérifié en utilisant la méthode [**getType()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getType--) de la classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). En fait, la méthode [**getType()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getType--) de la classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) est basée sur l'énumération [**CellValueType**](https://reference.aspose.com/cells/nodejs-cpp/cellvaluetype) dont les valeurs prédéfinies sont listées ci-dessous :

|**Types de valeur de cellule**|**Description**|
| :- | :- |
|IsBool| Spécifie que la valeur de la cellule est un booléen.
|IsDateTime| Spécifie que la valeur de la cellule est une date/heure.
|IsNull| Représente une cellule vide.
|IsNumeric| Spécifie que la valeur de la cellule est numérique.
|IsString| Spécifie que la valeur de la cellule est une chaîne de caractères.
|IsUnknown| Spécifie que la valeur de la cellule est inconnue.

Vous pouvez également utiliser les types de valeur de cellule prédéfinis ci-dessus pour comparer avec le Type de données présent dans chaque cellule.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-RetrieveDataFromCells.js" >}}


{{% alert color="primary" %}}

Lors de la manipulation de feuilles de calcul, les utilisateurs peuvent ajouter différents types de données dans les cellules. Ces types de données peuvent inclure des valeurs Boolean, entiers, flottants, texte ou date/heure. Avec Aspose.Cells, vous pouvez obtenir les valeurs appropriées des cellules selon leurs types de données.

{{% /alert %}}

## **Sujets avancés**
- [Accès aux cellules d'une feuille de calcul](/cells/fr/nodejs-cpp/accessing-cells-of-a-worksheet/)
- [Convertir des données numériques textuelles en nombre](/cells/fr/nodejs-cpp/convert-text-numeric-data-to-number/)
- [Création de sous-totaux](/cells/fr/nodejs-cpp/creating-subtotals/)
- [Filtrage des données](/cells/fr/nodejs-cpp/data-filtering/)
- [Tri des données](/cells/fr/nodejs-cpp/sort-data-of-excel/)
- [Validation des données](/cells/fr/nodejs-cpp/data-validation/)
- [Trouver ou rechercher des données](/cells/fr/nodejs-cpp/find-or-search-data/)
- [Obtenir la valeur de chaîne de cellule avec et sans mise en forme](/cells/fr/nodejs-cpp/get-cell-string-value-with-and-without-formatting/)
- [Ajouter du texte enrichi HTML à l'intérieur de la cellule](/cells/fr/nodejs-cpp/adding-html-rich-text-inside-the-cell/)
- [Insérer des hyperliens dans Excel ou OpenOffice](/cells/fr/nodejs-cpp/insert-hyperlinks-to-excel/)
- [Comment et où utiliser des énumérateurs](/cells/fr/nodejs-cpp/how-and-where-to-use-enumerators/)
- [Mesurer la largeur et la hauteur de la valeur de la cellule en pixels](/cells/fr/nodejs-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Lire les valeurs de cellule dans plusieurs threads simultanément](/cells/fr/nodejs-cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Conversion entre le nom de cellule et l'indice de ligne/colonne](/cells/fr/nodejs-cpp/names-and-indices/)
- [Peupler d'abord les données par ligne puis par colonne](/cells/fr/nodejs-cpp/populate-data-first-by-row-then-by-column/)
- [Préserver le préfixe d'apostrophe unique de la valeur de la cellule ou de la plage](/cells/fr/nodejs-cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Accéder et mettre à jour les parties du texte enrichi de la cellule](/cells/fr/nodejs-cpp/access-and-update-the-portions-of-rich-text-of-cell/)
{{< app/cells/assistant language="nodejs-cpp" >}}
