---
title: Mettre en œuvre un moteur de calcul personnalisé pour étendre le moteur de calcul par défaut d Aspose.Cells avec Node.js via C++
linktitle: Implémenter un moteur de calcul personnalisé pour étendre le moteur de calcul par défaut de Aspose.Cells
description: Cet article décrit comment étendre le moteur de calcul par défaut dans Node.js en implémentant un moteur de calcul personnalisé en utilisant la bibliothèque Aspose.Cells pour Node.js via C++. Chargez un fichier Excel existant ou créez en un nouveau pour utiliser les méthodes fournies et enregistrez le fichier Excel modifié.
keywords: Aspose.Cells, Excel, moteur de calcul personnalisé, Node.js via C++
type: docs
weight: 80
url: /fr/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Implémenter un moteur de calcul personnalisé**

Aspose.Cells dispose d'un puissant moteur de calcul qui peut calculer presque toutes les formules Microsoft Excel. Malgré cela, il vous permet également d'étendre le moteur de calcul par défaut, ce qui vous offre plus de puissance et de flexibilité.

La propriété et les classes suivantes sont utilisées pour implémenter cette fonctionnalité.

- [**CalculationOptions.getCustomEngine()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getCustomEngine--)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/nodejs-cpp/calculationdata)

Le code suivant implémente le moteur de calcul personnalisé. Il implémente l'interface [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) qui possède une méthode [**calculate(CalculationData data)**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine/#calculate-calculationdata-). Cette méthode est appelée pour toutes vos formules. À l'intérieur de cette méthode, nous capturons la fonction **TODAY** et ajoutons un jour à la date système. Donc, si la date actuelle est le 27/07/2023, alors le moteur personnalisé calculera TODAY() comme étant le 28/07/2023.

### **Exemple de programmation**

```javascript
const AsposeCells = require("aspose.cells.node");

// Create a new class derived from AbstractCalculationEngine
class CustomEngine extends AsposeCells.AbstractCalculationEngine {
// Override the Calculate method with custom logic
calculate(data) {
// Check the formula name and change the implementation
if (data.getFunctionName().toUpperCase() === "TODAY") {
// Assign the CalculationData.CalculatedValue: add one day offset for the date
data.setCalculatedValue(AsposeCells.CellsHelper.getDoubleFromDateTime(new Date(), false) + 1.0);
}
}
getProcessBuiltInFunctions() {
return true;
}
}

class ImplementCustomCalculationEngine {
static run() {
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook();

// Access first Worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Access Cell A1 and put a formula to sum values of B1 to B2
const a1 = sheet.getCells().get("A1");
const style = a1.getStyle();
style.setNumber(14);
a1.setStyle(style);

a1.setFormula("=TODAY()");

// Calculate all formulas in the Workbook 
workbook.calculateFormula();

// The result of A1 should be 20 as per default calculation engine
console.log("The value of A1 with default calculation engine: " + a1.getStringValue());

// Create an instance of CustomEngine
const engine = new CustomEngine();

// Create an instance of CalculationOptions
const opts = new AsposeCells.CalculationOptions();

// Assign the CalculationOptions.CustomEngine property to the instance of CustomEngine
opts.setCustomEngine(engine);

// Recalculate all formulas in Workbook using the custom calculation engine
workbook.calculateFormula(opts);

// The result of A1 will be 50 as per custom calculation engine
console.log("The value of A1 with custom calculation engine: " + a1.getStringValue());

console.log("Press any key to continue...");
}
}

// Call the run method to execute the example
ImplementCustomCalculationEngine.run();
```

### **Résultat**

Veuillez vérifier la sortie de la console du code d'exemple ci-dessus ; la valeur (date-heure) de A1 avec le moteur personnalisé devrait être un jour plus tard que le résultat sans le moteur personnalisé.

### **Article connexe**

{{% alert color="primary" %}}

[Calcul direct de la fonction personnalisée sans l'écrire dans une feuille](/cells/fr/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
