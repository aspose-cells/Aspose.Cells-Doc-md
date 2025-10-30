---
title: Imposta il codice di formato dei valori delle serie del grafico con JavaScript tramite C++
description: Impara come impostare il codice di formato dei valori delle serie del grafico in Script Aspose.Cells for Java tramite C++. Questa guida ti aiuterà a comprendere come formattare i dati delle serie del grafico usando il codice di formato appropriato, permettendoti di presentare i tuoi dati in modo accurato e professionale.
keywords: Script Aspose.Cells for Java tramite C++, serie del grafico, codice di formato dei valori, formattazione, presentazione dei dati, precisione, professionalità.
linktitle: Formato numero
type: docs
weight: 100
url: /it/javascript-cpp/set-the-values-format-code-of-chart-series/
---

## **Possibili Scenari di Utilizzo**
Puoi impostare il codice di formato dei valori delle serie del grafico usando la proprietà [Series.valuesFormatCode](https://reference.aspose.com/cells/javascript-cpp/series/#valuesFormatCode--). Questa proprietà è utile non solo per le serie basate sull'intervallo all’interno del foglio di lavoro, ma anche per le serie create con un array di valori.

## **Impostare il codice di formato dei valori della serie del grafico**
Il seguente esempio di codice aggiunge una serie nel grafico vuoto che non aveva serie precedenti. Aggiunge la serie usando l’array di valori. Una volta aggiunta, la formatta con il codice $#,##0 usando la proprietà [Series.valuesFormatCode](https://reference.aspose.com/cells/javascript-cpp/series/#valuesFormatCode--) e il numero 10000 diventa $10.000. Lo screenshot mostra l’effetto del codice sul [file Excel di esempio](51740712.xlsx) e sul [file Excel di output](51740713.xlsx) dopo l'esecuzione.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Codice di Esempio**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Chart Series Example</h1>
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

            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                if (!fileInput.files.length) {
                    document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Instantiating a Workbook object from the uploaded file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Access first worksheet
                const worksheet = workbook.worksheets.get(0);

                // Access first chart
                const chart = worksheet.charts.get(0);

                // Add series using an array of values
                chart.nSeries.add("{10000, 20000, 30000, 40000}", true);

                // Access the series and set its values format code
                const series = chart.nSeries.get(0);
                series.valuesFormatCode = "$#,##0";

                // Saving the modified Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = '51740713.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Modified Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```
