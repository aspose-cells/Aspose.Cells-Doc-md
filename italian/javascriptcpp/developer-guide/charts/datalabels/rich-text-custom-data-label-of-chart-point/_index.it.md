---
title: Etichetta dati personalizzata di testo ricco di punto grafico con JavaScript tramite C++
description: Impara come aggiungere etichette dati personalizzate di testo ricco ai punti del grafico in Aspose.Cells for JavaScript tramite C++. La nostra guida ti mostrerà come formattare le etichette con diversi caratteri, colori e opzioni di allineamento per migliorare l aspetto e la leggibilità dei tuoi grafici.
keywords: Aspose.Cells for JavaScript tramite C++, grafici, testo ricco, etichette personalizzate, caratteri, colori, allineamento, aspetto, leggibilità.
type: docs
weight: 10
url: /it/javascript-cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

Puoi usare Aspose.Cells per creare etichette dati personalizzate in formato Rich Text per i punti del grafico. Aspose.Cells fornisce il metodo [**ChartTextFrame.characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/charttextframe/#characters-number-number-) per restituire l'oggetto [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting) che può essere usato per impostare le proprietà del font del testo come il colore, il grassetto, ecc.

{{% /alert %}}

## Etichetta dati personalizzata di testo ricco del punto del grafico

Il seguente codice accede al primo punto del grafico della prima serie, imposta il suo testo e poi imposta il font dei primi 10 caratteri impostando il colore su rosso e il grassetto su **true**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Creating a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first chart inside the sheet
            const chart = worksheet.charts.get(0);

            // Access the data label of first series first point
            const dlbls = chart.nSeries.get(0).points.get(0).dataLabels;

            // Set data label text
            dlbls.text = "Rich Text Label";

            // Set the font setting of the first 10 characters
            const fntSetting = dlbls.characters(0, 10);
            const font = fntSetting.font;
            font.color = AsposeCells.Color.Red;
            font.isBold = true;

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Data label updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
