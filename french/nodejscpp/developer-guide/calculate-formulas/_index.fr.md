---
title: Calculer les formules avec Node.js via C++
linktitle: Calcul des formules
description: Cet article présente comment utiliser la bibliothèque Aspose.Cells pour calculer les formules dans Microsoft Excel en utilisant Node.js via C++. En chargeant un fichier Excel existant ou en créant un nouveau fichier Excel, nous pouvons utiliser les méthodes fournies par Aspose.Cells pour calculer la formule et obtenir le résultat. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, formules, calculs, Calcul direct d une formule, Calculer les formules à répétition, ajouter des formules Node.js via C++
type: docs
weight: 125
url: /fr/nodejs-cpp/calculate-formulas/
---

## **Ajout de formules et calcul de résultats**

Aspose.Cells dispose d’un moteur de calcul de formules intégré. Il peut non seulement recalculer les formules importées à partir de modèles de conception, mais également supporter le calcul des résultats des formules ajoutées en temps réel.

Aspose.Cells supporte la plupart des formules ou fonctions qui font partie de Microsoft Excel (lisez [une liste des fonctions prises en charge par le moteur de calcul](/cells/fr/nodejs-cpp/supported-formula-functions/)). Ces fonctions peuvent être utilisées via les API ou la création de feuilles de calcul. Aspose.Cells supporte un vaste ensemble de formules mathématiques, de chaînes, logiques, date/heure, statistiques, bases de données, recherche et référence.

Utilisez la propriété [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--) ou les méthodes [**setFormula(string, object)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setFormula-string-object-) de la classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) pour ajouter une formule à une cellule. Lors de l’application d’une formule, commencez toujours la chaîne par un signe égal (=), comme lors de la création d’une formule dans Microsoft Excel, et utilisez une virgule (,) pour délimiter les paramètres des fonctions.

Pour calculer les résultats des formules, l'utilisateur peut appeler la méthode [**calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) de la classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) qui traite toutes les formules intégrées dans un fichier Excel. Ou, l'utilisateur peut appeler la méthode [**calculateFormula(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-) de la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) qui traite toutes les formules d'une feuille. Ou, l'utilisateur peut aussi appeler la méthode [**calculate(CalculationOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#calculate-calculationoptions-) de la classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) qui traite la formule d'une seule cellule :

```javascript
const path = require("path");
const fs = require("fs");
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

### **Important à savoir pour les formules**

{{% alert color="primary" %}}

La propriété **Formula** et les méthodes **setFormula(...)** de la classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) fonctionnent différemment des méthodes **calculate** des classes [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet), et [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). La propriété **Formula** et les méthodes **setFormula(...)** ajoutent simplement la formule à une cellule mais ne calculent pas le résultat à l'exécution. Pour obtenir le résultat des formules, veuillez appeler les méthodes **calculate**.

{{% /alert %}}

## **Calcul direct de formule**

Aspose.Cells possède un moteur de calcul de formules intégré. En plus de calculer les formules importées à partir d'un fichier, Aspose.Cells peut calculer les résultats des formules directement.

Parfois, vous souhaitez calculer directement les résultats des formules sans les ajouter dans une feuille de calcul. Les valeurs des cellules utilisées dans la formule existent déjà dans une feuille, et tout ce que vous avez à faire est de trouver le résultat de ces valeurs en utilisant une formule Microsoft Excel sans ajouter la formule dans une feuille.

Vous pouvez utiliser les API du moteur de calcul de formules d'Aspose.Cells pour [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) à [**calculateFormula(string, FormulaParseOptions, CalculationOptions, number, number, CalculationData)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-formulaparseoptions-calculationoptions-number-number-calculationdata-) pour obtenir les résultats de telles formules sans les ajouter dans la feuille :

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put 20 in cell A1
const cellA1 = worksheet.getCells().get("A1");
cellA1.putValue(20);

// Put 30 in cell A2
const cellA2 = worksheet.getCells().get("A2");
cellA2.putValue(30);

// Calculate the Sum of A1 and A2
const results = worksheet.calculateFormula("=Sum(A1:A2)");

// Print the output
console.log("Value of A1: " + cellA1.getStringValue());
console.log("Value of A2: " + cellA2.getStringValue());
console.log("Result of Sum(A1:A2): " + results.toString());
```

Le code ci-dessus produit la sortie suivante :
{{< highlight nodejs >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Comment calculer des formules de manière répétée**

Lorsqu'il y a beaucoup de formules dans le classeur, et que l'utilisateur doit les calculer à plusieurs reprises en modifiant uniquement une petite partie d'entre elles, il peut être utile pour la performance d'activer la chaîne de calcul des formules : [**formulaSettings.getEnableCalculationChain()**](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getEnableCalculationChain--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load the template workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Print the time before formula calculation
console.log(new Date());

// Set the CreateCalcChain as true
workbook.getSettings().getFormulaSettings().setEnableCalculationChain(true);

// Calculate the workbook formulas
workbook.calculateFormula();

// Print the time after formula calculation
console.log(new Date());

// Change the value of one cell
workbook.getWorksheets().get(0).getCells().get("A1").putValue("newvalue");

// Re-calculate those formulas which depend on cell A1
workbook.calculateFormula();
```

### **Important à savoir**

{{% alert color="primary" %}}

Par défaut, la chaîne de calcul est désactivée. Car la création de la chaîne nécessite également du temps supplémentaire, la première fois que vous calculez les formules ([**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)) peut consommer plus de temps CPU et de mémoire par rapport au calcul sans chaîne. Si l'utilisateur n'a pas besoin de recalculer les formules à plusieurs reprises, le comportement par défaut (calculer directement la formule sans créer une chaîne de calcul) devrait être la meilleure option.

{{% /alert %}}

## **Sujets avancés**
- [Ajouter des cellules à la fenêtre de surveillance des formules Microsoft Excel](/cells/fr/nodejs-cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Calcul de la fonction SIERREUR en utilisant Aspose.Cells](/cells/fr/nodejs-cpp/calculating-ifna-function-using-aspose-cells/)
- [Calcul de la formule de tableau de données](/cells/fr/nodejs-cpp/calculation-of-array-formula-of-data-tables/)
- [Calcul des fonctions MINIFS et MAXIFS d'Excel 2016](/cells/fr/nodejs-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Réduire le temps de calcul de la méthode Cell.calculate](/cells/fr/nodejs-cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Détection des références circulaires](/cells/fr/nodejs-cpp/detecting-circular-reference/)
- [Calcul direct d'une fonction personnalisée sans l'écrire dans une feuille de calcul](/cells/fr/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implémenter un moteur de calcul personnalisé pour étendre le moteur de calcul par défaut d'Aspose.Cells](/cells/fr/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Interrompre ou annuler le calcul de formule du classeur](/cells/fr/nodejs-cpp/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Retourner une plage de valeurs en utilisant AbstractCalculationEngine](/cells/fr/nodejs-cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Définir le mode de calcul de formule du classeur](/cells/fr/nodejs-cpp/setting-formula-calculation-mode-of-workbook/)
- [Utilisation de la fonction FormulaText dans Aspose.Cells](/cells/fr/nodejs-cpp/using-formulatext-function-in-aspose-cells/)
