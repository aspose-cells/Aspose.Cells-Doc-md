---
title: Trova il tipo di valori X e Y dei punti nella serie di grafici con JavaScript tramite C++
linktitle: Trova il tipo di valori X e Y dei punti nella serie del grafico
description: Impara come determinare il tipo di valori X e Y nei punti della serie di grafici usando Aspose.Cells for JavaScript tramite C++. Questa guida spiega i tipi di valori dei dati e come accedervi e lavorarci nei tuoi grafici.
keywords: Aspose.Cells for JavaScript tramite C++, visualizzazione grafici, valori X, valori Y, tipi di dati, accesso, lavoro, serie di grafici.
type: docs
weight: 150
url: /it/javascript-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Possibili Scenari di Utilizzo**  
A volte, vuoi conoscere il tipo di valori X e Y dei punti nel grafico di una serie. Aspose.Cells for JavaScript tramite C++ fornisce le proprietà `ChartPoint.XValueType` e `ChartPoint.YValueType` che possono essere utilizzate a questo scopo. Nota bene, dovrai chiamare il metodo `Chart.calculate()` prima di poter utilizzare efficacemente queste proprietà.  

## **Trova il tipo di valori X e Y dei punti nella serie del grafico**  
Il seguente esempio di codice carica il [file Excel di esempio](64716905.xlsx) e accede al primo grafico all'interno del primo foglio di lavoro. Poi chiama il metodo `Chart.calculate()` e determina il tipo di valori X e Y del primo punto del grafico, stampandoli in console. Consulta l'output della console mostrato di seguito come riferimento.  

## **Codice di Esempio**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Find Type Of X and Y Values Of Points In Chart Series</h1>
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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first chart.
            const chart = worksheet.charts.get(0);

            // Calculate chart data.
            chart.calculate();

            // Access first chart point in the first series.
            const point = chart.nSeries.get(0).points.get(0);

            // Get the types of X and Y values of chart point.
            const xValueType = point.xValueType;
            const yValueType = point.yValueType;

            // Display results
            document.getElementById('result').innerHTML = `
                <p style="color: green;">Operation completed successfully!</p>
                <p>X Value Type: ${xValueType}</p>
                <p>Y Value Type: ${yValueType}</p>
            `;
        });
    </script>
</html>
```  

## **Output della console**  

{{< highlight java >}}  
 X Value Type: IsString  

Y Value Type: IsNumeric  
{{< /highlight >}}
