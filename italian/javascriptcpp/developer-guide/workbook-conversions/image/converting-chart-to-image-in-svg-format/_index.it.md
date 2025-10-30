---
title: Conversione di grafici in formato SVG in JavaScript tramite C++
linktitle: Conversione del grafico in un immagine nel formato SVG
type: docs
weight: 240
url: /it/javascript-cpp/converting-chart-to-image-in-svg-format/
description: Impara come convertire un grafico in immagine in formato SVG usando Aspose.Cells for JavaScript tramite C++.
---

{{% alert color="primary" %}}

Scalable Vector Graphics (SVG) è un formato di immagine vettoriale basato su XML per grafica bidimensionale che supporta anche l'interattività e l'animazione. La specifica SVG è uno standard aperto sviluppato dal World Wide Web Consortium (W3C) dal 1999.

Le immagini SVG e i loro comportamenti sono definiti in file di testo XML. Ciò significa che possono essere cercati, indicizzati, scriptati e compressi. Come file XML, le immagini SVG possono essere create e modificate con qualsiasi editor di testo, ma vengono più spesso create con software di disegno.

Aspose.Cells può salvare grafici in immagini in vari formati come BMP, JPEG, PNG, GIF, SVG, ecc. Questo articolo spiega come salvare un grafico in formato SVG.

{{% /alert %}}

Nel seguente codice di esempio viene spiegato come utilizzare Aspose.Cells per convertire un grafico in un'immagine nel formato SVG. Il codice carica il file Microsoft Excel di origine e poi salva il primo grafico trovato nel primo foglio di lavoro in SVG.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Export Chart to SVG</title>
    </head>
    <body>
        <h1>Export First Chart to SVG</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType } = AsposeCells;

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

            // Create workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Set image or print options
            const opts = new ImageOrPrintOptions();
            opts.imageType = ImageType.Svg;

            // Export the chart to SVG format (returns image bytes)
            const imageData = chart.toImage(opts);

            // Create downloadable SVG blob
            const blob = new Blob([imageData], { type: 'image/svg+xml' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Image_out.svg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download SVG Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart exported to SVG. Click the download link to download the SVG file.</p>';
        });
    </script>
</html>
```
