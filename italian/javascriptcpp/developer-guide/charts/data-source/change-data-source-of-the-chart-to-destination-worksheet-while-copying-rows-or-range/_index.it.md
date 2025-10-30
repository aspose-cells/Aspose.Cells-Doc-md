---
title: Cambia la fonte dati del grafico alla worksheet di destinazione durante la copia di righe o intervalli con JavaScript tramite C++
linktitle: Cambia origine dati del grafico al foglio di lavoro di destinazione durante la copia di righe o intervalli
description: Impara come cambiare la fonte dati di un grafico a una worksheet di destinazione mentre copi righe o un intervallo in Script Aspose.Cells for Java tramite C++. Questa guida dimostra come aggiornare l’intervallo di dati del grafico e collegarlo alla worksheet di destinazione.
keywords: Script Aspose.Cells for Java tramite C++, creazione di grafici, origine dati, worksheet di destinazione, righe, intervallo, copia, aggiornamento, intervallo di dati, collegamento.
type: docs
weight: 440
url: /it/javascript-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Possibili Scenari di Utilizzo**

Quando si copiano righe o intervalli contenenti grafici in un nuovo foglio di lavoro, la fonte dei dati del grafico non cambia. Ad esempio, se la fonte dei dati del grafico è `=Sheet1!$A$1:$B$4`, dopo aver copiato righe o intervallo in un nuovo foglio di lavoro, la fonte dei dati rimarrà uguale, cioè `=Sheet1!$A$1:$B$4`. Si riferisce ancora al vecchio foglio di lavoro, ovvero Sheet1. Questo è anche il comportamento in Microsoft Excel. Ma se si desidera che si riferisca al nuovo foglio di lavoro di destinazione, utilizzare la proprietà [**CopyOptions.referToDestinationSheet**](https://reference.aspose.com/cells/javascript-cpp/copyoptions/#referToDestinationSheet--) e impostarla su **true** durante la chiamata del metodo [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-). Ora, se il foglio di lavoro di destinazione è DestSheet, la fonte dei dati del grafico cambierà da `=Sheet1!$A$1:$B$4` a `=DestSheet!$A$1:$B$4`.

## **Modifica dell'origine dei dati del grafico al foglio di lavoro di destinazione durante la copia delle righe o dell'intervallo**

Il seguente esempio di codice spiega come utilizzare la proprietà [**CopyOptions.referToDestinationSheet**](https://reference.aspose.com/cells/javascript-cpp/copyoptions/#referToDestinationSheet--) durante la copia di righe o intervalli contenenti grafici in un nuovo worksheet. Il codice utilizza il [file Excel di esempio](5113699.xlsx) e genera il [file Excel di output](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Worksheet with Charts</title>
    </head>
    <body>
        <h1>Copy Worksheet with Charts Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiate Workbook from the uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first sheet which contains chart
            const source = wb.worksheets.get(0);

            // Add another sheet named DestSheet
            const destination = wb.worksheets.add("DestSheet");

            // Set CopyOptions.referToDestinationSheet to true
            const options = new AsposeCells.CopyOptions();
            options.referToDestinationSheet = true;

            // Copy all the rows of source worksheet to destination worksheet which includes chart as well
            // The chart data source will now refer to DestSheet
            destination.cells.copyRows(source.cells, 0, 0, source.cells.maxDisplayRange.rowCount, options);

            // Save workbook in xlsx format and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
