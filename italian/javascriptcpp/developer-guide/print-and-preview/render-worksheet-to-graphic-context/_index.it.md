---
title: Renderizza il foglio di lavoro nel contesto grafico con JavaScript tramite C++
linktitle: Rappresentare il foglio di calcolo nel contesto grafico
type: docs
weight: 300
url: /it/javascript-cpp/render-worksheet-to-graphic-context/
description: Impara come rendere un foglio di lavoro nel contesto grafico usando Aspose.Cells for JavaScript tramite C++. Questo include il rendering su file immagine, schermi e stampanti.
---

{{% alert color="primary" %}}

Aspose.Cells ora può rendere i fogli di lavoro in un contesto grafico. Il contesto grafico può essere qualsiasi cosa come un file immagine, schermo o stampante, ecc. Usa uno dei seguenti due metodi per rendere un foglio di lavoro in un contesto grafico.

- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-)
- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-)

{{% /alert %}}

Il seguente codice illustra come usare Aspose.Cells per rendere un foglio di lavoro in un contesto grafico. Una volta eseguito, stamperà l'intero foglio di lavoro e riempirà lo spazio vuoto residuo con colore blu nel contesto grafico, salvando l'immagine come file **OutputImage_out_.png**. Puoi usare qualsiasi file Excel di origine per provare questo codice. Si consiglia anche di leggere i commenti all’interno del codice per una migliore comprensione.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Render Worksheet to Image</title>
    </head>
    <body>
        <h1>Render Worksheet to Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, Utils } = AsposeCells;

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

            // Create empty image buffer options
            const bmpOptions = new ImageOrPrintOptions();
            bmpOptions.onePagePerSheet = true;

            // Render worksheet to image
            const sheetRender = new SheetRender(worksheet, bmpOptions);
            const imageData = sheetRender.toImage(0);

            // Create blob and provide download link for PNG
            const blob = new Blob([imageData], { type: 'image/png' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputImage_out.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to download the PNG.</p>';
        });
    </script>
</html>
```
