---
title: Gestion des données des fichiers Excel.
linktitle: Cells Données
type: docs
weight: 110
url: /fr/net/view-and-edit-excel-data/
description: Cet article décrit comment afficher et modifier les données des fichiers Excel avec la bibliothèque Aspose.Cells.
---
{{% alert color="primary" %}}

 Dans[Accéder au Cells d'une feuille de calcul](/cells/fr/net/accessing-cells-of-a-worksheet/), nous avons discuté des approches de base pour accéder aux cellules d'une feuille de calcul. Cet article utilise l'une de ces approches pour ajouter différents types de données aux cellules.

{{% /alert %}}

## **Ajout de données au Cells**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , qui représente un fichier Excel Microsoft. Le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**Feuilles de travail**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe offre une[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) le recueil. Chaque élément de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection représente un objet de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe.

Aspose.Cells permet aux développeurs d'ajouter des données aux cellules des feuilles de calcul en appelant le[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) classe'[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) méthode. Aspose.Cells fournit des versions surchargées du[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) méthode qui permet aux développeurs d'ajouter différents types de données aux cellules. L'utilisation de ces versions surchargées du[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index), il est possible d'ajouter une valeur booléenne, chaîne, double, entier ou date/heure, etc. à la cellule.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}

## **Améliorer l'efficacité**

 Si tu utilises[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)Pour placer une grande quantité de données dans une feuille de calcul, vous devez ajouter des valeurs aux cellules, d'abord par lignes, puis par colonnes. Cette approche améliore considérablement l'efficacité de vos applications.

## **Récupération des données du Cells**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Excel Microsoft. Le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**Feuilles de travail**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection qui permet d'accéder aux feuilles de calcul du fichier. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe offre une[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) le recueil. Chaque élément de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection représente un objet de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe.

 Le[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)La classe fournit plusieurs propriétés qui permettent aux développeurs de récupérer les valeurs des cellules en fonction de leurs types de données. Ces propriétés comprennent :

- [**Valeur de chaîne**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue): renvoie la valeur de chaîne de la cellule.
- [**DoubleValeur**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue): renvoie la valeur double de la cellule.
- [**BoolValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/boolvalue): renvoie la valeur booléenne de la cellule.
- [**DateHeureValeur**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/datetimevalue): renvoie la valeur date/heure de la cellule.
- [**Valeurflottante**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue): renvoie la valeur flottante de la cellule.
- [**ValeurEntier**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/intvalue)renvoie la valeur entière de la cellule.

 Lorsqu'un champ n'est pas rempli, les cellules avec[**DoubleValeur**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue) ou alors[**Valeurflottante**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue)lève une exception.

 Le type de données contenues dans une cellule peut également être vérifié à l'aide de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) classe'[**Taper**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) la propriété. En fait, le[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) classe'[**Taper**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) la propriété est basée sur[**CellValueType**](https://reference.aspose.com/cells/net/aspose.cells/cellvaluetype)énumération dont les valeurs prédéfinies sont listées ci-dessous :

|**Cell Types de valeur**|**Description**|
|:- |:- |
|EstBool|Spécifie que la valeur de la cellule est booléenne.|
|EstDateHeure|Spécifie que la valeur de la cellule est date/heure.|
|EstNull|Représente une cellule vide.|
|EstNumérique|Spécifie que la valeur de la cellule est numérique.|
|EstChaîne|Spécifie que la valeur de la cellule est une chaîne.|
|EstInconnu|Spécifie que la valeur de la cellule est inconnue.|

Vous pouvez également utiliser les types de valeur de cellule prédéfinis ci-dessus pour comparer avec le type de données présentes dans chaque cellule.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}}

Lorsqu'ils travaillent sur des feuilles de calcul, les utilisateurs peuvent ajouter différents types de données dans les cellules. Ces types de données peuvent inclure des valeurs booléennes, entières, à virgule flottante, texte ou date/heure. Avec Aspose.Cells, vous pouvez obtenir les valeurs appropriées des cellules en fonction de leurs types de données.

{{% /alert %}}

## **Sujets avancés**
- [Accéder au Cells d'une feuille de calcul](/cells/fr/net/accessing-cells-of-a-worksheet/)
- [Convertir des données numériques de texte en nombre](/cells/fr/net/convert-text-numeric-data-to-number/)
- [Création de sous-totaux](/cells/fr/net/creating-subtotals/)
- [Filtrage des données](/cells/fr/net/data-filtering/)
- [Tri des données](/cells/fr/net/sort-data-of-excel/)
- [La validation des données](/cells/fr/net/data-validation/)
- [Exporter les données de la feuille de calcul](/cells/fr/net/export-data-from-worksheet/)
- [Rechercher ou rechercher des données](/cells/fr/net/find-or-search-data/)
- [Obtenir la valeur de chaîne Cell avec et sans formatage](/cells/fr/net/get-cell-string-value-with-and-without-formatting/)
- [Ajout de texte enrichi HTML à l'intérieur du Cell](/cells/fr/net/adding-html-rich-text-inside-the-cell/)
- [Insérer des hyperliens dans Excel ou OpenOffice](/cells/fr/net/insert-hyperlinks-to-excel/)
- [Importer des données dans la feuille de calcul](/cells/fr/net/import-data-into-worksheet/)
- [Comment et où utiliser les énumérateurs](/cells/fr/net/how-and-where-to-use-enumerators/)
- [Mesurer la largeur et la hauteur de la valeur Cell en unité de pixels](/cells/fr/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Lecture simultanée de valeurs Cell dans plusieurs threads](/cells/fr/net/reading-cell-values-in-multiple-threads-simultaneously/)
- [Conversion entre le nom de cellule et l'index de ligne/colonne](/cells/fr/net/names-and-indices/)
- [Remplir les données d'abord par ligne puis par colonne](/cells/fr/net/populate-data-first-by-row-then-by-column/)
- [Conserver le préfixe de guillemets simples de la valeur ou de la plage Cell](/cells/fr/net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Accéder et mettre à jour les portions de texte enrichi de Cell](/cells/fr/net/access-and-update-the-portions-of-rich-text-of-cell/)



