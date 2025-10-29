---
title: Retourner une plage de valeurs en utilisant AbstractCalculationEngine avec Node.js via C++
linktitle: Renvoyer une plage de valeurs en utilisant AbstractCalculationEngine
description: Cet article présente un moteur de calcul abstrait qui retourne une plage de valeurs dans Excel en utilisant la bibliothèque Aspose.Cells pour Node.js via C++. Apprenez à charger ou créer un fichier Excel et à enregistrer le fichier modifié sur le disque.
keywords: Aspose.Cells, Excel, moteur de calcul abstrait retournant des valeurs Node.js via C++, fonctions personnalisées
type: docs
weight: 55
url: /fr/nodejs-cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells fournit la classe [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) qui est utilisée pour implémenter des fonctions définies par l'utilisateur ou personnalisées non prises en charge par Microsoft Excel en tant que fonctions intégrées.

Cet article expliquera comment renvoyer la plage de valeurs de [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine).

{{% /alert %}}

Le code suivant démontre l'utilisation de la classe [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) et retourne la plage de valeurs via sa méthode.

Créez une classe avec une fonction *calculateCustomFunction*. Cette classe implémente [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine).

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomFunctionStaticValue extends AsposeCells.AbstractCalculationEngine {
calculate(data) {
data.setCalculatedValue([
[new Date(2015, 5, 12, 10, 6, 30), 2],
[3.0, "Test"]
]);
}
}
```

Utilisez maintenant la fonction ci-dessus dans votre programme

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomFunctionStaticValue extends AsposeCells.AbstractCalculationEngine {
calculate(data) {
data.setCalculatedValue([
[new Date(2015, 5, 12, 10, 6, 30), 2],
[3.0, "Test"]
]);
}
}

try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook
const workbook = new AsposeCells.Workbook();
const cells = workbook.getWorksheets().get(0).getCells();

// Set formula
const cell = cells.get(0, 0);
cell.setArrayFormula("=MYFUNC()", 2, 2);

const style = cell.getStyle();
style.setNumber(14);
cell.setStyle(style);

// Set calculation options for formula
const calculationOptions = new AsposeCells.CalculationOptions();
calculationOptions.setCustomEngine(new CustomFunctionStaticValue());
workbook.calculateFormula(calculationOptions);

// Save to xlsx by setting the calc mode to manual
workbook.getSettings().getFormulaSettings().setCalculationMode(AsposeCells.CalcModeType.Manual);
workbook.save(dataDir + "output_out.xlsx");

// Save to pdf
workbook.save(dataDir + "output_out.pdf");
} catch (error) {
console.error(`Test failed: ${error.message}`);
throw error;
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
