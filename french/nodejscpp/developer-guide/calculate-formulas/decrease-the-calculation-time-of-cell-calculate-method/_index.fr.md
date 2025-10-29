---  
title: Diminuer le temps de calcul de la méthode Cell.Calculate avec Node.js via C++  
linktitle: Réduire le temps de calcul de la méthode Cell.Calculate  
description: Cet article présente comment utiliser la bibliothèque Aspose.Cells pour réduire le temps de calcul des méthodes de calcul de cellules dans Excel en utilisant Node.js via C++.  
keywords: Aspose.Cells, Excel, méthodes de calcul de cellule, optimisation, performance, réduction du temps de calcul, Node.js via C++  
type: docs  
weight: 100  
url: /fr/nodejs-cpp/decrease-the-calculation-time-of-cell-calculate-method/  
---  

## **Scénarios d'utilisation possibles**

Normalement, nous recommandons aux utilisateurs d'appeler la méthode [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) une fois puis d’obtenir les valeurs calculées de chaque cellule. Mais parfois, les utilisateurs ne veulent pas calculer tout le classeur. Ils veulent juste calculer une seule cellule. Aspose.Cells offre la propriété [**CalculationOptions.getRecursive()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getRecursive--), que vous pouvez définir sur **false** pour réduire considérablement le temps de calcul des cellules individuelles. Si la propriété récursive est définie sur **true**, toutes les dépendances des cellules sont recalculées à chaque appel. Cependant, si la propriété récursive est **false**, les cellules dépendantes ne sont calculées qu’une seule fois et ne sont pas recalculées lors des appels suivants.

## **Diminuer le temps de calcul de la méthode Cell.calculate()**

Le code d'exemple ci-dessous illustre l’utilisation de la propriété [**CalculationOptions.getRecursive()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getRecursive--). Veuillez exécuter ce code avec le [fichier Excel d'exemple](5113710.xlsx) fourni et vérifier sa sortie console. Vous constaterez que la mise en propriété récursive sur **false** a considérablement réduit le temps de calcul. Veuillez également lire les commentaires pour une meilleure compréhension de cette propriété.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Test calculation time after setting recursive true
workbook.calculateFormula(); // Call calculateFormula method to initiate calculation

// Test calculation time after setting recursive false
workbook.calculateFormula(false); // Specify ignoreError as false
```  
```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

function testCalcTimeRecursive(rec) {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your sample workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

// Set the calculation option, set recursive true or false as per parameter
const opts = new AsposeCells.CalculationOptions();
opts.setRecursive(rec);

// Start stop watch            
const start = process.hrtime();

// Calculate cell A1 one million times
for (let i = 0; i < 1000000; i++) {
ws.getCells().get("A1").calculate(opts);
}

// Stop the watch
const end = process.hrtime(start);

// Calculate elapsed time in seconds
const estimatedTime = end[0] + end[1] / 1e9;

// Print the elapsed time in seconds
console.log(`Recursive ${rec}: ${estimatedTime} seconds`);
}

// Call the function for testing
testCalcTimeRecursive(true);
testCalcTimeRecursive(false);
```

## **Sortie console**

Voici la sortie console du code d'exemple ci-dessus lorsqu’il est exécuté avec le [fichier Excel d'exemple](5113710.xlsx) sur notre machine. Notez que votre sortie peut différer, mais le temps écoulé après avoir défini la propriété récursive sur **false** sera toujours inférieur à celui lorsqu’elle est sur **true**.

{{< highlight java >}}  
Recursive True: 96 seconds  

Recursive False: 42 seconds  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
