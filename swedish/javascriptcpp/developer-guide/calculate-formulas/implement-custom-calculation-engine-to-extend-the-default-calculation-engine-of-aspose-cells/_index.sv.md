---
title: Implementera anpassad beräkningsmotor för att utöka den standardmässiga beräkningsmotorn i Aspose.Cells med JavaScript via C++
linktitle: Implementera anpassad beräkningsmotor för att utöka Aspose.Cells standardberäkningsmotor
description: Denna artikel beskriver hur man utökar den standardmässiga beräkningsmotorn i JavaScript genom att implementera en anpassad beräkningsmotor med Aspose.Cells biblioteket för JavaScript via C++. Ladda en befintlig Excel fil eller skapa en ny för att använda de tillhandahållna metoderna och spara den modifierade Excel filen.
keywords: Aspose.Cells, Excel, Anpassad beräkningsmotor, JavaScript via C++
type: docs
weight: 80
url: /sv/javascript-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Implementera anpassad beräkningsmotor**

Aspose.Cells har en kraftfull beräkningsmotor som kan beräkna nästan alla Microsoft Excel formler. Trots detta tillåter det dig också att utöka standardberäkningsmotorn vilket ger dig större kraft och flexibilitet.

Följande egenskap och klasser används vid implementering av denna funktion.

- [**CalculationOptions.customEngine**](https://reference.aspose.com/cells/javascript-cpp/calculationoptions/#customEngine--)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/javascript-cpp/calculationdata)

Följande kod implementerar den anpassade beräkningsmotorn. Den implementerar gränssnittet [**AbstractCalculationEngine**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine) som har en [**calculate(CalculationData data)**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine/#calculate-calculationdata-) metod. Denna metod anropas för alla dina formler. Inuti denna metod fångar vi **TODAY**-funktionen och lägger till en dag till systemdatumet. Så om dagens datum är 27/07/2023, kommer den anpassade motorn att beräkna TODAY() som 28/07/2023.

### **Programmeringsexempel**

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

### **Resultat**

Vänligen kontrollera konsolutmatningen för ovanstående exempel; värdet (datum/tid) för A1 med den anpassade motorn bör vara en dag senare än resultatet utan den anpassade motorn.

### **Relaterad artikel**

{{% alert color="primary" %}}

 [Direkt beräkning av anpassad funktion utan att skriva den i ett kalkylblad](/cells/sv/javascript-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
