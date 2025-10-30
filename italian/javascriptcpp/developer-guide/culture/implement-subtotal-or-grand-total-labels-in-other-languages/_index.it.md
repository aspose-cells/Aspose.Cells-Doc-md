---
title: Implementa etichette di Subtotal o Grand Total in altre lingue con JavaScript tramite C++
linktitle: Implementa etichette Subtotal o Grand Total in altre lingue
type: docs
weight: 50
url: /it/javascript-cpp/implement-subtotal-or-grand-total-labels-in-other-languages/
---

## **Possibili Scenari di Utilizzo**  

A volte vuoi mostrare etichette di subtotale e totale generale in lingue non inglesi come cinese, giapponese, arabo, hindi, ecc. Aspose.Cells for JavaScript tramite C++ consente di farlo usando la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings) e la proprietà [**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/). Si prega di consultare questo articolo su come utilizzare la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings).  

- [Utilizzo della classe GlobalizationSettings per le etichette Subtotali personalizzate e altre etichette del grafico a torta](/cells/it/javascript-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)  

## **Implementa etichette Subtotal o Grand Total in altre lingue**  

Il seguente esempio di codice carica il [file excel di esempio](5115151.xlsx) e implementa nomi di subtotale e totale generale in cinese. Consulta il [file Excel di output](5115152.xlsx) generato da questo codice come riferimento. Prima creiamo una classe di [**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings) e poi la usiamo nel nostro codice.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Globalization Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Globalization Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

        // Converted GlobalizationSettingsImp class
        class GlobalizationSettingsImp extends AsposeCells.GlobalizationSettings {
            // This function will return the sub total name
            totalName(functionType) {
                return "Chinese Total - 可能的用法";
            }

            // This function will return the grand total name
            grandTotalName(functionType) {
                return "Chinese Grand Total - 可能的用法";
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');

            // Instantiate and register globalization settings
            const globalization = new GlobalizationSettingsImp();
            AsposeCells.globalizationSettings = globalization;

            let resultHtml = '';
            resultHtml += '<p style="color: green;">Globalization settings registered globally.</p>';
            resultHtml += `<p>TotalName (example): ${globalization.totalName('Sum')}</p>`;
            resultHtml += `<p>GrandTotalName (example): ${globalization.grandTotalName('Sum')}</p>`;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Open workbook from the selected file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Optionally, the global AsposeCells.globalizationSettings will be used by the library where applicable

                // Save the workbook back to XLSX and provide a download link
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'output.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Modified Excel File';

                resultHtml += '<p style="color: green;">File processed. Click the download link to get the file.</p>';
            } else {
                resultHtml += '<p style="color: orange;">No file selected. The globalization settings are registered and can be used by Aspose.Cells operations.</p>';
            }

            document.getElementById('result').innerHTML = resultHtml;
        });
    </script>
</html>
```  

Ora usa la classe creata sopra nel codice come segue:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Subtotal Example</h1>
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

            // Instantiate Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set the globalization setting to change subtotal and grand total names
            const globalizationSettings = new AsposeCells.GlobalizationSettings();
            workbook.settings.globalizationSettings = globalizationSettings;

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Apply subtotal on A1:B10
            const cellArea = AsposeCells.CellArea.createCellArea("A1", "B10");
            worksheet.cells.subtotal(cellArea, 0, AsposeCells.ConsolidationFunction.Sum, [2, 3, 4]);

            // Set the width of the first column
            worksheet.cells.columns.get(0).width = 40;

            // Save the output excel file
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
