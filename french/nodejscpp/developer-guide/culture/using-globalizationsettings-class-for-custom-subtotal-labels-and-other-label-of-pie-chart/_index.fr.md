---
title: Utilisation de la classe GlobalizationSettings pour des étiquettes personnalisées de sous totaux et autres étiquettes de graphique à secteurs avec Node.js via C++
linktitle: Utilisation de la classe GlobalizationSettings pour les étiquettes de sous total personnalisées et d autres étiquettes de graphique circulaire
type: docs
weight: 70
url: /fr/nodejs-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
description: Apprenez comment personnaliser les étiquettes de sous totaux et autres étiquettes de graphiques à secteurs en utilisant la classe GlobalizationSettings dans Aspose.Cells for Node.js via C++.
---

## **Scénarios d'utilisation possibles**

Les API Aspose.Cells ont exposé la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) afin de gérer les scénarios où l'utilisateur souhaite utiliser des étiquettes personnalisées pour les sous-totaux dans une feuille de calcul. De plus, la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) peut également être utilisée pour modifier l'étiquette **Autre** pour le graphique à secteurs lors du rendu de la feuille de calcul ou du graphique.

## **Introduction à la classe GlobalizationSettings**

La classe [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) offre actuellement les 3 méthodes suivantes qui peuvent être surchargées dans une classe personnalisée pour obtenir les étiquettes souhaitées pour les sous-totaux ou pour rendre un texte personnalisé pour l’étiquette **Autre** d’un graphique à secteurs.

1. [**GlobalizationSettings.getTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getTotalName-consolidationfunction-) : Obtient le nom total de la fonction.
1. [**GlobalizationSettings.getGrandTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getGrandTotalName-consolidationfunction-) : Obtient le nom du total général de la fonction.


### **Étiquettes personnalisées pour les sous-totaux**

La classe [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) peut être utilisée pour personnaliser les étiquettes de sous-totaux en surchargeant les méthodes [**GlobalizationSettings.getTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getTotalName-consolidationfunction-) & [**GlobalizationSettings.getGrandTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getGrandTotalName-consolidationfunction-) comme démontré ci-après.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Defines a custom class derived from GlobalizationSettings class
class CustomSettings extends AsposeCells.GlobalizationSettings {
// Overrides the GetTotalName method
getTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "AVG";
// Handle other cases as per requirement
default:
return super.getTotalName(functionType);
}
}

// Overrides the GetGrandTotalName method
getGrandTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "GRD AVG";
// Handle other cases as per requirement
default:
return super.getGrandTotalName(functionType);
}
}
}
```

Pour injecter des étiquettes personnalisées, il est nécessaire d'assigner la propriété [**WorkbookSettings.getGlobalizationSettings()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getGlobalizationSettings--) à une instance de la classe **CustomSettings** définie ci-dessus avant d'ajouter les sous-totaux à la feuille de calcul.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// Defines a custom class derived from GlobalizationSettings class
class CustomSettings extends AsposeCells.GlobalizationSettings {
// Overrides the GetTotalName method
getTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "AVG";
// Handle other cases as per requirement
default:
return super.getTotalName(functionType);
}
}

// Overrides the GetGrandTotalName method
getGrandTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "GRD AVG";
// Handle other cases as per requirement
default:
return super.getGrandTotalName(functionType);
}
}
}

try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Loads an existing spreadsheet containing some data
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Assigns the GlobalizationSettings property of the WorkbookSettings class to a custom class created
workbook.getSettings().setGlobalizationSettings(new CustomSettings());

// Accesses the 1st worksheet from the collection which contains data that resides in the cell range A2:B9
const sheet = workbook.getWorksheets().get(0);

// Adds Subtotal of type Average to the worksheet
sheet.getCells().subtotal(AsposeCells.CellArea.createCellArea("A2", "B9"), 0, AsposeCells.ConsolidationFunction.Average, [1]);

// Calculates Formulas
workbook.calculateFormula();

// Auto fits all columns
sheet.autoFitColumns();

// Saves the workbook on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
} catch (error) {
console.error(`Test failed: ${error.message}`);
throw error;
}
```

{{% alert color="primary" %}}

La classe [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) fonctionne uniquement pour l'ajout de nouveaux sous-totaux. Si une feuille de calcul contient déjà des sous-totaux, leurs étiquettes ne peuvent pas être modifiées.

{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}
