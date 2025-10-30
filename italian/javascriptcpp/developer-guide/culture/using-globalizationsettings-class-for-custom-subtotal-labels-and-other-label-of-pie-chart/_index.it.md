---
title: Utilizzo della classe GlobalizationSettings per etichette di subtotale personalizzate e altre etichette di grafici a torta con JavaScript tramite C++
linktitle: Utilizzo della classe GlobalizationSettings per etichette subtotali personalizzate e altre etichette del grafico a torta
type: docs
weight: 70
url: /it/javascript-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
description: Impara come personalizzare le etichette di subtotale e altre etichette di grafici a torta usando la classe GlobalizationSettings in Aspose.Cells for JavaScript tramite C++.
---

## **Possibili Scenari di Utilizzo**

Le API di Aspose.Cells hanno esposto la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings) per gestire scenari in cui l'utente desidera usare etichette personalizzate per i Subtotali in un foglio di calcolo. Inoltre, la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings) può essere usata anche per modificare l'etichetta **Other** del grafico a torta durante il rendering del foglio o del grafico.

## **Introduzione alla classe GlobalizationSettings**

La classe [**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings) offre attualmente i seguenti 3 metodi che possono essere sovrascritti in una classe personalizzata per ottenere le etichette desiderate per i Subtotali o per rendere testi personalizzati per l'etichetta **Other** di un grafico a torta.

1. [**GlobalizationSettings.totalName(ConsolidationFunction)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#totalName-consolidationfunction-): Ottiene il nome totale della funzione.
1. [**GlobalizationSettings.grandTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#grandTotalName-consolidationfunction-): Ottiene il nome del totale generale della funzione.


### **Etichette personalizzate per le subtotali**

La classe [**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings) può essere usata per personalizzare le etichette di subtotale sovrascrivendo i metodi [**GlobalizationSettings.totalName(ConsolidationFunction)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#totalName-consolidationfunction-) & [**GlobalizationSettings.grandTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#grandTotalName-consolidationfunction-) come dimostrato in avanti.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Custom GlobalizationSettings Example</title>
    </head>
    <body>
        <h1>Custom GlobalizationSettings Example</h1>
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

        // Defines a custom class derived from GlobalizationSettings class
        class CustomSettings extends AsposeCells.GlobalizationSettings {
            // Overrides the totalName method (converted from getTotalName)
            totalName(functionType) {
                switch (functionType) {
                    case AsposeCells.ConsolidationFunction.Average:
                        return "AVG";
                    default:
                        return super.totalName(functionType);
                }
            }

            // Overrides the grandTotalName method (converted from getGrandTotalName)
            grandTotalName(functionType) {
                switch (functionType) {
                    case AsposeCells.ConsolidationFunction.Average:
                        return "GRD AVG";
                    default:
                        return super.grandTotalName(functionType);
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Read the selected file and process with Aspose.Cells
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object from the file bytes
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create and assign the custom globalization settings to the workbook
            const customSettings = new CustomSettings();
            workbook.globalizationSettings = customSettings;

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Custom globalization settings applied. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Per aggiungere etichette personalizzate, è necessario assegnare la proprietà [**WorkbookSettings.globalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#globalizationSettings--) a un'istanza della classe **CustomSettings** definita sopra prima di aggiungere i Subtotali al foglio di calcolo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Subtotal with Custom Globalization Settings</h1>
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

        // Defines a custom class derived from GlobalizationSettings class
        class CustomSettings extends AsposeCells.GlobalizationSettings {
            // Overrides the TotalName method (converted from getTotalName)
            totalName(functionType) {
                // Checks the function type used to add the subtotals
                switch (functionType) {
                    // Returns custom value based on the function type used to add the subtotals
                    case AsposeCells.ConsolidationFunction.Average:
                        return "AVG";
                    // Handle other cases as per requirement
                    default:
                        return super.totalName(functionType);
                }
            }

            // Overrides the GrandTotalName method (converted from getGrandTotalName)
            grandTotalName(functionType) {
                // Checks the function type used to add the subtotals
                switch (functionType) {
                    // Returns custom value based on the function type used to add the subtotals
                    case AsposeCells.ConsolidationFunction.Average:
                        return "GRD AVG";
                    // Handle other cases as per requirement
                    default:
                        return super.grandTotalName(functionType);
                }
            }
        }

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

            // Assigns the GlobalizationSettings property of the WorkbookSettings class to a custom class created
            workbook.settings.globalizationSettings = new CustomSettings();

            // Accesses the 1st worksheet from the collection which contains data that resides in the cell range A2:B9
            const sheet = workbook.worksheets.get(0);

            // Adds Subtotal of type Average to the worksheet
            sheet.cells.subtotal(AsposeCells.CellArea.createCellArea("A2", "B9"), 0, AsposeCells.ConsolidationFunction.Average, [1]);

            // Calculates Formulas
            workbook.calculateFormula();

            // Auto fits all columns
            sheet.autoFitColumns();

            // Saving the workbook and preparing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

La classe [**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings) funziona solo per aggiungere nuovi Subtotali. Se un foglio di calcolo contiene già Subtotali, le loro etichette non potranno essere modificate.

{{% /alert %}}
