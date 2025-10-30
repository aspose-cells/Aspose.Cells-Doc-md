---
title: Leggere le etichette dell asse dopo aver calcolato il grafico con JavaScript tramite C++
linktitle: Leggere le etichette dell asse dopo il calcolo del grafico
description: Impara come leggere le etichette dell asse in Aspose.Cells for JavaScript tramite C++ dopo aver calcolato il grafico. La nostra guida ti mostrerà come accedere e recuperare le etichette dell asse, inclusa la loro formattazione e posizione.
keywords: Aspose.Cells for JavaScript, grafico, etichette asse, calcolo, lettura, accesso, recupero, formattazione, posizionamento, JavaScript tramite C++
type: docs
weight: 90
url: /it/javascript-cpp/read-axis-labels-after-calculating-the-chart/
---

## **Possibili Scenari di Utilizzo**

Puoi leggere le etichette dell'asse del tuo grafico dopo aver calcolato i suoi valori usando il metodo [**Chart.calculate()**](https://reference.aspose.com/cells/javascript-cpp/chart/#calculate--). Si prega di usare la proprietà [**Axis.axisTexts**](https://reference.aspose.com/cells/javascript-cpp/axis/#axisTexts--) a questo scopo, che restituirà la lista delle etichette dell'asse.

## **Leggere le etichette dell'asse dopo il calcolo del grafico**

Si prega di vedere il seguente codice di esempio che carica il file Excel di esempio e legge le etichette dell'asse delle categorie del grafico nel primo foglio di lavoro. Stampa quindi i valori delle etichette degli assi sulla console. Si prega di vedere l'output della console del codice di esempio riportato di seguito per un riferimento.

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Read Axis Labels</title>
    </head>
    <body>
        <h1>Read Chart Category Axis Labels</h1>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the chart
            const chart = worksheet.charts.get(0);

            // Calculate the chart
            chart.calculate();

            // Read axis labels of category axis
            const lstLabels = chart.categoryAxis.axisTexts;

            // Display axis labels
            let html = '<h2>Category Axis Labels:</h2>';
            html += '<hr/>';
            if (!lstLabels || !lstLabels.length) {
                html += '<p>No axis labels found.</p>';
            } else {
                html += '<ul>';
                for (let i = 0; i < lstLabels.length; i++) {
                    console.log(lstLabels[i]);
                    html += `<li>${lstLabels[i]}</li>`;
                }
                html += '</ul>';
            }
            resultDiv.innerHTML = html;
        });
    </script>
</html>
```

## **Output della console**

{{< highlight javascript >}}  
 Category Axis Labels:  

\---------------------  

Iran  

China  

USA  

Brazil  

England  
{{< /highlight >}}
