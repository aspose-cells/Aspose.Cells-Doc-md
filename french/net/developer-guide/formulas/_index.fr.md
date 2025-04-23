---
title: Gérer les formules des fichiers Excel
linktitle: Formules
type: docs
weight: 122
url: /fr/net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells peut simplement obtenir, définir et calculer des formules de fichiers Excel.
description: Apprenez comment gérer les formules des fichiers Excel via les API Aspose.Cells for NET.
keywords: Comment calculer les formules en C#, Formules et fonctions en utilisant C#, Gérer les fonctions intégrées en C#, Comment utiliser des fonctions supplémentaires avec C#, Comment utiliser une formule de tableau via C#, Comment utiliser une formule R1C1 en C#.
---

## **Introduction**

 L’une des fonctionnalités attrayantes de Microsoft Excel est sa capacité à traiter des données avec des formules et des fonctions. Microsoft Excel fournit un ensemble de fonctions et de formules intégrées qui aident les utilisateurs à effectuer des calculs complexes rapidement. Aspose.Cells offre également un vaste ensemble de fonctions et de formules intégrées qui facilitent le calcul pour les développeurs. Aspose.Cells supporte également les fonctions add-in. De plus, Aspose.Cells supporte les formules de tableau et R1C1.

## **Comment utiliser des formules et des fonctions**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Chaque élément de la collection Cells représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Il est possible d'appliquer des formules aux cellules à l'aide des propriétés et des méthodes offertes par la classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell), comme discuté plus en détail ci-dessous.

- Utilisation de fonctions intégrées.
- Utilisation de fonctions supplémentaires.
- Travailler avec des formules de tableau.
- Créer une formule R1C1.

## **Comment utiliser les fonctions intégrées**

Les fonctions ou formules intégrées sont fournies sous forme de fonctions prêtes à l'emploi pour réduire les efforts et le temps des développeurs. Voir [une liste de fonctions intégrées](/cells/fr/net/supported-formula-functions/) supportées par Aspose.Cells. Les fonctions sont répertoriées par ordre alphabétique. D'autres fonctions seront prises en charge à l'avenir.

Aspose.Cells prend en charge la plupart des formules ou fonctions offertes par Microsoft Excel. Les développeurs peuvent utiliser ces formules via l'API ou le [tableur de concepteur](/cells/fr/net/what-is-a-designer-spreadsheet/). Aspose.Cells prend en charge un ensemble important de formules mathématiques, de chaînes de caractères, logiques, de date/heure, statistiques, de base de données, de recherche et de référence.

Utilisez la propriété [**Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) de la classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) pour ajouter une formule à une cellule. **Les formules complexes**, par exemple

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, sont également prises en charge dans Aspose.Cells. Lors de l'application d'une formule à une cellule, commencez toujours la chaîne par un signe égal (=) comme vous le faites lors de la création d'une formule dans Microsoft Excel et utilisez une virgule (,) pour délimiter les paramètres de la fonction.

Dans l'exemple ci-dessous, une formule complexe est appliquée à la première cellule de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) de la feuille de calcul. La formule utilise une fonction intégrée **SI** fournie par Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

## **Comment utiliser les fonctions d'extension**

Nous pouvons avoir certaines formules définies par l'utilisateur que nous voulons inclure dans un complément Excel. Lors du réglage de la fonction cell.Formula les fonctions intégrées fonctionnent bien, cependant il est nécessaire de définir les fonctions ou formules personnalisées en utilisant les fonctions d'extension.

Aspose.Cells propose des fonctionnalités pour enregistrer des fonctions d'extension en utilisant [**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index). Ensuite, lorsque nous définissons cell.Formula = anyFunctionFromAddIn, le fichier Excel de sortie contient la valeur calculée à partir de la fonction AddIn.

Le fichier XLAM suivant doit être téléchargé pour enregistrer la fonction d'extension dans le code d'exemple ci-dessous. De même, le fichier de sortie "test_udf.xlsx" peut être téléchargé pour vérifier la sortie.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

## **Comment utiliser les formules de tableau**

Les formules de tableau sont des formules qui prennent des tableaux, au lieu de nombres individuels, en tant qu'arguments pour les fonctions qui composent la formule. Lorsqu'une formule de tableau est affichée, elle est entourée d'accolades ({}).

Certaines fonctions Microsoft Excel renvoient des tableaux de valeurs. Pour calculer plusieurs résultats avec une formule de tableau, entrez le tableau dans une plage de cellules avec le même nombre de lignes et de colonnes que les arguments du tableau.

Il est possible d'appliquer une formule de tableau à une cellule en appelant la méthode [**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) de la classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). La méthode [**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) prend les paramètres suivants:

- **Formule de tableau**, la formule de tableau.
- **Nombre de lignes**, le nombre de lignes pour remplir le résultat de la formule de tableau.
- **Nombre de colonnes**, le nombre de colonnes pour peupler le résultat de la formule de tableau.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

## **Comment utiliser la formule R1C1**

Ajoutez une formule de référence R1C1 à une cellule avec la propriété de la classe [**R1C1Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula) de la classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

## **Sujets avancés**
- [Précédents et dépendants](/cells/fr/net/precedents-and-dependents/)
- [Définir des liens externes dans les formules](/cells/fr/net/set-external-links-in-formulas/)
- [Propager la formule dans un tableau ou un objet de liste automatiquement lors de la saisie de données dans de nouvelles lignes](/cells/fr/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Définition de la formule pour une plage nommée](/cells/fr/net/setting-formula-for-named-range/)
- [Définition de formules - Avis aux utilisateurs non anglophones](/cells/fr/net/setting-formulas-notice-for-non-english-users/)
- [Définition de formule partagée](/cells/fr/net/setting-shared-formula/)
- [Spécifier le nombre maximum de lignes de formule partagée](/cells/fr/net/specify-maximum-rows-of-shared-formula/)
- [Fonctions Excel prises en charge](/cells/fr/net/supported-formula-functions/)

{{< app/cells/assistant language="csharp" >}}
