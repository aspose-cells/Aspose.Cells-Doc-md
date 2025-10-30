---
title: Calcolo diretto di funzione personalizzata senza scriverla in un foglio di lavoro con JavaScript tramite C++.
linktitle: Calcolo diretto di una funzione personalizzata senza scriverla in un foglio di lavoro
description: Quest articolo introduce come usare la libreria Aspose.Cells per calcolare direttamente funzioni personalizzate in Microsoft Excel senza scrivere la funzione in un foglio di lavoro usando JavaScript tramite C++. Carica un file Excel esistente o creane uno nuovo, calcola la funzione personalizzata, e salva il file modificato.
keywords: Aspose.Cells, Excel, funzioni personalizzate, calcoli diretti, JavaScript tramite C++, nessuna necessità di scrivere, fogli di lavoro
type: docs
weight: 90
url: /it/javascript-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Calcolo diretto della funzione personalizzata senza scriverla in un foglio di lavoro**

Questo argomento spiega come calcolare direttamente le proprie funzioni personalizzate senza prima scriverle in un foglio di lavoro. Utilizzare il metodo [**Worksheet.calculateFormula(formula, opts)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#calculateFormula-string-CalculationOptions-) a questo scopo.

Si prega di vedere il seguente codice di esempio che illustra l'uso di questo metodo. Abbiamo utilizzato una funzione personalizzata chiamata MyCompany.CustomFunction() e ne calcoliamo il valore come "Aspose.Cells." e questo valore viene automaticamente concatenato con il valore della cella A1 che è "Benvenuto in " dall'interprete di calcolo e il valore calcolato finale ritorna come "Benvenuto in Aspose.Cells.".". Come si può vedere dal codice, non abbiamo scritto la nostra funzione personalizzata da nessuna parte in un foglio di lavoro ed è calcolata direttamente dalla nostra logica personalizzata.

### **Esempio di programmazione**

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

### **Output della console**

Di seguito è riportato l'output della console del codice di esempio sopra.

{{< highlight javascript >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Articolo correlato**

{{% alert color="primary" %}}

[Implementare il motore di calcolo personalizzato per estendere il motore di calcolo predefinito di Aspose.Cells](/cells/it/javascript-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
