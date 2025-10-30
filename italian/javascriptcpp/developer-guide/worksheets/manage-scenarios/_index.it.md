---
title: Crea, manipola o rimuovi scenari dai fogli di lavoro con JavaScript tramite C++
linktitle: Gestire gli scenari
type: docs
weight: 190
url: /it/javascript-cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: Impara come creare, manipolare o rimuovere scenari dai fogli di Excel programmaticamente usando l API JavaScript tramite C++.
keywords: crea scenario foglio di lavoro JavaScript tramite C++, rimuovi scenario foglio di lavoro Excel JavaScript tramite C++, manipola scenario foglio di lavoro JavaScript tramite C++
---

{{% alert color="primary" %}}

A volte è necessario creare, manipolare o eliminare scenari nei fogli di calcolo. Uno scenario è un modello 'cosa succederebbe se?' che include celle di input variabili collegate da una o più formule. Prima di creare uno scenario, progetta il foglio di lavoro in modo che contenga almeno una formula che dipende da celle in cui possono essere inseriti valori diversi. L'esempio seguente mostra come creare e rimuovere scenari da un foglio di lavoro in un libro tramite le API Aspose.Cells.

{{% /alert %}}

Aspose.Cells fornisce alcune classi utili, ad esempio, le classi [**ScenarioCollection**](https://reference.aspose.com/cells/javascript-cpp/scenariocollection), [**Scenario**](https://reference.aspose.com/cells/javascript-cpp/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/javascript-cpp/scenarioinputcellcollection) e [**ScenarioInputCell**](https://reference.aspose.com/cells/javascript-cpp/scenarioinputcell). Fornisce anche la proprietà [**Worksheet.scenarios**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#scenarios--). Il codice esempio qui sotto apre un file XLSX di Excel che contiene alcuni scenari e rimuove uno scenario esistente. Inoltre, aggiunge un nuovo scenario al foglio di lavoro prima di salvare il file Excel. L'esempio utilizza un file modello molto semplice che contiene uno scenario.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Scenarios Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Scenarios Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate the Workbook by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            if (worksheet.scenarios.count > 0) {
                // Remove the existing first scenario from the sheet
                worksheet.scenarios.removeAt(0);
            }

            // Create a scenario
            const i = worksheet.scenarios.add("MyScenario");
            // Get the scenario
            const scenario = worksheet.scenarios.get(i);
            // Add comment to it
            scenario.comment = "Test scenario is created.";
            // Get the input cells for the scenario
            const sic = scenario.inputCells;
            // Add the scenario on B4 (as changing cell) with default value
            sic.add(3, 1, "1100000");

            // Save the Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outBk_scenarios1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Process completed successfully. File ready for download.</p>';
        });
    </script>
</html>
```
