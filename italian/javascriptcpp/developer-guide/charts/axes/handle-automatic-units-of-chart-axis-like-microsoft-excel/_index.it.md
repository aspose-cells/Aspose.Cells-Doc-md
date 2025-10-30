---
title: Gestisci le unità automatiche dell asse del grafico come Microsoft Excel con JavaScript tramite C++
linktitle: Gestire le unità automatiche dell asse del grafico come Microsoft Excel
description: Impara come gestire le unità automatiche sugli assi del grafico in Aspose.Cells for JavaScript tramite C++. La nostra guida ti mostrerà come configurare e personalizzare le unità automatiche su un asse del grafico, incluso la visualizzazione della notazione scientifica e la regolazione della scala.
keywords: Aspose.Cells for JavaScript tramite C++, assi del grafico, unità automatiche, Microsoft Excel, configurazione, personalizzazione, notazione scientifica, scalatura.
type: docs
weight: 120
url: /it/javascript-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/
---

## **Possibili Scenari di Utilizzo**  
 Le prime versioni di Aspose.Cells for JavaScript tramite C++ non erano in grado di gestire correttamente le unità automatiche dell'asse del grafico quando il grafico viene esportato come immagine o PDF. Ora, Aspose.Cells for JavaScript tramite C++ supporta la gestione delle unità automatiche dell'asse del grafico. Non è necessario modificare il codice. Basta convertire il grafico in un'immagine o PDF e verrà renderizzato come in Microsoft Excel.  

## **Gestire le unità automatiche dell'asse del grafico come Microsoft Excel**  
Il seguente esempio di codice carica il [file Excel di esempio](61767755.xlsx) e genera il [grafico PDF in output](61767752.pdf). Lo screenshot mostra le unità automatiche dell'asse del grafico evidenziate da rettangoli rossi e confronta anche il grafico del file Excel di esempio con il grafico PDF in output. Entrambi sono esattamente simili.  

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)  

## **Codice di Esempio**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Handle Automatic Units Of Chart Axis Like Microsoft Excel</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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

            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first chart
            const chart = worksheet.charts.get(0);

            // Render chart to pdf
            const outputData = await chart.toPdf();

            // Create download link for the generated PDF
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart rendered to PDF successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
