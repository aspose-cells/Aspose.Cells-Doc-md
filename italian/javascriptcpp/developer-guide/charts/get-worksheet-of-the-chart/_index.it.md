---
title: Ottieni il foglio di lavoro del grafico con JavaScript tramite C++
linktitle: Ottieni il foglio di lavoro del grafico
description: Impara come recuperare il foglio di lavoro associato a un grafico Excel utilizzando Script via C++. Accedi e manipola i dati sottostanti del grafico in modo efficiente.
keywords: Script via C++, grafici Excel, fogli di lavoro, manipolazione dei dati, dati sottostanti, operazioni, JavaScript tramite C++
type: docs
weight: 1000
url: /it/javascript-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

A volte, potresti voler accedere a un foglio di lavoro da un riferimento di un grafico. Aspose.Cells fornisce la proprietà [**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--) che restituisce il riferimento del foglio di lavoro che contiene il grafico.

{{% /alert %}}

Il seguente esempio mostra come usare la proprietà [**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--). Il codice prima stampa il nome del foglio di lavoro, poi accede al primo grafico nel foglio di lavoro. Quindi stampa di nuovo il nome del foglio di lavoro, usando la proprietà [**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Print worksheet name
            const sheetName = worksheet.name;
            let outputHtml = `<p>Sheet Name: ${sheetName}</p>`;

            // Access the first chart inside this worksheet
            const charts = worksheet.charts;
            if (charts.count > 0) {
                const chart = charts.get(0);

                // Access the chart's sheet and display its name again
                const chartSheetName = chart.worksheet.name;
                outputHtml += `<p>Chart's Sheet Name: ${chartSheetName}</p>`;
            } else {
                outputHtml += `<p>No charts available in the worksheet.</p>`;
            }

            document.getElementById('result').innerHTML = outputHtml;
        });
    </script>
</html>
```

Di seguito viene riportato l'output della console che il codice di esempio produce. Come puoi vedere, stampa lo stesso nome del foglio di lavoro entrambe le volte.

{{< highlight javascript >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
