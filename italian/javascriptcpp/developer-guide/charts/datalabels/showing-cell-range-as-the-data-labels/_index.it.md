---
title: Mostrare l intervallo di celle come etichette dati con JavaScript tramite C++
linktitle: Mostrare l intervallo di celle come etichette dati
description: Impara come mostrare un intervallo di celle come etichette dati nei grafici usando Aspose.Cells for JavaScript tramite C++. La nostra guida dimostrerà come collegare le etichette alla tua fonte di dati e formattarle per fornire informazioni accurate e significative nei tuoi grafici.
keywords: Aspose.Cells for JavaScript tramite C++, grafici, etichette dati, intervallo di Celle, fonte di dati, formattazione, precisione, informazioni significative.
type: docs
weight: 130
url: /it/javascript-cpp/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}
In Microsoft Excel 2013, puoi visualizzare un intervallo di celle come etichette dati. Aspose.Cells for JavaScript tramite C++ supporta questa funzionalità.
{{% /alert %}}

## **Casella di controllo per mostrare l'intervallo di celle come etichette dati**

Per mostrare l'intervallo di celle come etichette dati in Microsoft Excel:

1. Seleziona le etichette dati della serie e fai clic con il tasto destro per aprire il menu contestuale.  
1. Seleziona **Formatta etichette dati**. Le opzioni di etichettatura vengono visualizzate.  
1. Seleziona o deseleziona l'opzione **L'etichetta contiene - Valore dalle celle**.  

Il codice di esempio di seguito accede alle etichette dei dati di una serie di grafico e imposta la proprietà [**DataLabels.showCellRange**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#showCellRange--) su **true** per selezionare l'opzione **Etichetta Contiene - Valore Da Celle**.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Show Range in Data Labels</title>
    </head>
    <body>
        <h1>Show Range in Data Labels Example</h1>
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

            // Create workbook from the source Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Check the "Label Contains - Value From Cells"
            const dataLabels = chart.nSeries.get(0).dataLabels;
            dataLabels.showCellRange = true;

            // Save the workbook
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
