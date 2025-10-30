---
title: Adattare automaticamente le righe per la resa con JavaScript tramite C++
linktitle: AutoAdattamento righe per il rendering
type: docs
weight: 130
url: /it/javascript-cpp/autofit-rows-for-rendering/
description: Impara come adattare automaticamente le righe per la visualizzazione in Excel usando Aspose.Cells for JavaScript via C++. Previeni il taglio del testo nei file PDF salvati.
---

Generalmente, quando vuoi visualizzare tutto il testo in una cella, puoi autofittare la riga in visualizzazione normale con zoom al 100% in Microsoft Excel. Questo permette al testo di essere completamente visibile in visualizzazione normale, e anche quando stampi o salvi il file come PDF, il testo sarà visualizzato correttamente.

Tuttavia, in alcuni casi, l'autofitting della riga funziona bene in visualizzazione normale, ma quando passi in modalità anteprima di stampa o salvi il file come PDF, il testo viene tagliato. Verifica il file di origine [Book1.xlsx](Book1.xlsx) e gli screenshot.

![il testo viene tagliato nella visualizzazione di stampa](text_clipped_in_printview.png)

Se desideri prevenire che il testo venga tagliato nel file PDF salvato, puoi adattare automaticamente la riga con l'opzione [AutoFitterOptions.forRendering](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions/#forRendering--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Autofit Rows and Save as PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, AutoFitterOptions, SaveFormat, Utils } = AsposeCells;

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

            // Init workbook instance from uploaded file.
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set autofit options for rendering.
            const autoFitterOptions = new AutoFitterOptions();
            autoFitterOptions.forRendering = true;

            // Autofit rows with options on first worksheet.
            const worksheet = workbook.worksheets.get(0);
            worksheet.autoFitRows(autoFitterOptions);

            // Save to pdf.
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

Ora, il testo non è tagliato nel file PDF di output.

![il testo non è tagliato nel pdf salvato](text_not_clipped_in_saved_pdf.png)
