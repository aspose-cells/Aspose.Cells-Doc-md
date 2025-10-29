---
title: Implémenter un moteur de calcul personnalisé pour étendre le moteur de calcul par défaut d Aspose.Cells avec JavaScript via C++
linktitle: Implémenter un moteur de calcul personnalisé pour étendre le moteur de calcul par défaut de Aspose.Cells
description: Cet article décrit comment étendre le moteur de calcul par défaut en JavaScript en implémentant un moteur de calcul personnalisé en utilisant la bibliothèque Aspose.Cells pour JavaScript via C++. Charger un fichier Excel existant ou en créer un nouveau pour utiliser les méthodes fournies et sauvegarder le fichier Excel modifié.
keywords: Aspose.Cells, Excel, moteur de calcul personnalisé, JavaScript via C++
type: docs
weight: 80
url: /fr/javascript-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Implémenter un moteur de calcul personnalisé**

Aspose.Cells dispose d'un puissant moteur de calcul qui peut calculer presque toutes les formules Microsoft Excel. Malgré cela, il vous permet également d'étendre le moteur de calcul par défaut, ce qui vous offre plus de puissance et de flexibilité.

La propriété et les classes suivantes sont utilisées pour implémenter cette fonctionnalité.

- [**CalculationOptions.customEngine**](https://reference.aspose.com/cells/javascript-cpp/calculationoptions/#customEngine--)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/javascript-cpp/calculationdata)

Le code suivant implémente le moteur de calcul personnalisé. Il implémente l'interface [**AbstractCalculationEngine**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine) qui possède une méthode [**calculate(CalculationData data)**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine/#calculate-calculationdata-). Cette méthode est appelée pour toutes vos formules. À l'intérieur de cette méthode, nous capturons la fonction **TODAY** et ajoutons un jour à la date système. Donc, si la date actuelle est le 27/07/2023, alors le moteur personnalisé calculera TODAY() comme étant le 28/07/2023.

### **Exemple de programmation**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Custom Calculation Engine Example</title>
    </head>
    <body>
        <h1>Custom Calculation Engine Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CalculationOptions, CellsHelper } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').disabled = false;
        });

        // Create a new class derived from AbstractCalculationEngine
        class CustomEngine extends AsposeCells.AbstractCalculationEngine {
            constructor() {
                super();
                // Indicate processing built-in functions
                this.processBuiltInFunctions = true;
            }

            // Override the Calculate method with custom logic
            calculate(data) {
                // Check the formula name and change the implementation
                if (data.functionName.toUpperCase() === "TODAY") {
                    // Assign the CalculationData.CalculatedValue: add one day offset for the date
                    data.calculatedValue = CellsHelper.getDoubleFromDateTime(new Date(), false) + 1.0;
                }
            }
        }

        class ImplementCustomCalculationEngine {
            static run() {
                // Create an instance of Workbook
                const workbook = new Workbook();

                // Access first Worksheet from the collection
                const sheet = workbook.worksheets.get(0);

                // Access Cell A1 and put a formula to sum values of B1 to B2
                const a1 = sheet.cells.get("A1");
                const style = a1.style;
                style.number = 14;
                a1.style = style;

                a1.formula = "=TODAY()";

                // Calculate all formulas in the Workbook 
                workbook.calculateFormula();

                // The result of A1 with default calculation engine
                console.log("The value of A1 with default calculation engine: " + a1.stringValue);

                // Create an instance of CustomEngine
                const engine = new CustomEngine();

                // Create an instance of CalculationOptions
                const opts = new CalculationOptions();

                // Assign the CalculationOptions.CustomEngine property to the instance of CustomEngine
                opts.customEngine = engine;

                // Recalculate all formulas in Workbook using the custom calculation engine
                workbook.calculateFormula(opts);

                // The result of A1 with custom calculation engine
                console.log("The value of A1 with custom calculation engine: " + a1.stringValue);

                console.log("Press any key to continue...");

                document.getElementById('result').innerHTML = '<p style="color: green;">Calculation completed. Check console for output.</p>';
            }
        }

        document.getElementById('runExample').addEventListener('click', () => {
            ImplementCustomCalculationEngine.run();
        });
    </script>
</html>
```

### **Résultat**

Veuillez vérifier la sortie de la console du code d'exemple ci-dessus ; la valeur (date-heure) de A1 avec le moteur personnalisé devrait être un jour plus tard que le résultat sans le moteur personnalisé.

### **Article connexe**

{{% alert color="primary" %}}

[Calcul direct d'une fonction personnalisée sans l'écrire dans une feuille de calcul](/cells/fr/javascript-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
