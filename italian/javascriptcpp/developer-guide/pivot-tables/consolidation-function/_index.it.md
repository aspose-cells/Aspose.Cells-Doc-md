---
title: Funzione di consolidamento
type: docs
weight: 20
url: /it/javascript-cpp/consolidation-function/
description: Come applicare la funzione di consolidamento ai campi dati della tabella pivot con Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells for JavaScript tramite C++ Excel, libreria Excel JavaScript, funzione di consolidamento ai campi dati della tabella pivot usando Aspose.Cells for JavaScript via C++ Excel.
---

## **funzione di consolidamento**

Aspose.Cells for JavaScript via C++ può essere usato per applicare la funzione di consolidamento ai campi dati (o campi valore) della tabella pivot. In Microsoft Excel, puoi cliccare con il tasto destro sul campo valore e selezionare l'opzione **Impostazioni del campo valore...** quindi selezionare la scheda **Riepiloga valori per**. Da qui, puoi scegliere qualsiasi funzione di consolidamento come Somma, Conta, Media, Max, Min, Prodotto, Conta distinta, ecc.

Aspose.Cells for JavaScript via C++ fornisce l'enumerazione [**ConsolidationFunction**](https://reference.aspose.com/cells/javascript-cpp/consolidationfunction/) per supportare le seguenti funzioni di consolidamento.

- ConsolidationFunction.Average
- ConsolidationFunction.Count
- ConsolidationFunction.CountNums
- ConsolidationFunction.DistinctCount
- ConsolidationFunction.Max
- ConsolidationFunction.Min
- ConsolidationFunction.Product
- ConsolidationFunction.StdDev
- ConsolidationFunction.StdDevp
- ConsolidationFunction.Sum
- ConsolidationFunction.Var
- ConsolidationFunction.Varp

## **Come applicare la funzione di consolidamento ai campi dati della tabella pivot usando Aspose.Cells for JavaScript via C++**

Il seguente codice applica la funzione di consolidamento **Media** al primo campo dati (o campo valore) e la funzione di consolidamento **ConteggioDistinto** al secondo campo dati (o campo valore).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PivotTable Consolidation Function</title>
    </head>
    <body>
        <h1>Apply Consolidation Function to PivotTable</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet of the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access the first pivot table of the worksheet
            const pivotTable = worksheet.pivotTables.get(0);

            // Apply Average consolidation function to first data field
            pivotTable.dataFields.get(0).function = AsposeCells.ConsolidationFunction.Average;

            // Apply DistinctCount consolidation function to second data field
            pivotTable.dataFields.get(1).function = AsposeCells.ConsolidationFunction.DistinctCount;

            // Calculate the data to make changes affect
            pivotTable.calculateData();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PivotTable consolidation functions applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

La funzione di consolidamento **CONTEGGIODISTINTO** è supportata solo da Microsoft Excel 2013.

{{% /alert %}}
