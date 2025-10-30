---
title: Implementieren Sie eine benutzerdefinierte Berechnungseinheit, um die Standard Berechnungseinheit von Aspose.Cells mit JavaScript via C++ zu erweitern
linktitle: Implementieren eines benutzerdefinierten Berechnungsmotors zur Erweiterung des standardmäßigen Berechnungsmotors von Aspose.Cells
description: Dieser Artikel beschreibt, wie man die Standard Berechnungseinheit in JavaScript erweitert, indem man eine benutzerdefinierte Berechnungseinheit unter Verwendung der Aspose.Cells Bibliothek für JavaScript via C++ implementiert. Laden Sie eine bestehende Excel Datei oder erstellen Sie eine neue, verwenden Sie die bereitgestellten Methoden und speichern Sie die modifizierte Excel Datei.
keywords: Aspose.Cells, Excel, benutzerdefinierte Berechnungseinheit, JavaScript via C++
type: docs
weight: 80
url: /de/javascript-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Benutzerdefinierten Berechnungsmotor implementieren**

Aspose.Cells verfügt über einen leistungsstarken Berechnungsmotor, der fast alle Microsoft Excel-Formeln berechnen kann. Trotzdem ermöglicht es Ihnen auch, den standardmäßigen Berechnungsmotor zu erweitern, was Ihnen mehr Leistung und Flexibilität bietet.

Die folgenden Eigenschaften und Klassen werden zur Umsetzung dieses Merkmals verwendet.

- [**CalculationOptions.customEngine**](https://reference.aspose.com/cells/javascript-cpp/calculationoptions/#customEngine--)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/javascript-cpp/calculationdata)

Der folgende Code implementiert die benutzerdefinierte Berechnungs-Engine. Er implementiert die Schnittstelle [**AbstractCalculationEngine**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine), die eine [**calculate(CalculationData data)**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine/#calculate-calculationdata-) Methode hat. Diese Methode wird für alle Ihre Formeln aufgerufen. Innerhalb dieser Methode erfassen wir die Funktion **HEUTE** und addieren einen Tag zum Systemdatum. Wenn das aktuelle Datum 27.07.2023 ist, berechnet die benutzerdefinierte Engine **HEUTE()** als 28.07.2023.

### **Programmierbeispiel**

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

### **Ergebnis**

Bitte überprüfen Sie die Konsolenausgabe des obigen Beispielcodes; der Wert (Datum und Uhrzeit) von A1 mit der benutzerdefinierten Engine sollte einen Tag später sein als das Ergebnis ohne die benutzerdefinierte Engine.

### **Verwandter Artikel**

{{% alert color="primary" %}}

 [Direkte Berechnung einer benutzerdefinierten Funktion, ohne sie in einem Arbeitsblatt zu schreiben](/cells/de/javascript-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
