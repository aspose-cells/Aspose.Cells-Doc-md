---
title: Calcola il Fattore di Scala della Configurazione Pagina con JavaScript tramite C++
linktitle: Calcola il fattore di scala della pagina di impostazione
type: docs
weight: 300
url: /it/javascript-cpp/calculate-page-setup-scaling-factor/
description: Questo articolo fornisce un esempio di codice che spiega come utilizzare l API JavaScript tramite C++ per calcolare il fattore di scala della configurazione della pagina utilizzando l opzione Adatta a n pagine in larghezza per m in altezza del foglio Excel in modo programmatico.
keywords: Adatta a n pagine di larghezza per m di altezza Excel JavaScript tramite C++, calcola il fattore di scala della configurazione della pagina JavaScript tramite C++
---

{{% alert color="primary" %}}

Quando imposti la scalabilità della configurazione pagina usando l'opzione **Adatta a n pagina(i) in larghezza per m in altezza**, Microsoft Excel calcola il Fattore di Scala della Configurazione Pagina. Puoi calcolare la stessa cosa usando la proprietà [**SheetRender.pageScale**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#pageScale--). Questa proprietà restituisce un valore double che può essere convertito in percentuale. Ad esempio, se restituisce 0.5, significa che il fattore di scala è il 50%.

{{% /alert %}}

Il seguente codice di esempio illustra come calcolare il fattore di scala dell'impostazione della pagina utilizzando la proprietà [**SheetRender.pageScale**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#pageScale--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Page Scale</title>
    </head>
    <body>
        <h1>Page Scale Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, SheetRender, ImageOrPrintOptions, PaperSizeType, Utils } = AsposeCells;

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

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put some data in these cells
            worksheet.cells.get("A4").putValue("Test");
            worksheet.cells.get("S4").putValue("Test");

            // Set paper size
            worksheet.pageSetup.paperSize = PaperSizeType.PaperA4;

            // Set fit to pages wide as 1
            worksheet.pageSetup.fitToPagesWide = 1;

            // Calculate page scale via sheet render
            const sr = new SheetRender(worksheet, new ImageOrPrintOptions());

            // Convert page scale double value to percentage
            const strPageScale = (sr.pageScale * 100).toFixed(0) + "%";

            // Write the page scale value
            document.getElementById('result').innerHTML = `<p>Page Scale: ${strPageScale}</p>`;
            console.log(strPageScale);
        });
    </script>
</html>
```
