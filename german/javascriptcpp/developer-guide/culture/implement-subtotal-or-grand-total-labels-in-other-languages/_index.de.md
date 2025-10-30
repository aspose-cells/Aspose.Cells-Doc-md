---
title: Implementieren Sie Subtotal oder Gesamtsummen Labels in anderen Sprachen mit JavaScript in C++
linktitle: Implementieren Sie Subtotal oder Gesamtsummen Labels in anderen Sprachen
type: docs
weight: 50
url: /de/javascript-cpp/implement-subtotal-or-grand-total-labels-in-other-languages/
---

## **Mögliche Verwendungsszenarien**  

Manchmal möchten Sie Zwischensummen- und Gesamtsummen-Labels in nicht-englischen Sprachen wie Chinesisch, Japanisch, Arabisch, Hindi usw. anzeigen. Aspose.Cells for JavaScript in C++ ermöglicht dies, indem es die [**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings)-Klasse und die [**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/)-Eigenschaft verwendet. Bitte lesen Sie diesen Artikel, um zu erfahren, wie man die [**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings)-Klasse nutzt.  

- [Verwendung der GlobalizationSettings-Klasse für benutzerdefinierte Teilergebnisbeschriftungen und andere Beschriftungen des Kuchendiagramms](/cells/de/javascript-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)  

## **Implementieren Sie Subtotal- oder Gesamtsummen-Labels in anderen Sprachen**  

Das folgende Beispiel lädt die [Beispiel-Excel-Datei](5115151.xlsx) und implementiert Subtotal- und Gesamtsummen-Namen in chinesischer Sprache. Bitte prüfen Sie die [Ausgabe-Excel-Datei](5115152.xlsx), die durch diesen Code erzeugt wurde, zur Referenz. Zuerst erstellen wir eine Klasse von [**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings) und verwenden sie in unserem Code.  

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

Verwenden Sie die oben erstellte Klasse im folgenden Code:  

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
