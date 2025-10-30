---
title: Direkt beräkning av anpassad funktion utan att skriva den i ett kalkylblad med JavaScript via C++
linktitle: Direkt beräkning av anpassad funktion utan att skriva den i en kalkylblad
description: Denna artikel introducerar hur man använder Aspose.Cells biblioteket för att direkt beräkna anpassade funktioner i Microsoft Excel utan att skriva funktionen i ett kalkylblad med JavaScript via C++. Ladda en befintlig Excel fil eller skapa en ny, beräkna den anpassade funktionen och spara den modifierade filen.
keywords: Aspose.Cells, Excel, anpassade funktioner, direkt beräkningar, JavaScript via C++, behöver inte skriva, kalkylblad
type: docs
weight: 90
url: /sv/javascript-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Direkt beräkning av anpassad funktion utan att skriva den i en kalkylblad**

Denna artikel förklarar hur du kan direkt beräkna dina anpassade funktioner utan att först skriva dem i ett kalkylblad. Använd metod [**Worksheet.calculateFormula(formula, opts)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#calculateFormula-string-CalculationOptions-) för detta ändamål.

Se följande exempelkod som illustrerar användningen av denna metod. Vi har använt en anpassad funktion som heter MyCompany.CustomFunction() och beräknar dess värde som "Aspose.Cells." på egen hand och sedan konkateneras detta värde automatiskt med värdet för cell A1, vilket är "Välkommen till " av beräkningsmotorn och det slutliga beräknade värdet returneras som "Välkommen till Aspose.Cells.". Som du kan se i koden har vi inte skrivit vår anpassade funktion någonstans i en arbetsbok och den beräknas direkt av vår egen anpassade logik.

### **Programmeringsexempel**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Custom Function Example</title>
    </head>
    <body>
        <h1>Implement Direct Calculation Of Custom Function</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AbstractCalculationEngine, CalculationOptions } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        class CustomEngine extends AbstractCalculationEngine {
            // Override the calculate method with custom logic
            calculate(data) {
                // Check the formula name and calculate it yourself
                if (data.functionName === "MyCompany.CustomFunction") {
                    // This is our calculated value
                    data.calculatedValue = "Aspose.Cells.";
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Add some text in cell A1
            ws.cells.get("A1").putValue("Welcome to ");

            // Create a calculation options with custom engine
            const opts = new CalculationOptions();
            opts.customEngine = new CustomEngine();

            // This line shows how you can call your own custom function without
            // a need to write it in any worksheet cell
            // After the execution of this line, it will return
            // Welcome to Aspose.Cells.
            const ret = ws.calculateFormula("=A1 & MyCompany.CustomFunction()", opts);

            // Write the returned value into B1 for demonstration
            ws.cells.get("B1").putValue(ret);

            // Prepare download of the modified workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Calculated Value: ' + ret + '</p>';
        });
    </script>
</html>
```

### **Konsoloutput**

Nedan är konsol utmatningen av ovanstående provkod.

{{< highlight javascript >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Relaterad artikel**

{{% alert color="primary" %}}

 [Implementera anpassad beräkningsmotor för att utöka den standardmässiga beräkningsmotorn i Aspose.Cells](/cells/sv/javascript-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
