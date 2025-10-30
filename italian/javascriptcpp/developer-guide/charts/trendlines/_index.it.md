---
title: Ottenere il testo dell equazione della trendline del grafico con JavaScript tramite C++
description: Impara come usare Aspose.Cells for JavaScript via C++ per recuperare il testo dell equazione di una trendline in un grafico creato in Microsoft Excel. La nostra guida dimostrerà come accedere ed estrarre l equazione di una trendline per ulteriori analisi o visualizzazione.
keywords: Script Aspose.Cells for Java tramite C++, Trendline del grafico, Testo dell equazione, Microsoft Excel, Analisi dei dati, Visualizzazione.
linktitle: Retta di Tendenza
type: docs
weight: 110
url: /it/javascript-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Puoi recuperare il testo dell'equazione della trendline del grafico usando Aspose.Cells for JavaScript tramite C++. Aspose.Cells fornisce la proprietà [**DataLabels.text**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#text--) che restituisce il testo dell'equazione della trendline del grafico. Per utilizzare questa proprietà, devi prima chiamare il metodo [**Chart.calculate()**](https://reference.aspose.com/cells/javascript-cpp/chart/#calculate--).

{{% /alert %}}

Lo screenshot seguente mostra il grafico con una Trendline e il suo testo dell’equazione mostrato in rosso. Recupereremo questo testo usando la proprietà [**DataLabels.text**](https://reference.aspose.com/cells/javascript-cpp/datalabels/#text--) nel seguente esempio di codice.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## Codice JavaScript per ottenere il testo dell'equazione della trendline del grafico

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Trendline Equation Example</h1>
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

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Calculate the Chart to get the Equation Text of Trendline
            chart.calculate();

            // Access the Trendline
            const trendLine = chart.nSeries.get(0).trendLines.get(0);

            // Read the Equation Text of Trendline
            const equationText = trendLine.dataLabels.text;

            document.getElementById('result').innerHTML = `<p>Equation Text: ${equationText}</p>`;
        });
    </script>
</html>
```

## Output generato dal codice di esempio

Questo è l'output console del codice di esempio precedente.

{{< highlight javascript >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
