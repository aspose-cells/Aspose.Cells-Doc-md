---
title: Calcul direct d une fonction personnalisée sans l écrire dans une feuille de calcul avec Node.js via C++
linktitle: Calcul direct de fonction personnalisée sans l écrire dans une feuille de calcul
description: Cet article explique comment utiliser la bibliothèque Aspose.Cells pour calculer directement des fonctions personnalisées dans Microsoft Excel sans écrire la fonction dans une feuille de calcul en utilisant Node.js via C++. Chargez un fichier Excel existant ou créez en un nouveau, calculez la fonction personnalisée, et enregistrez le fichier modifié.
keywords: Aspose.Cells, Excel, fonctions personnalisées, calculs directs, Node.js via C++, pas besoin d’écrire, feuilles de calcul
type: docs
weight: 90
url: /fr/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Calcul direct d'une fonction personnalisée sans l'écrire dans une feuille de calcul**

Ce sujet explique comment vous pouvez calculer directement vos fonctions personnalisées sans les écrire d’abord dans une feuille de calcul. Veuillez utiliser la méthode [**Worksheet.calculateFormula(formula, opts)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-CalculationOptions-) à cette fin.

Veuillez consulter le code d'exemple suivant qui illustre l'utilisation de cette méthode. Nous avons utilisé une fonction personnalisée nommée MyCompany.CustomFunction() et nous calculons sa valeur comme "Aspose.Cells." par nous-mêmes, puis cette valeur est automatiquement concaténée avec la valeur de la cellule A1 qui est "Bienvenue à " par le moteur de calcul, et la valeur calculée finale retourne comme "Bienvenue à Aspose.Cells.". Comme vous pouvez le voir dans le code, nous n'avons pas écrit notre fonction personnalisée nulle part dans une feuille de calcul et elle est calculée directement par notre propre logique personnalisée.

### **Exemple de programmation**

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomEngine extends AsposeCells.AbstractCalculationEngine {
// Override the Calculate method with custom logic
calculate(data) {
// Check the formula name and calculate it yourself
if (data.getFunctionName() === "MyCompany.CustomFunction") {
// This is our calculated value
data.setCalculatedValue("Aspose.Cells.");
}
}
}

class ImplementDirectCalculationOfCustomFunction {
static run() {
// Create a workbook
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Add some text in cell A1
ws.getCells().get("A1").putValue("Welcome to ");

// Create a calculation options with custom engine
const opts = new AsposeCells.CalculationOptions();
opts.setCustomEngine(new CustomEngine());

// This line shows how you can call your own custom function without
// a need to write it in any worksheet cell
// After the execution of this line, it will return
// Welcome to Aspose.Cells.
const ret = ws.calculateFormula("=A1 & MyCompany.CustomFunction()", opts);

// Print the calculated value
console.log("Calculated Value: " + ret);
}
}

// Example invocation
ImplementDirectCalculationOfCustomFunction.run();
```

### **Sortie console**

Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight javascript >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Article connexe**

{{% alert color="primary" %}}

[Mettre en œuvre un moteur de calcul personnalisé pour étendre le moteur de calcul par défaut d'Aspose.Cells](/cells/fr/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
