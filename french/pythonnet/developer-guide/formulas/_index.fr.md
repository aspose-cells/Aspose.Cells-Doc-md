---
title: Gérer les formules des fichiers Excel
linktitle: Formules
type: docs
weight: 122
url: /fr/python-net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells pour Python via .NET peut simplement obtenir, définir et calculer les formules des fichiers Excel.
description: Apprenez comment gérer les formules des fichiers Excel via l API Aspose.Cells pour Python via .NET for NET.
keywords: Comment calculer des formules en Python, Formules et Fonctions en utilisant Python, gérer les fonctions intégrées en Python, comment utiliser les fonctions complémentaires avec Python, comment utiliser une formule en tableau via Python, comment utiliser une formule R1C1 en Python.
---

## **Introduction**

L'une des fonctionnalités captivantes de Microsoft Excel est sa capacité à traiter des données avec des formules et des fonctions. Microsoft Excel offre un ensemble de fonctions intégrées et de formules qui aident les utilisateurs à effectuer des calculs complexes rapidement. Aspose.Cells pour Python via .NET fournit également un grand ensemble de fonctions et de formules intégrées qui aident les développeurs à calculer facilement des valeurs. Aspose.Cells pour Python via .NET prend également en charge les fonctions complémentaires. De plus, Aspose.Cells pour Python via .NET supporte les formules en tableau et R1C1.

## **Comment utiliser des formules et des fonctions**

Aspose.Cells pour Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) permettant d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fournit une collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Chaque élément de la collection Cells représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Il est possible d'appliquer des formules aux cellules à l'aide des propriétés et des méthodes offertes par la classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell), comme discuté plus en détail ci-dessous.

- Utilisation de fonctions intégrées.
- Utilisation de fonctions supplémentaires.
- Travailler avec des formules de tableau.
- Créer une formule R1C1.

## **Comment utiliser les fonctions intégrées**

Les fonctions ou formules intégrées sont fournies sous forme de fonctions prêt-à-l’emploi pour réduire les efforts et le temps des développeurs. Voir [une liste des fonctions intégrées](/cells/fr/python-net/supported-formula-functions/) supportées par Aspose.Cells pour Python via .NET. Les fonctions sont listées par ordre alphabétique. Plus de fonctions seront supportées à l'avenir.

Aspose.Cells pour Python via .NET supporte la plupart des formules ou fonctions proposées par Microsoft Excel. Les développeurs peuvent utiliser ces formules via l'API ou [créer une feuille de calcul de conception](/cells/fr/net/what-is-a-designer-spreadsheet/). Aspose.Cells pour Python via .NET supporte un vaste ensemble de formules mathématiques, de chaînes, booléennes, date/heure, statistiques, bases de données, recherche et référence.

Utilisez la propriété [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/formula) de la classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) pour ajouter une formule à une cellule. **Les formules complexes**, par exemple

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, sont également supportées dans Aspose.Cells pour Python via .NET. Lors de l'application d'une formule à une cellule, commencez toujours la chaîne par un signe égal (=) comme lors de la création d'une formule dans Microsoft Excel et utilisez une virgule (,) pour délimiter les paramètres de la fonction.

Dans l'exemple ci-dessous, une formule complexe est appliquée à la première cellule de la collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) d'une feuille de calcul. La formule utilise une fonction **SI** intégrée fournie par Aspose.Cells pour Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingBuiltinfunction-1.py" >}}

## **Comment utiliser les fonctions d'extension**

Nous pouvons avoir certaines formules définies par l'utilisateur que nous voulons inclure dans un complément Excel. Lors du réglage de la fonction cell.Formula les fonctions intégrées fonctionnent bien, cependant il est nécessaire de définir les fonctions ou formules personnalisées en utilisant les fonctions d'extension.

Aspose.Cells pour Python via .NET offre des fonctionnalités pour enregistrer des fonctions complémentaires en utilisant [**worksheets.register_add_in_function()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/register_add_in_function). Ensuite, lorsque nous attribuons à la cellule la formule = anyFunctionFromAddIn, le fichier Excel de sortie contient la valeur calculée à partir de la fonction AddIn.

Le fichier XLAM suivant doit être téléchargé pour enregistrer la fonction d'extension dans le code d'exemple ci-dessous. De même, le fichier de sortie "test_udf.xlsx" peut être téléchargé pour vérifier la sortie.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-RegisterAndCallFuncFromAddIn-1.py" >}}

## **Comment utiliser les formules de tableau**

Les formules de tableau sont des formules qui prennent des tableaux, au lieu de nombres individuels, en tant qu'arguments pour les fonctions qui composent la formule. Lorsqu'une formule de tableau est affichée, elle est entourée d'accolades ({}).

Certaines fonctions Microsoft Excel renvoient des tableaux de valeurs. Pour calculer plusieurs résultats avec une formule de tableau, entrez le tableau dans une plage de cellules avec le même nombre de lignes et de colonnes que les arguments du tableau.

Il est possible d'appliquer une formule de tableau à une cellule en appelant la méthode [**set_array_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_array_formula) de la classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell). La méthode [**set_array_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_array_formula) prend les paramètres suivants:

- **Formule de tableau**, la formule de tableau.
- **Nombre de lignes**, le nombre de lignes pour remplir le résultat de la formule de tableau.
- **Nombre de colonnes**, le nombre de colonnes pour peupler le résultat de la formule de tableau.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingArrayFunction-1.py" >}}

## **Comment utiliser la formule R1C1**

Ajoutez une formule de référence R1C1 à une cellule avec la propriété de la classe [**r1c1_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/r1c1_formula) de la classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingR1C1-1.py" >}}

## **Sujets avancés**
- [Précédents et dépendants](/cells/fr/python-net/precedents-and-dependents/)
- [Définir des liens externes dans les formules](/cells/fr/python-net/set-external-links-in-formulas/)
- [Propager la formule dans un tableau ou un objet de liste automatiquement lors de la saisie de données dans de nouvelles lignes](/cells/fr/python-net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Définition de la formule pour une plage nommée](/cells/fr/python-net/setting-formula-for-named-range/)
- [Définition de formules - Avis aux utilisateurs non anglophones](/cells/fr/python-net/setting-formulas-notice-for-non-english-users/)
- [Définition de formule partagée](/cells/fr/python-net/setting-shared-formula/)
- [Spécifier le nombre maximum de lignes de formule partagée](/cells/fr/python-net/specify-maximum-rows-of-shared-formula/)
- [Fonctions Excel prises en charge](/cells/fr/python-net/supported-formula-functions/)


