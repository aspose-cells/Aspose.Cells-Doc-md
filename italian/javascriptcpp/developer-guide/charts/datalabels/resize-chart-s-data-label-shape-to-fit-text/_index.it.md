---
title: Ridimensionare la forma dell etichetta dati del grafico per adattarla al testo con JavaScript tramite C++
linktitle: Ridimensionare la forma dell etichetta dati del grafico per adattare il testo
description: Impara come ridimensionare la forma dell etichetta dati in un grafico per adattarla al testo in Aspose.Cells for JavaScript tramite C++. La nostra guida ti mostrerà come regolare la dimensione e la forma del contenitore dell etichetta per garantire che il testo venga visualizzato correttamente senza troncamenti o sovrapposizioni.
keywords: Aspose.Cells for JavaScript tramite C++, visualizzazione grafici, etichette dati, ridimensionamento forma, adattamento testo, troncamento, sovrapposizione.
type: docs
weight: 220
url: /it/javascript-cpp/resize-chart-s-data-label-shape-to-fit-text/
---

{{% alert color="primary" %}}  
L'applicazione Excel fornisce l'opzione **Ridimensiona forma per adattare il testo** per le etichette dati del grafico al fine di aumentare le dimensioni della forma in modo che il testo vi entri.  
{{% /alert %}}  

## **Come Ridimensionare la Forma della etichetta dati del grafico per Adattare il Testo in Microsoft Excel**  

Questa opzione può essere accessibile sull'interfaccia Excel selezionando qualsiasi etichetta dei dati sul grafico. Fai clic con il tasto destro e seleziona il menu **Formato etichette dati**. Nella scheda **Dimensione e proprietà**, espandi **Allineamento** per rivelare le proprietà correlate, inclusa l'opzione **Ridimensiona forma per adattare il testo**.  

## **Come ridimensionare la forma dell'etichetta dati del grafico per adattarla al testo usando Aspose.Cells for JavaScript tramite C++**  

Per imitare la funzione di Excel di ridimensionare le forme delle etichette dei dati per adattarsi al testo, le API Aspose.Cells hanno esposto la proprietà di tipo Boolean [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#isResizeShapeToFitText--). Il seguente esempio di codice mostra uno scenario di utilizzo semplice della proprietà [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#isResizeShapeToFitText--).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Chart Data Labels Resize Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet that contains the Chart
            const sheet = workbook.worksheets.get(0);

            for (let c = 0; c < sheet.charts.count; c++) {
                // Access the Chart
                const chart = sheet.charts.get(c);

                for (let index = 0; index < chart.nSeries.count; index++) {
                    // Access the DataLabels of indexed NSeries
                    const labels = chart.nSeries.get(index).dataLabels;

                    // Set ResizeShapeToFitText property to true
                    labels.isResizeShapeToFitText = true;
                }

                // Calculate Chart
                chart.calculate();
            }

            // Save the result
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
