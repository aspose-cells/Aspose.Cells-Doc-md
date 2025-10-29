---
title: Gérer les formules des fichiers Excel avec Node.js via C++
linktitle: Formules
type: docs
weight: 122
url: /fr/nodejs-cpp/using-formulas-or-functions-to-process-data/
description: Apprenez à gérer les formules des fichiers Excel à travers le Aspose.Cells for Node.js via C++. Aspose.Cells peut simplement obtenir, définir et calculer les formules des fichiers Excel.
keywords: Comment calculer des formules en Node.js via C++, Formules et Fonctions en utilisant Node.js via C++, Node.js via C++ Gestion des Fonctions Intégrées, Comment utiliser les Fonctions Add in avec Node.js via C++, Comment utiliser la formule tableau via Node.js via C++, Comment utiliser la formule R1C1 en Node.js via C++.
---

## **Introduction**

 L’une des fonctionnalités attrayantes de Microsoft Excel est sa capacité à traiter des données avec des formules et des fonctions. Microsoft Excel fournit un ensemble de fonctions et de formules intégrées qui aident les utilisateurs à effectuer des calculs complexes rapidement. Aspose.Cells offre également un vaste ensemble de fonctions et de formules intégrées qui facilitent le calcul pour les développeurs. Aspose.Cells supporte également les fonctions add-in. De plus, Aspose.Cells supporte les formules de tableau et R1C1.

## **Comment utiliser des formules et des fonctions**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fournit une collection [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Chaque élément de la collection Cells représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

Il est possible d'appliquer des formules aux cellules à l'aide des propriétés et des méthodes offertes par la classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell), comme discuté plus en détail ci-dessous.

- Utilisation de fonctions intégrées.
- Utilisation de fonctions supplémentaires.
- Travailler avec des formules de tableau.
- Créer une formule R1C1.

## **Comment utiliser les fonctions intégrées**

 Les fonctions ou formules intégrées sont fournies sous forme de fonctions toutes faites pour réduire les efforts et le temps des développeurs. Voir [une liste des fonctions intégrées](/cells/fr/nodejs-cpp/supported-formula-functions/) prises en charge par Aspose.Cells. Les fonctions sont listées par ordre alphabétique. Plus de fonctions seront prises en charge à l'avenir.

 Aspose.Cells supporte la plupart des formules ou fonctions offertes par Microsoft Excel. Les développeurs peuvent utiliser ces formules via l’API ou [designer spreadsheet](/cells/fr/nodejs-cpp/what-is-a-designer-spreadsheet/). Aspose.Cells supporte un vaste ensemble de formules mathématiques, de chaînes, booléennes, date/heure, statistiques, bases de données, recherche et référence.

Utilisez la propriété [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--) de la classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) pour ajouter une formule à une cellule. **Les formules complexes**, par exemple

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, sont également prises en charge dans Aspose.Cells. Lors de l'application d'une formule à une cellule, commencez toujours la chaîne par un signe égal (=) comme vous le faites lors de la création d'une formule dans Microsoft Excel et utilisez une virgule (,) pour délimiter les paramètres de la fonction.

Dans l'exemple ci-dessous, une formule complexe est appliquée à la première cellule de la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) de la feuille de calcul. La formule utilise une fonction intégrée **SI** fournie par Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a value to "A1" cell
worksheet.getCells().get("A1").putValue(1);

// Adding a value to "A2" cell
worksheet.getCells().get("A2").putValue(2);

// Adding a value to "A3" cell
worksheet.getCells().get("A3").putValue(3);

// Adding a SUM formula to "A4" cell
worksheet.getCells().get("A4").setFormula("=SUM(A1:A3)");

// Calculating the results of formulas
workbook.calculateFormula();

// Get the calculated value of the cell
const value = worksheet.getCells().get("A4").getValue().toString();

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Comment utiliser les fonctions d'extension**

Nous pouvons avoir certaines formules définies par l'utilisateur que nous voulons inclure dans un complément Excel. Lors du réglage de la fonction cell.Formula les fonctions intégrées fonctionnent bien, cependant il est nécessaire de définir les fonctions ou formules personnalisées en utilisant les fonctions d'extension.

Aspose.Cells propose des fonctionnalités pour enregistrer des fonctions d'extension en utilisant [**Worksheets.registerAddInFunction(string, string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#registerAddInFunction-string-string-boolean-). Ensuite, lorsque nous définissons cell.Formula = anyFunctionFromAddIn, le fichier Excel de sortie contient la valeur calculée à partir de la fonction AddIn.

Le fichier XLAM suivant doit être téléchargé pour enregistrer la fonction d'extension dans le code d'exemple ci-dessous. De même, le fichier de sortie "test_udf.xlsx" peut être téléchargé pour vérifier la sortie.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create empty workbook
const workbook = new AsposeCells.Workbook();

// Register macro enabled add-in along with the function name
const id = workbook.getWorksheets().registerAddInFunction(path.join(dataDir, "TESTUDF.xlam"), "TEST_UDF", false);

// Register more functions in the file (if any)
workbook.getWorksheets().registerAddInFunction(id, "TEST_UDF1"); // in this way you can add more functions that are in the same file

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first cell
const cell = worksheet.getCells().get("A1");

// Set formula name present in the add-in
cell.setFormula("=TEST_UDF()");

// Save workbook to output XLSX format.
workbook.save(path.join(outputDir, "test_udf.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **Comment utiliser les formules de tableau**

Les formules de tableau sont des formules qui prennent des tableaux, au lieu de nombres individuels, en tant qu'arguments pour les fonctions qui composent la formule. Lorsqu'une formule de tableau est affichée, elle est entourée d'accolades ({}).

Certaines fonctions Microsoft Excel renvoient des tableaux de valeurs. Pour calculer plusieurs résultats avec une formule de tableau, entrez le tableau dans une plage de cellules avec le même nombre de lignes et de colonnes que les arguments du tableau.

Il est possible d'appliquer une formule de tableau à une cellule en appelant la méthode [**setArrayFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setArrayFormula-string-number-number-) de la classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). La méthode [**setArrayFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setArrayFormula-string-number-number-) prend les paramètres suivants:

- **Formule de tableau**, la formule de tableau.
- **Nombre de lignes**, le nombre de lignes pour remplir le résultat de la formule de tableau.
- **Nombre de colonnes**, le nombre de colonnes pour peupler le résultat de la formule de tableau.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a value to "A1" cell
worksheet.getCells().get("A1").putValue(1);

// Adding a value to "A2" cell
worksheet.getCells().get("A2").putValue(2);

// Adding a value to "A3" cell
worksheet.getCells().get("A3").putValue(3);

// Adding a value to B1
worksheet.getCells().get("B1").putValue(4);

// Adding a value to "B2" cell
worksheet.getCells().get("B2").putValue(5);

// Adding a value to "B3" cell
worksheet.getCells().get("B3").putValue(6);

// Adding a value to C1
worksheet.getCells().get("C1").putValue(7);

// Adding a value to "C2" cell
worksheet.getCells().get("C2").putValue(8);

// Adding a value to "C3" cell
worksheet.getCells().get("C3").putValue(9);

// Adding a SUM formula to "A4" cell
worksheet.getCells().get("A6").setArrayFormula("=LINEST(A1:A3,B1:C3,TRUE,TRUE)", 5, 3);

// Calculating the results of formulas
workbook.calculateFormula();

// Get the calculated value of the cell
const value = worksheet.getCells().get("A6").getValue().toString();

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Comment utiliser la formule R1C1**

Ajoutez une formule de référence R1C1 à une cellule avec la propriété de la classe [**getR1C1Formula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getR1C1Formula--) de la classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");
// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

const worksheet = workbook.getWorksheets().get(0);

// Setting an R1C1 formula on the "A11" cell, 
// Row and Column indices are relative to destination index
worksheet.getCells().get("A11").setR1C1Formula("=SUM(R[-10]C[0]:R[-7]C[0])");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Sujets avancés**
- [Précédents et dépendants](/cells/fr/nodejs-cpp/precedents-and-dependents/)
- [Définir des liens externes dans les formules](/cells/fr/nodejs-cpp/set-external-links-in-formulas/)
- [Propager la formule dans un tableau ou un objet de liste automatiquement lors de la saisie de données dans de nouvelles lignes](/cells/fr/nodejs-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Définition de la formule pour une plage nommée](/cells/fr/nodejs-cpp/setting-formula-for-named-range/)
- [Définition de formules - Avis aux utilisateurs non anglophones](/cells/fr/nodejs-cpp/setting-formulas-notice-for-non-english-users/)
- [Définition de formule partagée](/cells/fr/nodejs-cpp/setting-shared-formula/)
- [Spécifier le nombre maximum de lignes de formule partagée](/cells/fr/nodejs-cpp/specify-maximum-rows-of-shared-formula/)
- [Fonctions Excel prises en charge](/cells/fr/nodejs-cpp/supported-formula-functions/)

{{< app/cells/assistant language="nodejs-cpp" >}}
